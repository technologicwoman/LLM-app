import streamlit as st
import requests
from datetime import datetime
from pytz import timezone

from services import ChatOpenAI
from controllers import MessagesController


# Set up the OpenAI API key in an environment variable (OPENAI_API_KEY)
chat_open_ai = ChatOpenAI(api_key=st.secrets["OPENAI_API_KEY"], model_name="gpt-3.5-turbo")
messages_controller = MessagesController(interface=st)


def main():
    st.title("Chefcito - Your Personal Recipe Assistant")

    # Initialize chat history
    if "messages" not in st.session_state:
        messages_controller.init_messages()

    # Display chat messages
    messages_controller.display_messages()

    # React to user input
    if prompt:= st.chat_input("I am looking for a recipe with the following ingredients: ..."):
        messages_controller.manage_user_message(prompt)
        messages_controller.processing_ingredients(chat_open_ai)


if __name__ == "__main__":
    main()