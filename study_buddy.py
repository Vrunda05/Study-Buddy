import ollama

notes = open("notes.txt").read()
messages = [{"role": "System", "content": "You are a friendly tutor. Answer using these notes:\n" + notes}]

while True:
    question = input("You: ")
    if question=="exit":
        break
    messages.append({"role": "User", "content": question})
    reply = ollama.chat(
        model="llama3.2",
        messages=messages
    )
    answer = reply["message"]["content"]
    print(answer)
    messages.append({"role": "Assistant", "content": answer})