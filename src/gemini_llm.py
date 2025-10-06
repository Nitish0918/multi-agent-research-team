from litellm import completion
import os

class GeminiLLM:
    def __init__(self, model="gemini/gemini-2.0-flash"):
        self.model = model
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not set")

    def __call__(self, prompt):
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            api_key=self.api_key
        )
        # Extract content safely
        try:
            return response["choices"][0]["message"]["content"]
        except Exception:
            return str(response)
