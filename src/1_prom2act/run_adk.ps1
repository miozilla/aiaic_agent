# Ensure GOOGLE_API_KEY is set in your environment before running
if (-not $env:GOOGLE_API_KEY) {
    Write-Host "❌ GOOGLE_API_KEY is not set. Use: setx GOOGLE_API_KEY your_key"
    exit 1
}

# 1. Create the sample agent
adk create sample-agent --model gemini-2.5-flash-lite --api_key $env:GOOGLE_API_KEY

# 2. Start the ADK web UI
# Replace {url_prefix} with the actual value returned by get_adk_proxy_url()
adk web --url_prefix {url_prefix} --api_key $env:GOOGLE_API_KEY
