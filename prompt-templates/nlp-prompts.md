<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Natural Language Processing Task Prompts

## Text Classification

**User Story:**
As a data scientist
I want to fine-tune a transformer model for text classification
So that I can automatically categorize documents with high accuracy

**Prompt:**
"I need to build a text classification system using BERT, RoBERTa, or DistilBERT variants. The system should handle sequences up to 512 tokens and achieve F1 score above 0.85 on custom labeled data. Training must complete within 4 hours on a single GPU. Please implement the complete pipeline including efficient tokenization, class weight balancing for imbalanced datasets, attention weight visualization for interpretability, confidence calibration, and a REST API with batch inference capabilities."

### CONSTRAINTS
- Model: BERT, RoBERTa, or DistilBERT variants
- Maximum sequence length: 512 tokens
- Dataset: Custom labeled data or benchmark dataset
- Training time: <4 hours on single GPU

### REWARDS
- F1 score >0.85 on validation set
- Efficient tokenization strategy
- Class weight balancing
- Interpretability via attention weights

### PENALTIES
- No handling of imbalanced classes
- Missing confidence calibration
- Tokenization errors on edge cases

### GOAL STATE
- Fine-tuned classifier with saved tokenizer
- Confusion matrix and classification report
- REST API with batch inference
- Error analysis documentation

---

## Named Entity Recognition

**User Story:**
As an information extraction specialist
I want to identify and classify named entities in text
So that I can extract structured information from unstructured documents

**Prompt:**
"I need to implement a Named Entity Recognition system that can identify PER, ORG, LOC, and MISC entities using a transformer with token classification head. The system should use BIO or BILOU labeling schemes and process sentences in under 10ms. I need entity-level F1 above 0.9, with support for nested entities and cross-lingual capabilities. Please build the complete NER pipeline including CRF layer consideration, entity linking, active learning setup, and visualization tools for the extracted entities."

### CONSTRAINTS
- Architecture: Token classification head on transformer
- Entity types: PER, ORG, LOC, MISC minimum
- Sequence labeling: BIO or BILOU scheme
- Inference speed: <10ms per sentence

### REWARDS
- Entity-level F1 >0.9
- Nested entity support
- Cross-lingual capability
- Active learning setup

### PENALTIES
- No CRF layer consideration
- Missing entity linking
- Poor handling of rare entities

### GOAL STATE
- NER model with visualization
- Entity extraction pipeline
- Evaluation per entity type
- Integration with knowledge base

---

## Text Generation

**User Story:**
As a content creator
I want to generate high-quality text with controllable parameters
So that I can produce diverse and contextually appropriate content at scale

**Prompt:**
"I need to implement a text generation system using GPT-2, T5, or LLaMA variants with a context window of at least 2048 tokens. The model should achieve perplexity below 20 and support multiple decoding strategies (greedy, beam search, nucleus sampling). Please implement controllable generation with repetition penalties, efficient KV-cache, streaming output, content safety filters, and a parameter playground UI for experimentation. Include comprehensive metrics for generation quality and diversity."

### CONSTRAINTS
- Model: GPT-2, T5, or LLaMA variants
- Context window: 2048 tokens minimum
- Decoding: Support multiple strategies
- Safety: Content filtering required

### REWARDS
- Perplexity <20 on validation
- Controllable generation parameters
- Efficient KV-cache implementation
- Multiple decoding strategies

### PENALTIES
- No repetition penalty
- Missing safety filters
- Lack of generation diversity metrics

### GOAL STATE
- Generation model with streaming
- Parameter playground UI
- Quality metrics dashboard
- Prompt engineering guide

---

## Question Answering

**User Story:**
As a knowledge management specialist
I want to build a system that answers questions from documents
So that users can quickly extract specific information from large text corpora

**Prompt:**
"I need to create a Question Answering system supporting both extractive and generative approaches. The system should handle documents up to 4096 tokens with F1 score above 0.8 on SQuAD-like metrics and response latency under 500ms. Please implement multi-hop reasoning, confidence scoring, answer highlighting, handling of unanswerable questions, and integration with a document retrieval pipeline. Include an interactive demo interface with benchmark evaluation results."

### CONSTRAINTS
- Type: Extractive or generative QA
- Context: Support documents up to 4096 tokens
- Latency: <500ms per query
- Accuracy: F1 >0.8 on SQuAD-like metrics

### REWARDS
- Support for multi-hop reasoning
- Confidence scoring
- Answer highlighting
- Context retrieval integration

### PENALTIES
- No handling of unanswerable questions
- Missing context truncation strategy
- Poor long-context performance

### GOAL STATE
- QA system with confidence scores
- Document retrieval pipeline
- Interactive demo interface
- Benchmark evaluation results