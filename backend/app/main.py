from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="水印检测系统API",
    description="基于扩散模型的数字水印检测和图像生成系统",
    version="1.0.0"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "水印检测系统API",
        "status": "骨架模式 - 暂未实现具体功能",
        "docs": "/docs"
    }

# TODO: 导入API路由
# from app.api import generation, detection, attack, evaluation
# app.include_router(generation.router, prefix="/api/generation", tags=["图像生成"])
# app.include_router(detection.router, prefix="/api/detection", tags=["水印检测"])
# app.include_router(attack.router, prefix="/api/attack", tags=["攻击模拟"])
# app.include_router(evaluation.router, prefix="/api/evaluation", tags=["性能评估"])
