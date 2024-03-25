from openai import OpenAI
from dotenv import load_dotenv
import os


# load the enviroments variables
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)


# creating the func to assistent
def chat_answer(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a musician's assistant, proficient in elucidating intricate programming concepts with a touch of creative finesse."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message


if __name__ == "__main__":
    while True:
        user_input = input("Type your question: ")
        if user_input.lower() in ["quit", "text", "bye"]:
            break

        response = chat_answer(user_input)
        print("Chatbot: ", response)
