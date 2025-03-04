from google import genai
import os
import backend.config as config

API_KEY = os.getenv("API_KEY")


def sumarry_key_points_ai(text):
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            f"""Summarize the key insights from this content:{text}. Provide a well-structured, concise summary that highlights the following:

Main Ideas: What are the central concepts or arguments presented in the video?
Key Points: Break down important details, ideas, or lessons discussed.
Action Steps: If applicable, list actionable takeaways or practical steps the viewer can apply.
Relevant Quotes: Include any powerful or thought-provoking quotes that help explain the message.
Audience Takeaways: What should viewers remember or apply after watching the video?
Ensure the summary is insightful, neutral, and digestible for viewers interested in knowledge-based content. The summary should be clear and easy to read, whether the video is long or short."""
        ],
    )
    return response.text

    
