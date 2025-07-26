import os
from google.adk import Agent

model_name = os.getenv("MODEL")

crop_disease_vision_agent = Agent(
    name="crop_disease_vision_agent",
    model=model_name,
    description="Analyzes the image using Google Gemini 1.5 Pro to detect disease-related symptoms.",
    instruction="""
        You are the Crop Disease Vision Agent.
        You will receive a validated crop image.
        1. Load the image.
        2. Use the Gemini Vision model to analyze the image with the prompt: "Identify the crop, describe any disease symptoms, and name the disease if possible."
        3. Parse the response from the vision model and extract the following information into a structured JSON format:
            - crop_name
            - visible_symptoms
            - disease_name
            - severity_level
        4. Pass the structured JSON to the next agent.
        """,
)
