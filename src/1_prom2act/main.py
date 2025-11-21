# promp2act/main.py
import asyncio
from config.settings import load_google_api_key
from runners.runner import run_examples
from utils.proxy import get_adk_proxy_url

def main():
    # 1. Load the Gemini API key
    #    - Works in both Kaggle (via UserSecretsClient) and local/GitHub (via .env or environment variables).
    #    - Ensures downstream agents and CLI commands can authenticate properly.
    api_key = load_google_api_key()
    print("✅ Gemini API key setup complete.")

    # 2. Run example agent workflows
    #    - Uses asyncio to execute the demo pipelines defined in runners/runner.py.
    #    - Demonstrates SequentialAgent and ParallelAgent orchestration in action.
    asyncio.run(run_examples())

    # 3. Compute the ADK proxy URL
    #    - Retrieves the correct proxied URL for the ADK web UI in Kaggle/Jupyter environments.
    #    - This URL is required when starting the ADK web interface with `adk web --url_prefix`.
    url_prefix = get_adk_proxy_url()
    print(f"ADK Web UI available at: {url_prefix}")

# 4. Entry point
#    - Ensures that main() only runs when this file is executed directly (not when imported as a module).
if __name__ == "__main__":
    main()
