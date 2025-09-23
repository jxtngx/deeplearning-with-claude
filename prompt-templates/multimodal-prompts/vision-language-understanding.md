<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Multimodal Task Prompts

## Vision-Language Understanding

**User Story:**
As a multimodal AI researcher
I want to build models that understand both images and text
So that I can enable zero-shot classification and cross-modal retrieval

**Prompt:**
"I need to implement a vision-language model using CLIP, ALIGN, or BLIP variants that can process images at 224x224 resolution and text up to 77 tokens. The model should achieve over 70% zero-shot classification accuracy and support efficient image-text matching with contrastive learning. Please build the complete pipeline including multi-lingual support, hard negative mining, image augmentation, gradient accumulation for large batches, image search functionality, and embedding visualization tools."

### CONSTRAINTS
- Model: CLIP, ALIGN, or BLIP variants
- Image resolution: 224x224 minimum
- Text length: Up to 77 tokens
- Batch size: Optimize for available GPU memory

### REWARDS
- Zero-shot classification accuracy >70%
- Efficient image-text matching
- Multi-lingual support
- Contrastive learning implementation

### PENALTIES
- No image augmentation pipeline
- Missing hard negative mining
- Poor batch sampling strategy

### GOAL STATE
- Trained vision-language model
- Image search functionality
- Zero-shot classifier interface
- Embedding visualization