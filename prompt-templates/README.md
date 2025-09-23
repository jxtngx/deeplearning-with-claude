<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Prompt Templates

## Overview

This directory contains ready-to-use prompt templates for common machine learning tasks. These templates are designed to work with the specialized agents in this PyTorch ML project, providing structured requests that include constraints, rewards, and clear goal states.

## How to Use

1. **Browse** the template files to find a task matching your needs
2. **Copy** the entire prompt text from the relevant section
3. **Paste** into your conversation with Claude Code
4. **Customize** the specific parameters to match your requirements
5. **Submit** to trigger the appropriate agent workflow

## Template Categories

### vision-prompts.md
Computer vision tasks including:
- **Image Classification**: Transfer learning with Vision Transformers or ResNet
- **Object Detection**: YOLO, Faster R-CNN, DETR implementations
- **Semantic Segmentation**: DeepLab, U-Net architectures

### nlp-prompts.md
Natural language processing tasks including:
- **Text Classification**: BERT/RoBERTa fine-tuning
- **Named Entity Recognition**: Token classification with transformers
- **Question Answering**: Extractive QA systems

### multimodal-prompts.md
Cross-modal understanding tasks including:
- **Vision-Language Models**: CLIP, ALIGN, BLIP implementations
- **Audio-Visual Learning**: Multi-modal fusion architectures
- **Video Understanding**: Temporal modeling with transformers

### pretraining-prompts.md
Pre-training from scratch including:
- **Language Model Pre-training**: PyTorch native transformer training
- **Vision Model Pre-training**: Self-supervised learning (SimCLR, MAE)
- **Foundation Model Pre-training**: HuggingFace + PyTorch large-scale training

### finetuning-prompts.md
Model adaptation strategies including:
- **Full Fine-tuning**: PyTorch native parameter updates
- **Parameter-Efficient Fine-tuning**: LoRA, QLoRA with HuggingFace PEFT
- **Domain Adaptation**: Specialized domain transfer learning
- **Instruction Tuning**: SFT, RLHF, DPO for conversational models

### interface-prompts.md
Web interface development including:
- **ML Model Playground**: Interactive parameter tuning interfaces
- **Data Visualization Dashboard**: Real-time metrics and charts
- **Model Comparison Tool**: Side-by-side evaluation interfaces
- **Training Monitor**: Live training progress visualization

### test-prompts.md
Test-driven development templates including:
- **Data Pipeline Tests**: DataLoader and transform validation
- **Model Architecture Tests**: Layer functionality verification
- **Training Loop Tests**: Optimizer and loss computation checks
- **API Endpoint Tests**: Request/response validation

## Template Structure

Each template follows a consistent structure combining agile methodologies with AI optimization:

### INVEST User Stories
Templates begin with user stories following the agile INVEST principles:
- **Independent**: Self-contained requirements
- **Negotiable**: Flexible implementation approach
- **Valuable**: Clear benefit to stakeholder
- **Estimable**: Defined scope and complexity
- **Small**: Achievable in reasonable timeframe
- **Testable**: Measurable success criteria

### CRPG Optimization Framework
Following the user story, each template includes a custom CRPG framework that guides AI agent behavior:

```markdown
**User Story:** (INVEST format)
As a [role]
I want to [goal]
So that [benefit]

**Prompt:**
"[Detailed task description with specific requirements]"

### CONSTRAINTS
- Technical limitations and requirements
- Resource boundaries (GPU, memory, time)
- Compatibility requirements

### REWARDS
- Success metrics and targets
- Performance goals
- Quality indicators

### PENALTIES
- Anti-patterns to avoid
- Common pitfalls
- Quality deductions

### GOAL STATE
- Expected deliverables
- Success criteria
- Validation methods
```

This dual format ensures agents receive both high-level intent (INVEST) and specific optimization parameters (CRPG) for optimal task execution.

## Customization Guide

When adapting templates:

1. **Keep the structure**: Maintain constraints/rewards/penalties format
2. **Be specific**: Replace placeholder values with actual requirements
3. **Set realistic targets**: Adjust performance metrics to your hardware
4. **Include your data**: Specify your dataset or provide sample data
5. **Define success**: Clear metrics help agents optimize correctly

## Agent Routing

Templates automatically route to appropriate agents:

- **@agent-InterfaceDesigner**: For UI/UX tasks
- **@agent-TestArchitect**: For TDD workflows
- **@agent-NetworkArchitect**: For custom model architectures
- **@agent-DatasetCurator**: For dataset selection
- **@agent-TrainingOrchestrator**: For training pipelines

Agents not explicitly mentioned are selected automatically based on task requirements.

## Best Practices

### DO:
- Start with test prompts for TDD workflow
- Include specific performance targets
- Specify hardware constraints upfront
- Mention preferred libraries/frameworks
- Set clear success criteria

### DON'T:
- Remove constraints section (agents need boundaries)
- Skip rewards/penalties (they guide optimization)
- Use vague requirements ("make it fast")
- Combine unrelated tasks in one prompt
- Ignore the user story format

## Examples

### Quick Start: Image Classification
```bash
# 1. Copy prompt from vision-prompts.md
# 2. Replace "ImageNet-1K or CIFAR-10" with your dataset
# 3. Adjust "8 GPU hours" to your budget
# 4. Submit to Claude Code
```

### Test-First Development
```bash
# 1. Start with test-prompts.md template
# 2. Let TestArchitect write tests first
# 3. Then use vision/nlp/multimodal prompts for implementation
# 4. Ensure all tests pass before deployment
```

## Template Combinations

Common workflows:

1. **Full Pipeline**: Test → Data → Model → Training → Deployment
2. **Research**: Data exploration → Model experimentation → Metrics
3. **Production**: Model optimization → API → Interface → Testing
4. **Iteration**: Metrics analysis → Model refinement → A/B testing

## Support

- Review CLAUDE.md for agent capabilities
- Check .claude/agents/ for detailed agent documentation
- Consult team.md for agent coordination patterns