---
name: Bug report
about: Report a defect using INVEST user story format
title: ''
labels: 'bug'
assignees: ''

---

<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

## User Story (INVEST Format)

**As a** [role: researcher/developer/user]
**I want to** [fix the specific defect]
**So that** [benefit/value delivered]

**Examples:**

1. As a model developer
   I want to fix the DataLoader memory leak during multi-GPU training
   So that I can train models without OOM errors on long-running jobs

2. As a cloud engineer
   I want to fix the model checkpoint corruption when saving to S3
   So that I can reliably resume training from any checkpoint

3. As a training engineer
   I want to fix gradient accumulation producing incorrect gradient values
   So that I can train large models with small batch sizes accurately

4. As a network architect
   I want to fix the custom attention layer causing NaN loss values
   So that I can train transformer models to convergence

5. As a developer using LocalStack
   I want to fix the LocalStackEmulator failing to mock SageMaker endpoints
   So that I can test deployment workflows locally before using AWS

---

### Additional Context

**Error Messages/Stack Traces:**
```
[Paste complete error output here]
```

**Screenshots/Logs:**
[If applicable, add visual evidence]

**Related Issues:**
[Link to related issues if any]
