from crewai import Task
from .agents import researcher, analyst, critic, writer

# Define tasks for each agent
task1 = Task(description="Summarize 3 recent papers on LLM fine-tuning", agent=researcher,expected_output = "Concise, humanized LinkedIn post highlighting the key takeaways from the papers")
task2 = Task(description="Extract strengths and weaknesses from the summaries", agent=analyst,expected_output = "Clear LinkedIn-style post listing strengths and weaknesses in an easy-to-read format")
task3 = Task(description="Critique the analysis and highlight gaps", agent=critic,expected_output = "Engaging LinkedIn post pointing out overlooked aspects and providing fresh perspectives")
task4 = Task(description="Write a research summary report", agent=writer,expected_output = "Polished LinkedIn-ready post summarizing the entire research discussion in a professional tone")

tasks = [task1, task2, task3, task4]
