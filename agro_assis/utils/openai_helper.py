import os
import json
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

def analyze_plant_disease(base64_image):
    """Analyze plant image for diseases using OpenAI's vision capabilities"""
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert agricultural scientist specializing in plant disease detection. "
                    "Analyze the image and provide detailed information about any diseases detected, including "
                    "treatment recommendations. Respond in JSON format with the following structure: "
                    "{'disease_detected': boolean, 'disease_name': string, 'confidence': float, "
                    "'description': string, 'treatments': list of strings}"
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Analyze this plant image for diseases and provide treatment recommendations."
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                        }
                    ]
                }
            ],
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        raise Exception(f"Failed to analyze image: {str(e)}")
