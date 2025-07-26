🧠 Agent 1: CropImageIntakeAgent
🔹 Role:
Responsible for receiving, validating, and preparing the crop image for downstream processing.

📋 Responsibilities:
Accept an image file (from UI, API, CLI, etc.).

Validate image format, size, and resolution.

Convert or resize image if needed (e.g., to JPEG/PNG, 512x512).

Save to temporary path or pass the image buffer to the next agent.

⚙️ Key Notes:
Accept only allowed image types: .jpg, .jpeg, .png.

Reject corrupt or blank images.

(Optional) Log metadata like image size, timestamp.

🧠 Agent 2: CropDiseaseVisionAgent
🔹 Role:
Analyzes the image using Google Gemini 1.5 Pro (multimodal) to detect disease-related symptoms.

📋 Responsibilities:
Load the image from input or path.

Call Gemini Vision model with the image and prompt.

Parse the Gemini response to extract:

Crop name

Visible symptoms

Disease name (if recognized)

Severity level

⚙️ Key Notes:
Use Gemini 1.5 Pro with image + prompt like:

plaintext
Copy
Edit
"Identify the crop, describe any disease symptoms, and name the disease if possible."
Expect freeform text → convert into structured output (dict or JSON).

🧠 Agent 3: CropTreatmentAdvisorAgent
🔹 Role:
Uses LLM reasoning (text-only) to confirm the diagnosis and suggest treatment plans.

📋 Responsibilities:
Accept structured output from CropDiseaseVisionAgent.

Confirm the disease name and validate symptoms.

Suggest pesticide/fungicide, environmental changes, or other next steps.

Include risk level and urgency of treatment.

⚙️ Key Notes:
Use Gemini text model (no image input).

Allow prompt chaining: e.g., “Given this disease and severity, what is the best treatment for [crop]?”

Return concise, practical advice (avoid long essays).

🧩 Agent Flow Summary
mermaid
Copy
Edit
graph LR
A[User uploads image] --> B[CropImageIntakeAgent]
B --> C[CropDiseaseVisionAgent]
C --> D[CropTreatmentAdvisorAgent]
D --> E[Final structured response]
