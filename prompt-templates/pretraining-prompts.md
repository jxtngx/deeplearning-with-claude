<!-- Copyright 2024 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Pre-training Task Prompts

## Language Model Pre-training (PyTorch Native)

**User Story:**
As a research engineer
I want to pre-train a transformer language model from scratch
So that I can develop domain-specific foundation models with custom vocabularies

**Prompt:**
"I need to pre-train a transformer-based language model from scratch using native PyTorch. The model should have [6-24] layers, [768-1024] hidden dimensions, and support sequences up to [512-2048] tokens. Training data consists of [your corpus description] totaling [X GB] of text. The model should achieve perplexity below [target value] on validation data within [GPU hours budget]. Please implement the complete pre-training pipeline including tokenizer training, data preprocessing, model architecture, distributed training setup, and checkpoint management."

### CONSTRAINTS
- Architecture: Transformer decoder or encoder-decoder
- Model size: [100M-1B] parameters
- Sequence length: [512-2048] tokens
- Training data: [10GB-1TB] text corpus
- Hardware: [specify GPU type and count]

### REWARDS
- Achieve target perplexity on validation set
- Efficient tokenizer with [vocab size] tokens
- Gradient accumulation for large batch training
- Checkpoint saving every [N] steps
- Training loss visualization

### PENALTIES
- Gradient explosion or vanishing
- Memory inefficiency causing OOM
- No learning rate scheduling
- Missing validation metrics
- Poor tokenization coverage

### GOAL STATE
- Pre-trained model checkpoints
- Custom tokenizer files
- Training curves and metrics
- Model card documentation
- Inference benchmark results

---

## Vision Model Pre-training (PyTorch Native)

**User Story:**
As a computer vision researcher
I want to pre-train vision models using self-supervised learning
So that I can leverage unlabeled image data for downstream tasks

**Prompt:**
"I need to implement self-supervised pre-training for vision models using [SimCLR/MoCo/BYOL/MAE] approach in native PyTorch. The model should work with [ResNet/ViT] backbone processing images at [224-384] resolution. Pre-training will use [dataset size] unlabeled images and should achieve [target metric] on linear evaluation within [GPU hours]. Please build the complete pipeline including augmentation strategies, contrastive loss implementation, momentum encoders if applicable, and distributed training across multiple GPUs."

### CONSTRAINTS
- Method: [SimCLR/MoCo/BYOL/MAE]
- Backbone: [ResNet50/ViT-B]
- Image resolution: [224-384] pixels
- Batch size: [256-4096] depending on method
- Training duration: [100-800] epochs

### REWARDS
- Linear probe accuracy > [target]%
- Efficient negative sampling strategy
- Strong augmentation pipeline
- Multi-GPU synchronization
- Temperature scheduling for contrastive methods

### PENALTIES
- Mode collapse in representations
- Insufficient augmentation diversity
- Poor negative sampling
- Missing momentum update logic
- No downstream evaluation setup

### GOAL STATE
- Pre-trained encoder weights
- Training dynamics visualization
- Linear evaluation results
- Transfer learning benchmarks
- Augmentation configuration

---

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