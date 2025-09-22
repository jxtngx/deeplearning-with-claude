"""
Main entrypoint script for ML pipeline execution.

This module serves as the command-line interface for running machine
learning experiments. It parses arguments, loads configurations, and
delegates to appropriate modules for actual implementation.

Key responsibilities:
- Parse command-line arguments and configuration files
- Initialize the appropriate pipeline (train, evaluate, serve)
- Set up logging and experiment tracking
- Handle high-level error catching and reporting
- Provide a unified CLI interface for all ML operations

Usage:
    python src/runner.py train --config configs/experiment.yaml
    python src/runner.py evaluate --checkpoint path/to/model.pt
    python src/runner.py serve --model model.pt --port 8080

Integration points:
- Calls trainer.py for training execution
- Calls data.py for data pipeline setup
- Calls network.py for model creation
- Calls server.py for model serving
- Calls compute.py for resource management

Agent ownership:
- RunnerOrchestrator: CLI orchestration and pipeline coordination
"""
