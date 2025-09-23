<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Natural Language Processing Task Prompts

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