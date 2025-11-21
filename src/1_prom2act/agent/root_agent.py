# Import ADK Components
from google.adk.agents import Agent
from google.adk.tools import google_search

print("✅ ADK components (root_agent) imported successfully.")

# Define agent
def create_root_agent():
    print("✅ Root Agent defined.")
    return Agent(
        name="helpful_assistant",
        model="gemini-2.5-flash-lite",
        description="A simple agent that can answer general questions.",
        instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
        tools=[google_search],
    )
