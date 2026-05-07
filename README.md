# CrewAI Multi-Agent System

A modular multi-agent AI system built with **CrewAI**, designed to demonstrate autonomous agent collaboration, task orchestration, and workflow automation using Large Language Models (LLMs).

This project showcases how multiple specialized AI agents can work together sequentially to solve problems such as mathematical reasoning and Python code generation.

---

# Project Overview

This project implements a multi-agent architecture using the CrewAI framework.

The system contains:

- A **Math Teacher Agent** responsible for reasoning and problem solving
- A **Python Developer Agent** responsible for generating executable Python code
- Structured task orchestration using CrewAI
- YAML-based configuration for agents and tasks
- Sequential execution workflow
- Modular project architecture

The project demonstrates practical concepts used in modern AI agent systems including:

- Agent specialization
- Agent collaboration
- Task delegation
- Workflow automation
- LLM orchestration
- Autonomous reasoning pipelines

---

# Technologies Used

- Python
- CrewAI
- Large Language Models (LLMs)
- YAML Configuration
- UV Package Manager
- PyProject
- Markdown Output Generation

---

# Project Structure

```text
crewai-multi-agent-system/
│
├── my_crew/
│   ├── src/
│   │   └── my_crew/
│   │       ├── config/
│   │       │   ├── agents.yaml
│   │       │   └── tasks.yaml
│   │       ├── tools/
│   │       │   └── custom_tool.py
│   │       ├── crew.py
│   │       ├── main.py
│   │       └── __init__.py
│   │
│   ├── knowledge/
│   │   └── user_preference.txt
│   │
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── README.md
│   └── AGENTS.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Multi-Agent Architecture

## 1. Math Teacher Agent

The first agent specializes in mathematical reasoning and problem solving.

```python
@agent
def math_teacher(self) -> Agent:
```

Responsibilities:

- Understand mathematical problems
- Explain logic and reasoning
- Prepare structured solutions
- Collaborate with downstream agents

Configuration:

```python
allow_delegation=False
```

This ensures focused and isolated task execution.

---

## 2. Python Developer Agent

The second agent specializes in Python programming and code generation.

```python
@agent
def python_developer(self) -> Agent:
```

Responsibilities:

- Convert problem logic into Python code
- Generate executable implementations
- Produce structured outputs
- Save generated code into markdown files

Configuration:

```python
allow_code_execution=True
```

This enables the agent to work with executable Python workflows.

---

# Task Workflow

The system defines two sequential tasks:

## Math Task

```python
@task
def math_task(self) -> Task:
```

This task handles:

- Mathematical reasoning
- Problem understanding
- Logical decomposition

---

## Python Task

```python
@task
def python_task(self) -> Task:
```

This task:

- Generates Python implementations
- Produces output files
- Converts reasoning into code

Generated code is automatically saved into:

```text
python_code.md
```

---

# Crew Orchestration

The agents and tasks are orchestrated using a CrewAI sequential workflow.

```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    verbose=True
)
```

This demonstrates:

- Ordered task execution
- Agent coordination
- Multi-step reasoning pipelines
- Autonomous workflow management

---

# Features Implemented

## Sequential Multi-Agent Execution

The project uses:

```python
Process.sequential
```

to coordinate agents step-by-step.

---

## YAML-Based Configuration

Agents and tasks are configured externally using:

```text
agents.yaml
tasks.yaml
```

This improves:

- Scalability
- Maintainability
- Separation of logic and configuration

---

## Autonomous Problem Solving

Example input:

```python
inputs = {
    'problem': "How can I make the sum of two numbers?"
}
```

The crew:

1. Understands the mathematical problem
2. Generates reasoning steps
3. Produces Python code automatically

---

## Training Support

The project includes training functionality:

```python
def train():
```

This allows iterative crew improvement and experimentation.

---

## Replay Support

The system supports replaying executions from specific tasks:

```python
def replay():
```

Useful for:

- Debugging
- Workflow analysis
- Agent behavior inspection

---

## Testing Pipeline

The project includes testing utilities:

```python
def test():
```

This enables evaluation of agent outputs and workflows.

---

## Trigger-Based Execution

The system also supports JSON trigger payloads:

```python
def run_with_trigger():
```

This makes the architecture adaptable for:

- APIs
- Automation systems
- Event-driven workflows
- AI pipelines

---

# How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/mhditani/crewai-multi-agent-system.git
cd crewai-multi-agent-system
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run the Crew

```bash
python main.py
```

The crew will execute the workflow sequentially.

---

# Example Workflow

Input:

```text
How can I make the sum of two numbers?
```

Workflow:

1. Math Teacher Agent analyzes the problem
2. Python Developer Agent generates Python code
3. Output is saved automatically

---

# Learning Outcomes

Through this project, I practiced:

- Building autonomous AI agent systems
- Multi-agent orchestration
- CrewAI framework architecture
- Task sequencing
- LLM workflow design
- Agent specialization
- AI automation pipelines
- YAML configuration management
- Modular AI engineering practices

---

# Why This Project Matters

AI agents and multi-agent systems are becoming a major area in modern AI engineering.

Frameworks like CrewAI are increasingly used for:

- AI workflow automation
- Autonomous task execution
- Multi-step reasoning
- AI copilots
- Research agents
- Development assistants

This project demonstrates practical experience designing modular AI agent architectures using real-world orchestration patterns.

---

# Future Improvements

Potential future enhancements include:

- Web interface with Streamlit or Gradio
- Tool integration
- API deployment
- Internet-enabled agents
- Memory systems
- Retrieval-Augmented Generation (RAG)
- Hierarchical agent workflows
- Multi-agent collaboration strategies
- Database integration
- LangChain tools support

---

# Author

Created by Mohammad Itani
