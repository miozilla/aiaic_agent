# Import ADK Components
from google.adk.runners import InMemoryRunner
from agents.root_agent import create_root_agent

print("✅ ADK components (runner) imported successfully.")

# Run agent

def get_runner():
    agent = create_root_agent()
    print("✅ Runner created.")
    return InMemoryRunner(agent=agent)

async def run_examples():
    runner = get_runner()
    resp1 = await runner.run_debug("What is Agent Development Kit from Google? What languages is the SDK available in?")
    print(resp1)

    resp2 = await runner.run_debug("What's the weather in London?")
    print(resp2)
