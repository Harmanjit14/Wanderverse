import google.generativeai as genai
from ..API.constants import geoGuesserFormat, geoGuesserString
import json


# Helper function to create a consistent JSON response format
def format_json_response(item):
    data = item.get("data", {})
    return {
        "context": data.get("context", "No description available"),
        "location": data.get("location", {}),
        "hints": data.get("hints", []),
    }


def getRandomQuiz():
    # Refine query for Gemini API to specify type of response requested
    refined_query = geoGuesserString + geoGuesserFormat
    # Send query to Gemini API and get response
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(refined_query)
        # Check if the response contains candidates and valid content
        if response and response.candidates:
            candidate = response.candidates[0]
            content_text = candidate.content.parts[0].text.strip()

            # Assuming the content text is in a JSON-compatible format, parse it
            try:
                # Parse the response content to JSON
                content_text = content_text.strip("json")
                content_text = content_text.strip("```")
                generated_data = json.loads(content_text)

                # Format the response into a constant structure
                formatted_response = format_json_response(generated_data)

                return formatted_response

            except Exception as e:
                print("Error while parsing JSON response ", e)
                print("Response \n", content_text)
    except Exception as e:
        print(f"Error while generating quiz: {e}")
        return None

    return None
