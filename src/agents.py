from crewai import Agent
from .gemini_llm import GeminiLLM

gemini_llm = GeminiLLM(model="gemini/gemini-2.0-flash")

researcher = Agent(
    role="Researcher",
    goal="Summarize 3 recent papers on LLM fine-tuning",
    backstory="Expert researcher with NLP focus",
    llm=gemini_llm
)

analyst = Agent(
    role="Analyst",
    goal="Extract strengths and weaknesses from summaries",
    backstory="Analyst who compares methodologies",
    llm=gemini_llm
)

critic = Agent(
    role="Critic",
    goal="Critique analysis and highlight research gaps",
    backstory="Skeptical peer reviewer",
    llm=gemini_llm
)

writer = Agent(
    role="Writer",
    goal="Create a humanized LinkedIn post summarizing the research findings",
    backstory="Academic writer and communicator",
    llm=gemini_llm
)
