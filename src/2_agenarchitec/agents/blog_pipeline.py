# Import ADK Component
from google.adk.agents import Agent, SequentialAgent

print("✅ ADK components (blog_pipeline) imported successfully.")

def build_blog_pipeline():

    # Outline Agent: Creates the initial blog post outline.
    outline_agent = Agent(
        name="OutlineAgent",
        model="gemini-2.5-flash-lite",
        instruction="Create blog outline with headline, intro, sections, conclusion.",
        output_key="blog_outline", # The result of this agent will be stored in the session state with this key.
    )
    print("✅ outline_agent created.")

    # Writer Agent: Writes the full blog post based on the outline from the previous agent.
    writer_agent = Agent(
        name="WriterAgent",
        model="gemini-2.5-flash-lite",
        # The `{blog_outline}` placeholder automatically injects the state value from the previous agent's output.
        instruction="Write 200-300 word blog post from {blog_outline}.",
        output_key="blog_draft", # The result of this agent will be stored with this key.
    )
    print("✅ writer_agent created.")

    # Editor Agent: Edits and polishes the draft from the writer agent.
    editor_agent = Agent(
        name="EditorAgent",
        model="gemini-2.5-flash-lite",
        # This agent receives the `{blog_draft}` from the writer agent's output.
        instruction="Polish {blog_draft} for grammar, flow, clarity.",
        output_key="final_blog", # This is the final output of the entire pipeline.
    )
    print("✅ editor_agent created.")

    print("✅ Sequential Agent created.")
    return SequentialAgent(
        name="BlogPipeline",
        sub_agents=[outline_agent, writer_agent, editor_agent],
    )
    

