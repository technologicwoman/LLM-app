# Chefcito - Your Personal Recipe Assistant

Chefcito is a recipe assistant that uses OpenAI's GPT-3.5-turbo model as its foundational model and Streamlit for the front-end interface. It helps users find recipes based on their input.

## Project Description

Chefcito is built around the concept of Clean Architecture, ensuring that the design is modular, flexible, and testable. It separates concerns into different layers:

- **Entity Layer:** Contains the business rules and models.
- **Use Case Layer:** Contains specific business scenarios.
- **Interface Adapters Layer:** Converts data from a format usable for the use cases and entities to a format usable for things like the web, database, UI, etc.
- **Frameworks and Drivers Layer:** Contains all the high-level details like UI, database, web, etc.

The application uses the OpenAI API to generate responses to user queries, and Streamlit to create an interactive web-based user interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of Python.
- You have a Linux machine. This code may work with other operating systems, but it was tested and developed in Linux.
- You have set up the OpenAI API key in an environment variable (OPENAI_API_KEY).

## Using Chefcito

To use Chefcito, follow these steps:

1. Clone the repository
2. Install the required packages using pip:
    ```
    pip install -r requirements.txt
    ```
3. Run the application:
    ```
    streamlit run Chefcito_app.py
    ```

## Live Application

You can access the live application at [https://chefcito.streamlit.app/](https://chefcito.streamlit.app/)

## Contact

If you want to contact me you can reach me at `lacardenas.code@gmail.com`.
