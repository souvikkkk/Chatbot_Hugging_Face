from model_loader import load_model

def main():
    qa_pipeline = load_model()
    print("🤖 QA Chatbot is ready! Type /exit to quit.\n")

    # Static context (you can also load from a file or wiki later)
    context = """
    Paris is the capital and most populous city of France.
    Rome is the capital city of Italy.
    Droupadi Murmu is the current president of India.
    Narendra Modi is the Prime Minister of India.
    """

    while True:
        question = input("User: ")
        if question.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        result = qa_pipeline(question=question, context=context)
        print(f"Bot: {result['answer']}")

if __name__ == "__main__":
    main()
