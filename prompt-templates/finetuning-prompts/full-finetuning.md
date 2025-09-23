<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Full Fine-tuning (PyTorch Native)

**User Story:**
As a machine learning engineer
I want to fine-tune all parameters of a pre-trained model
So that I can maximize task-specific performance with sufficient compute resources

**Prompt:**
"I need to implement full fine-tuning of a pre-trained [model type] using native PyTorch. Starting from [checkpoint/weights], the model should be adapted for [task description] with [dataset size] labeled examples. Training should complete within [hours] on [GPU type] while achieving [metric] > [target]. Please build the complete pipeline including model loading, layer freezing strategies, learning rate scheduling with warmup, early stopping, and comprehensive evaluation metrics."

## CONSTRAINTS
- Base model: [model name and size]
- Dataset: [size] samples with [classes/labels]
- Hardware: [GPU memory] available
- Training time: [hours] maximum
- Batch size: [range based on memory]

## REWARDS
- Achieve target performance metric
- Gradual unfreezing strategy
- Discriminative learning rates
- Validation-based checkpointing
- Confusion matrix and error analysis

## PENALTIES
- Catastrophic forgetting of pre-trained knowledge
- Overfitting to small datasets
- No learning rate decay
- Missing baseline comparisons
- Uniform learning rates across layers

## GOAL STATE
- Fine-tuned model weights
- Training history plots
- Performance metrics report
- Best checkpoint selection
- Deployment-ready model