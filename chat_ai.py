from transformers import pipeline

print("Loading AI model... please wait")

chatbot = pipeline("text-generation", model="gpt2", pad_token_id=50256)

print("AI ready! Type 'exit' to stop.\n")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("AI: Bye 👋")
        break

    prompt = f"Question: {user}\nAnswer:"

    response = chatbot(
        prompt, max_new_tokens=60, do_sample=True, temperature=0.6, top_p=0.9
    )

    text = response[0]["generated_text"]
    answer = text.split("Answer:")[-1].strip()

    print("AI:", answer)
