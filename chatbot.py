from groq import Groq
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_attendance():
    if not os.path.exists("attendance.csv"):
        return "No attendance data found."
    df = pd.read_csv("attendance.csv")
    return df.to_string()

def ask_attendance(question):
    attendance_data = load_attendance()
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""Here is the attendance data:

{attendance_data}

Answer this question: {question}"""
            }
        ]
    )
    return response.choices[0].message.content

print("Attendance Chatbot Ready. Type 'quit' to exit.")
print("-" * 40)

while True:
    question = input("Ask a question: ")
    if question.lower() == 'quit':
        break
    answer = ask_attendance(question)
    print(f"Answer: {answer}")
    print("-" * 40)