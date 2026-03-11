# 后端骨架

这是后端API的骨架结构，暂不实现具体逻辑。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行（占位）

```bash
cd backend
uvicorn app.main:app --reload
```

## 说明

当前阶段前端使用Mock数据，后端仅作为接口规范的占位。后续将实现：

1. Gaussian Shading水印嵌入算法
2. Stable Diffusion模型集成
3. 水印检测和验证
4. 攻击模拟
5. 性能评估（FID/CLIP Score）
