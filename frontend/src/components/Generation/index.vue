<template>
  <div class="generation-page">
    <div class="page-header">
      <div class="header-content">
        <div class="header-title">
          <h1>AI 图像生成</h1>
          <p class="header-subtitle">基于 Stable Diffusion 的水印嵌入式图像生成</p>
        </div>
        <div class="status-badge">
          <span class="status-dot"></span>
          <span class="status-text">Mock 演示模式</span>
        </div>
      </div>
    </div>

    <div class="generation-container">
      <el-row :gutter="32">
        <!-- 左侧：生成表单 -->
        <el-col :span="10">
          <div class="form-card">
            <div class="card-header">
              <h3>生成配置</h3>
              <div class="header-line"></div>
            </div>

            <el-form :model="form" label-position="top" class="generation-form">
              <el-form-item label="文本提示 (Prompt)" class="form-item-custom">
                <el-input
                  v-model="form.prompt"
                  type="textarea"
                  :rows="5"
                  placeholder="描述你想生成的图像，例如：A beautiful sunset over the ocean with vibrant colors..."
                  class="textarea-custom"
                />
                <div class="input-hint">
                  <el-icon><InfoFilled /></el-icon>
                  <span>详细的描述能生成更精确的图像</span>
                </div>
              </el-form-item>

              <el-form-item label="水印消息" class="form-item-custom">
                <el-input
                  v-model="form.watermarkMessage"
                  placeholder="例如：SWU-2024"
                  class="input-custom"
                >
                  <template #prefix>
                    <el-icon><Key /></el-icon>
                  </template>
                </el-input>
              </el-form-item>

              <el-form-item label="水印开关" class="form-item-custom">
                <div class="switch-container">
                  <el-switch
                    v-model="form.withWatermark"
                    size="large"
                    active-text="启用水印"
                    inactive-text="禁用水印"
                  />
                  <span class="switch-status" :class="{ active: form.withWatermark }">
                    {{ form.withWatermark ? '已启用' : '已禁用' }}
                  </span>
                </div>
              </el-form-item>

              <el-form-item label="推理步数" class="form-item-custom">
                <div class="slider-container">
                  <el-slider
                    v-model="form.numSteps"
                    :min="20"
                    :max="100"
                    :step="10"
                    show-stops
                    class="slider-custom"
                  />
                  <div class="slider-value">{{ form.numSteps }}</div>
                </div>
                <div class="slider-labels">
                  <span>快速</span>
                  <span>平衡</span>
                  <span>精细</span>
                </div>
              </el-form-item>

              <el-form-item label="引导系数" class="form-item-custom">
                <div class="slider-container">
                  <el-slider
                    v-model="form.guidanceScale"
                    :min="1"
                    :max="15"
                    :step="0.5"
                    show-stops
                    class="slider-custom"
                  />
                  <div class="slider-value">{{ form.guidanceScale }}</div>
                </div>
                <div class="slider-labels">
                  <span>创意</span>
                  <span>标准</span>
                  <span>精确</span>
                </div>
              </el-form-item>

              <el-form-item class="form-item-custom">
                <el-button
                  type="primary"
                  @click="handleGenerate"
                  :loading="loading"
                  size="large"
                  class="generate-button"
                >
                  <el-icon v-if="!loading"><MagicStick /></el-icon>
                  <span>{{ loading ? '生成中...' : '开始生成' }}</span>
                </el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-col>

        <!-- 右侧：图像预览 -->
        <el-col :span="14">
          <div class="preview-card">
            <div class="card-header">
              <h3>生成结果</h3>
              <div class="header-line"></div>
            </div>

            <div class="preview-content">
              <!-- 加载状态 -->
              <div v-if="loading" class="loading-state">
                <div class="loading-animation">
                  <div class="loading-circle"></div>
                  <div class="loading-circle"></div>
                  <div class="loading-circle"></div>
                </div>
                <div class="progress-container">
                  <div class="progress-bar">
                    <div class="progress-fill" :style="{ width: progress + '%' }"></div>
                  </div>
                  <div class="progress-text">{{ progress }}%</div>
                </div>
                <p class="loading-message">正在生成图像，请稍候...</p>
                <div class="loading-steps">
                  <div class="step" :class="{ active: progress > 0 }">
                    <div class="step-icon">1</div>
                    <span>文本编码</span>
                  </div>
                  <div class="step" :class="{ active: progress > 33 }">
                    <div class="step-icon">2</div>
                    <span>扩散生成</span>
                  </div>
                  <div class="step" :class="{ active: progress > 66 }">
                    <div class="step-icon">3</div>
                    <span>水印嵌入</span>
                  </div>
                </div>
              </div>

              <!-- 生成结果 -->
              <div v-else-if="generatedImage" class="result-state">
                <div class="image-wrapper">
                  <img :src="generatedImage" alt="Generated Image" class="generated-image" />
                  <div class="image-overlay">
                    <el-button type="primary" circle @click="handleDownload" class="download-btn">
                      <el-icon><Download /></el-icon>
                    </el-button>
                  </div>
                </div>

                <div class="metadata-section">
                  <div class="metadata-header">
                    <h4>生成信息</h4>
                    <el-tag type="success" effect="dark">成功</el-tag>
                  </div>

                  <div class="metadata-grid">
                    <div class="metadata-item">
                      <span class="item-label">任务 ID</span>
                      <span class="item-value">{{ metadata.taskId }}</span>
                    </div>
                    <div class="metadata-item">
                      <span class="item-label">生成时间</span>
                      <span class="item-value">{{ metadata.timestamp }}</span>
                    </div>
                    <div class="metadata-item full-width">
                      <span class="item-label">文本提示</span>
                      <span class="item-value">{{ metadata.prompt }}</span>
                    </div>
                    <div class="metadata-item">
                      <span class="item-label">水印消息</span>
                      <span class="item-value">{{ metadata.watermarkMessage || '无' }}</span>
                    </div>
                    <div class="metadata-item">
                      <span class="item-label">推理步数</span>
                      <span class="item-value">{{ metadata.numSteps }}</span>
                    </div>
                    <div class="metadata-item">
                      <span class="item-label">引导系数</span>
                      <span class="item-value">{{ metadata.guidanceScale }}</span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 空状态 -->
              <div v-else class="empty-state">
                <div class="empty-icon">
                  <el-icon><Picture /></el-icon>
                </div>
                <h3>等待生成</h3>
                <p>配置参数并点击"开始生成"按钮</p>
              </div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

const form = ref({
  prompt: 'A beautiful sunset over the ocean',
  watermarkMessage: 'SWU-2024',
  withWatermark: true,
  numSteps: 50,
  guidanceScale: 7.5
})

const loading = ref(false)
const progress = ref(0)
const generatedImage = ref(null)
const metadata = ref({})

const handleGenerate = async () => {
  if (!form.value.prompt) {
    ElMessage.warning('请输入文本提示')
    return
  }

  loading.value = true
  progress.value = 0

  // 模拟生成进度
  const interval = setInterval(() => {
    progress.value += 10
    if (progress.value >= 100) {
      clearInterval(interval)
    }
  }, 300)

  // 模拟3秒生成时间
  setTimeout(() => {
    // 使用Unsplash随机图片作为Mock数据
    generatedImage.value = `https://picsum.photos/512/512?random=${Date.now()}`

    metadata.value = {
      taskId: `gen_${Date.now()}`,
      timestamp: new Date().toLocaleString('zh-CN'),
      prompt: form.value.prompt,
      watermarkMessage: form.value.withWatermark ? form.value.watermarkMessage : null,
      numSteps: form.value.numSteps,
      guidanceScale: form.value.guidanceScale
    }

    loading.value = false
    ElMessage.success('图像生成成功！')
  }, 3000)
}

const handleDownload = () => {
  const link = document.createElement('a')
  link.href = generatedImage.value
  link.download = `generated_${metadata.value.taskId}.png`
  link.click()
  ElMessage.success('图像下载成功！')
}
</script>

<style scoped>
:root {
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --accent-cyan: #00f5ff;
  --accent-magenta: #ff006e;
  --dark-bg: #0a0e27;
  --darker-bg: #060920;
  --card-bg: rgba(255, 255, 255, 0.03);
  --text-primary: #ffffff;
  --text-secondary: rgba(255, 255, 255, 0.6);
  --border-color: rgba(255, 255, 255, 0.1);
}

.generation-page {
  min-height: 100%;
  animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ========== 页面头部 ========== */
.page-header {
  margin-bottom: 32px;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-title h1 {
  font-size: 32px;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0 0 8px 0;
  letter-spacing: 0.5px;
}

.header-subtitle {
  font-size: 14px;
  color: var(--text-secondary);
  margin: 0;
}

.status-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 20px;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent-cyan);
  animation: pulse 2s ease-in-out infinite;
}

.status-text {
  font-size: 12px;
  color: var(--text-secondary);
  font-weight: 500;
}

/* ========== 卡片样式 ========== */
.form-card,
.preview-card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 24px;
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.form-card:hover,
.preview-card:hover {
  border-color: rgba(102, 126, 234, 0.3);
  box-shadow: 0 8px 32px rgba(102, 126, 234, 0.1);
}

.card-header {
  margin-bottom: 24px;
}

.card-header h3 {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 8px 0;
}

.header-line {
  height: 2px;
  background: linear-gradient(90deg, var(--accent-cyan), transparent);
  border-radius: 2px;
}

/* ========== 表单样式 ========== */
.generation-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-item-custom :deep(.el-form-item__label) {
  color: var(--text-primary);
  font-weight: 600;
  font-size: 13px;
  letter-spacing: 0.5px;
  margin-bottom: 12px;
}

.textarea-custom :deep(textarea),
.input-custom :deep(input) {
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  border-radius: 8px;
  transition: all 0.3s ease;
}

.textarea-custom :deep(textarea):focus,
.input-custom :deep(input):focus {
  border-color: var(--accent-cyan);
  box-shadow: 0 0 0 2px rgba(0, 245, 255, 0.1);
}

.textarea-custom :deep(textarea)::placeholder,
.input-custom :deep(input)::placeholder {
  color: var(--text-secondary);
}

.input-hint {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 8px;
  font-size: 12px;
  color: var(--text-secondary);
}

.input-hint .el-icon {
  color: var(--accent-cyan);
}

/* 开关样式 */
.switch-container {
  display: flex;
  align-items: center;
  gap: 16px;
}

.switch-container :deep(.el-switch) {
  --el-switch-on-color: var(--accent-cyan);
  --el-switch-off-color: rgba(255, 255, 255, 0.2);
}

.switch-status {
  font-size: 13px;
  color: var(--text-secondary);
  font-weight: 500;
  transition: color 0.3s ease;
}

.switch-status.active {
  color: var(--accent-cyan);
}

/* 滑块样式 */
.slider-container {
  display: flex;
  align-items: center;
  gap: 16px;
}

.slider-custom {
  flex: 1;
}

.slider-custom :deep(.el-slider__runway) {
  background: rgba(255, 255, 255, 0.1);
  height: 6px;
}

.slider-custom :deep(.el-slider__bar) {
  background: linear-gradient(90deg, var(--accent-cyan), var(--accent-magenta));
  height: 6px;
}

.slider-custom :deep(.el-slider__button) {
  width: 16px;
  height: 16px;
  border: 2px solid var(--accent-cyan);
  background: var(--dark-bg);
}

.slider-value {
  min-width: 40px;
  text-align: center;
  font-family: 'Orbitron', monospace;
  font-size: 14px;
  font-weight: 600;
  color: var(--accent-cyan);
  padding: 4px 12px;
  background: rgba(0, 245, 255, 0.1);
  border-radius: 8px;
}

.slider-labels {
  display: flex;
  justify-content: space-between;
  margin-top: 8px;
  font-size: 11px;
  color: var(--text-secondary);
}

/* 生成按钮 */
.generate-button {
  width: 100%;
  height: 48px;
  background: var(--primary-gradient);
  border: none;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: 1px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.generate-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s ease;
}

.generate-button:hover::before {
  left: 100%;
}

.generate-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
}

/* ========== 预览区域 ========== */
.preview-content {
  min-height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* 加载状态 */
.loading-state {
  text-align: center;
  width: 100%;
}

.loading-animation {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-bottom: 32px;
}

.loading-circle {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--accent-cyan);
  animation: bounce 1.4s ease-in-out infinite;
}

.loading-circle:nth-child(2) {
  animation-delay: 0.2s;
  background: var(--accent-magenta);
}

.loading-circle:nth-child(3) {
  animation-delay: 0.4s;
  background: #667eea;
}

@keyframes bounce {
  0%, 80%, 100% { transform: scale(0); opacity: 0.5; }
  40% { transform: scale(1); opacity: 1; }
}

.progress-container {
  max-width: 400px;
  margin: 0 auto 16px;
}

.progress-bar {
  height: 8px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--accent-cyan), var(--accent-magenta));
  border-radius: 4px;
  transition: width 0.3s ease;
  position: relative;
  overflow: hidden;
}

.progress-fill::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

.progress-text {
  text-align: center;
  margin-top: 8px;
  font-family: 'Orbitron', monospace;
  font-size: 14px;
  color: var(--accent-cyan);
  font-weight: 600;
}

.loading-message {
  font-size: 14px;
  color: var(--text-secondary);
  margin: 24px 0;
}

.loading-steps {
  display: flex;
  justify-content: center;
  gap: 32px;
  margin-top: 32px;
}

.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  opacity: 0.3;
  transition: opacity 0.3s ease;
}

.step.active {
  opacity: 1;
}

.step-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--card-bg);
  border: 2px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Orbitron', monospace;
  font-weight: 600;
  color: var(--text-secondary);
  transition: all 0.3s ease;
}

.step.active .step-icon {
  border-color: var(--accent-cyan);
  color: var(--accent-cyan);
  box-shadow: 0 0 20px rgba(0, 245, 255, 0.3);
}

.step span {
  font-size: 12px;
  color: var(--text-secondary);
}

/* 结果状态 */
.result-state {
  width: 100%;
}

.image-wrapper {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 24px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.generated-image {
  width: 100%;
  display: block;
  transition: transform 0.3s ease;
}

.image-wrapper:hover .generated-image {
  transform: scale(1.02);
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.image-wrapper:hover .image-overlay {
  opacity: 1;
}

.download-btn {
  width: 56px;
  height: 56px;
  background: var(--primary-gradient);
  border: none;
  font-size: 24px;
  transition: all 0.3s ease;
}

.download-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
}

/* 元数据区域 */
.metadata-section {
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 20px;
}

.metadata-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border-color);
}

.metadata-header h4 {
  font-size: 16px;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.metadata-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.metadata-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.metadata-item.full-width {
  grid-column: 1 / -1;
}

.item-label {
  font-size: 11px;
  color: var(--text-secondary);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.item-value {
  font-size: 13px;
  color: var(--text-primary);
  font-weight: 500;
  word-break: break-word;
}

/* 空状态 */
.empty-state {
  text-align: center;
  padding: 60px 20px;
}

.empty-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto 24px;
  border-radius: 50%;
  background: var(--card-bg);
  border: 2px dashed var(--border-color);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 36px;
  color: var(--text-secondary);
}

.empty-state h3 {
  font-size: 18px;
  color: var(--text-primary);
  margin: 0 0 8px 0;
}

.empty-state p {
  font-size: 14px;
  color: var(--text-secondary);
  margin: 0;
}
</style>
