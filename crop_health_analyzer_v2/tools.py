import os
from google.cloud import storage
from google import genai
from google.genai.types import Part
from dotenv import load_dotenv

load_dotenv()

GCS_BUCKET_PATH = os.getenv("GCS_BUCKET_PATH")
MODEL = os.getenv("MODEL", "gemini-2.0-flash")


def analyze_crop_image(image_name: str, farmer_prompt: str) -> str:
    """
    Analyzes a crop image from a GCS bucket using the Gemini model.

    Args:
        image_name (str): The name of the image file in the GCS bucket.
        farmer_prompt (str): The prompt from the farmer.

    Returns:
        str: The analysis of the crop image.
    """
    try:
        client = genai.Client()
        image_uri = f"{GCS_BUCKET_PATH}/{image_name}"
        response = client.generate_content(
            model=MODEL,
            contents=[
                farmer_prompt,
                Part.from_uri(
                    file_uri=image_uri,
                    mime_type="image/jpeg",  # Assuming JPEG, adjust if needed
                ),
            ],
        )
        return response.text
    except Exception as e:
        return f"Error analyzing image: {e}"
