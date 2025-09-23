<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Computer Vision Task Prompts

## Image Classification

**User Story:**
As a computer vision engineer
I want to build a high-accuracy image classifier using transfer learning
So that I can categorize images efficiently while minimizing training costs

**Prompt:**
"I need to build an image classification system using PyTorch and HuggingFace. The system should leverage pre-trained Vision Transformers or ResNet models to classify images from either ImageNet-1K or CIFAR-10. I have access to GPUs but need to keep training under 8 hours. The model must achieve over 90% accuracy while maintaining fast inference speeds below 50ms per image. Please help me set up the complete pipeline including data loading, model selection, training loop, and API deployment."

### CONSTRAINTS
- Dataset: ImageNet-1K or CIFAR-10
- Model family: Vision Transformers or ResNet variants
- Training budget: 8 GPU hours maximum
- Inference latency: <50ms per image

### REWARDS
- Achieve >90% top-1 accuracy on validation set
- Model size under 100MB
- Support mixed precision training
- Implement data augmentation pipeline

### PENALTIES
- Overfitting (>5% train-val gap)
- Memory leaks during training
- Missing reproducibility seeds

### GOAL STATE
- Trained model with checkpoints
- Evaluation metrics dashboard
- Inference API endpoint
- Documentation of hyperparameters

---

## Object Detection

**User Story:**
As a robotics engineer
I want to implement real-time object detection with bounding boxes
So that my autonomous system can identify and track multiple objects simultaneously

**Prompt:**
"I need to implement a real-time object detection system that can process video streams at over 30 FPS. The system should use modern architectures like YOLO, Faster R-CNN, or DETR to detect objects in 640x640 resolution images. I'm working with COCO dataset format and need the model to achieve mAP@0.5 above 0.7. The solution must include visualization capabilities, performance benchmarking, and be deployable to edge devices via ONNX export. Please architect the complete detection pipeline with multi-scale training and optimized NMS."

### CONSTRAINTS
- Framework: YOLO, Faster R-CNN, or DETR
- Input resolution: 640x640
- Real-time requirement: >30 FPS
- Dataset: COCO or custom annotated data

### REWARDS
- mAP@0.5 above 0.7
- Multi-scale training implementation
- NMS optimization
- Anchor-free approach consideration

### PENALTIES
- False positive rate >10%
- GPU memory overflow
- Missing bounding box post-processing

### GOAL STATE
- Detection model with visualization
- Performance benchmarks
- Export to ONNX format
- Edge deployment ready

---

## Semantic Segmentation

**User Story:**
As a medical imaging specialist
I want to perform pixel-level segmentation of images into multiple classes
So that I can accurately identify and measure regions of interest in scans

**Prompt:**
"I need to build a semantic segmentation model for multi-class image segmentation with up to 20 categories. The model should use architectures like U-Net, DeepLab, or SegFormer to process images at minimum 512x512 resolution while fitting on a single GPU. The system needs to achieve mean IoU above 0.75 with efficient inference under 100ms. Please implement the complete pipeline including multi-scale inference, boundary refinement, colormap visualization, per-class metrics, and both web demo and mobile-optimized variants."

### CONSTRAINTS
- Architecture: U-Net, DeepLab, or SegFormer
- Resolution: Minimum 512x512
- Classes: Up to 20 categories
- Memory: Fit on single GPU

### REWARDS
- Mean IoU >0.75
- Efficient backbone selection
- Multi-scale inference
- Boundary refinement

### PENALTIES
- Class imbalance handling missing
- Inference time >100ms
- Missing CRF post-processing option

### GOAL STATE
- Segmentation model with colormap
- Per-class metrics
- Interactive web demo
- Mobile-optimized variant