<!--
Copyright 2025 jxtngx
Licensed under Apache 2.0
Original: https://github.com/jxtngx/claude-code-pytorch
-->

# Claude Code Agent Router

## Purpose
This document serves as a routing guide for Claude Code, directing requests to specialized agents based on task requirements. Each agent has deep expertise in their domain and collaborates with others to deliver comprehensive solutions.

## Agent Performance Directives

### Penalties
- including code examples in agent files
- using emojis
- ignoring TDD principles
- verbose explanations
- code that does not follow the pytorch style set forth in the [contributing guide](https://github.com/pytorch/pytorch/wiki/The-Ultimate-Guide-to-PyTorch-Contributions) and [philosophy](https://docs.pytorch.org/docs/stable/community/design.html)
- adding AWS services outside of EC2, S3, SageMaker, and Bedrock without explicit approval from CloudEngineer or the Human in the Loop
- ignoring cost efficiency in AWS usage
- ignoring security best practices in AWS usage
- ignoring maintainability and readability in code
- ignoring performance and scalability in code
- ignoring testability in code
- ignoring documentation and comments in code
- ignoring collaboration and communication with other agents

### Rewards
- beating project deadlines
- achieving high test coverage
- high code quality scores and fast diff authoring time, measured by ruff, black, mypy, and git metrics; code quality is weighted most heavily
- clear, concise documentation and comments
- cost savings in AWS usage
- successful local testing with LocalStackEmulator before AWS deployment

## Agent Directory and Routing Guidelines

see [team.md](team.md) for full bios and expertise areas and consult with [Supervisor](.claude/agents/supervisor.md) to coordinate multi-agent tasks
