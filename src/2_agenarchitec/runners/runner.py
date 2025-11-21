# Import ADK Component
from google.adk.runners import InMemoryRunner

print("✅ ADK components (runner) imported successfully.")

async def run_agent(agent, prompt):
    runner = InMemoryRunner(agent=agent)
    response = await runner.run_debug(prompt)
    print(response)
    return response
