# 🤖 Multi-Agent Research Team (Gemini + CrewAI)

This project demonstrates a **multi-agent system** where different AI agents collaborate like a research group.

## 🚀 Features
- **Researcher Agent**: Finds and summarizes papers
- **Analyst Agent**: Extracts pros/cons
- **Critic Agent**: Challenges analysis
- **Writer Agent**: Generates a final research report

## 🛠️ Tech Stack
- [CrewAI](https://github.com/joaomdmoura/crewai) for agent orchestration
- [Gemini](https://ai.google.dev/) as the LLM backend
- [Streamlit](https://streamlit.io/) for UI

## 📂 Project Structure
```
multi-agent-research-team/
 ┣ src/
 ┃ ┣ app.py         # Streamlit UI
 ┃ ┣ agents.py      # Agent definitions
 ┃ ┣ tasks.py       # Task definitions
 ┣ requirements.txt
 ┣ README.md
```

## 🛠️ Setup
```bash
git clone https://github.com/yourusername/multi-agent-research-team.git
cd multi-agent-research-team
pip install -r requirements.txt
```

Set your **Google API Key**:
```bash
export GOOGLE_API_KEY="your_api_key"
```

## ▶️ Run
```bash
streamlit run src/app.py
```

The agents will collaborate and generate a final research report.
