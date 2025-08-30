import pandas as pd

# Access the questions.csv file
file_path = "questions.csv"
df = pd.read_csv(file_path)
first_question = df["questions"][0]
print(first_question)


df["answer"] = ""


# Initialise gemini API
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=f"answer the following question in a single sentence: {first_question}",
)

# stores the answer at the specified index
df["answer"][0] = response.text
df.to_csv("data/answers_gemini-2.5-flash-lite.csv")

print(response.text)
