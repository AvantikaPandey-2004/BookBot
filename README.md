# BookBot
An intelligent chatbot that recommends books based on user preferences using Google Gemini (LLM), LangChain, Milvus for vector search, and a Flask web interface. Users describe what they like to read, and the chatbot suggests personalized book recommendations using AI embeddings.
| Layer           | Technology                                                                 |
| --------------- | -------------------------------------------------------------------------- |
| 🤖 LLM          | [Google Gemini (gemini-pro)](https://ai.google.dev/gemini-api)             |
| 🔍 Embedding    | `GoogleGenerativeAIEmbeddings`                                             |
| 🧠 AI Framework | [LangChain](https://python.langchain.com/)                                 |
| 💬 Backend      | Flask                                                                      |
| 📦 Vector DB    | [Milvus](https://milvus.io/) via [Zilliz Cloud](https://cloud.zilliz.com/) |
| 🔐 Secrets      | `.env` + `python-dotenv`                                                   |
| 🌐 Frontend     | HTML + JavaScript (Flask + Jinja)                                          |
