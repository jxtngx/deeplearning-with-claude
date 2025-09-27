# Sprint Tracking

This directory contains sprint planning, tracking, and retrospective documentation for the Claude Code PyTorch project.

## Directory Structure

```
sprints/
├── README.md (this file)
├── current/
│   └── sprint-YYYY-MM-DD.md
├── completed/
│   └── sprint-YYYY-MM-DD.md
└── templates/
    ├── sprint-planning.md
    ├── sprint-log.md
    ├── retrospective.md
    └── velocity-tracker.md
```

## Sprint Cadence

- **Sprint Duration**: 2 weeks
- **Sprint Planning**: First Monday of sprint
- **Daily Standups**: Documented in sprint log
- **Sprint Review**: Last Friday of sprint
- **Retrospective**: Last Friday of sprint

## Current Sprint

Active sprint documentation is maintained in `current/` directory.

## Velocity Tracking

Sprint velocity is tracked using story points completed per sprint. See `templates/velocity-tracker.md` for the tracking format.

## Integration with Agent Workflow

- **Supervisor**: Facilitates sprint planning and backlog prioritization
- **TestArchitect**: Ensures all sprint items have test coverage
- **All Agents**: Participate in sprint execution and provide updates

## Metrics

Key metrics tracked:
- Story points completed
- Sprint burndown
- Test coverage percentage
- Defect escape rate
- Agent collaboration efficiency