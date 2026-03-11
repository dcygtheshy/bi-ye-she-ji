<template>
  <div class="generation-page">
    <el-card class="page-card">
      <template #header>
        <div class="card-header">
          <span>图像生成</span>
          <el-tag type="info">使用Mock数据演示</el-tag>
        </div>
      </template>

      <el-row :gutter="24">
        <!-- 左侧：生成表单 -->
        <el-col :span="10">
          <el-form :model="form" label-width="120px" label-position="left">
            <el-form-item label="文本提示">
              <el-input
                v-model="form.prompt"
                type="textarea"
                :rows="4"
                placeholder="请输入图像描述，例如：A beautiful sunset over the ocean"
              />
            </el-form-item>

            <el-form-item label="水印消息">
              <el-input
                v-model="form.watermarkMessage"
                placeholder="例如：SWU-2024"
              />
            </el-form-item>

            <el-form-item label="启用水印">
              <el-switch v-model="form.withWatermark" />
            </el-form-item>

            <el-form-item label="推理步数">
              <el-slider v-model="form.numSteps" :min="20" :max="100" :step="10" show-input />
            </el-form-item>

            <el-form-item label="引导系数">
              <el-slider v-model="form.guidanceScale" :min="1" :max="15" :step="0.5" show-input />
            </el-form-item>

            <el-form-item>
              <el-button type="primary" @click="handleGenerate" :loading="loading" size="large">
                <el-icon><Picture /></el-icon>
                生成图像
              </el-button>
            </el-form-item>
          </el-form>
        </el-col>

        <!-- 右侧：图像预览 -->
        <el-col :span="14">
          <div class="preview-area">
            <div v-if="loading" class="loading-container">
              <el-progress :percentage="progress" :stroke-width="20" />
              <p class="loading-text">正在生成图像，请稍候...</p>
            </div>

            <div v-else-if="generatedImage" class="image-container">
              <img :src="generatedImage" alt="Generated Image" class="generated-image" />
              <div class="image-actions">
                <el-button type="success" @click="handleDownload">
                  <el-icon><Download /></el-icon>
                  下载图像
                </el-button>
              </div>
              <div class="metadata">
                <el-descriptions title="生成信息" :column="1" border>
                  <el-descriptions-item label="任务ID">{{ metadata.taskId }}</el-descriptions-item>
                  <el-descriptions-item label="生成时间">{{ metadata.timestamp }}</el-descriptions-item>
                  <el-descriptions-item label="文本提示">{{ metadata.prompt }}</el-descriptions-item>
                  <el-descriptions-item label="水印消息">{{ metadata.watermarkMessage || '无' }}</el-descriptions-item>
                  <el-descriptions-item label="推理步数">{{ metadata.numSteps }}</el-descriptions-item>
                  <el-descriptions-item label="引导系数">{{ metadata.guidanceScale }}</el-descriptions-item>
                </el-descriptions>
              </div>
            </div>

            <el-empty v-else description="请配置参数并点击生成图像" />
          </div>
        </el-col>
      </el-row>
    </el-card>
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
.generation-page {
  height: 100%;
}

.page-card {
  height: 100%;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.preview-area {
  min-height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.loading-container {
  width: 100%;
  text-align: center;
}

.loading-text {
  margin-top: 20px;
  color: #666;
  font-size: 14px;
}

.image-container {
  width: 100%;
}

.generated-image {
  width: 100%;
  max-width: 512px;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  display: block;
  margin: 0 auto;
}

.image-actions {
  text-align: center;
  margin-top: 20px;
}

.metadata {
  margin-top: 24px;
}
</style>
