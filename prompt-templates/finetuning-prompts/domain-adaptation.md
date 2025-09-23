# Domain Adaptation (HuggingFace + PyTorch)

**User Story:**
As a domain expert
I want to adapt pre-trained models to specialized domains
So that I can leverage general knowledge while optimizing for domain-specific patterns

**Prompt:**
"I need to adapt [base model] to [target domain] using domain adaptation techniques with HuggingFace and PyTorch. The source model was trained on [source domain] and needs adaptation using [unlabeled domain data size] unlabeled examples and [labeled size] labeled examples from target domain. Implement [continued pre-training/intermediate training/multi-task learning] strategy achieving [metric] on domain-specific benchmarks. Please create the pipeline including domain-specific tokenization/preprocessing, curriculum learning, domain discriminator if adversarial, and evaluation on both domains."

## CONSTRAINTS
- Source model: [HF model name]
- Target domain: [domain description]
- Unlabeled data: [size] examples
- Labeled data: [size] examples
- Adaptation strategy: [method]

## REWARDS
- Domain-specific metric improvement > [X%]
- Maintained source domain performance
- Effective use of unlabeled data
- Domain-specific vocabulary handling
- Progressive adaptation schedule

## PENALTIES
- Catastrophic forgetting of source domain
- No domain-specific preprocessing
- Ignoring unlabeled data
- Missing domain shift analysis
- No multi-domain evaluation

## GOAL STATE
- Domain-adapted model
- Performance on both domains
- Domain shift visualization
- Vocabulary analysis report
- Transfer learning metrics