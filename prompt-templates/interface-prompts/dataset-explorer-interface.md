# Dataset Explorer Interface

**User Story:**
As a data engineer
I want to explore and analyze datasets visually
So that I can identify patterns, outliers, and data quality issues before training

**Prompt:**
"@agent-InterfaceDesigner I need to create a dataset explorer interface for ML datasets with support for images, text, audio, and tabular data. The interface should provide grid/list view toggles, filtering and search capabilities, statistical summaries and distributions, data augmentation preview, and annotation tools for labeling. Please implement lazy loading for large datasets, virtual scrolling for performance, batch operations for multiple items, keyboard navigation, and integration with label studio formats."

## CONSTRAINTS
- Dataset size: Up to 1M samples
- Load time: <2s for initial view
- Supported formats: Images, CSV, JSON, Audio
- Browser memory: <500MB usage

## REWARDS
- Multi-format data support
- Advanced filtering/search
- Statistical visualizations
- Annotation capabilities

## PENALTIES
- No pagination or virtualization
- Missing data statistics
- Poor search performance
- No batch operations

## GOAL STATE
- Universal dataset explorer
- Efficient data browsing
- Statistical insights
- Annotation interface