import streamlit as st
from pydantic import BaseModel, Field
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_tagging_chain_pydantic

class Attribute(BaseModel):
    language: str = Field(enum=["ja", "em"])
    tags: list[str] = Field(examples=[["Python", "Streamlit"]])

def app():
    st.title("タグ付け")

    text = st.text_area("タグ付けするテキスト")

    if text:
        with st.spinner("タグ付け中．．．"):
            llm = ChatOpenAI(model="gpt-4")
            chain = create_tagging_chain_pydantic(Attribute, llm)
            attr = chain.run(text)
            st.write(attr.dict())

if __name__ == "__main__":
    app()