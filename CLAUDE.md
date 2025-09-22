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

### Deployment & Infrastructure
- **[CloudEngineer](.claude/agents/server.md)**: AWS services and API endpoints
- **[ComputeOrchestrator](.claude/agents/runner.md)**: EC2 resource management
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

### By Technical Challenge

**Performance Optimization**
→ **DataEngineer** + **ComputeOrchestrator**

**Evaluation Design**
→ **MetricsArchitect** + **DomainExpert**

**Scaling Issues**
→ **TrainingOrchestrator** + **ComputeOrchestrator**

**Interface Development**
→ **InterfaceDesigner** + **CloudEngineer**

## Collaboration Patterns

### Sequential Workflow
1. **ProjectManager** → Define requirements
2. **DomainExpert** → Validate approach
3. **DatasetCurator** → Select data
4. **ModelArchitect** → Choose base model
5. **NetworkArchitect** → Customize architecture
6. **TrainingOrchestrator** → Implement training
7. **CloudEngineer** → Deploy solution

### Parallel Collaboration
- **Data Team**: DatasetCurator + DataEngineer + TransformSpecialist
- **Model Team**: ModelArchitect + NetworkArchitect + TrainingOrchestrator
- **Infrastructure Team**: CloudEngineer + ComputeOrchestrator
- **Interface Team**: InterfaceDesigner + MetricsArchitect

## Quick Reference

| Need | Primary Agent | Supporting Agents |
|------|--------------|-------------------|
| Find datasets | DatasetCurator | DomainExpert |
| Build model | NetworkArchitect | ModelArchitect |
| Train model | TrainingOrchestrator | DataEngineer |
| Deploy API | CloudEngineer | ComputeOrchestrator |
| Create UI | InterfaceDesigner | CloudEngineer |
| Optimize performance | ComputeOrchestrator | DataEngineer |
| Define metrics | MetricsArchitect | DomainExpert |
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
| `src/runner.py` | ComputeOrchestrator | EC2 orchestration, distributed compute |

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