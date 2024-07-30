## Gemini Chatbot with Python Tutorial  

This repository contains the code for a chatbot built using the Gemini API and Python. It's accompanied by a YouTube video tutorial that guides you through the creation process.

### YouTube Tutorial

Watch the full tutorial on YouTube:

[![Watch the video](https://img.youtube.com/vi/CaxPa1FuHx4/0.jpg)](https://www.youtube.com/watch?v=CaxPa1FuHx4)


### Dependencies

This project requires the following Python libraries:

* `google-generativeai`
* `python-dotenv`

You can install them using pip:

```bash
pip install google-generativeai python-dotenv
```

### Usage

1. Set up your GEMINI_API_KEY:

Create a file named .env in the root directory of this project.
Add the following line to the .env file, replacing YOUR_API_KEY with your actual Gemini API key:

```bash
GEMINI_API_KEY=YOUR_API_KEY
```

2.  Run the Script:

```bash
python chat.py
```

This will start the chatbot. You can then interact with it by typing your questions or prompts.

Note: You'll need to replace chatbot.py with the actual filename of your Python script if it's named differently.

### Code Structure

 - The code consists of a single Python script (chatbot.py) that performs the following:
 - Imports necessary libraries and loads the API key from the .env file.
 - Configures the GenerativeModel with safety settings, generation configurations, and system instructions.
 - Creates a chat history list.
 - Starts a loop that continuously prompts the user for input and sends it to the model.
 - Receives the model's response and prints it to the console.
 - Updates the chat history with both user input and model responses.

### License
The MIT License is used for this project. You can find the full license text here: https://opensource.org/license/mit.



