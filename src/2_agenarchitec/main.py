# agenarchitec/main.py
import asyncio
from config.settings import load_google_api_key
from agents.research import build_research_system
from agents.blog_pipeline import build_blog_pipeline
from agents.executive import build_executive_system
from agents.story_pipeline import build_story_pipeline
from runners.runner import run_agent

async def main():
    load_google_api_key()

    # Run agent & ask about a topic
    await run_agent(build_research_system(),
        "What are the latest advancements in quantum computing and what do they mean for AI?")
    await run_agent(build_blog_pipeline(),
        "Write a blog post about the benefits of multi-agent systems for software developers")
    await run_agent(build_executive_system(),
        "Run the daily executive briefing on Tech, Health, and Finance")
    await run_agent(build_story_pipeline(),
        "Write a short story about a lighthouse keeper who discovers a mysterious, glowing map")

if __name__ == "__main__":
    asyncio.run(main())
