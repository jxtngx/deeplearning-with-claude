# ADR-001: Adopt Agile Methodology with INVEST and CRPG

## Title
Adopt Agile Methodology with INVEST User Stories and CRPG Optimization Framework

## Status
Accepted

## Context
The Claude Code PyTorch project requires a structured approach to manage complex machine learning development with multiple specialized AI agents. Traditional waterfall approaches are insufficient for the iterative nature of ML development, where requirements often evolve based on experimental results and stakeholder feedback.

The project needs:
- Clear requirement specifications that agents can understand
- Iterative development cycles for continuous improvement
- Test-driven development practices
- Measurable success criteria
- Flexibility to adapt based on learning

## Decision
We adopt a dual-track agile methodology combining:

1. **INVEST User Stories** for requirement specification:
   - Independent, Negotiable, Valuable, Estimable, Small, Testable
   - Provides clear intent and scope for each task
   - Ensures deliverables have business value

2. **CRPG Optimization Framework** for AI agent guidance:
   - Constraints: Technical boundaries and limitations
   - Rewards: Success metrics and performance targets
   - Penalties: Anti-patterns and quality deductions
   - Goal State: Clear deliverables and validation criteria

3. **Dual-Track Agile Workflow**:
   - Discovery Track: Continuous research and planning
   - Delivery Track: Sprint-based implementation
   - TestArchitect writes tests first (TDD)
   - Parallel agent collaboration within sprints

## Consequences

### Positive
- Clear communication between stakeholders and AI agents
- Iterative improvement through sprint cycles
- Built-in quality through TDD practices
- Measurable progress via sprint velocity
- Flexible adaptation to changing requirements
- Optimized agent behavior through CRPG parameters

### Negative
- Additional overhead in maintaining sprint artifacts
- Learning curve for INVEST/CRPG format
- Requires discipline in following TDD practices

### Neutral
- All prompt templates must follow the combined format
- Agents must be trained to recognize and respond to CRPG parameters
- Sprint planning becomes a critical coordination point

## Compliance
This decision fully aligns with agile principles:
- **Individuals and interactions**: Agent collaboration patterns
- **Working software**: Sprint deliverables and continuous integration
- **Customer collaboration**: Stakeholder involvement in sprint reviews
- **Responding to change**: Flexible backlog and iterative refinement

The INVEST principles ensure all work items are:
- Properly scoped and estimated
- Delivering clear value
- Testable and verifiable
- Small enough for sprint completion

## References
- [Agile Manifesto](https://agilemanifesto.org/)
- [INVEST in Good Stories](https://www.agilealliance.org/glossary/invest/)
- Project documentation: README.md, team.md, prompt-templates/README.md
- Related: Supervisor agent documentation (.claude/agents/supervisor.md)