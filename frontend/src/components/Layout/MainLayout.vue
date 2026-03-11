<template>
  <el-container class="main-layout">
    <!-- 侧边栏 -->
    <el-aside width="200px" class="sidebar">
      <div class="logo">
        <h2>水印检测系统</h2>
      </div>
      <el-menu
        :default-active="activeMenu"
        class="sidebar-menu"
        @select="handleMenuSelect"
      >
        <el-menu-item index="/generation">
          <el-icon><Picture /></el-icon>
          <span>图像生成</span>
        </el-menu-item>
        <el-menu-item index="/detection">
          <el-icon><Search /></el-icon>
          <span>水印检测</span>
        </el-menu-item>
        <el-menu-item index="/attack">
          <el-icon><Warning /></el-icon>
          <span>攻击模拟</span>
        </el-menu-item>
        <el-menu-item index="/evaluation">
          <el-icon><DataAnalysis /></el-icon>
          <span>性能评估</span>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <!-- 主内容区 -->
    <el-container>
      <!-- 顶部导航 -->
      <el-header class="header">
        <div class="header-content">
          <h3>{{ currentTitle }}</h3>
          <div class="header-right">
            <span>基于扩散模型的数字水印检测和图像生成系统</span>
          </div>
        </div>
      </el-header>

      <!-- 内容区域 -->
      <el-main class="main-content">
        <router-view />
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
.main-layout {
  height: 100vh;
}

.sidebar {
  background: #001529;
  color: #fff;
}

.logo {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #002140;
}

.logo h2 {
  color: #fff;
  font-size: 18px;
  margin: 0;
}

.sidebar-menu {
  border-right: none;
  background: #001529;
}

.sidebar-menu .el-menu-item {
  color: rgba(255, 255, 255, 0.65);
}

.sidebar-menu .el-menu-item:hover {
  color: #fff;
  background: #1890ff;
}

.sidebar-menu .el-menu-item.is-active {
  color: #fff;
  background: #1890ff;
}

.header {
  background: #fff;
  border-bottom: 1px solid #f0f0f0;
  padding: 0 24px;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}

.header-content h3 {
  margin: 0;
  font-size: 20px;
  color: #000;
}

.header-right {
  color: #666;
  font-size: 14px;
}

.main-content {
  background: #f0f2f5;
  padding: 24px;
  overflow-y: auto;
}
</style>
