<!-- Copyright 2024 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Fine-tuning Task Prompts

## Full Fine-tuning (PyTorch Native)

**User Story:**
As a machine learning engineer
I want to fine-tune all parameters of a pre-trained model
So that I can maximize task-specific performance with sufficient compute resources

**Prompt:**
"I need to implement full fine-tuning of a pre-trained [model type] using native PyTorch. Starting from [checkpoint/weights], the model should be adapted for [task description] with [dataset size] labeled examples. Training should complete within [hours] on [GPU type] while achieving [metric] > [target]. Please build the complete pipeline including model loading, layer freezing strategies, learning rate scheduling with warmup, early stopping, and comprehensive evaluation metrics."

### CONSTRAINTS
- Base model: [model name and size]
- Dataset: [size] samples with [classes/labels]
- Hardware: [GPU memory] available
- Training time: [hours] maximum
- Batch size: [range based on memory]

### REWARDS
- Achieve target performance metric
- Gradual unfreezing strategy
- Discriminative learning rates
- Validation-based checkpointing
- Confusion matrix and error analysis

### PENALTIES
- Catastrophic forgetting of pre-trained knowledge
- Overfitting to small datasets
- No learning rate decay
- Missing baseline comparisons
- Uniform learning rates across layers

### GOAL STATE
- Fine-tuned model weights
- Training history plots
- Performance metrics report
- Best checkpoint selection
- Deployment-ready model

---

## Parameter-Efficient Fine-tuning (HuggingFace + PyTorch)

**User Story:**
As a practitioner with limited resources
I want to fine-tune large models using parameter-efficient methods
So that I can adapt models with minimal GPU memory and storage

**Prompt:**
"I need to implement parameter-efficient fine-tuning using [LoRA/QLoRA/Prefix Tuning/Adapters] with HuggingFace PEFT and PyTorch. Starting with [base model name], adapt it for [task] using only [0.1-1%] of parameters. The model should be quantized to [4/8]-bit if using QLoRA. Dataset contains [size] examples in [format]. Training should fit within [GPU memory] GB and achieve [metric] comparable to full fine-tuning. Please set up the complete workflow including PEFT configuration, quantization setup, training with gradient checkpointing, and adapter merging."

### CONSTRAINTS
- Method: [LoRA/QLoRA/Prefix Tuning/Adapters]
- Base model: [HF model name]
- Trainable parameters: [0.1-1%] of total
- Quantization: [none/4-bit/8-bit]
- Memory budget: [GPU memory] GB

### REWARDS
- Memory usage < [threshold] GB
- LoRA rank optimization
- Gradient checkpointing enabled
- Adapter merging for deployment
- Performance within [X%] of full fine-tuning

### PENALTIES
- Loading full precision model unnecessarily
- Suboptimal LoRA rank selection
- Missing quantization configuration
- No comparison with full fine-tuning
- Inefficient batch sizing

### GOAL STATE
- PEFT adapter weights
- Merged model option
- Memory usage report
- Performance comparison table
- Inference optimization guide

---

## Domain Adaptation (HuggingFace + PyTorch)

**User Story:**
As a domain expert
I want to adapt pre-trained models to specialized domains
So that I can leverage general knowledge while optimizing for domain-specific patterns

**Prompt:**
"I need to adapt [base model] to [target domain] using domain adaptation techniques with HuggingFace and PyTorch. The source model was trained on [source domain] and needs adaptation using [unlabeled domain data size] unlabeled examples and [labeled size] labeled examples from target domain. Implement [continued pre-training/intermediate training/multi-task learning] strategy achieving [metric] on domain-specific benchmarks. Please create the pipeline including domain-specific tokenization/preprocessing, curriculum learning, domain discriminator if adversarial, and evaluation on both domains."

### CONSTRAINTS
- Source model: [HF model name]
- Target domain: [domain description]
- Unlabeled data: [size] examples
- Labeled data: [size] examples
- Adaptation strategy: [method]

### REWARDS
- Domain-specific metric improvement > [X%]
- Maintained source domain performance
- Effective use of unlabeled data
- Domain-specific vocabulary handling
- Progressive adaptation schedule

### PENALTIES
- Catastrophic forgetting of source domain
- No domain-specific preprocessing
- Ignoring unlabeled data
- Missing domain shift analysis
- No multi-domain evaluation

### GOAL STATE
- Domain-adapted model
- Performance on both domains
- Domain shift visualization
- Vocabulary analysis report
- Transfer learning metrics

---

## Instruction Tuning (HuggingFace + PyTorch)

**User Story:**
As an AI application developer
I want to fine-tune models to follow instructions and conversations
So that I can deploy helpful and harmonic AI assistants

**Prompt:**
"I need to instruction-tune [base model] using [supervised fine-tuning/RLHF/DPO] with HuggingFace TRL and PyTorch. Training data consists of [dataset name or format] with [number] instruction-response pairs. The model should handle [conversation length] turn conversations and maintain [safety/helpfulness/honesty] alignment. Implement training with [method-specific requirements], achieving [metric] on held-out evaluation. Please build the complete pipeline including chat template formatting, response generation sampling, preference modeling if applicable, and comprehensive evaluation."

### CONSTRAINTS
- Base model: [HF model name]
- Training method: [SFT/RLHF/DPO]
- Dataset: [instruction dataset]
- Max conversation length: [tokens]
- Training compute: [GPU hours]

### REWARDS
- Instruction following accuracy > [target]
- Consistent chat formatting
- Length-controlled generation
- Safety alignment metrics
- Multi-turn coherence

### PENALTIES
- Incorrect chat template usage
- No safety filtering
- Missing evaluation metrics
- Poor conversation handling
- Reward hacking in RLHF

### GOAL STATE
- Instruction-tuned model
- Chat interface implementation
- Evaluation suite results
- Safety assessment report
- Deployment configuration