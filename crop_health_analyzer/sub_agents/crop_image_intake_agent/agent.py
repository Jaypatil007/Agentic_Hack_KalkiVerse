import os
from google.adk import Agent

model_name = os.getenv("MODEL")

crop_image_intake_agent = Agent(
    name="crop_image_intake_agent",
    model=model_name,
    description="Receives, validates, and prepares crop images for processing.",
    instruction="""
        You are the Crop Image Intake Agent.
        Your job is to receive an image, validate it, and prepare it for the next step.
        1. Accept an image file.
        2. Validate the image format (must be .jpg, .jpeg, or .png).
        3. Reject corrupt or blank images.
        4. If the image is valid, pass the image path or buffer to the next agent.
        """,
)
