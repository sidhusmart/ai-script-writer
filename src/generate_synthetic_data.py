import json
from openai import OpenAI
client = OpenAI(api_key='API_KEY')

def generate_logline_title():
    response = client.chat.completions.create(
    model="gpt-4o",
    response_format={ "type": "json_object" },
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "You are responsible for generating synthetic data for a script-writing task. Be creative in your approach and add diversity to the examples by considering various genres, different audience types, multi-ethnic situations."
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "I want your help in creating several examples of user-provided log lines and the corresponding movie or story titles that can be given for that log line. I have provided some examples below in JSON format:\n\n{ \"logline\": \"A historical drama centered around the life of a young woman in Victorian England who defies societal norms to become a pioneering doctor. Her journey is fraught with challenges as she faces gender discrimination, personal sacrifices, and the struggle to gain acceptance in a male-dominated field.\", \"title\": \"Against All Odds\"}\n{ \"logline\": \"A fantasy story set in a magical kingdom where a young farm girl discovers she has the power to communicate with dragons. As tensions rise between humans and dragons, she must navigate political intrigue and ancient prophecies to unite the two factions and save her world from impending doom.\", \"title\": \"Dragon Whisperer\"}\n{ \"logline\": \"A modern-day thriller where a brilliant but troubled detective must solve a series of cryptic murders that are linked to an underground network of hackers. As he delves deeper into the case, he uncovers a conspiracy that threatens national security and must race against time to prevent a catastrophe.\", \"title\": \"Code of Silence\"}\n\nI want you to create several examples and provide the output in the same JSON format as above. Please give me only the examples directly and nothing else. I don't want any other information or sentences as that will hurt the downstream processing of these examples.\n"
            }
        ]
        },
    ],
    temperature=1.28,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    print (response.choices[0].message.content)
    parsed_response = json.loads(response.choices[0].message.content)  # Parse the JSON content of the response
    return parsed_response

if __name__ == "__main__":
    examples = generate_logline_title()
    print (examples)