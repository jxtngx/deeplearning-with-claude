<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Computer Vision Task Prompts

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