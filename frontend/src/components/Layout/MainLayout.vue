<template>
  <el-container class="main-layout">
    <!-- 侧边栏 -->
    <el-aside width="280px" class="sidebar">
      <div class="logo">
        <div class="logo-icon">
          <div class="icon-layer layer-1"></div>
          <div class="icon-layer layer-2"></div>
          <div class="icon-layer layer-3"></div>
        </div>
        <div class="logo-text">
          <h2>WATERMARK</h2>
          <span class="subtitle">Detection System</span>
        </div>
      </div>

      <div class="menu-section">
        <div class="section-label">核心功能</div>
        <el-menu
          :default-active="activeMenu"
          class="sidebar-menu"
          @select="handleMenuSelect"
        >
          <el-menu-item index="/generation" class="menu-item-custom">
            <div class="menu-item-content">
              <el-icon class="menu-icon"><Picture /></el-icon>
              <div class="menu-text">
                <span class="menu-title">图像生成</span>
                <span class="menu-desc">AI Image Generation</span>
              </div>
            </div>
          </el-menu-item>
          <el-menu-item index="/detection" class="menu-item-custom">
            <div class="menu-item-content">
              <el-icon class="menu-icon"><Search /></el-icon>
              <div class="menu-text">
                <span class="menu-title">水印检测</span>
                <span class="menu-desc">Watermark Detection</span>
              </div>
            </div>
          </el-menu-item>
          <el-menu-item index="/attack" class="menu-item-custom">
            <div class="menu-item-content">
              <el-icon class="menu-icon"><Warning /></el-icon>
              <div class="menu-text">
                <span class="menu-title">攻击模拟</span>
                <span class="menu-desc">Attack Simulation</span>
              </div>
            </div>
          </el-menu-item>
          <el-menu-item index="/evaluation" class="menu-item-custom">
            <div class="menu-item-content">
              <el-icon class="menu-icon"><DataAnalysis /></el-icon>
              <div class="menu-text">
                <span class="menu-title">性能评估</span>
                <span class="menu-desc">Performance Metrics</span>
              </div>
            </div>
          </el-menu-item>
        </el-menu>
      </div>

      <div class="sidebar-footer">
        <div class="footer-info">
          <div class="info-item">
            <span class="info-label">Version</span>
            <span class="info-value">1.0.0</span>
          </div>
          <div class="info-item">
            <span class="info-label">Model</span>
            <span class="info-value">SD v2.1</span>
          </div>
        </div>
      </div>
    </el-aside>

    <!-- 主内容区 -->
    <el-container>
      <!-- 顶部导航 -->
      <el-header class="header">
        <div class="header-content">
          <div class="header-left">
            <h3 class="page-title">{{ currentTitle }}</h3>
            <div class="breadcrumb">
              <span class="breadcrumb-item">系统</span>
              <span class="breadcrumb-separator">/</span>
              <span class="breadcrumb-item active">{{ currentTitle }}</span>
            </div>
          </div>
          <div class="header-right">
            <div class="system-info">
              <div class="info-badge">
                <span class="badge-dot"></span>
                <span class="badge-text">基于扩散模型的数字水印检测和图像生成系统</span>
              </div>
            </div>
          </div>
        </div>
      </el-header>

      <!-- 内容区域 -->
      <el-main class="main-content">
        <div class="content-wrapper">
          <router-view v-slot="{ Component }">
            <transition name="fade-slide" mode="out-in">
              <component :is="Component" />
            </transition>
          </router-view>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const activeMenu = computed(() => route.path)
const currentTitle = computed(() => route.meta.title || '')

const handleMenuSelect = (index) => {
  router.push(index)
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

.main-layout {
  height: 100vh;
  background: var(--darker-bg);
  font-family: 'Noto Sans SC', sans-serif;
}

/* ========== 侧边栏样式 ========== */
.sidebar {
  background: var(--dark-bg);
  border-right: 1px solid var(--border-color);
  position: relative;
  overflow: hidden;
}

.sidebar::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 300px;
  background: radial-gradient(circle at 50% 0%, rgba(102, 126, 234, 0.15), transparent 70%);
  pointer-events: none;
}

/* Logo区域 */
.logo {
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  padding: 24px;
  position: relative;
  z-index: 1;
}

.logo-icon {
  width: 48px;
  height: 48px;
  position: relative;
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

.icon-layer {
  position: absolute;
  width: 100%;
  height: 100%;
  border: 2px solid;
  border-radius: 12px;
  animation: rotate-layers 8s linear infinite;
}

.layer-1 {
  border-color: var(--accent-cyan);
  animation-delay: 0s;
}

.layer-2 {
  border-color: var(--accent-magenta);
  animation-delay: -2.67s;
  transform: rotate(45deg);
}

.layer-3 {
  border-color: #667eea;
  animation-delay: -5.33s;
  transform: rotate(90deg);
}

@keyframes rotate-layers {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.logo-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.logo-text h2 {
  font-family: 'Orbitron', sans-serif;
  font-size: 20px;
  font-weight: 800;
  margin: 0;
  background: linear-gradient(135deg, var(--accent-cyan), var(--accent-magenta));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: 1px;
}

.subtitle {
  font-size: 10px;
  color: var(--text-secondary);
  font-weight: 500;
  letter-spacing: 2px;
  text-transform: uppercase;
}

/* 菜单区域 */
.menu-section {
  padding: 0 16px;
  margin-top: 24px;
}

.section-label {
  font-size: 11px;
  color: var(--text-secondary);
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 0 16px 12px;
  margin-bottom: 8px;
}

.sidebar-menu {
  border-right: none;
  background: transparent;
}

.menu-item-custom {
  margin-bottom: 8px;
  border-radius: 12px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.menu-item-custom::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: var(--primary-gradient);
  transform: scaleY(0);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.menu-item-custom:hover::before,
.menu-item-custom.is-active::before {
  transform: scaleY(1);
}

.menu-item-content {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 4px 8px;
}

.menu-icon {
  font-size: 22px;
  color: var(--text-secondary);
  transition: all 0.3s ease;
}

.menu-item-custom:hover .menu-icon,
.menu-item-custom.is-active .menu-icon {
  color: var(--accent-cyan);
  transform: scale(1.1);
}

.menu-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.menu-title {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  transition: color 0.3s ease;
}

.menu-desc {
  font-size: 10px;
  color: var(--text-secondary);
  font-weight: 400;
  letter-spacing: 0.5px;
}

.menu-item-custom:hover {
  background: var(--card-bg);
}

.menu-item-custom.is-active {
  background: linear-gradient(90deg, rgba(102, 126, 234, 0.15), transparent);
}

.menu-item-custom.is-active .menu-title {
  background: linear-gradient(135deg, var(--accent-cyan), var(--accent-magenta));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* 侧边栏底部 */
.sidebar-footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 24px;
  border-top: 1px solid var(--border-color);
  background: rgba(0, 0, 0, 0.2);
}

.footer-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.info-label {
  font-size: 11px;
  color: var(--text-secondary);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.info-value {
  font-family: 'Orbitron', monospace;
  font-size: 12px;
  color: var(--accent-cyan);
  font-weight: 600;
}

/* ========== 顶部导航样式 ========== */
.header {
  background: var(--dark-bg);
  border-bottom: 1px solid var(--border-color);
  padding: 0 32px;
  position: relative;
}

.header::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--accent-cyan), transparent);
  opacity: 0.3;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}

.header-left {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.page-title {
  margin: 0;
  font-size: 24px;
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: 0.5px;
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
}

.breadcrumb-item {
  color: var(--text-secondary);
  transition: color 0.3s ease;
}

.breadcrumb-item.active {
  color: var(--accent-cyan);
  font-weight: 600;
}

.breadcrumb-separator {
  color: var(--border-color);
}

.header-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.system-info {
  display: flex;
  align-items: center;
}

.info-badge {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 16px;
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 20px;
  transition: all 0.3s ease;
}

.info-badge:hover {
  background: rgba(102, 126, 234, 0.1);
  border-color: var(--accent-cyan);
}

.badge-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent-cyan);
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(1.2); }
}

.badge-text {
  font-size: 13px;
  color: var(--text-secondary);
  font-weight: 500;
}

/* ========== 主内容区样式 ========== */
.main-content {
  background: var(--darker-bg);
  padding: 32px;
  overflow-y: auto;
  position: relative;
}

.main-content::before {
  content: '';
  position: fixed;
  top: 0;
  left: 280px;
  right: 0;
  bottom: 0;
  background-image:
    radial-gradient(circle at 20% 30%, rgba(102, 126, 234, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(255, 0, 110, 0.08) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}

.content-wrapper {
  position: relative;
  z-index: 1;
}

/* 页面切换动画 */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

/* 滚动条样式 */
.main-content::-webkit-scrollbar {
  width: 8px;
}

.main-content::-webkit-scrollbar-track {
  background: var(--darker-bg);
}

.main-content::-webkit-scrollbar-thumb {
  background: var(--border-color);
  border-radius: 4px;
  transition: background 0.3s ease;
}

.main-content::-webkit-scrollbar-thumb:hover {
  background: rgba(102, 126, 234, 0.5);
}
</style>
