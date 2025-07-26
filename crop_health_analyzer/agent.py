import os
from google.adk import Agent
from .sub_agents.crop_image_intake_agent.agent import crop_image_intake_agent
from .sub_agents.crop_disease_vision_agent.agent import crop_disease_vision_agent
from .sub_agents.crop_treatment_advisor_agent.agent import crop_treatment_advisor_agent

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-flash-001")

root_agent = Agent(
    name="crop_health_analyzer",
    model=MODEL_NAME,
    description="Main agent that orchestrates the crop health analysis workflow.",
    instruction="""
        You are the Crop Health Analyzer, a system that helps identify crop diseases and recommends treatments.
        You will receive an image of a crop. You must process this image in sequence using your specialized sub-agents.
        1. First, send the image to the 'crop_image_intake_agent' to validate and prepare it.
        2. Next, the output from the intake agent should be sent to the 'crop_disease_vision_agent' for analysis.
        3. Finally, the analysis from the vision agent should be sent to the 'crop_treatment_advisor_agent' for a treatment plan.
        The final output should be the analysis and treatment plan.
        """,
    sub_agents=[
        crop_image_intake_agent,
        crop_disease_vision_agent,
        crop_treatment_advisor_agent,
    ],
)
