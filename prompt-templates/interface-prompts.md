<!-- Copyright 2025 jxtngx | Apache 2.0 License | https://github.com/jxtngx/claude-code-pytorch -->

# Interface Design Task Prompts

## ML Model Playground Interface

**User Story:**
As a machine learning researcher
I want an interactive web interface for experimenting with model parameters
So that I can visualize predictions and understand model behavior in real-time

**Prompt:**
"@agent-InterfaceDesigner I need to create an interactive ML model playground interface with real-time parameter adjustment, live prediction visualization, and performance metrics display. The interface should handle model selection from a dropdown, hyperparameter sliders with instant updates, input data upload or manual entry, and animated visualizations of predictions. Please implement using the dark theme design system in apps/global.css with CSS custom properties, WebSocket connections for real-time updates, responsive layout for desktop and mobile using CSS Grid/Flexbox, keyboard shortcuts for power users (space for play/pause, arrow keys for parameter adjustment), and export functionality for results and configurations as JSON/CSV."

### CONSTRAINTS
- Framework: Vanilla JavaScript with global.css CSS custom properties
- Real-time updates: <100ms latency via WebSocket
- Browser support: Chrome 88+, Firefox 85+, Safari 14+, Edge 88+
- Mobile responsive: 320px minimum width with touch-friendly controls
- Accessibility: WCAG 2.1 AA compliance with keyboard navigation

### REWARDS
- Real-time parameter adjustment
- Live prediction visualization
- Performance metrics dashboard
- Export/import configurations

### PENALTIES
- No loading states for async operations
- Missing error handling for WebSocket
- Poor mobile experience
- Inaccessible to screen readers

### GOAL STATE
- Interactive playground interface
- Real-time model experimentation
- Performance visualization
- Configuration management

---

## Training Progress Dashboard

**User Story:**
As a data scientist
I want to monitor training progress across multiple experiments
So that I can compare models and make informed decisions about hyperparameters

**Prompt:**
"@agent-InterfaceDesigner I need to build a comprehensive training progress dashboard that displays real-time metrics for multiple concurrent training runs. The dashboard should show loss curves with zoom and pan capabilities, accuracy and validation metrics over epochs, resource utilization (GPU/CPU/memory), estimated time remaining, and comparative views between experiments. Please implement using Chart.js for visualizations, server-sent events for live updates, collapsible experiment panels, metric export to CSV/JSON, and integration with TensorBoard logs."

### CONSTRAINTS
- Update frequency: Every 1-5 seconds
- Maximum concurrent experiments: 10
- Chart performance: 60fps scrolling
- Data retention: Last 1000 epochs

### REWARDS
- Multi-experiment comparison
- Interactive chart controls
- Resource monitoring
- Export capabilities

### PENALTIES
- No data persistence on refresh
- Missing comparison features
- Poor performance with many datapoints
- No mobile optimization

### GOAL STATE
- Live training dashboard
- Multi-run comparison
- Interactive visualizations
- Metric export system

---

## Dataset Explorer Interface

**User Story:**
As a data engineer
I want to explore and analyze datasets visually
So that I can identify patterns, outliers, and data quality issues before training

**Prompt:**
"@agent-InterfaceDesigner I need to create a dataset explorer interface for ML datasets with support for images, text, audio, and tabular data. The interface should provide grid/list view toggles, filtering and search capabilities, statistical summaries and distributions, data augmentation preview, and annotation tools for labeling. Please implement lazy loading for large datasets, virtual scrolling for performance, batch operations for multiple items, keyboard navigation, and integration with label studio formats."

### CONSTRAINTS
- Dataset size: Up to 1M samples
- Load time: <2s for initial view
- Supported formats: Images, CSV, JSON, Audio
- Browser memory: <500MB usage

### REWARDS
- Multi-format data support
- Advanced filtering/search
- Statistical visualizations
- Annotation capabilities

### PENALTIES
- No pagination or virtualization
- Missing data statistics
- Poor search performance
- No batch operations

### GOAL STATE
- Universal dataset explorer
- Efficient data browsing
- Statistical insights
- Annotation interface

---

## Model Comparison Matrix

**User Story:**
As a model evaluator
I want to compare multiple models side-by-side
So that I can select the best model for production deployment

**Prompt:**
"@agent-InterfaceDesigner I need to build a model comparison matrix interface that displays performance metrics, inference speed, model size, and accuracy across different test sets. The interface should include sortable columns, heatmap coloring for metric values, detailed drill-down views, confidence intervals, and export to presentation formats. Please implement radar charts for multi-metric comparison, parallel coordinates for hyperparameters, statistical significance tests, model card generation, and shareable comparison links."

### CONSTRAINTS
- Maximum models: 20 for comparison
- Metrics: Customizable up to 50
- Export formats: PDF, PNG, CSV
- Load time: <1s for 20 models

### REWARDS
- Comprehensive comparison matrix
- Visual metric representations
- Statistical significance testing
- Export and sharing features

### PENALTIES
- No sorting or filtering
- Missing confidence intervals
- Poor handling of missing data
- No responsive design

### GOAL STATE
- Model comparison interface
- Multi-metric visualization
- Statistical analysis
- Export capabilities

---

## Inference API Testing Console

**User Story:**
As an API developer
I want to test ML model endpoints interactively
So that I can validate API behavior and debug integration issues

**Prompt:**
"@agent-InterfaceDesigner I need to create an API testing console for ML model inference endpoints with support for multiple input formats, authentication methods, and response visualization. The console should provide request builder with syntax highlighting, response formatter with JSON/XML views, latency and throughput metrics, batch request testing, and request history with replay. Please implement cURL command generation, Postman collection export, response diff comparison, mock response mode, and WebSocket endpoint testing."

### CONSTRAINTS
- Request size: Up to 10MB
- History retention: Last 100 requests
- Batch size: Up to 100 requests
- Response time tracking: Microsecond precision

### REWARDS
- Multi-format request builder
- Response visualization
- Performance metrics
- Request history and replay

### PENALTIES
- No authentication support
- Missing batch testing
- Poor error visualization
- No request templates

### GOAL STATE
- API testing console
- Performance monitoring
- Request management
- Integration debugging

---

## Hyperparameter Optimization Visualizer

**User Story:**
As an ML engineer
I want to visualize hyperparameter optimization progress
So that I can understand the search space and identify optimal configurations

**Prompt:**
"@agent-InterfaceDesigner I need to build a hyperparameter optimization visualizer that shows parameter importance, optimization trajectory, and parallel coordinate plots. The interface should display Bayesian optimization progress, grid/random search coverage, early stopping indicators, convergence metrics, and best configuration highlights. Please implement 3D parameter space visualization, interactive parameter filtering, optimization history timeline, configuration comparison tools, and integration with Optuna/Ray Tune/Weights & Biases."

### CONSTRAINTS
- Parameter dimensions: Up to 20
- Trial history: Up to 10,000 trials
- Update frequency: Real-time
- Visualization performance: 30fps minimum

### REWARDS
- Multi-dimensional visualization
- Optimization progress tracking
- Parameter importance analysis
- Integration with HPO frameworks

### PENALTIES
- No real-time updates
- Missing importance metrics
- Poor high-dimensional handling
- No export functionality

### GOAL STATE
- HPO visualization dashboard
- Parameter space exploration
- Optimization insights
- Framework integration

---

## Model Deployment Monitor

**User Story:**
As a DevOps engineer
I want to monitor ML model deployments in production
So that I can track performance, health, and resource usage across multiple endpoints

**Prompt:**
"@agent-InterfaceDesigner I need to build a model deployment monitoring dashboard that tracks multiple ML model endpoints in production. The interface should display real-time inference latency, throughput metrics, error rates, model drift detection, resource utilization (CPU/GPU/memory), and endpoint health status. Please implement alerting thresholds with visual indicators, historical performance charts, A/B testing comparison views, logs viewer with filtering, and integration with monitoring services like Prometheus/Grafana/DataDog."

### CONSTRAINTS
- Endpoint monitoring: Up to 50 concurrent models
- Metrics refresh: Every 5-30 seconds
- Historical data: 30 days retention
- Alert response: <1 second notification

### REWARDS
- Multi-endpoint monitoring
- Real-time alerting system
- Performance trend analysis
- A/B testing visualization

### PENALTIES
- No alerting system
- Missing historical charts
- Poor handling of offline endpoints
- No mobile responsiveness

### GOAL STATE
- Production monitoring dashboard
- Automated alerting system
- Performance analytics
- Health status overview

---

## Data Annotation Studio

**User Story:**
As a data labeler
I want an efficient annotation interface for various data types
So that I can create high-quality training datasets with minimal effort

**Prompt:**
"@agent-InterfaceDesigner I need to create a comprehensive data annotation studio supporting images (bounding boxes, polygons, keypoints), text (NER, classification, sentiment), audio (transcription, speaker identification), and video (object tracking, activity recognition). The interface should provide annotation templates, quality control workflows, inter-annotator agreement metrics, batch operations, and export to common formats (COCO, YOLO, spaCy, etc.). Please implement keyboard shortcuts for efficiency, undo/redo functionality, collaborative annotation modes, and progress tracking with time estimates."

### CONSTRAINTS
- Data types: Images, text, audio, video
- Annotation formats: COCO, YOLO, spaCy, Label Studio
- Team size: Up to 20 concurrent annotators
- File size: Up to 500MB per media file

### REWARDS
- Multi-format data support
- Collaborative workflows
- Quality control metrics
- Efficient annotation tools

### PENALTIES
- No collaborative features
- Missing annotation validation
- Poor performance with large files
- No export capabilities

### GOAL STATE
- Universal annotation platform
- Team collaboration tools
- Quality assurance workflows
- Multi-format export system

---

## Experiment Reproducibility Hub

**User Story:**
As a research scientist
I want to track and reproduce ML experiments
So that I can ensure scientific rigor and share reproducible results

**Prompt:**
"@agent-InterfaceDesigner I need to build an experiment reproducibility hub that captures code versions, hyperparameters, dataset versions, environment configurations, and random seeds for ML experiments. The interface should provide experiment comparison tables, dependency graphs, reproducibility checklists, one-click experiment recreation, and integration with version control (Git) and experiment tracking (MLflow, Weights & Biases). Please implement environment diff visualization, dependency conflict detection, experiment cloning workflows, and automated documentation generation."

### CONSTRAINTS
- Version control: Git integration required
- Experiment tracking: MLflow/W&B compatibility
- Environment capture: Docker/conda support
- Storage: Up to 10GB per experiment

### REWARDS
- Complete experiment tracking
- One-click reproduction
- Dependency management
- Automated documentation

### PENALTIES
- No version control integration
- Missing environment capture
- Poor comparison features
- No automated checks

### GOAL STATE
- Reproducibility tracking system
- Experiment comparison tools
- Environment management
- Documentation automation