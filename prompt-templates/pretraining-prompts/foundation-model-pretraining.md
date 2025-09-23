## Foundation Model Pre-training (HuggingFace + PyTorch)

**User Story:**
As an ML engineer
I want to pre-train a foundation model using HuggingFace infrastructure
So that I can leverage optimized training libraries and model architectures

**Prompt:**
"I need to pre-train a [model architecture] foundation model using HuggingFace Transformers and PyTorch. Starting from [config/scratch], the model should have [parameter count] parameters and handle [modality: text/vision/multimodal]. Training will use [dataset names or custom data] with HuggingFace datasets library. Target compute budget is [GPU hours] using [hardware specs]. Please set up the complete workflow including dataset streaming, model initialization, training with HF Trainer or Accelerate, mixed precision training, and model hub integration."

### CONSTRAINTS
- Architecture: [GPT/BERT/T5/ViT/CLIP variant]
- Parameters: [100M-10B]
- Dataset: HF datasets or custom format
- Training framework: HF Trainer or Accelerate
- Precision: fp16/bf16/fp32

### REWARDS
- Streaming large datasets efficiently
- Gradient checkpointing for memory optimization
- WandB/TensorBoard integration
- Model card generation
- Hub upload with proper tags

### PENALTIES
- Not using dataset streaming for large data
- Missing mixed precision setup
- No experiment tracking
- Inefficient data loading
- Missing model documentation

### GOAL STATE
- Pre-trained model on HuggingFace Hub
- Training metrics and logs
- Model card with performance details
- Conversion scripts for deployment
- Benchmark comparisons