import google.generativeai as genai
import config; google_api = config.API_KEY

writing_sample = input("Paste your writing sample here:\n")
genai.configure(api_key=google_api)
model = genai.GenerativeModel("gemini-1.5-flash")
                              
my_prompt = f"""
[YOUR PROMPT GOES HERE])

Writing sample:
{writing_sample}
"""

response = model.generate_content(my_prompt)
output = response.text
print(output)