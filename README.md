# Claude Code PyTorch

A modular, multi-agent based system for PyTorch, Hugging Face, and AWS.

## Philosophy

This repository embodies an **agent-based architecture** for machine learning projects, where specialized AI agents collaborate to deliver comprehensive solutions. Each agent maintains deep expertise in their domain while remaining modality and task agnostic.

## Core Principles

### Separation of Concerns
Each agent owns a specific technical domain, preventing overlap and ensuring expertise depth.

### Modality Agnostic
Agents adapt to any ML task—vision, NLP, audio, multimodal—without hardcoded assumptions.

### Performance First
Optimized for PyTorch 2.3+ with distributed training and NVIDIA GPU acceleration.

### Cloud Native
Built for AWS EC2 environments with scalable infrastructure patterns.

### Collaborative Intelligence
Agents work in concert, sharing context and building on each other's outputs.

## Getting Started

1. **Define Your Project**: Consult `CLAUDE.md` to engage the ProjectManager
2. **Select Your Team**: Claude routes to appropriate specialist agents
3. **Iterate and Build**: Agents collaborate to implement your solution

## Architecture

```
Agents → Specialized Expertise → Collaborative Implementation → Deployed Solution
```

Each agent operates as an expert consultant, providing:
- Domain-specific knowledge
- Best practice implementations
- Performance optimizations
- Quality assurance

## Key Technologies

- **PyTorch 2.3+**: Core deep learning framework
- **Hugging Face**: Model and dataset ecosystem
- **AWS**: Cloud infrastructure and services
- **Claude Code**: AI-powered development assistance

## Repository Structure

- `.claude/agents/`: Specialized agent definitions
- `CLAUDE.md`: Agent routing and coordination
- `docs/`: Task-specific prompt examples
- `src/`: Core Python modules (non-package structure)
  - `data.py`: Data pipeline components
  - `network.py`: Model architectures
  - `trainer.py`: Training orchestration
  - `server.py`: API and serving
  - `runner.py`: CLI entry point

## Quick Start

### Setup with uv

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv pip install -r requirements.txt

# Install dev dependencies
uv pip install -e ".[dev]"

# Setup pre-commit hooks
pre-commit install
```

### Basic Usage

```bash
# Train a model
python src/runner.py train --dataset cifar10 --epochs 10

# Serve trained model
python src/runner.py serve --model-path checkpoints/best.pt

# Evaluate model
python src/runner.py evaluate --model-path checkpoints/best.pt --dataset cifar10
```

### Development

```bash
# Format code
black src/
ruff format src/

# Lint code
ruff check src/

# Type check
mypy src/

# Run pre-commit on all files
pre-commit run --all-files
```

## Design Principles

### Non-Package Architecture
The `src/` directory contains standalone modules that can be run directly without package installation. This simplifies deployment and reduces complexity while maintaining clear separation of concerns.

### Modern Tooling
- **uv**: Fast, reliable Python package management
- **Ruff**: Single tool for linting and formatting
- **Pre-commit**: Automated code quality checks
- **Type hints**: Full typing support throughout

This template provides the foundation for any ML project, from research prototypes to production systems.