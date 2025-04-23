# Pizza QA Assistant

## Overview

**Pizza QA Assistant** is a Streamlit-based web application designed to assist users in answering questions about a pizza restaurant. It uses a RAG Syetem with LLM to analyze and retrieve relevant reviews from a restaurant's review dataset to generate responses to user questions. The system is powered by Hugging Face’s model and the **Chroma** vector store for efficient document retrieval.

The core of the application is the ability to:
1. Take user queries about the pizza restaurant.
2. Retrieve relevant reviews from a dataset.
3. Pass the reviews to a language model (in our case DeepSeek) to generate answers.

This project serves as a practical demonstration of integrating **natural language processing (NLP)** with a review-based dataset for answering domain-specific questions.

---

## Features

- **Streamlit-based UI**: Simple interface where users can input their questions.
- **Review Retriever**: Uses **Chroma** vector store to efficiently retrieve relevant reviews from the database.
- **Hugging Face API**: Sends the question along with the retrieved reviews to a pre-trained language model to generate answers.
- **Environment variables**: Use of `.env` file for managing sensitive data like API keys.

---

## How to Run Locally

### Prerequisites

To run this project locally, you’ll need the following:

- Python 3.7+
- `pip` package manager

### Step-by-Step Instructions

1. **Clone the Repository**:

   First, clone the project repository to your local machine.

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Set Up Virtual Environment**:

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - **For Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

   - **For macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:

   Install the required packages by running:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure the `requirements.txt` file includes necessary libraries like `streamlit`, `huggingface_hub`, `langchain`, `pandas`, `python-dotenv`, and `chromadb`.

4. **Set Up `.env` File**:

   You need to create a `.env` file in the root directory and add the following content to store your sensitive keys:

   ```plaintext
   HF_API_KEY=your_huggingface_api_key
   HF_PROVIDER=sambanova
   ```

   Replace `your_huggingface_api_key` with your Hugging Face API key. You can obtain it from [Hugging Face's website](https://huggingface.co/).

5. **Run the Application**:

   After setting everything up, run the Streamlit app locally with:

   ```bash
   streamlit run main.py
   ```

   The application should now be accessible in your browser at `http://localhost:8501`.

---

## Technical Choices

### 1. **Streamlit**:

- **Streamlit** is used for building the user interface, allowing easy input and output interaction with users.
- It provides a simple way to deploy machine learning models as interactive web applications with minimal effort.

### 2. **Hugging Face API**:

- The app utilizes a pre-trained **Hugging Face model** to generate answers. The model used is from the Hugging Face platform and is designed to interpret user queries in the context of pizza restaurant reviews.

### 3. **Chroma (Vector Database)**:

- **Chroma** is used to store the reviews as **vectors** (numerical representations) that allow for fast retrieval of the most relevant reviews based on the user query.
- **LangChain** is used in combination with **OllamaEmbeddings** to embed the reviews and make them searchable.
  
  The reviews are pre-processed and stored as vectors for efficient search.

### 4. **Environment Variables**:

- **.env** file is used to securely store API keys and configuration values (like the Hugging Face API key and provider).

---

## Limitations

- **Deployment Platform**: The app is currently designed to be run locally or on platforms like **Streamlit Cloud**. However, the current setup may run into issues if the underlying system doesn’t support certain packages (like SQLite) that are required for the vector database (Chroma).
- **Dataset Size**: The app works with a specific dataset of pizza restaurant reviews. As the dataset grows, the performance of the app might be impacted due to the increased size of the vector database.
- **Dependence on Internet**: Since the app uses the Hugging Face API to generate answers, a stable internet connection is required to fetch the model responses.

---

## Conclusion

The **Pizza QA Assistant** is an interactive RAG web application that demonstrates how machine learning models can be used to provide answers to questions based on real-world data. The app leverages **Streamlit**, **Hugging Face**, and **Chroma** for efficient document retrieval, making it a powerful tool for answering domain-specific questions.

---

### You can now enjoy running the app locally or deploy it to any cloud platform! 
