from flask import Flask, request, jsonify, render_template
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_milvus import Milvus
from dotenv import load_dotenv
import os

# Setup Flask
app = Flask(__name__)

# Load API Key
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

# LangChain setup with Gemini
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=google_api_key)
vectorstore = Milvus(embedding_function=embedding, collection_name="books_index")
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.9, google_api_key=google_api_key)

# Prompt
template = """You are a helpful assistant that recommends books based on user preferences.
User: {user_input}
Assistant:"""

prompt = PromptTemplate.from_template(template)
chain = LLMChain(prompt=prompt, llm=llm)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json.get('user_input')
    if not user_input:
        return jsonify({'error': 'Invalid input'}), 400

    response = chain.run(user_input)
    return jsonify({'recommendation': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
