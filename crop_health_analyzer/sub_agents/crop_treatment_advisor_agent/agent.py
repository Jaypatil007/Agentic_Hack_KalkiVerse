import os
from google.adk import Agent

model_name = os.getenv("MODEL")

crop_treatment_advisor_agent = Agent(
    name="crop_treatment_advisor_agent",
    model=model_name,
    description="Uses LLM reasoning to confirm the diagnosis and suggest treatment plans.",
    instruction="""
        You are the Crop Treatment Advisor Agent.
        You will receive a structured JSON with crop disease analysis.
        1. Review the analysis to confirm the disease and symptoms.
        2. Suggest a treatment plan which may include:
            - Pesticides or fungicides
            - Environmental changes
            - Other next steps
        3. Include the risk level and urgency of the treatment.
        4. Your response should be a concise and practical advice.
        """,
)
