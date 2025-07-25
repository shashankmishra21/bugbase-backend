def generate_ai_suggestion(title, description):
    if "error" in description.lower():
        return "Check the stack trace and ensure all dependencies are correctly installed."
    elif "login" in description.lower():
        return "Ensure authentication credentials and token headers are properly set."
    elif "database" in description.lower():
        return "Check DB connection string and run migrations if needed."
    elif "css" in description.lower():
        return "Make sure stylesheets are properly linked and no syntax errors exist."
    else:
        return "Try debugging step-by-step or searching the issue online."
