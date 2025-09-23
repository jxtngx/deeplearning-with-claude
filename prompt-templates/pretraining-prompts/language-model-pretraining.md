<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

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