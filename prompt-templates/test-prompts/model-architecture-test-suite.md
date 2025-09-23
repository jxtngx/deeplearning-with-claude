# Model Architecture Test Suite

**User Story:**
As a model developer
I want tests that validate model architecture before coding
So that I can ensure correct tensor flow and gradient computation

**Prompt:**
"@agent-TestArchitect I need test suite for a custom Vision Transformer model before implementation. Write tests using torch.testing that validate forward pass shapes for multiple batch sizes, gradient flow through all layers using torch.autograd.gradcheck, parameter initialization ranges, attention weight dimensions, and positional encoding correctness. Include tests for mixed precision compatibility, JIT compilation support, and checkpoint/restore functionality. All tests should use torch.testing.make_tensor() for input generation."

## CONSTRAINTS
- Primary tool: torch.testing and torch.autograd
- Gradient checking: All custom layers
- Shape testing: Dynamic batch sizes
- Precision: FP32, FP16, BF16 compatibility

## REWARDS
- torch.autograd.gradcheck() for custom ops
- torch.testing.assert_allclose() for numerical checks
- Dynamic shape validation
- Mixed precision testing

## PENALTIES
- Hardcoded test tensors
- Missing gradient flow tests
- No JIT compatibility checks
- Static batch size only

## GOAL STATE
- Architecture specification via tests
- Gradient flow validation
- Shape contract enforcement
- Performance baseline establishment