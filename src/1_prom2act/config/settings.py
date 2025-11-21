# Configure Gemini API Key
import os

def load_google_api_key():
    try:
        # In Kaggle, secrets come from UserSecretsClient
        from kaggle_secrets import UserSecretsClient
        GOOGLE_API_KEY = UserSecretsClient().get_secret("GOOGLE_API_KEY")
    except Exception:
        # Fallback: environment variable
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    if not GOOGLE_API_KEY:
        raise RuntimeError("GOOGLE_API_KEY not found. Set it in env or Kaggle secrets.")

    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
    return GOOGLE_API_KEY
