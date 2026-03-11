# 项目结构说明

## 目录树

```
毕业设计/
├── frontend/                         # 前端应用
│   ├── public/                      # 静态资源
│   │   └── favicon.ico
│   ├── src/
│   │   ├── assets/                  # 资源文件
│   │   │   ├── images/              # 图片资源
│   │   │   └── styles/              # 全局样式
│   │   ├── components/              # Vue组件
│   │   │   ├── Layout/              # 布局组件
│   │   │   │   ├── Header.vue       # 顶部导航
│   │   │   │   ├── Sidebar.vue      # 侧边栏
│   │   │   │   └── MainLayout.vue   # 主布局
│   │   │   ├── Generation/          # 图像生成模块
│   │   │   │   ├── GenerationForm.vue
│   │   │   │   ├── ImagePreview.vue
│   │   │   │   └── index.vue
│   │   │   ├── Detection/           # 水印检测模块
│   │   │   │   ├── ImageUpload.vue
│   │   │   │   ├── DetectionResult.vue
│   │   │   │   └── index.vue
│   │   │   ├── Attack/              # 攻击模拟模块
│   │   │   │   ├── AttackConfig.vue
│   │   │   │   ├── AttackResult.vue
│   │   │   │   └── index.vue
│   │   │   └── Evaluation/          # 性能评估模块
│   │   │       ├── EvaluationConfig.vue
│   │   │       ├── MetricsChart.vue
│   │   │       └── index.vue
│   │   ├── api/                     # API服务层
│   │   │   ├── request.js           # Axios配置
│   │   │   ├── generation.js        # 图像生成API
│   │   │   ├── detection.js         # 水印检测API
│   │   │   ├── attack.js            # 攻击模拟API
│   │   │   ├── evaluation.js        # 性能评估API
│   │   │   └── mock.js              # Mock数据
│   │   ├── stores/                  # Pinia状态管理
│   │   │   └── app.js               # 应用状态
│   │   ├── router/                  # 路由配置
│   │   │   └── index.js             # 路由定义
│   │   ├── utils/                   # 工具函数
│   │   │   ├── format.js            # 格式化工具
│   │   │   └── constants.js         # 常量定义
│   │   ├── App.vue                  # 根组件
│   │   └── main.js                  # 入口文件
│   ├── index.html                   # HTML模板
│   ├── package.json                 # 依赖配置
│   ├── vite.config.js               # Vite配置
│   └── README.md                    # 前端说明
│
├── backend/                          # 后端骨架
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                  # FastAPI入口
│   │   ├── api/                     # API路由
│   │   │   ├── __init__.py
│   │   │   ├── generation.py        # 图像生成路由
│   │   │   ├── detection.py         # 水印检测路由
│   │   │   ├── attack.py            # 攻击模拟路由
│   │   │   └── evaluation.py        # 性能评估路由
│   │   └── models/                  # Pydantic数据模型
│   │       ├── __init__.py
│   │       ├── generation.py
│   │       ├── detection.py
│   │       └── evaluation.py
│   ├── requirements.txt             # Python依赖
│   └── README.md                    # 后端说明
│
├── docs/                             # 文档
│   ├── API.md                       # API接口规范
│   ├── FRONTEND.md                  # 前端开发说明
│   └── STRUCTURE.md                 # 项目结构说明（本文件）
│
├── CLAUDE.md                         # Claude开发指南
├── 开题报告.md                       # 毕业设计开题报告
└── README.md                         # 项目总README
```

## 模块说明

### 前端模块

#### 1. Layout（布局）
- **MainLayout.vue:** 主布局组件，包含侧边栏和顶部导航
- **Sidebar.vue:** 侧边栏导航菜单
- **Header.vue:** 顶部导航栏

#### 2. Generation（图像生成）
- **GenerationForm.vue:** 图像生成表单，包含Prompt输入、参数配置
- **ImagePreview.vue:** 图像预览组件，显示生成的图像和元数据
- **index.vue:** 图像生成页面入口

#### 3. Detection（水印检测）
- **ImageUpload.vue:** 图像上传组件，支持拖拽上传
- **DetectionResult.vue:** 检测结果展示，包含BER、置信度等
- **index.vue:** 水印检测页面入口

#### 4. Attack（攻击模拟）
- **AttackConfig.vue:** 攻击配置组件，选择攻击类型和参数
- **AttackResult.vue:** 攻击结果展示，对比原图和攻击后图像
- **index.vue:** 攻击模拟页面入口

#### 5. Evaluation（性能评估）
- **EvaluationConfig.vue:** 评估配置组件，设置数据集大小和Prompt
- **MetricsChart.vue:** 性能指标图表，展示FID和CLIP Score
- **index.vue:** 性能评估页面入口

### API服务层

- **request.js:** Axios实例配置，统一请求拦截和错误处理
- **generation.js:** 图像生成相关API
- **detection.js:** 水印检测相关API
- **attack.js:** 攻击模拟相关API
- **evaluation.js:** 性能评估相关API
- **mock.js:** Mock数据服务，模拟后端响应

### 状态管理

- **app.js:** 应用全局状态，包括用户设置、生成历史等

### 路由

- **index.js:** 路由配置，定义四个主要页面的路由

### 工具函数

- **format.js:** 格式化工具（日期、数字等）
- **constants.js:** 常量定义（API地址、配置项等）

### 后端模块

#### API路由
- **generation.py:** 图像生成接口
- **detection.py:** 水印检测接口
- **attack.py:** 攻击模拟接口
- **evaluation.py:** 性能评估接口

#### 数据模型
- **generation.py:** 图像生成请求/响应模型
- **detection.py:** 水印检测请求/响应模型
- **evaluation.py:** 性能评估请求/响应模型

## 数据流

### 图像生成流程
```
用户输入 → GenerationForm → API调用 → Mock数据 → ImagePreview → 展示结果
```

### 水印检测流程
```
用户上传 → ImageUpload → API调用 → Mock数据 → DetectionResult → 展示结果
```

### 攻击模拟流程
```
选择图像 → AttackConfig → API调用 → Mock数据 → AttackResult → 展示对比
```

### 性能评估流程
```
配置参数 → EvaluationConfig → API调用 → Mock数据 → MetricsChart → 展示图表
```

## 技术架构

```
┌─────────────────────────────────────────┐
│           用户界面（Vue 3）              │
├─────────────────────────────────────────┤
│  Layout  │ Generation │ Detection │ ... │
├─────────────────────────────────────────┤
│         API服务层（Axios + Mock）        │
├─────────────────────────────────────────┤
│         状态管理（Pinia）                │
├─────────────────────────────────────────┤
│         路由管理（Vue Router）           │
└─────────────────────────────────────────┘
              ↓ HTTP请求（未来）
┌─────────────────────────────────────────┐
│         后端API（FastAPI）               │
├─────────────────────────────────────────┤
│  水印嵌入 │ 水印检测 │ 攻击模拟 │ 评估  │
├─────────────────────────────────────────┤
│    Stable Diffusion + Gaussian Shading  │
└─────────────────────────────────────────┘
```

## 开发阶段

### Phase 1: 项目搭建（当前）
- ✅ 创建目录结构
- ✅ 初始化前端项目
- ✅ 配置路由和布局
- ✅ 创建后端骨架
- ✅ 编写API文档

### Phase 2-5: 功能实现
- 图像生成模块
- 水印检测模块
- 攻击模拟模块
- 性能评估模块

### Phase 6: 优化与文档
- UI优化
- 错误处理
- 文档完善

## 文件命名规范

- **Vue组件:** PascalCase，如`GenerationForm.vue`
- **JavaScript文件:** camelCase，如`request.js`
- **Python文件:** snake_case，如`generation.py`
- **文档文件:** UPPERCASE，如`README.md`

## 注意事项

1. **前后端分离:** 前端和后端完全独立，通过API通信
2. **Mock数据:** 当前阶段前端使用Mock数据，无需启动后端
3. **模块化:** 每个功能模块独立，便于维护和扩展
4. **文档齐全:** 每个目录都有README说明
5. **代码规范:** 遵循Vue 3和Python最佳实践
