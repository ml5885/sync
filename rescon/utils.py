from openai.error import AuthenticationError, PermissionError, RateLimitError

def handle_error(e):
    if isinstance(e, AuthenticationError): return "API key is invalid."
    if isinstance(e, PermissionError): return "Account does not have permission to run GPT-4 Turbo model."
    if isinstance(e, RateLimitError): return "Rate limit is too low for API key."
    return "An error has occured."