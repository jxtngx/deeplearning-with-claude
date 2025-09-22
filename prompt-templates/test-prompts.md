# Test-Driven Development Prompts

## Data Pipeline Test Suite

**User Story:**
As a data engineer
I want comprehensive tests for data pipelines before implementation
So that I can ensure data integrity and transformation correctness

**Prompt:**
"@agent-TestArchitect I need comprehensive tests for a data pipeline that will handle image datasets with augmentations. The tests should verify DataLoader functionality, transformation pipelines, batch collation, and dataset iteration. Please write tests using torch.testing utilities that check tensor shapes after transforms, data type preservation, augmentation reproducibility with seeds, proper handling of edge cases (empty batches, single samples), and memory efficiency. Tests should fail initially and guide the implementation of create_dataloaders(), get_transforms(), and HFDatasetWrapper classes."

### CONSTRAINTS
- Testing framework: torch.testing preferred
- Coverage target: >95% for data modules
- Test execution: <5 seconds for unit tests
- Memory limit: <1GB for test data

### REWARDS
- Shape validation using torch.testing.assert_close()
- Deterministic testing with fixed seeds
- Edge case coverage
- Performance benchmarks included

### PENALTIES
- Using pytest assertions for tensor comparisons
- Missing edge case tests
- No memory leak detection
- Slow test execution

### GOAL STATE
- Complete test suite before implementation
- All tests initially fail (red phase)
- Guide implementation to pass (green phase)
- Enable safe refactoring

---

## Model Architecture Test Suite

**User Story:**
As a model developer
I want tests that validate model architecture before coding
So that I can ensure correct tensor flow and gradient computation

**Prompt:**
"@agent-TestArchitect I need test suite for a custom Vision Transformer model before implementation. Write tests using torch.testing that validate forward pass shapes for multiple batch sizes, gradient flow through all layers using torch.autograd.gradcheck, parameter initialization ranges, attention weight dimensions, and positional encoding correctness. Include tests for mixed precision compatibility, JIT compilation support, and checkpoint/restore functionality. All tests should use torch.testing.make_tensor() for input generation."

### CONSTRAINTS
- Primary tool: torch.testing and torch.autograd
- Gradient checking: All custom layers
- Shape testing: Dynamic batch sizes
- Precision: FP32, FP16, BF16 compatibility

### REWARDS
- torch.autograd.gradcheck() for custom ops
- torch.testing.assert_allclose() for numerical checks
- Dynamic shape validation
- Mixed precision testing

### PENALTIES
- Hardcoded test tensors
- Missing gradient flow tests
- No JIT compatibility checks
- Static batch size only

### GOAL STATE
- Architecture specification via tests
- Gradient flow validation
- Shape contract enforcement
- Performance baseline establishment

---

## Training Loop Test Suite

**User Story:**
As a training engineer
I want tests for training loops before implementation
So that I can ensure convergence and optimization correctness

**Prompt:**
"@agent-TestArchitect I need comprehensive tests for a distributed training loop implementation. Write tests that verify loss decreases over iterations, gradients are computed correctly, optimizer steps update parameters, learning rate scheduling works as expected, and checkpointing preserves training state. Use torch.testing to validate tensor operations, torch.distributed tests for multi-GPU scenarios, and performance benchmarks using torch.utils.benchmark. Include tests for gradient accumulation, mixed precision training, and early stopping logic."

### CONSTRAINTS
- Distributed testing: Up to 4 GPUs
- Convergence test: Synthetic data
- State validation: Checkpoint/restore
- Performance: Baseline throughput

### REWARDS
- Loss decrease validation
- Distributed correctness tests
- State preservation checks
- Performance regression detection

### PENALTIES
- No distributed testing
- Missing convergence checks
- Incomplete state validation
- No performance benchmarks

### GOAL STATE
- Training correctness guaranteed
- Distributed behavior validated
- Optimization verified
- Performance baselines set

---

## API Endpoint Test Suite

**User Story:**
As an API developer
I want tests for ML inference endpoints before implementation
So that I can ensure correct serialization and prediction serving

**Prompt:**
"@agent-TestArchitect I need test suite for REST API endpoints serving ML models. Write tests that validate request/response formats, model loading and caching, batch inference correctness, error handling for malformed inputs, and latency requirements. Use torch.testing for tensor validation in responses, test concurrent requests, memory usage under load, and graceful degradation. Include tests for different input modalities (images, text, tabular) and output format validation (JSON, protobuf)."

### CONSTRAINTS
- Response time: <100ms for single inference
- Batch size: Up to 32 samples
- Concurrency: 100 simultaneous requests
- Memory: Model caching validation

### REWARDS
- Tensor serialization validation
- Concurrency testing
- Memory leak detection
- Latency benchmarks

### PENALTIES
- No load testing
- Missing error handling tests
- Single format testing only
- No memory profiling

### GOAL STATE
- API contract validation
- Performance requirements met
- Error handling verified
- Scale testing passed

---

## Performance Optimization Test Suite

**User Story:**
As a performance engineer
I want tests that validate optimizations before implementation
So that I can ensure speedups don't compromise correctness

**Prompt:**
"@agent-TestArchitect I need performance validation tests for model optimization techniques. Write tests using torch.testing and torch.utils.benchmark that validate quantization maintains accuracy within 1%, pruning preserves critical connections, torch.compile optimizations produce identical outputs, and kernel fusion improves throughput. Include tests for ONNX export correctness, TensorRT compatibility, and mobile deployment constraints. Benchmark memory usage, inference latency, and throughput."

### CONSTRAINTS
- Accuracy drop: <1% after optimization
- Speedup target: >2x for inference
- Memory reduction: >30%
- Platform: CPU, GPU, Mobile

### REWARDS
- torch.utils.benchmark integration
- Accuracy preservation validation
- Cross-platform testing
- Memory profiling

### PENALTIES
- No baseline comparisons
- Missing accuracy validation
- Single platform testing
- No memory analysis

### GOAL STATE
- Optimization correctness verified
- Performance gains validated
- Accuracy maintained
- Deployment ready

---

## Integration Test Suite

**User Story:**
As a system architect
I want integration tests for the complete ML pipeline
So that I can ensure components work together correctly

**Prompt:**
"@agent-TestArchitect I need end-to-end integration tests for the complete ML system. Write tests that validate data flows correctly from input to prediction, model training convergence on real data, API endpoints serve trained models correctly, and monitoring captures all metrics. Use torch.testing for ML components, create test fixtures with torch.testing.make_tensor(), and validate the entire pipeline from data loading through inference. Include tests for error propagation, recovery mechanisms, and system resilience."

### CONSTRAINTS
- Pipeline coverage: Data → Training → Serving
- Test data: Synthetic but realistic
- Execution time: <2 minutes
- Resource usage: Single GPU

### REWARDS
- Full pipeline validation
- Component integration tests
- Error propagation checks
- Recovery mechanism validation

### PENALTIES
- Component isolation only
- No error path testing
- Missing integration points
- No resilience testing

### GOAL STATE
- System integration verified
- Data flow validated
- Error handling confirmed
- Production readiness assured

---

## Regression Test Suite

**User Story:**
As a maintainer
I want regression tests that catch breaking changes
So that I can safely refactor and update dependencies

**Prompt:**
"@agent-TestArchitect I need regression test suite to prevent breaking changes in ML components. Write tests using torch.testing that capture current behavior baselines, validate backward compatibility, check for performance regressions, and ensure reproducibility across versions. Include golden tests for model outputs, compatibility tests for saved checkpoints, and performance benchmarks with acceptable variance thresholds. Use torch.testing.assert_close() with appropriate tolerances for numerical stability."

### CONSTRAINTS
- Compatibility: Last 3 versions
- Performance variance: <5%
- Numerical tolerance: 1e-5
- Checkpoint formats: All supported

### REWARDS
- Golden output validation
- Version compatibility tests
- Performance tracking
- Reproducibility checks

### PENALTIES
- No baseline capturing
- Missing compatibility tests
- No performance tracking
- Hardcoded tolerances

### GOAL STATE
- Regression prevention
- Compatibility assured
- Performance maintained
- Safe refactoring enabled