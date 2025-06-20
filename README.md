# 🤖 Local Command-Line Chatbot using Hugging Face

# 📌 Project Overview
Developed a fully functional local chatbot interface using a Hugging Face text generation model.
This task focuses on integrating language models into a CLI environment, managing conversational
context, and delivering a smooth developer experience via modular, maintainable
Python code.

# 🎯 Objectives
Designed and implemented a command-line chatbot in Python using any small Hugging Facesupported
text generation model. The chatbot should maintain a short-term memory of
previous exchanges using a sliding window mechanism to ensure coherent multi-turn conversation.

# 📂 Project Structure
huggingface_chatbot/
├── model_loader.py        # Loads the QA model   
├── chat_memory.py         # Simple memory class to track dialogue  
├── interface.py           # CLI for chatbot interaction   
└── README.md              # Project documentation    

# ⚙️ Setup Instructions    
  # 1. Clone the Repository    
  git clone https://github.com/yourusername/huggingface_chatbot.git    
  cd huggingface_chatbot     
  # 2. Install Dependencies    
  pip install transformers    

# ▶️ How to Run  
 python interface.py

# 🧪 Sample Interaction
🤖 QA Chatbot is ready! Type /exit to quit.     
   
User: Who is the Prime Minister of India?    
Bot: Narendra Modi    

User: What is the capital of France?    
Bot: Paris   

User: Who is the president of India?   
Bot: Droupadi Murmu   

User: /exit   
Exiting chatbot. Goodbye!    





 
