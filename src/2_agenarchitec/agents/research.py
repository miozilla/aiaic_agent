# Import ADK Component
from google.adk.agents import Agent
from google.adk.tools import google_search, AgentTool

print("✅ ADK components (research) imported successfully.")


def build_research_system():
    # Research Agent: Its job is to use the google_search tool and present findings.
    research_agent = Agent(
        name="ResearchAgent",
        model="gemini-2.5-flash-lite",
        instruction="Use google_search to find 2-3 pieces of info with citations.",
        tools=[google_search],
        output_key="research_findings", # The result of this agent will be stored in the session state with this key.
    )
    print("✅ research_agent created.")

    # Summarizer Agent: Its job is to summarize the text it receives.
    summarizer_agent = Agent(
        name="SummarizerAgent",
        model="gemini-2.5-flash-lite",
        # The instruction is modified to request a bulleted list for a clear output format.
        instruction="Summarize {research_findings} into 3-5 bullet points.",
        output_key="final_summary",
    )
    print("✅ summarizer_agent created.")

    # Root Coordinator: Orchestrates the workflow by calling the sub-agents as tools.
    '''
    # Explicit Instructions
    root_agent = Agent(
        name="ResearchCoordinator",
        model="gemini-2.5-flash-lite",
        instruction="""You are a research coordinator. Your goal is to answer the user's query by orchestrating a workflow.
        1. First, you MUST call the `ResearchAgent` tool to find relevant information on the topic provided by the user.
        2. Next, after receiving the research findings, you MUST call the `SummarizerAgent` tool to create a concise summary.
        3. Finally, present the final summary clearly to the user as your response.""",
        tools=[
            AgentTool(research_agent),
            AgentTool(summarizer_agent)
        ],
    )
    return root_agent
    '''
    root_agent = Agent(
        name="ResearchCoordinator",
        model="gemini-2.5-flash-lite",
        # This instruction tells the root agent HOW to use its tools (which are the other agents).
        instruction="Orchestrate research then summarization.",
        # We wrap the sub-agents in `AgentTool` to make them callable tools for the root agent.
        tools=[AgentTool(research_agent), AgentTool(summarizer_agent)],
    )
    print("✅ root_agent created.")
    return root_agent

