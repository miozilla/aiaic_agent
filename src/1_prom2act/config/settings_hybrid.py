import os

def load_google_api_key():
    """
    Load the Google API key in a portable way:
    1. Try Kaggle secrets if running inside a Kaggle notebook.
    2. Fall back to environment variables (supports .env via python-dotenv).
    """

    GOOGLE_API_KEY = None

    # 1. Kaggle secrets (only available inside Kaggle notebooks)
    try:
        from kaggle_secrets import UserSecretsClient
        GOOGLE_API_KEY = UserSecretsClient().get_secret("GOOGLE_API_KEY")
    except ImportError:
        # Not running in Kaggle
        pass
    except Exception:
        # Kaggle secrets client exists but secret not found
        pass

    # 2. Local environment or .env file
    if not GOOGLE_API_KEY:
        try:
            from dotenv import load_dotenv
            load_dotenv()  # loads variables from .env if present
        except ImportError:
            # python-dotenv not installed, skip
            pass

        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    # 3. Final check
    if not GOOGLE_API_KEY:
        raise RuntimeError(
            "GOOGLE_API_KEY not found. "
            "Set it in Kaggle secrets, environment variables, or a local .env file."
        )

    # Export to environment for downstream libraries
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"

    return GOOGLE_API_KEY
