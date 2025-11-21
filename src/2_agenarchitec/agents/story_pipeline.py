# Import ADK Component
from google.adk.agents import Agent, SequentialAgent, LoopAgent
from google.adk.tools import FunctionTool

print("✅ ADK components (story_pipeline) imported successfully.")

# This is the function that the RefinerAgent will call to exit the loop.
def exit_loop():
    print("✅ exit_loop function created.")
    return {"status": "approved", "message": "Story approved. Exiting refinement loop."}

def build_story_pipeline():

    # This agent runs ONCE at the beginning to create the first draft.
    initial_writer = Agent(
        name="InitialWriterAgent",
        model="gemini-2.5-flash-lite",
        instruction="Write 100-150 word short story draft.",
        output_key="current_story", # Stores the first draft in the state.
    )
    print("✅ initial_writer_agent created.")

    # This agent's only job is to provide feedback or the approval signal. It has no tools.
    critic = Agent(
        name="CriticAgent",
        model="gemini-2.5-flash-lite",
        instruction="Review {current_story}. Respond 'APPROVED' or give feedback.",
        output_key="critique", # Stores the feedback in the state.
    )
    print("✅ critic_agent created.")

    # This agent refines the story based on critique OR calls the exit_loop function.
    refiner = Agent(
        name="RefinerAgent",
        model="gemini-2.5-flash-lite",
        instruction="If critique=='APPROVED', call exit_loop. Else, rewrite {current_story}.",
        output_key="current_story", # It overwrites the story with the new, refined version.
        tools=[FunctionTool(exit_loop)], # The tool is now correctly initialized with the function reference.
    )
    print("✅ refiner_agent created.")

    # The LoopAgent contains the agents that will run repeatedly: Critic -> Refiner.
    loop = LoopAgent(
        name="StoryRefinementLoop",
        sub_agents=[critic, refiner],
        max_iterations=2,
    )

    # The root agent is a SequentialAgent that defines the overall workflow: Initial Write -> Refinement Loop.
    print("✅ Loop and Sequential Agents created.")
    return SequentialAgent(
        name="StoryPipeline",
        sub_agents=[initial_writer, loop],
    )
