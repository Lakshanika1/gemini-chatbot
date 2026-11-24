# 🤖 Gemini AI Chatbot

## 📌 Project Overview

Gemini AI Chatbot is a Python-based conversational application powered by Google's Gemini 2.5 Flash model.

The chatbot uses the Google Gen AI SDK to interact with the Gemini API and generate intelligent, context-aware responses to user queries.

It provides an interactive command-line interface (CLI), maintains conversation history, and allows users to have continuous conversations with the AI model.

## ✨ Features

- **AI-Powered Responses:** Generates responses using Google's Gemini 2.5 Flash model.
- **Interactive Conversations:** Accepts user queries through a command-line interface.
- **Conversation History:** Maintains previous messages to provide contextual responses.
- **Context Management:** Sends the latest six conversation messages to the AI model.
- **Secure API Key Handling:** Uses environment variables to manage API credentials.
- **Simple Exit Option:** Allows users to terminate the chatbot by typing `exit`.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **AI Model:** Google Gemini 2.5 Flash
- **API Integration:** Google Gen AI SDK
- **Libraries:** `google-genai`, `os`

## 📂 Project Structure

```text
gemini-chatbot/
│
├── chatbot.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Lakshanika1/gemini-chatbot.git
```

### Step 2: Navigate to the Project Directory

```bash
cd gemini-chatbot
```

### Step 3: Install Required Dependency

```bash
pip install google-genai
```

### Step 4: Configure Google Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/).
2. Generate your Gemini API key.
3. Configure the API key as an environment variable.

**Windows PowerShell:**

```powershell
$env:GOOGLE_API_KEY="your_api_key"
```

**Linux / macOS:**

```bash
export GOOGLE_API_KEY="your_api_key"
```

**Important:** Never share your API key or upload it to a public GitHub repository.

### Step 5: Run the Chatbot

```bash
python chatbot.py
```

## 💻 Sample Output

```text
🤖 Gemini Chatbot is running...
Type 'exit' to stop.

You: Hello!
Chatbot: Hello! How can I help you today?

You: Explain Artificial Intelligence.
Chatbot: Artificial Intelligence (AI) is a field of
computer science that focuses on creating machines
capable of performing tasks that typically require
human intelligence.

You: exit
Chatbot: Goodbye 👋
```

*Note: The responses shown above are illustrative. Actual responses are generated dynamically by the Gemini API.*

## 🔄 Working Process

1. **Initialize the Client:** Establishes a connection with the Google Gemini API using the API key.
2. **Receive User Input:** Accepts messages from the user through the terminal.
3. **Store Conversation:** Adds user messages to the chat history.
4. **Manage Context:** Selects the latest six conversation entries.
5. **Generate Response:** Sends the conversation to the Gemini 2.5 Flash model.
6. **Display Response:** Prints the generated response in the terminal.
7. **Continue or Exit:** Repeats the process until the user enters `exit`.

## 🎯 Learning Outcomes

- Gained practical experience integrating Generative AI APIs with Python.
- Understood the fundamentals of Large Language Models (LLMs).
- Learned how to manage conversational context using chat history.
- Practiced working with environment variables for API key security.
- Developed an interactive AI-powered command-line application.

## 🚀 Future Enhancements

- Develop a user-friendly web interface using Flask or Streamlit.
- Implement persistent conversation storage.
- Add conversation export functionality.
- Improve exception handling and API error management.
- Explore additional Gemini models and capabilities.

## 📝 Conclusion

The Gemini AI Chatbot project demonstrates how Generative AI can be integrated into Python applications using Google's Gemini API.

Through this project, I gained hands-on experience with API integration, Large Language Models (LLMs), conversation history management, and environment variable configuration.

This project strengthened my understanding of building AI-powered conversational applications and provided a foundation for exploring more advanced Generative AI and chatbot development.

## 👩‍💻 Author

**Lakshanika A P**

B.E. Computer Science and Engineering

GitHub: [Lakshanika1](https://github.com/Lakshanika1)

---

⭐ If you find this project useful, consider giving this repository a star!
