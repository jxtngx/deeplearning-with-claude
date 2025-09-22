"""
Data pipeline orchestration for machine learning workflows.

This module manages the complete data pipeline from raw datasets to
optimized PyTorch DataLoaders. It handles dataset discovery, preprocessing,
augmentation, and efficient batch loading for training and inference.

Key responsibilities:
- Dataset loading from HuggingFace Hub and custom sources
- DataLoader creation with optimized sampling and batching strategies
- Transform pipeline composition for data augmentation
- Memory-efficient data loading with prefetching and caching
- Distributed data loading for multi-GPU training
- Dataset versioning and reproducibility management

Core components:
- create_dataloaders(): Factory function for train/val/test DataLoaders
- get_transforms(): Task-specific transformation pipelines
- HFDatasetWrapper: Adapter for HuggingFace datasets to PyTorch format
- Custom dataset classes for specialized data formats
- Collation functions for variable-length sequences

Integration points:
- Interfaces with HuggingFace datasets library for dataset discovery
- Leverages torchvision.transforms for image augmentations
- Integrates with NVIDIA DALI for GPU-accelerated preprocessing
- Supports distributed sampling for DDP training
- Provides reproducible data splits with configurable seeds

Agent ownership:
- DatasetCurator: Dataset discovery and selection
- DataEngineer: DataLoader optimization and pipeline engineering
- TransformSpecialist: Augmentation and preprocessing strategies
"""
