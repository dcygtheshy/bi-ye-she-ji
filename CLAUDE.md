# 基于扩散模型的数字水印检测和图像生成系统

## 项目概述

这是一个西南大学本科毕业设计项目，旨在构建一个基于Stable Diffusion扩散模型的数字水印检测和图像生成系统的Web Demo。

**核心功能：**
1. 图像生成（带水印/不带水印）
2. 水印检测与验证
3. 攻击模拟与鲁棒性测试
4. 性能评估（FID/CLIP Score对比）

**当前阶段：** Phase 1 - 项目搭建和前端实现

## 技术栈

### 前端
- **Vue 3** + Composition API
- **Element Plus** - UI组件库
- **Vite** - 构建工具
- **Vue Router** - 路由管理
- **Pinia** - 状态管理
- **Axios** - HTTP请求
- **ECharts** - 数据可视化

### 后端（骨架）
- **FastAPI** - Python Web框架（暂不实现具体逻辑）
- **Pydantic** - 数据模型

## 项目结构

```
毕业设计/
├── frontend/                    # 前端应用
│   ├── src/
│   │   ├── components/         # Vue组件
│   │   │   ├── Layout/         # 布局组件
│   │   │   ├── Generation/     # 图像生成模块
│   │   │   ├── Detection/      # 水印检测模块
│   │   │   ├── Attack/         # 攻击模拟模块
│   │   │   └── Evaluation/     # 性能评估模块
│   │   ├── api/                # API服务层（含Mock数据）
│   │   ├── stores/             # Pinia状态管理
│   │   ├── router/             # 路由配置
│   │   └── utils/              # 工具函数
│   └── package.json
│
├── backend/                     # 后端骨架
│   ├── app/
│   │   ├── api/                # API路由（空骨架）
│   │   └── models/             # 数据模型
│   └── requirements.txt
│
├── docs/                        # 文档
│   ├── API.md                  # API接口规范
│   ├── FRONTEND.md             # 前端开发说明
│   └── STRUCTURE.md            # 项目结构说明
│
└── 开题报告.md
```

## 开发指南

### 前端开发

**启动开发服务器：**
```bash
cd frontend
npm install
npm run dev
```

**构建生产版本：**
```bash
npm run build
```

### 代码规范

1. **组件命名：** 使用PascalCase，如`GenerationForm.vue`
2. **文件组织：** 每个功能模块独立目录，包含`index.vue`作为入口
3. **API调用：** 统一通过`api/`目录下的服务层调用
4. **状态管理：** 全局状态使用Pinia，局部状态使用组件内`ref`/`reactive`
5. **样式：** 优先使用Element Plus组件样式，自定义样式使用scoped

### Mock数据策略

当前阶段前端使用Mock数据模拟后端响应：

- **图像生成：** 使用占位图片（Unsplash API或本地示例）
- **水印检测：** 随机生成BER值（0.05-0.15）和置信度（85%-95%）
- **攻击模拟：** 使用CSS滤镜模拟攻击效果
- **性能评估：** 预设FID和CLIP Score数据

所有Mock逻辑集中在`frontend/src/api/mock.js`中。

## API接口规范

详见 [docs/API.md](docs/API.md)

### 核心接口

1. **POST /api/generation/generate** - 生成图像
2. **GET /api/generation/status/{task_id}** - 查询生成状态
3. **POST /api/detection/detect** - 检测水印
4. **POST /api/attack/simulate** - 模拟攻击
5. **POST /api/evaluation/evaluate** - 性能评估

## 实现计划

### Phase 1: 项目搭建（当前阶段）
- [x] 创建项目目录结构
- [ ] 初始化前端项目（Vite + Vue 3）
- [ ] 安装前端依赖
- [ ] 配置路由和布局组件
- [ ] 创建后端骨架目录
- [ ] 编写API接口规范文档

### Phase 2: 图像生成模块
- [ ] 实现GenerationForm组件
- [ ] 实现ImagePreview组件
- [ ] 实现Mock数据服务
- [ ] 集成表单提交和图像展示逻辑

### Phase 3: 水印检测模块
- [ ] 实现ImageUpload组件（拖拽上传）
- [ ] 实现DetectionResult组件
- [ ] 实现Mock检测逻辑
- [ ] 添加可视化图表

### Phase 4: 攻击模拟模块
- [ ] 实现AttackConfig组件
- [ ] 实现AttackResult组件
- [ ] 使用CSS滤镜模拟攻击效果
- [ ] 实现批量测试表格

### Phase 5: 性能评估模块
- [ ] 实现EvaluationConfig组件
- [ ] 实现MetricsChart组件
- [ ] 实现Mock评估数据
- [ ] 添加数据可视化

### Phase 6: 优化与文档
- [ ] UI优化和响应式设计
- [ ] 添加错误处理和用户提示
- [ ] 编写前端开发文档
- [ ] 准备演示数据和截图

## 注意事项

1. **本地运行：** 项目设计为本地运行，无需部署服务器
2. **Mock数据：** 当前阶段完全使用前端Mock数据，无需启动后端
3. **后端骨架：** 后端目录仅作为接口规范和未来实现的占位
4. **美观优先：** 使用Element Plus确保界面美观，适合毕业答辩展示
5. **简单实用：** 避免过度工程化，专注于核心功能演示

## 后续工作

完成前端Demo后，可以进行：
1. 后端核心算法实现（Gaussian Shading水印嵌入）
2. Stable Diffusion模型集成
3. 真实API接口开发
4. 前后端联调
5. 性能优化和部署

## 参考资料

- [开题报告](开题报告.md)
- [实现计划](/.claude/plans/replicated-chasing-pond.md)
- [Element Plus文档](https://element-plus.org/)
- [Vue 3文档](https://cn.vuejs.org/)
- [ECharts文档](https://echarts.apache.org/zh/index.html)
