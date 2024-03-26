import streamlit as st
import openai

def app():
    st.title("simple chat")

    user_message = st.text_input(label="どうしましたか？")

    if user_message:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        st.write(completion)

if __name__ == "__main__":
    app()
