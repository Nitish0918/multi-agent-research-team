import streamlit as st
from crewai import Crew
from src.agents import researcher, analyst, critic, writer
from src.tasks import tasks

st.set_page_config(page_title="Multi-Agent Research Team", layout="centered")
st.title("🤖 Multi-Agent Research Team (Gemini + CrewAI)")

if st.button("Run Research Team"):
    crew = Crew(agents=[researcher, analyst, critic, writer], tasks=tasks)
    result = crew.kickoff()
    st.subheader("📄 Final Research Report")
    st.write(result)
