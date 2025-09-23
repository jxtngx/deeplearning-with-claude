## Vision Model Pre-training (PyTorch Native)

**User Story:**
As a computer vision researcher
I want to pre-train vision models using self-supervised learning
So that I can leverage unlabeled image data for downstream tasks

**Prompt:**
"I need to implement self-supervised pre-training for vision models using [SimCLR/MoCo/BYOL/MAE] approach in native PyTorch. The model should work with [ResNet/ViT] backbone processing images at [224-384] resolution. Pre-training will use [dataset size] unlabeled images and should achieve [target metric] on linear evaluation within [GPU hours]. Please build the complete pipeline including augmentation strategies, contrastive loss implementation, momentum encoders if applicable, and distributed training across multiple GPUs."

### CONSTRAINTS
- Method: [SimCLR/MoCo/BYOL/MAE]
- Backbone: [ResNet50/ViT-B]
- Image resolution: [224-384] pixels
- Batch size: [256-4096] depending on method
- Training duration: [100-800] epochs

### REWARDS
- Linear probe accuracy > [target]%
- Efficient negative sampling strategy
- Strong augmentation pipeline
- Multi-GPU synchronization
- Temperature scheduling for contrastive methods

### PENALTIES
- Mode collapse in representations
- Insufficient augmentation diversity
- Poor negative sampling
- Missing momentum update logic
- No downstream evaluation setup

### GOAL STATE
- Pre-trained encoder weights
- Training dynamics visualization
- Linear evaluation results
- Transfer learning benchmarks
- Augmentation configuration