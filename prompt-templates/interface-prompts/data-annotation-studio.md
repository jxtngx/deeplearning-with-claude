# Data Annotation Studio

**User Story:**
As a data labeler
I want an efficient annotation interface for various data types
So that I can create high-quality training datasets with minimal effort

**Prompt:**
"@agent-InterfaceDesigner I need to create a comprehensive data annotation studio supporting images (bounding boxes, polygons, keypoints), text (NER, classification, sentiment), audio (transcription, speaker identification), and video (object tracking, activity recognition). The interface should provide annotation templates, quality control workflows, inter-annotator agreement metrics, batch operations, and export to common formats (COCO, YOLO, spaCy, etc.). Please implement keyboard shortcuts for efficiency, undo/redo functionality, collaborative annotation modes, and progress tracking with time estimates."

## CONSTRAINTS
- Data types: Images, text, audio, video
- Annotation formats: COCO, YOLO, spaCy, Label Studio
- Team size: Up to 20 concurrent annotators
- File size: Up to 500MB per media file

## REWARDS
- Multi-format data support
- Collaborative workflows
- Quality control metrics
- Efficient annotation tools

## PENALTIES
- No collaborative features
- Missing annotation validation
- Poor performance with large files
- No export capabilities

## GOAL STATE
- Universal annotation platform
- Team collaboration tools
- Quality assurance workflows
- Multi-format export system