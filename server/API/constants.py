validate_string = "Analyze the following input and check if it is anything related to trip/holiday/weekend/eateries/event/movie/shows planning. Return only '1' if true and only '0' if false: "
generate_string = "Generate a 5 item list based on the user's query, including items with the following fields: name, description, reviews, best thing to do/eat/try, average cost per person in dollars and location in longitude and latitude. The query can be about restaurants, shows, or trip itineraries. Provide the response strictly in plain text in this format "
format_string = """{"type":"Query Type","items":[{"name":"SAMPLE NAME","description":"SAMPLE DESCRIPTION","reviews":"4.5","best_to_try":"SAMPLE BEST THING","average_cost_per_person":"$20-30","location":{"longitude":"","latitude":}},],}"""
geoGuesserString = """
Let's play a game of geo-guessing!
Step 1: Choose a random country from the following list=[ "United States","United Kingdom","France","Germany","Spain","Italy","Japan","Australia","Canada","Netherlands","Switzerland","Belgium","New Zealand","Portugal","Singapore"]
Step 2: Select a random location within the chosen country.
Step 3: Provide a historical context for the location without mentioning its name.
Step 4: Offer three clues to help the guesser identify the location.
Step 5: Include the latitude and longitude coordinates of the location.
Very Important Output format: Provide the response strictly in plain text and in this format  """
geoGuesserFormat = """
{
    "data":{
            "context": "SAMPLE DESCRIPTION CONTEXT ABOUT LOCATION",
            "location": {
                "location_name":"SAMPLE LOCATION NAME",
                "longitude": "",
                "latitude": ""
            },
            "hints": [
                "HINT 1",
                "HINT 2",
                "HINT 3"
            ]
        }
}
"""
# server/API/constants.py

scoreFormat = """
You are a judge in a place guessing game. Your task is to evaluate the player's guess against the correct answer and assign a score based on the following criteria:

- **5 points**: The guess is an exact match of the location name.
- **4 points**: The guess is a close variation (e.g., city vs. region) of the correct answer.
- **3 points**: The guess identifies the correct state/province.
- **1 point**: The guess identifies correct the country.
- **0 points**: The guess is incorrect.

Input:
- `correct_answer`: {correct_answer}
- `user_guess`: {user_guess}

Match both correct answer and user guess with the location name, state/province, or country. Assign a score based on the criteria above.
Also very Important Output format: Provide the response strictly in plain text and in this format 

"""
scoreResponseFormat = """
{
    "scoring": {
        "score": "score for the guess in number in integer , max 5",
    }
}
"""



