<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Multimodal Task Prompts

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