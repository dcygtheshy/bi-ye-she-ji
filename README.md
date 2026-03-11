# 基于扩散模型的数字水印检测和图像生成系统

## 项目简介

这是一个西南大学本科毕业设计项目，旨在构建一个基于Stable Diffusion扩散模型的数字水印检测和图像生成系统的Web Demo。

**核心功能：**
- 🎨 图像生成（带水印/不带水印）
- 🔍 水印检测与验证
- ⚔️ 攻击模拟与鲁棒性测试
- 📊 性能评估（FID/CLIP Score对比）

**技术栈：**
- 前端：Vue 3 + Element Plus + Vite
- 后端：FastAPI（骨架）
- 算法：Gaussian Shading水印嵌入

## 项目结构

```
毕业设计/
├── frontend/          # 前端应用（Vue 3）
├── backend/           # 后端骨架（FastAPI）
├── docs/              # 文档
├── CLAUDE.md          # Claude开发指南
└── 开题报告.md        # 开题报告
```

详细结构见 [docs/STRUCTURE.md](docs/STRUCTURE.md)

## 快速开始

### 前端开发

```bash
cd frontend
npm install
npm run dev
```

访问 http://localhost:3000

### 后端（暂未实现）

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 文档

- [API接口规范](docs/API.md)
- [前端开发说明](docs/FRONTEND.md)
- [项目结构说明](docs/STRUCTURE.md)
- [Claude开发指南](CLAUDE.md)
- [开题报告](开题报告.md)

## 开发进度

### Phase 1: 项目搭建 ✅
- [x] 创建项目目录结构
- [x] 初始化前端项目（Vite + Vue 3）
- [x] 配置路由和布局组件
- [x] 创建后端骨架目录
- [x] 编写API接口规范文档

### Phase 2: 图像生成模块 🚧
- [x] 实现GenerationForm组件
- [ ] 完善ImagePreview组件
- [ ] 实现Mock数据服务
- [ ] 集成表单提交和图像展示逻辑

### Phase 3: 水印检测模块
- [ ] 实现ImageUpload组件
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

## 当前状态

**已完成：**
- ✅ 项目结构搭建
- ✅ 前端基础框架（Vue 3 + Element Plus）
- ✅ 路由和布局组件
- ✅ 图像生成页面（基础版本）
- ✅ API接口规范文档
- ✅ 后端骨架

**下一步：**
- 安装前端依赖并启动项目
- 完善图像生成模块
- 实现水印检测模块

## 技术特点

1. **性能无损：** 采用Gaussian Shading算法，理论上不影响图像生成质量
2. **前后端分离：** 清晰的架构，便于维护和扩展
3. **Mock数据：** 前端可独立运行，无需后端支持
4. **美观界面：** 使用Element Plus，适合毕业答辩展示
5. **文档齐全：** 完整的API规范和开发文档

## 注意事项

- 当前阶段前端使用Mock数据，无需启动后端
- 后端目录仅作为接口规范和未来实现的占位
- 项目设计为本地运行，无需部署服务器

## 后续工作

完成前端Demo后，可以进行：
1. 后端核心算法实现（Gaussian Shading水印嵌入）
2. Stable Diffusion模型集成
3. 真实API接口开发
4. 前后端联调
5. 性能优化和部署

## 参考资料

- [Vue 3文档](https://cn.vuejs.org/)
- [Element Plus文档](https://element-plus.org/)
- [FastAPI文档](https://fastapi.tiangolo.com/)
- [Stable Diffusion](https://github.com/Stability-AI/stablediffusion)

## 许可证

本项目仅用于学术研究和毕业设计展示。

## 联系方式

西南大学 - 毕业设计项目
