import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env

load_dotenv()

print("API KEY:", os.getenv("GROQ_API_KEY"))

# Initialize Groq client (make sure GROQ_API_KEY is in .env)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(query, context_chunks):
    """
    Generate answer using Groq LLM + retrieved context
    """

    # Safety check
    if not context_chunks:
        return "No relevant information found in the document."

    # Limit context to avoid overload
    context = "\n".join(context_chunks[:5])

    # Prompt
    prompt = f"""
You are a legal assistant.

Use ONLY the context below to answer the question.
If the answer is not in the context, say:
"I could not find this in the provided document."

Explain in simple, clear English.

Context:
{context}

Question:
{query}

Answer:
"""

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful legal assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=512,
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("LLM ERROR:", e)  # debug log
        return "Error generating answer. Please try again."
    
   