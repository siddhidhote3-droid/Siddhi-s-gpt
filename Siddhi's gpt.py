from openai import OpenAI
from config import OPENAI_API_KEY, MODEL, MEMORY_LIMIT
from memory import AIMemory
from file_reader import read_file
from robotics import robot_controller

client = OpenAI(api_key=OPENAI_API_KEY)
memory = AIMemory(MEMORY_LIMIT)

print("🚀 Mega AI Assistant (type 'exit' to quit)")
print("Commands:")
print("- read file.txt / file.pdf")
print("- robot move forward / left / right / stop\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    memory.add("user", user_input)

    # FILE READER
    if user_input.lower().startswith("read "):
        file_path = user_input.replace("read ", "")
        file_content = read_file(file_path)
        reply = f"📄 File Content Summary:\n{file_content[:1000]}"

    # ROBOTICS
    elif "robot" in user_input.lower():
        reply = robot_controller(user_input)

    # NORMAL AI CHAT
    else:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are an intelligent, helpful AI assistant."},
                *memory.get()
            ]
        )
        reply = response.choices[0].message.content

    memory.add("assistant", reply)
    print("AI:", reply, "\n")
