# ReAct Workflow Example

## Scenario
Debugging a model that's not converging during training.

## ReAct Process

```markdown
**Initial Problem**: Model loss stays constant at 2.3 after 10 epochs

### Iteration 1: Check Learning Rate

**Thought**: Loss not decreasing might indicate learning rate issues
**Action**: Print current learning rate and try different values
```python
print(f"Current LR: {optimizer.param_groups[0]['lr']}")
# Test with different learning rates
for lr in [1e-5, 1e-4, 1e-3, 1e-2]:
    test_train_step(lr)
```
**Observation**: Loss decreases with lr=1e-3 but explodes with 1e-2

### Iteration 2: Verify Gradient Flow

**Thought**: Even with good LR, need to check if gradients are flowing
**Action**: Monitor gradient magnitudes
```python
for name, param in model.named_parameters():
    if param.grad is not None:
        print(f"{name}: {param.grad.norm().item():.6f}")
```
**Observation**: Final layers have gradients, but early layers show 0.000000

### Iteration 3: Investigate Dead Gradients

**Thought**: Zero gradients in early layers suggests vanishing gradient problem
**Action**: Check activation functions and initialization
```python
# Check for ReLU dying problem
def hook_fn(module, input, output):
    print(f"Dead neurons: {(output == 0).sum().item() / output.numel():.2%}")

for layer in model.modules():
    if isinstance(layer, nn.ReLU):
        layer.register_forward_hook(hook_fn)
```
**Observation**: 78% of ReLU neurons are dead in early layers

### Iteration 4: Fix Initialization

**Thought**: Poor initialization causing dead ReLUs
**Action**: Re-initialize with better scheme
```python
def init_weights(m):
    if isinstance(m, nn.Linear):
        nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
        if m.bias is not None:
            nn.init.constant_(m.bias, 0.01)  # Small positive bias

model.apply(init_weights)
```
**Observation**: After re-initialization, gradient flow restored

### Iteration 5: Verify Fix

**Thought**: Should verify the complete fix works
**Action**: Run full training for 5 epochs
```python
for epoch in range(5):
    train_loss = train_epoch(model, loader, optimizer)
    print(f"Epoch {epoch}: Loss = {train_loss:.4f}")
```
**Observation**:
- Epoch 0: Loss = 2.3012
- Epoch 1: Loss = 1.8734
- Epoch 2: Loss = 1.4521
- Epoch 3: Loss = 1.1032
- Epoch 4: Loss = 0.8234

### Solution Summary

**Root Cause**: Poor weight initialization caused dying ReLU problem
**Fix Applied**: Kaiming initialization with small positive bias
**Result**: Model now converges properly
```

## Key Insights

1. **Systematic Investigation**: Each thought leads to specific action
2. **Evidence-Based**: Decisions based on observations, not assumptions
3. **Iterative Refinement**: Each iteration narrows down the problem
4. **Tool Usage**: Leverages debugging tools and monitoring
5. **Verification**: Confirms fix works before concluding