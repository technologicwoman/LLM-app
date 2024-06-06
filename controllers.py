class MessagesController:
    def __init__(self, interface):
        self.interface = interface
        self.avartars = {
            "assistant": "https://raw.githubusercontent.com/technologicwoman/LLM-app/main/images/chefcito-avatar.png",
            "user": "👩‍🍳"
        }

    def init_messages(self):
        # Initialize chat history
        self.interface.session_state.messages = [
            {"role": "system", "content": "You are a helpful recipe assistant that helps users find recipes based on the ingredients they have in their fridge. \
            You can also suggest recipes that are low in carbon emissions. Please always provide a detailed recipe and ask for diary restrictions. Your name is Chefcito. If people ask you for your name, you should respond with 'Chefcito'. \
            If people ask you about your purpose, you should respond with 'I am a recipe assistant that helps you find recipes based on the ingredients you have in your fridge so that we can reduce \
            food waste together. I can also suggest recipes that are low in carbon emissions.' If people ask you about other subjects, please let them know that you are a recipe assistant."},
            {"role": "assistant", "content": "Hello! I am Chefcito, your personal recipe assistant. Let me know what ingredients you have in your fridge and I will suggest a recipe for you. \
            If you have any dietary restrictions, please let me know. Lets take care of the planet and your health together!"},
        ]

    def display_messages(self):
        # Display chat messages
        for message in self.interface.session_state.messages:
            if message['role'] != "system":
                role = message['role']
                with self.interface.chat_message(role, avatar=self.avartars[role]):
                    self.interface.markdown(message['content'])

    def manage_user_message(self, message):
        # Display user message in chat 
        with self.interface.chat_message("user", avatar=self.avartars["user"]):
            self.interface.markdown(message)
        self.interface.session_state.messages.append({"role": "user", "content": message})

    def processing_ingredients(self, chat_open_ai):
        # Process user input
        with self.interface.chat_message("assistant", avatar=self.avartars["assistant"]):
            stream = chat_open_ai.call(self.interface.session_state.messages)
            # Display the response from the OpenAI API
            response = self.interface.write_stream(stream)
        self.interface.session_state.messages.append({"role": "assistant", "content": response})
