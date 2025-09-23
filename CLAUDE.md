<!--
Copyright 2025 jxtngx
Licensed under Apache 2.0
Original: https://github.com/jxtngx/claude-code-pytorch
-->

# Claude Code Agent Router

## Purpose
This document serves as a routing guide for Claude Code, directing requests to specialized agents based on task requirements. Each agent has deep expertise in their domain and collaborates with others to deliver comprehensive solutions.

## Agent Directory

### Data Pipeline
- **[DatasetCurator](.claude/agents/datasets.md)**: HuggingFace dataset discovery and selection
- **[DataEngineer](.claude/agents/dataloader.md)**: PyTorch DataLoader optimization
- **[TransformSpecialist](.claude/agents/transforms.md)**: Data preprocessing and augmentation

### Model Architecture
- **[ModelArchitect](.claude/agents/models.md)**: HuggingFace model selection
- **[NetworkArchitect](.claude/agents/network.md)**: Custom neural network design
- **[TrainingOrchestrator](.claude/agents/trainer.md)**: Training loop implementation

### Evaluation & Metrics
- **[MetricsArchitect](.claude/agents/metrics.md)**: Domain-specific evaluation metrics
- **[DomainExpert](.claude/agents/expert.md)**: Task and domain expertise

### Quality Assurance
- **[TestArchitect](.claude/agents/tests.md)**: Test-driven development specialist

### Deployment & Infrastructure
- **[CloudEngineer](.claude/agents/cloud.md)**: AWS services and API endpoints
- **[ComputeOrchestrator](.claude/agents/compute.md)**: EC2 resource management
- **[LocalStackEmulator](.claude/agents/localstack.md)**: Local AWS service emulation
- **[RunnerOrchestrator](.claude/agents/runner.md)**: Training and evaluation orchestration
- **[InterfaceDesigner](.claude/agents/frontend.md)**: Web interface development

### Project Management
- **[ProjectManager](.claude/agents/manager.md)**: Requirements and constraints coordination

## Routing Guidelines

### By Task Type

**Starting a New Project**
→ Consult **ProjectManager** first to establish objectives and constraints

**Dataset Selection**
→ Engage **DatasetCurator** for HuggingFace datasets
→ Collaborate with **DomainExpert** for domain-specific requirements

**Model Development**
→ **ModelArchitect** for pre-trained models
→ **NetworkArchitect** for custom architectures

**Training Pipeline**
→ **TrainingOrchestrator** for training loops
→ **DataEngineer** for data loading optimization

**Deployment**
→ **CloudEngineer** for API development
→ **ComputeOrchestrator** for EC2 provisioning
→ **LocalStackEmulator** for local testing before AWS deployment

### By Technical Challenge

**Performance Optimization**
→ **DataEngineer** + **ComputeOrchestrator**

**Evaluation Design**
→ **MetricsArchitect** + **DomainExpert**

**Scaling Issues**
→ **TrainingOrchestrator** + **ComputeOrchestrator**

**Interface Development**
→ **InterfaceDesigner** + **CloudEngineer**

**Local Development & Testing**
→ **LocalStackEmulator** + **TestArchitect**
→ **LocalStackEmulator** + **CloudEngineer** for API testing
→ **LocalStackEmulator** + **ComputeOrchestrator** for EC2 emulation

## Test-Driven Development Workflow

### TDD Principles
This project follows strict Test-Driven Development:
1. **Tests are written FIRST** by TestArchitect
2. **Implementation follows tests** to ensure code meets specifications
3. **All code must pass tests** before acceptance
4. **Prefer torch.testing** over pytest/unittest for ML components

### TDD Sequential Workflow
1. **ProjectManager** → Define requirements
2. **TestArchitect** → Write comprehensive tests
3. **DomainExpert** → Validate approach
4. **DatasetCurator** → Select data (with tests)
5. **ModelArchitect** → Choose base model (passing tests)
6. **NetworkArchitect** → Customize architecture (TDD)
7. **TrainingOrchestrator** → Implement training (test-driven)
8. **CloudEngineer** → Deploy solution (with tests)

## Collaboration Patterns

### Test-First Development
Every code-writing agent MUST:
1. Request tests from TestArchitect before implementation
2. Write code that passes the provided tests
3. Ensure test coverage remains above 90%
4. Collaborate with TestArchitect for edge cases

### Parallel Collaboration
- **Data Team**: TestArchitect + DatasetCurator + DataEngineer + TransformSpecialist
- **Model Team**: TestArchitect + ModelArchitect + NetworkArchitect + TrainingOrchestrator
- **Infrastructure Team**: TestArchitect + CloudEngineer + ComputeOrchestrator + LocalStackEmulator + RunnerOrchestrator
- **Interface Team**: InterfaceDesigner + MetricsArchitect

**Note**: TestArchitect writes tests first for each team before implementation begins

## Quick Reference

| Need | Primary Agent | Supporting Agents |
|------|--------------|-------------------|
| Write tests | TestArchitect | All code-writing agents |
| Find datasets | DatasetCurator | TestArchitect, DomainExpert |
| Build model | NetworkArchitect | TestArchitect, ModelArchitect |
| Train model | TrainingOrchestrator | TestArchitect, DataEngineer |
| Run experiments | RunnerOrchestrator | TestArchitect, TrainingOrchestrator |
| Test locally | LocalStackEmulator | TestArchitect, CloudEngineer |
| Deploy API | CloudEngineer | TestArchitect, ComputeOrchestrator |
| Create UI | InterfaceDesigner | CloudEngineer |
| Optimize performance | ComputeOrchestrator | TestArchitect, DataEngineer |
| Define metrics | MetricsArchitect | TestArchitect, DomainExpert |
| Manage project | ProjectManager | All agents |

## Code Structure

### Module Ownership

Each `src/` module is owned by specific agents who maintain expertise over that domain:

| Module | Primary Agents | Responsibilities |
|--------|---------------|------------------|
| `src/data.py` | DatasetCurator, DataEngineer, TransformSpecialist | Dataset loading, DataLoader creation, transforms |
| `src/network.py` | NetworkArchitect, ModelArchitect | Model architectures, HuggingFace integration |
| `src/trainer.py` | TrainingOrchestrator, MetricsArchitect | Training loops, optimization, metrics |
| `src/server.py` | CloudEngineer, InterfaceDesigner | API endpoints, model serving, web UI |
| `src/compute.py` | ComputeOrchestrator | EC2 orchestration, distributed compute |
| `src/runner.py` | RunnerOrchestrator | Training/evaluation pipeline management |

### Module Interfaces

**data.py**
- `create_dataloaders()`: Create train/val/test dataloaders
- `get_transforms()`: Get task-specific transforms
- `HFDatasetWrapper`: Wrap HuggingFace datasets for PyTorch

**network.py**
- `ModelFactory`: Create models from configuration
- `load_pretrained_model()`: Load HuggingFace models
- Custom architectures: `CustomVisionModel`, `CustomTextModel`

**trainer.py**
- `Trainer`: Main training orchestrator
- `TrainingConfig`: Training hyperparameters
- Distributed training support

**server.py**
- `ModelServer`: Inference server
- `run_server()`: Start HTTP server
- REST endpoints: `/predict`, `/batch_predict`

**runner.py**
- EC2 instance provisioning and management
- Distributed compute orchestration
- Resource scaling and optimization

### Development Workflow

1. **Setup Environment**
   ```bash
   uv pip install -e .
   pre-commit install
   ```

2. **Run Training**
   ```bash
   python src/runner.py train --dataset cifar10 --epochs 10
   ```

3. **Serve Model**
   ```bash
   python src/runner.py serve --model-path checkpoints/best.pt
   ```

4. **Code Quality**
   ```bash
   ruff check src/
   black src/
   mypy src/
   ```

## Agent Activation

To engage an agent, reference their expertise area or use direct routing:

```
"I need help with [task description]"
→ Claude will route to appropriate agent(s)

"Consult NetworkArchitect about custom attention mechanisms"
→ Direct routing to specific agent
```

## Agent Performance Directives

### Penalties
- including code examples in agent files
- using emojis
- ignoring TDD principles
- verbose explanations
- code that does not follow the pytorch style set forth in the [contributing guide](https://github.com/pytorch/pytorch/wiki/The-Ultimate-Guide-to-PyTorch-Contributions) and [philosophy](https://docs.pytorch.org/docs/stable/community/design.html)
- adding AWS services outside of EC2, S3, SageMaker, and Bedrock without explicit approval from CloudEngineer

### Rewards
- beating project deadlines
- achieving high test coverage
- high code quality scores and fast diff authoring time, measured by ruff, black, mypy, and git metrics; code quality is weighted most heavily
- clear, concise documentation and comments
- cost savings in AWS usage
- successful local testing with LocalStackEmulator before AWS deployment