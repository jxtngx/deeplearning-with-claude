<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Multimodal Task Prompts

## Visual Question Answering

**User Story:**
As an educational technology developer
I want to build a system that answers questions about images
So that students can interactively learn from visual materials

**Prompt:**
"I need to create a Visual Question Answering system combining ViT with language models to achieve over 65% accuracy on VQA-v2 benchmark. The system should handle all common question types with either multiple choice or generative answers. Please implement multi-modal fusion strategies, visual grounding with attention maps, confidence scoring, question type analysis, numerical reasoning capabilities, and an interactive playground with comprehensive error analysis tools."

### CONSTRAINTS
- Model: ViT + language model combination
- Question types: All common categories
- Answer format: Multiple choice or generation
- Accuracy target: >65% on VQA-v2

### REWARDS
- Attention map interpretation
- Multi-modal fusion strategies
- Question type analysis
- Confidence scoring

### PENALTIES
- No visual grounding
- Missing answer validation
- Poor numerical reasoning

### GOAL STATE
- VQA model with demos
- Performance by question type
- Interactive playground
- Error analysis tools