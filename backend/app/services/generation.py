# This file will handle two jobs:
#Build the prompt using the retrieved chunks.
#Send that prompt to Llama 3.2 through Ollama.

import ollama

from app.core.config import settings


def build_prompt(question: str, results):

    context_parts = []

    for i, document in enumerate(results["documents"][0]):

        source = results["metadatas"][0][i]["source"]

        context_parts.append(
            f"[Source {i + 1}: {source}]\n{document}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a helpful AI and Machine Learning document assistant.

Answer the user's question using ONLY the information provided in the context.

Rules:
- Do not use outside knowledge.
- Do not invent facts.
- If the answer is not available in the context, say:
  "The information was not found in the provided documents."
- At the end, mention the source document(s) used.

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt


def generate_answer(question: str, results):

    prompt = build_prompt(
        question,
        results
    )

    response = ollama.chat(
        model=settings.ollama_model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    sources = list(dict.fromkeys(
    metadata["source"]
    for metadata in results["metadatas"][0]
))

    return answer, sources
