import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)


def extract_resume_insights(resume_text):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Analyze the resume carefully and identify the DOMAIN first.

    Then return roles ONLY from that domain.

    STRICT RULES:
    - If resume contains Networking → give Network roles
    - If resume contains Java → give Software/Backend roles
    - If resume contains Data Science → give Data roles
    - DO NOT always give Data Scientist
    - Roles must match skills exactly

    Output ONLY JSON:
    {{
      "roles": ["Role1", "Role2", "Role3"]
    }}

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    try:
        data = json.loads(response.text)
        return data["roles"]
    except:
        return ["Software Engineer"]