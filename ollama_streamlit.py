import streamlit as st
from ollama import chat
from ollama import ChatResponse
import asyncio

async def generate_response(prompt, model):
    try:
        loop = asyncio.get_running_loop()
        response: ChatResponse = await loop.run_in_executor(None, lambda: chat(model, messages=[
            {'role': 'user', 'content': prompt}
        ]))
        return response['message']['content']
    except Exception as e:
        st.error(f"An error occurred during response generation: {e}")
        return None

model_selected = st.selectbox('Select model', ['llama3.2:1b', 'gemma2:2b'])

async def main():
    st.title("Ollama LLM App")
    user_input = st.text_input("Enter your prompt:")

    if st.button("Generate"):
        if user_input:
            with st.spinner("Generating response..."):
                response = await generate_response(prompt=user_input, model=model_selected)
                if response:
                    st.write("Model Response:")
                    st.write(response)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    asyncio.run(main())