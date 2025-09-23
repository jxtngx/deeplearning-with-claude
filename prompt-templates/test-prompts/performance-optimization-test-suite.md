# Performance Optimization Test Suite

**User Story:**
As a performance engineer
I want tests that validate optimizations before implementation
So that I can ensure speedups don't compromise correctness

**Prompt:**
"@agent-TestArchitect I need performance validation tests for model optimization techniques. Write tests using torch.testing and torch.utils.benchmark that validate quantization maintains accuracy within 1%, pruning preserves critical connections, torch.compile optimizations produce identical outputs, and kernel fusion improves throughput. Include tests for ONNX export correctness, TensorRT compatibility, and mobile deployment constraints. Benchmark memory usage, inference latency, and throughput."

## CONSTRAINTS
- Accuracy drop: <1% after optimization
- Speedup target: >2x for inference
- Memory reduction: >30%
- Platform: CPU, GPU, Mobile

## REWARDS
- torch.utils.benchmark integration
- Accuracy preservation validation
- Cross-platform testing
- Memory profiling

## PENALTIES
- No baseline comparisons
- Missing accuracy validation
- Single platform testing
- No memory analysis

## GOAL STATE
- Optimization correctness verified
- Performance gains validated
- Accuracy maintained
- Deployment ready