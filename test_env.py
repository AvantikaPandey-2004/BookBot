from dotenv import load_dotenv, find_dotenv
import os

# Find and load the .env file
dotenv_path = find_dotenv()
print("Using .env file at:", dotenv_path)

load_dotenv(dotenv_path)

# Try reading the variable
google_api_key = os.getenv('GOOGLE_API_KEY')

if google_api_key:
    print("✅ GOOGLE_API_KEY loaded successfully!")
    print("GOOGLE_API_KEY =", google_api_key)
else:
    print("❌ GOOGLE_API_KEY not found.")
