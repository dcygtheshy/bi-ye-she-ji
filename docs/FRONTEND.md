# 前端开发说明

## 技术栈

- **Vue 3** - 渐进式JavaScript框架
- **Element Plus** - 基于Vue 3的UI组件库
- **Vite** - 下一代前端构建工具
- **Vue Router** - 官方路由管理器
- **Pinia** - Vue官方状态管理库
- **Axios** - HTTP客户端
- **ECharts** - 数据可视化库

## 项目结构

```
frontend/
├── public/                 # 静态资源
├── src/
│   ├── assets/            # 资源文件
│   │   ├── images/        # 图片
│   │   └── styles/        # 样式
│   ├── components/        # Vue组件
│   │   ├── Layout/        # 布局组件
│   │   ├── Generation/    # 图像生成模块
│   │   ├── Detection/     # 水印检测模块
│   │   ├── Attack/        # 攻击模拟模块
│   │   └── Evaluation/    # 性能评估模块
│   ├── api/               # API服务层
│   │   ├── request.js     # Axios配置
│   │   ├── generation.js  # 图像生成API
│   │   ├── detection.js   # 水印检测API
│   │   ├── attack.js      # 攻击模拟API
│   │   ├── evaluation.js  # 性能评估API
│   │   └── mock.js        # Mock数据
│   ├── stores/            # Pinia状态管理
│   │   └── app.js         # 应用状态
│   ├── router/            # 路由配置
│   │   └── index.js       # 路由定义
│   ├── utils/             # 工具函数
│   │   ├── format.js      # 格式化工具
│   │   └── constants.js   # 常量定义
│   ├── App.vue            # 根组件
│   └── main.js            # 入口文件
├── index.html             # HTML模板
├── package.json           # 依赖配置
└── vite.config.js         # Vite配置
```

## 开发指南

### 安装依赖

```bash
cd frontend
npm install
```

### 启动开发服务器

```bash
npm run dev
```

访问 http://localhost:3000

### 构建生产版本

```bash
npm run build
```

### 预览生产构建

```bash
npm run preview
```

## 组件开发规范

### 1. 组件命名

- 使用PascalCase命名组件文件，如`GenerationForm.vue`
- 组件名应该清晰描述其功能

### 2. 组件结构

```vue
<template>
  <!-- 模板 -->
</template>

<script setup>
// 使用Composition API
import { ref, computed } from 'vue'

// 组件逻辑
</script>

<style scoped>
/* 样式 */
</style>
```

### 3. 状态管理

**局部状态：** 使用`ref`或`reactive`

```javascript
const count = ref(0)
const form = reactive({ name: '', age: 0 })
```

**全局状态：** 使用Pinia

```javascript
import { useAppStore } from '@/stores/app'

const store = useAppStore()
```

### 4. API调用

统一通过`api/`目录下的服务层调用：

```javascript
import { generateImage } from '@/api/generation'

const handleGenerate = async () => {
  const result = await generateImage(params)
}
```

### 5. 样式规范

- 优先使用Element Plus组件样式
- 自定义样式使用`scoped`避免污染全局
- 使用CSS变量定义主题色

```css
<style scoped>
.my-component {
  color: var(--el-color-primary);
}
</style>
```

## Mock数据策略

当前阶段前端使用Mock数据模拟后端响应，所有Mock逻辑集中在`src/api/mock.js`中。

### Mock数据示例

```javascript
// src/api/mock.js
export const mockGenerateImage = async (params) => {
  // 模拟3秒延迟
  await new Promise(resolve => setTimeout(resolve, 3000))

  return {
    task_id: `gen_${Date.now()}`,
    status: 'completed',
    image_url: `https://picsum.photos/512/512?random=${Date.now()}`,
    metadata: {
      prompt: params.prompt,
      timestamp: new Date().toISOString()
    }
  }
}
```

### 使用Mock数据

```javascript
import { mockGenerateImage } from '@/api/mock'

const handleGenerate = async () => {
  const result = await mockGenerateImage(form.value)
  generatedImage.value = result.image_url
}
```

## 路由配置

路由定义在`src/router/index.js`中：

```javascript
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
      // ...其他路由
    ]
  }
]
```

## Element Plus使用

### 按需导入组件

已在`main.js`中全局注册Element Plus，可直接使用：

```vue
<template>
  <el-button type="primary">按钮</el-button>
  <el-input v-model="value" placeholder="请输入" />
</template>
```

### 图标使用

已全局注册所有Element Plus图标：

```vue
<template>
  <el-icon><Picture /></el-icon>
  <el-icon><Search /></el-icon>
</template>
```

### 消息提示

```javascript
import { ElMessage } from 'element-plus'

ElMessage.success('操作成功')
ElMessage.error('操作失败')
ElMessage.warning('警告信息')
```

## ECharts使用

### 安装

```bash
npm install echarts vue-echarts
```

### 使用示例

```vue
<template>
  <v-chart :option="chartOption" style="height: 400px" />
</template>

<script setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart } from 'echarts/charts'
import { GridComponent, TooltipComponent } from 'echarts/components'
import VChart from 'vue-echarts'

use([CanvasRenderer, BarChart, GridComponent, TooltipComponent])

const chartOption = {
  xAxis: { type: 'category', data: ['A', 'B', 'C'] },
  yAxis: { type: 'value' },
  series: [{ data: [120, 200, 150], type: 'bar' }]
}
</script>
```

## 常见问题

### 1. npm权限错误

```bash
sudo chown -R $(whoami) ~/.npm
```

### 2. 端口被占用

修改`vite.config.js`中的端口：

```javascript
export default defineConfig({
  server: {
    port: 3001  // 修改为其他端口
  }
})
```

### 3. 图片跨域问题

使用占位图片服务（如picsum.photos）或配置CORS。

## 开发建议

1. **组件拆分：** 保持组件单一职责，复杂组件拆分为多个子组件
2. **代码复用：** 提取公共逻辑到`utils/`或`composables/`
3. **类型安全：** 虽然使用JavaScript，但可以通过JSDoc添加类型注释
4. **性能优化：** 使用`v-if`而非`v-show`隐藏大型组件
5. **错误处理：** 统一处理API错误，提供友好的用户提示

## 下一步

完成Phase 1后，继续实现：
- Phase 2: 图像生成模块（完善GenerationForm和ImagePreview）
- Phase 3: 水印检测模块（实现ImageUpload和DetectionResult）
- Phase 4: 攻击模拟模块（实现AttackConfig和AttackResult）
- Phase 5: 性能评估模块（实现EvaluationConfig和MetricsChart）
