# API接口规范文档

## 概述

本文档定义了水印检测系统的RESTful API接口规范。当前阶段前端使用Mock数据，后端仅作为接口规范的占位。

**Base URL:** `http://localhost:8000/api`

**数据格式:** JSON

---

## 1. 图像生成接口

### 1.1 生成图像

**接口:** `POST /generation/generate`

**描述:** 根据文本提示生成带水印或不带水印的图像

**请求体:**
```json
{
  "prompt": "A beautiful sunset over the ocean",
  "watermark_message": "SWU-2024",
  "num_inference_steps": 50,
  "guidance_scale": 7.5,
  "with_watermark": true
}
```

**参数说明:**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| prompt | string | 是 | 文本提示，描述要生成的图像 |
| watermark_message | string | 否 | 水印消息内容 |
| num_inference_steps | integer | 否 | 推理步数，默认50，范围20-100 |
| guidance_scale | float | 否 | 引导系数，默认7.5，范围1-15 |
| with_watermark | boolean | 否 | 是否启用水印，默认true |

**响应体:**
```json
{
  "task_id": "gen_1234567890",
  "status": "processing",
  "image_url": null,
  "metadata": {
    "prompt": "A beautiful sunset over the ocean",
    "watermark_message": "SWU-2024",
    "timestamp": "2024-03-11T10:30:00Z"
  }
}
```

**状态码:**
- 200: 成功
- 400: 参数错误
- 500: 服务器错误

---

### 1.2 查询生成状态

**接口:** `GET /generation/status/{task_id}`

**描述:** 查询图像生成任务的状态

**路径参数:**
| 参数 | 类型 | 说明 |
|------|------|------|
| task_id | string | 任务ID |

**响应体（处理中）:**
```json
{
  "task_id": "gen_1234567890",
  "status": "processing",
  "progress": 45,
  "image_url": null
}
```

**响应体（完成）:**
```json
{
  "task_id": "gen_1234567890",
  "status": "completed",
  "progress": 100,
  "image_url": "/outputs/generated/gen_1234567890.png",
  "metadata": {
    "prompt": "A beautiful sunset over the ocean",
    "watermark_message": "SWU-2024",
    "num_inference_steps": 50,
    "guidance_scale": 7.5,
    "timestamp": "2024-03-11T10:30:00Z"
  }
}
```

**状态说明:**
- `processing`: 处理中
- `completed`: 已完成
- `failed`: 失败

---

## 2. 水印检测接口

### 2.1 检测水印

**接口:** `POST /detection/detect`

**描述:** 检测图像中是否包含水印

**请求体:** `multipart/form-data`
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| image | file | 是 | 图像文件 |
| key | string | 是 | 密钥字符串 |

**响应体:**
```json
{
  "has_watermark": true,
  "ber": 0.08,
  "confidence": 0.92,
  "extracted_message": "SWU-2024",
  "threshold": 0.1
}
```

**参数说明:**
| 参数 | 类型 | 说明 |
|------|------|------|
| has_watermark | boolean | 是否检测到水印 |
| ber | float | 比特错误率（Bit Error Rate） |
| confidence | float | 置信度分数（0-1） |
| extracted_message | string | 提取的水印消息 |
| threshold | float | BER判定阈值 |

**判定逻辑:**
- BER < 0.1: 检测到水印（高置信度）
- 0.1 ≤ BER < 0.3: 可能包含水印（中等置信度）
- BER ≥ 0.3: 未检测到水印

---

## 3. 攻击模拟接口

### 3.1 模拟攻击

**接口:** `POST /attack/simulate`

**描述:** 对图像进行攻击模拟并检测水印鲁棒性

**请求体:**
```json
{
  "image_id": "gen_1234567890",
  "attack_type": "jpeg_compression",
  "attack_params": {
    "quality": 50
  }
}
```

**攻击类型及参数:**

| 攻击类型 | attack_type | 参数 | 说明 |
|---------|-------------|------|------|
| JPEG压缩 | jpeg_compression | quality (10-100) | 压缩质量 |
| 缩放 | resize | scale (0.5-2.0) | 缩放比例 |
| 裁剪 | crop | crop_ratio (0.5-0.9) | 裁剪比例 |
| 旋转 | rotation | angle (-30~30) | 旋转角度 |
| 高斯噪声 | gaussian_noise | std (5-20) | 标准差 |
| 椒盐噪声 | salt_pepper_noise | prob (0.01-0.05) | 噪声概率 |
| 高斯模糊 | gaussian_blur | kernel_size (3-9) | 核大小 |
| 中值滤波 | median_filter | kernel_size (3-7) | 核大小 |

**响应体:**
```json
{
  "attacked_image_url": "/outputs/attacked/attack_1234567890.png",
  "detection_result": {
    "has_watermark": true,
    "ber": 0.15,
    "confidence": 0.75
  },
  "attack_info": {
    "attack_type": "jpeg_compression",
    "attack_params": {
      "quality": 50
    }
  }
}
```

---

### 3.2 批量攻击测试

**接口:** `POST /attack/batch`

**描述:** 对同一图像进行多种攻击测试

**请求体:**
```json
{
  "image_id": "gen_1234567890",
  "attacks": [
    {
      "attack_type": "jpeg_compression",
      "attack_params": {"quality": 50}
    },
    {
      "attack_type": "gaussian_noise",
      "attack_params": {"std": 10}
    }
  ]
}
```

**响应体:**
```json
{
  "results": [
    {
      "attack_type": "jpeg_compression",
      "attack_params": {"quality": 50},
      "ber": 0.12,
      "has_watermark": true
    },
    {
      "attack_type": "gaussian_noise",
      "attack_params": {"std": 10},
      "ber": 0.18,
      "has_watermark": true
    }
  ]
}
```

---

## 4. 性能评估接口

### 4.1 开始评估

**接口:** `POST /evaluation/evaluate`

**描述:** 批量生成图像并计算FID和CLIP Score

**请求体:**
```json
{
  "dataset_size": 100,
  "prompts": [
    "A cat sitting on a chair",
    "A dog running in the park",
    "A sunset over the ocean"
  ]
}
```

**参数说明:**
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| dataset_size | integer | 是 | 数据集大小 |
| prompts | array | 是 | 文本提示列表 |

**响应体:**
```json
{
  "task_id": "eval_1234567890",
  "status": "processing",
  "progress": 0
}
```

---

### 4.2 查询评估结果

**接口:** `GET /evaluation/result/{task_id}`

**描述:** 查询性能评估结果

**路径参数:**
| 参数 | 类型 | 说明 |
|------|------|------|
| task_id | string | 任务ID |

**响应体:**
```json
{
  "task_id": "eval_1234567890",
  "status": "completed",
  "results": {
    "fid_score_no_watermark": 12.3,
    "fid_score_with_watermark": 12.5,
    "clip_score_no_watermark": 0.82,
    "clip_score_with_watermark": 0.81,
    "comparison_report": {
      "fid_difference": 0.2,
      "clip_difference": -0.01,
      "conclusion": "性能无损：FID和CLIP Score差异在可接受范围内"
    }
  }
}
```

**指标说明:**
- **FID (Fréchet Inception Distance):** 越低越好，衡量生成图像与真实图像的相似度
- **CLIP Score:** 越高越好，衡量图像与文本提示的匹配度

---

## 5. 错误响应

所有接口在发生错误时返回统一格式：

```json
{
  "error": {
    "code": "INVALID_PARAMETER",
    "message": "参数错误：prompt不能为空",
    "details": {}
  }
}
```

**错误码:**
- `INVALID_PARAMETER`: 参数错误
- `TASK_NOT_FOUND`: 任务不存在
- `FILE_TOO_LARGE`: 文件过大
- `UNSUPPORTED_FORMAT`: 不支持的文件格式
- `INTERNAL_ERROR`: 内部错误

---

## 6. 数据模型

### GenerationRequest
```python
class GenerationRequest(BaseModel):
    prompt: str
    watermark_message: Optional[str] = None
    num_inference_steps: int = 50
    guidance_scale: float = 7.5
    with_watermark: bool = True
```

### DetectionResult
```python
class DetectionResult(BaseModel):
    has_watermark: bool
    ber: float
    confidence: float
    extracted_message: Optional[str]
    threshold: float = 0.1
```

### AttackRequest
```python
class AttackRequest(BaseModel):
    image_id: str
    attack_type: str
    attack_params: dict
```

### EvaluationRequest
```python
class EvaluationRequest(BaseModel):
    dataset_size: int
    prompts: List[str]
```

---

## 7. 认证与授权

当前版本无需认证。后续版本可能添加API Key认证。

---

## 8. 速率限制

当前版本无速率限制。后续版本可能添加：
- 每分钟最多10次图像生成请求
- 每分钟最多50次检测请求

---

## 9. 版本历史

- **v1.0.0** (2024-03-11): 初始版本，定义核心接口规范
