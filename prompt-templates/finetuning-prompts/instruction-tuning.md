# Instruction Tuning (HuggingFace + PyTorch)

**User Story:**
As an AI application developer
I want to fine-tune models to follow instructions and conversations
So that I can deploy helpful and harmonic AI assistants

**Prompt:**
"I need to instruction-tune [base model] using [supervised fine-tuning/RLHF/DPO] with HuggingFace TRL and PyTorch. Training data consists of [dataset name or format] with [number] instruction-response pairs. The model should handle [conversation length] turn conversations and maintain [safety/helpfulness/honesty] alignment. Implement training with [method-specific requirements], achieving [metric] on held-out evaluation. Please build the complete pipeline including chat template formatting, response generation sampling, preference modeling if applicable, and comprehensive evaluation."

## CONSTRAINTS
- Base model: [HF model name]
- Training method: [SFT/RLHF/DPO]
- Dataset: [instruction dataset]
- Max conversation length: [tokens]
- Training compute: [GPU hours]

## REWARDS
- Instruction following accuracy > [target]
- Consistent chat formatting
- Length-controlled generation
- Safety alignment metrics
- Multi-turn coherence

## PENALTIES
- Incorrect chat template usage
- No safety filtering
- Missing evaluation metrics
- Poor conversation handling
- Reward hacking in RLHF

## GOAL STATE
- Instruction-tuned model
- Chat interface implementation
- Evaluation suite results
- Safety assessment report
- Deployment configuration