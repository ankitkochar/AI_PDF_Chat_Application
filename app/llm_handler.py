from typing import List
import google.generativeai as genai
from ratelimit import limits, sleep_and_retry
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import time

# Configure the LLM once and set it as a global variable
genai.configure(api_key="AIzaSyB_F2c0L5FeP-tJpdb8XUDPfZ38VOAIGyI")
model = genai.GenerativeModel("gemini-1.5-flash")

CALLS = 15
PERIOD = 70

@sleep_and_retry
@limits(calls=CALLS, period=PERIOD)
def generate_response(prompt: str, documents: List[str]):
    global current_key_index
    
    while True:
        try:
            # Rotate to the next API key
            current_key = "AIzaSyB_F2c0L5FeP-tJpdb8XUDPfZ38VOAIGyI"
            genai.configure(api_key=current_key)
            model = genai.GenerativeModel("gemini-1.5-pro-001")
            
            # Concatenate documents for context
            doc_text = " ".join(documents)
            full_prompt = f"{doc_text}\n\nQuery: {prompt}\nProvide a detailed answer in plain text format."
            
            # Generate response with specific settings
            response = model.generate_content(
                generation_config=genai.types.GenerationConfig(
                    candidate_count=1,
                    max_output_tokens=1200,  # Adjust as needed
                    temperature=0.05,
                ),
                contents=[full_prompt],
                safety_settings={
                    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE
                }
            )
            print(response)
            return response._result.candidates[0].content.parts[0].text

        except Exception as e:
            # Check if the error is due to rate-limiting
            if "429" in str(e):
                print(f"Rate limit exceeded for API key {current_key}. Switching keys...")
                # Rotate to the next key
                current_key_index = "AIzaSyB_F2c0L5FeP-tJpdb8XUDPfZ38VOAIGyI"
                time.sleep(1)  # Brief pause before retrying
            else:
                print("Error in response generation:", e)
                raise  # Re-raise other exceptions
