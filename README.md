# Performance Review Analyzer

**AI-powered spreadsheet analysis assistant for employee performance and KPA review workflows**

This project is an LLM-assisted performance analysis tool that reads structured Excel inputs, compares monthly employee performance against KPA targets, and generates a clean, structured review summary through a simple Gradio interface.

## Why this project matters

Performance reviews are often stored in spreadsheets, which makes them easy to collect but slow to analyze at scale. This project shows how an AI workflow can help HR, team leads, or operations managers:

- read multiple Excel files as structured input
- compare monthly performance data against agreed KPAs
- extract objectives, metrics, blockers, and agreed actions
- generate a consistent review summary in a structured format
- expose the workflow through a lightweight upload UI



## What I built

### 1) Excel ingestion layer
The system accepts two spreadsheet inputs:
- a performance data file
- a KPA data file

It loads both files with Pandas and converts them into record dictionaries for downstream processing.

### 2) Agent-based analysis workflow
The project uses:
- a **reader agent** that reads and structures the Excel input
- an **analyst agent** that compares the data and generates the final analysis

### 3) Structured output schema
The output is organized into:
- SMART objectives
- KPI metrics
- employee self-reflection
- agreed action items
- final summary output

### 4) User interface
A Gradio-based interface lets a user upload the two Excel files and receive the generated analysis output directly in the browser.

## Technical highlights

- Excel ingestion with Pandas
- Agent-based workflow using the OpenAI Agents SDK
- Structured outputs with typed models
- Asynchronous task execution
- Gradio UI for business-user interaction
- Multi-file analysis workflow for performance vs KPA comparison


## Architecture overview

```text
User uploads Excel files
      ↓
Gradio Interface
      ↓
Task Runner
      ↓
Reader Agent
      ↓
Pandas Excel Loader
      ↓
Structured performance + KPA records
      ↓
Analyst Agent
      ↓
Schema-based performance summary
      ↓
Final review output in UI
```

## Project structure

```text
performance/
├── analyst.py
├── reader.py
├── task_runner.py
├── ui_app.py
├── .env
└── __pycache__/
```

## How it works

### Step 1: Upload source files
The user uploads:
- a performance file
- a KPA file

through the Gradio UI.

### Step 2: Read spreadsheet contents
The reader tool loads both Excel files with Pandas and converts them into structured record dictionaries.

### Step 3: Run the analysis workflow
The task runner first calls the reader agent, then passes the resulting data into the analyst agent for interpretation and summarization.

### Step 4: Generate structured output
The analyst agent returns a structured employee review containing:
- employee details
- SMART objectives
- KPI review
- self-reflection
- agreed next steps
- a final summary


## Tools and technologies

- Python
- Pandas
- Gradio
- OpenAI Agents SDK
- OpenAI models
- Async Python workflows

## Setup

```bash
git clone <your-repo-url>
cd performance
python -m venv venv
venv\Scripts\activate
pip install pandas gradio python-dotenv openai
python ui_app.py
```

## Author

**Omosule Aduramigba Adeleke**  
AI Engineer | Backend Developer | Enterprise Workflow Automation Builder
