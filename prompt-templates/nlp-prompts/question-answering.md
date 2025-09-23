<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Natural Language Processing Task Prompts

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