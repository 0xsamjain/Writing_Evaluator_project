import google.genai as genai
import config; google_api = config.API_KEY

print("Paste your writing sample. Type 'END' on a new line when done:")
lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)
writing_sample = "\n".join(lines)
client = genai.Client(api_key=google_api)
model = 'gemini-2.5-flash'

                              
my_prompt = f"""
You are a writing evaluator who first correctly identifies which of the following type of para this belongs to:
Argumentative Paragraph, Cause-Effect Paragraph, Comparison and Contrast Paragraph, Problem-Solution Paragraph, Process Paragraph, Visual Description Paragraph, Formal Email (Enquiry/Complaint/Response/Request), Academic Report (Introduction/Method/Result/Discussion/Conclusion/Abstract).

Then evaluate it on these 6 criteria. Score each out of 5.

--- TYPE-SPECIFIC CRITERIA ---

1. Structure & Format
   - Does it follow the expected structure for its type?

2. Purpose Fulfillment
   - Does the writing actually do what its type is supposed to do?

3. Type-Specific Language
   - Are the right phrases/vocabulary being used for this type?

--- GENERAL WRITING CRITERIA ---

4. Grammar & Sentence Structure

5. Clarity & Conciseness

6. Cohesion & Transitions

---

For each criterion output:
Criterion name: X/5
Feedback: [1-2 lines on what worked or what to fix]

At the end:
Detected Writing Type: [type]
Overall Score: [sum]/30
Top Priority to Fix: [single most important improvement]

Writing sample:
{writing_sample}
"""

response = client.models.generate_content(model=model, contents=my_prompt)
output = response.text
print(output)