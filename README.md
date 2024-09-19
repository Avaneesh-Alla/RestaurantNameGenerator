# Restaurant Name and Menu Generator Using LangChain

This project uses the LangChain framework and OpenAI's API to generate a fancy restaurant name and suggest menu items based on the specified cuisine. The project is built in Python and leverages the `LLMChain` and `SequentialChain` classes from LangChain to perform the tasks in sequence.

## Features
- Generates a creative and fancy restaurant name for a given cuisine.
- Suggests a list of menu items based on the generated restaurant name.

## Requirements
Before running the script, ensure you have the following installed:

- Python 3.8 or higher
- The following Python libraries:
  - `langchain-community`
  - `langchain`
  - `openai`
  - `streamlit`

You can install the necessary dependencies by running:
```bash
pip install streamlit
pip install langchain openai
```
## Cloning
- Clone this repository using:
```git clone https://github.com/Avaneesh-Alla/RestaurantNameGenerator.git```
## Setup

### 1. Get an OpenAI API Key:
- Go to [OpenAI](https://openai.com/signup/) and create an account.
- Retrieve your API key and store it in a `secret_key.py` file as follows:
  
```python
openaiapi_key = "your_openai_api_key_here"
```

### 2. Set the API key:
- The code automatically loads the API key from the environment variable OPENAI_API_KEY. Make sure your secret_key.py file is correctly set up.

### 3. File structure:
- Your file structure should look like this:
```css
├── main.py
├── secret_key.py
└── README.md
```

## How It Works
- The user provides a cuisine type (e.g., Italian, Chinese) through the Streamlit web application.
- The script generates a restaurant name and menu items using LangChain's LLMChain.
- The results are displayed on the Streamlit app interface.
- Run the Streamlit application with:
```bash
  streamlit run main.py
```

## Output
- The web interface will allow you to select a cuisine from a dropdown menu.
- After selection, the app will display a fancy restaurant name and a list of suggested menu items.
