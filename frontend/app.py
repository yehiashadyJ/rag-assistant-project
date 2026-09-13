import streamlit as st
import requests
import os


# App title
st.title("🤖 RAG Document Assistant")

# App description
st.write(
    "Ask questions about the provided technical documents."
)


# Get backend URL from environment variable
# The backend URL is NOT written here
api_url = os.getenv("API_BASE_URL")

# Check if the URL exists
if not api_url:
    st.error("API_BASE_URL is not set.")
    st.stop()


# Get user's question
question = st.chat_input("Ask a question...")


if question:

    # Show user's question
    with st.chat_message("user"):
        st.write(question)

    # Show AI answer
    with st.chat_message("assistant"):

        # Show loading message
        with st.spinner(
            "Searching documents and generating answer..."
        ):

            try:

                # Send question to the backend
                # api_url comes from the environment variable
                response = requests.post(
                    f"{api_url}/query",
                    json={"question": question}
                )

                # Check if backend was successful
                if response.status_code == 200:

                    # Get backend response
                    data = response.json()

                    # Show answer
                    st.write(data["answer"])

                    # Show sources
                    st.subheader("Sources")

                    for source in data["sources"]:
                        st.write("📄", source)

                else:
                    # Backend returned an error
                    st.error(
                        "The backend returned an error."
                    )

            except requests.exceptions.ConnectionError:

                # Backend is not running
                st.error(
                    "Could not connect to the backend. "
                    "Make sure FastAPI is running."
                )
