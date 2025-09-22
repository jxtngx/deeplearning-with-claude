"""
EC2 instance management for distributed ML compute.

This module handles spinning up and tearing down EC2 instances for
machine learning workloads. It provides a simple interface for provisioning
GPU instances and coordinating distributed training clusters.

Key responsibilities:
- EC2 instance lifecycle management (spinup/teardown)
- GPU instance provisioning for ML workloads
- Distributed training cluster setup
- Spot instance management with fallback strategies
- Basic cost optimization through instance selection

Supported instance types:
- P4/P5: High-performance GPU training (A100/H100)
- G4/G5: Cost-effective training and inference (T4/A10G)
- Standard CPU instances for data preprocessing

Core components:
- spin_up_instance(): Launch EC2 instances with specified configuration
- tear_down_instance(): Terminate instances and cleanup resources
- create_cluster(): Setup multi-node training clusters
- manage_spot_fleet(): Handle spot instance requests and interruptions

Agent ownership:
- ComputeOrchestrator: EC2 resource management and optimization
"""
