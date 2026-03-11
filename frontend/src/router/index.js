import { createRouter, createWebHistory } from 'vue-router'
import MainLayout from '@/components/Layout/MainLayout.vue'

const routes = [
  {
    path: '/',
    component: MainLayout,
    redirect: '/generation',
    children: [
      {
        path: '/generation',
        name: 'Generation',
        component: () => import('@/components/Generation/index.vue'),
        meta: { title: '图像生成' }
      },
      {
        path: '/detection',
        name: 'Detection',
        component: () => import('@/components/Detection/index.vue'),
        meta: { title: '水印检测' }
      },
      {
        path: '/attack',
        name: 'Attack',
        component: () => import('@/components/Attack/index.vue'),
        meta: { title: '攻击模拟' }
      },
      {
        path: '/evaluation',
        name: 'Evaluation',
        component: () => import('@/components/Evaluation/index.vue'),
        meta: { title: '性能评估' }
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
