# Multimodal Task Prompts

## Vision-Language Understanding

**User Story:**
As a multimodal AI researcher
I want to build models that understand both images and text
So that I can enable zero-shot classification and cross-modal retrieval

**Prompt:**
"I need to implement a vision-language model using CLIP, ALIGN, or BLIP variants that can process images at 224x224 resolution and text up to 77 tokens. The model should achieve over 70% zero-shot classification accuracy and support efficient image-text matching with contrastive learning. Please build the complete pipeline including multi-lingual support, hard negative mining, image augmentation, gradient accumulation for large batches, image search functionality, and embedding visualization tools."

### CONSTRAINTS
- Model: CLIP, ALIGN, or BLIP variants
- Image resolution: 224x224 minimum
- Text length: Up to 77 tokens
- Batch size: Optimize for available GPU memory

### REWARDS
- Zero-shot classification accuracy >70%
- Efficient image-text matching
- Multi-lingual support
- Contrastive learning implementation

### PENALTIES
- No image augmentation pipeline
- Missing hard negative mining
- Poor batch sampling strategy

### GOAL STATE
- Trained vision-language model
- Image search functionality
- Zero-shot classifier interface
- Embedding visualization

---

## Image Captioning

**User Story:**
As an accessibility engineer
I want to automatically generate descriptive captions for images
So that visual content becomes accessible to users with visual impairments

**Prompt:**
"I need to build an image captioning system using encoder-decoder or autoregressive architectures trained on COCO Captions. The system should generate captions up to 50 tokens with BLEU-4 score above 0.35, using beam search with width 3-5. Please implement diverse caption generation with length normalization, attention visualization, real-time inference, multiple caption sampling options, and a web interface where users can upload images and receive instant captions."

### CONSTRAINTS
- Architecture: Encoder-decoder or autoregressive
- Dataset: COCO Captions or custom annotations
- Beam search: Width 3-5
- Maximum caption length: 50 tokens

### REWARDS
- BLEU-4 score >0.35
- Diverse caption generation
- Attention visualization
- Real-time inference capability

### PENALTIES
- Repetitive caption patterns
- Missing evaluation metrics
- No length normalization

### GOAL STATE
- Caption generation model
- Multiple caption sampling
- Web interface with upload
- Evaluation suite with metrics

---

## Visual Question Answering

**User Story:**
As an educational technology developer
I want to build a system that answers questions about images
So that students can interactively learn from visual materials

**Prompt:**
"I need to create a Visual Question Answering system combining ViT with language models to achieve over 65% accuracy on VQA-v2 benchmark. The system should handle all common question types with either multiple choice or generative answers. Please implement multi-modal fusion strategies, visual grounding with attention maps, confidence scoring, question type analysis, numerical reasoning capabilities, and an interactive playground with comprehensive error analysis tools."

### CONSTRAINTS
- Model: ViT + language model combination
- Question types: All common categories
- Answer format: Multiple choice or generation
- Accuracy target: >65% on VQA-v2

### REWARDS
- Attention map interpretation
- Multi-modal fusion strategies
- Question type analysis
- Confidence scoring

### PENALTIES
- No visual grounding
- Missing answer validation
- Poor numerical reasoning

### GOAL STATE
- VQA model with demos
- Performance by question type
- Interactive playground
- Error analysis tools

---

## Audio-Visual Speech Recognition

**User Story:**
As a video processing engineer
I want to transcribe speech using both audio and visual lip reading cues
So that I can achieve robust transcription even in noisy environments

**Prompt:**
"I need to implement an audio-visual speech recognition system using Conformer or Wav2Vec2 architectures that combines audio with lip reading from video. The system should achieve WER below 10% on clean speech in English, with real-time processing capabilities. Please build the complete pipeline including audio-visual synchronization, multi-modal fusion, noise robustness testing, speaker diarization, streaming inference support, and evaluation on multiple datasets."

### CONSTRAINTS
- Input: Audio + video (lip reading)
- Model: Conformer or Wav2Vec2 based
- Languages: English minimum
- WER target: <10% on clean speech

### REWARDS
- Multi-modal fusion benefits
- Noise robustness
- Real-time processing
- Speaker diarization

### PENALTIES
- No synchronization handling
- Missing data augmentation
- Poor low-resource performance

### GOAL STATE
- AV-ASR model pipeline
- Streaming inference support
- Evaluation on multiple datasets
- Robustness testing suite

---

## Document Understanding

**User Story:**
As a document automation specialist
I want to extract structured information from scanned documents
So that I can digitize and process paper-based workflows automatically

**Prompt:**
"I need to build a document understanding system that processes scanned documents with layout awareness for classification, extraction, and QA tasks. The system should integrate OCR and support multi-lingual documents with layout-aware processing using coordinate embeddings. Please implement table extraction, form field understanding, handwriting support, confidence thresholds for extracted data, and a validation interface for reviewing and correcting extractions."

### CONSTRAINTS
- Input: Scanned documents with layout
- Tasks: Classification, extraction, QA
- OCR integration required
- Languages: Multi-lingual support

### REWARDS
- Layout-aware processing
- Table extraction capability
- Form understanding
- Handwriting support

### PENALTIES
- No coordinate embedding
- Missing layout features
- Poor scan quality handling

### GOAL STATE
- Document AI pipeline
- Field extraction API
- Confidence thresholds
- Validation interface