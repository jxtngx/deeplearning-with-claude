<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Multimodal Task Prompts

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