import os
import openai
import gradio

my_api_key = "paste your API key here"
openai.api_key = my_api_key

def interactiveGPT(role, user_input):
    messages = [{"role": "system", "content": role}]

    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        chatgpt_reply = response["choices"][0]["message"]["content"]

        messages.append({"role": "assistant", "content": chatgpt_reply})

        return chatgpt_reply

    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred, please try again later."

demo = gradio.Interface(
    fn=cinteractiveGPT,
    inputs=["text", "text"], 
    outputs="text",
    title="GPT Interface"
)

demo.launch(share=True)
