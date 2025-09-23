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

<table>
<thead>
<tr>
<th>Category</th>
<th>Templates</th>
<th>Description</th>
<th>Key Features</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="vision-prompts/">Vision Prompts</a></td>
<td>3</td>
<td>Computer vision tasks</td>
<td>Image Classification, Object Detection, Semantic Segmentation</td>
</tr>
<tr>
<td><a href="nlp-prompts/">NLP Prompts</a></td>
<td>4</td>
<td>Natural language processing</td>
<td>Text Classification, NER, Text Generation, Question Answering</td>
</tr>
<tr>
<td><a href="multimodal-prompts/">Multimodal Prompts</a></td>
<td>5</td>
<td>Cross-modal understanding</td>
<td>Vision-Language, Image Captioning, VQA, AV-ASR, Document AI</td>
</tr>
<tr>
<td><a href="pretraining-prompts/">Pre-training Prompts</a></td>
<td>3</td>
<td>Pre-training from scratch</td>
<td>Language Models, Vision Models, Foundation Models</td>
</tr>
<tr>
<td><a href="finetuning-prompts/">Fine-tuning Prompts</a></td>
<td>4</td>
<td>Model adaptation strategies</td>
<td>Full Fine-tuning, PEFT, Domain Adaptation, Instruction Tuning</td>
</tr>
<tr>
<td><a href="interface-prompts/">Interface Prompts</a></td>
<td>9</td>
<td>Web interface development</td>
<td>ML Playground, Dashboards, Monitoring, Annotation Studio</td>
</tr>
<tr>
<td><a href="test-prompts/">Test Prompts</a></td>
<td>7</td>
<td>Test-driven development</td>
<td>Data Pipeline, Architecture, Training, API, Performance Tests</td>
</tr>
</tbody>
</table>

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