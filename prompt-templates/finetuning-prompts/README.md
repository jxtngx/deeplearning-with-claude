# Fine-tuning Task Prompts

<table>
  <thead>
    <tr>
      <th>Template</th>
      <th>Description</th>
      <th>Use Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="full-finetuning.md">Full Fine-tuning</a></td>
      <td>PyTorch Native full parameter fine-tuning</td>
      <td>Maximum task-specific performance with sufficient compute resources</td>
    </tr>
    <tr>
      <td><a href="parameter-efficient-finetuning.md">Parameter-Efficient Fine-tuning</a></td>
      <td>HuggingFace PEFT with LoRA/QLoRA/Adapters</td>
      <td>Fine-tuning large models with minimal GPU memory and storage</td>
    </tr>
    <tr>
      <td><a href="domain-adaptation.md">Domain Adaptation</a></td>
      <td>HuggingFace + PyTorch domain transfer</td>
      <td>Adapting pre-trained models to specialized domains</td>
    </tr>
    <tr>
      <td><a href="instruction-tuning.md">Instruction Tuning</a></td>
      <td>HuggingFace TRL with SFT/RLHF/DPO</td>
      <td>Training models to follow instructions and conversations</td>
    </tr>
  </tbody>
</table>