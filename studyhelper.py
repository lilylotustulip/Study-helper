import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. Setup
load_dotenv()
client = InferenceClient(token=os.getenv("HFtoken"), model="meta-llama/Llama-3.1-8B-Instruct")

# 2. Session State Initialization
if 'mode' not in st.session_state:
    st.session_state.mode = None

# 3. UI - File Uploader
st.title("My Study Helper")


# File input
uploaded_file = st.file_uploader("Upload your notes", type=['txt', 'md'])
# Manual text input
manual_text = st.text_area("Or type your notes/question here:")

# Logic to combine inputs
if uploaded_file is not None:
    st.session_state.content = uploaded_file.read().decode("utf-8")
elif manual_text:
    st.session_state.content = manual_text
else:
    st.session_state.content = None

# 4. Mode Selection Buttons
col1, col2 = st.columns(2)
if col1.button("Learn"):
    st.session_state.mode = "learn"
if col2.button("Practice"):
    st.session_state.mode = "practice"

# 5. Logic based on mode
if st.session_state.mode == "learn":
    st.header("Learning Mode")
    learn_option = st.radio("What would you like to do?", ["Summarize", "Understand", "Mindmap"])

    if st.session_state.content: # Make sure we have notes first!
        if learn_option == "Summarize":
            if st.button("Generate Summary"):
                prompt = f"Summarize the following notes clearly: {st.session_state.content}"
                response = client.chat_completion(messages=[{"role": "user", "content": prompt}])
                st.write(response.choices[0].message.content)

        elif learn_option == "Understand":
            st.write("Ask me anything about your notes!")
            user_q = st.text_input("What do you want to understand further?")
            if user_q:
                prompt = f"Using these notes: {st.session_state.content}. Answer this question: {user_q}"
                response = client.chat_completion(messages=[{"role": "user", "content": prompt}])
                st.write(response.choices[0].message.content)

        elif learn_option == "Mindmap":
            if st.button("Create Mindmap"):
                # We ask for a Markdown outline, which serves as a text-based mindmap
                prompt = f"Create a hierarchical mindmap structure using Markdown bullet points for this text: {st.session_state.content}"
                response = client.chat_completion(messages=[{"role": "user", "content": prompt}])
                st.write(response.choices[0].message.content)
    else:
        st.warning("Please upload a file or type some notes first!")

elif st.session_state.mode == "practice":
    st.header("Practice Mode")
    
    if not st.session_state.content:
        st.warning("Please upload a file or type some notes first!")
    else:
        # Step 1: Choose the practice exercise type
        practice_option = st.radio(
            "Choose your practice exercise:", 
            ["Questions & Answers", "Multiple Choice", "Flashcards"]
        )
        
        # Step 2: Initialize session states
        if "quiz_question" not in st.session_state: st.session_state.quiz_question = None
        if "quiz_answer" not in st.session_state: st.session_state.quiz_answer = None
        if "quiz_hint" not in st.session_state: st.session_state.quiz_hint = None
        if st.button("Clear Practice Session"):
            # This wipes the questions so you start fresh
            st.session_state.quiz_question = None
            st.session_state.mcq_q = None
            st.session_state.fc_front = None
            st.session_state.fb_sentence = None
            st.rerun() # This tells Streamlit to refresh the page immediately

        # Step 3: Logic for Q&A
        if practice_option == "Questions & Answers":
            if st.button("Generate New Question"):
                prompt = f"Using these notes: {st.session_state.content}. Provide one study question, a short hint, and the answer. Format exactly as: \nQuestion: [Q]\nHint: [H]\nAnswer: [A]. No other text."
                response = client.chat_completion(messages=[{"role": "user", "content": prompt}])
                text = response.choices[0].message.content
                
                # Parsing
                try:
                    st.session_state.quiz_question = text.split("Question: ")[1].split("Hint:")[0].strip()
                    st.session_state.quiz_hint = text.split("Hint: ")[1].split("Answer:")[0].strip()
                    st.session_state.quiz_answer = text.split("Answer: ")[1].strip()
                except:
                    st.error("Model format error, please try generating again.")

            if st.session_state.quiz_question:
                st.write(f"**Question:** {st.session_state.quiz_question}")
                if st.button("Show Hint"):
                    st.info(f"Hint: {st.session_state.quiz_hint}")
                
                user_answer = st.text_input("Your Answer:")
                if st.button("Check Answer"):
                    if user_answer.lower() in st.session_state.quiz_answer.lower():
                        st.success("Correct!")
                    else:
                        st.error(f"Not quite. The answer was: {st.session_state.quiz_answer}")

        elif practice_option == "Multiple Choice":
            if st.button("Generate MCQ"):
                prompt = (f"Based on these notes: {st.session_state.content}, generate a multiple-choice question. "
                          "Format exactly as:\nQuestion: [Q]\nA) [Opt]\nB) [Opt]\nC) [Opt]\nD) [Opt]\nCorrect: [A/B/C/D]")
                response = client.chat_completion(messages=[{"role": "user", "content": prompt}])
                text = response.choices[0].message.content
                
                # Parsing
                try:
                    st.session_state.mcq_q = text.split("Question: ")[1].split("A)")[0].strip()
                    st.session_state.mcq_options = [
                        text.split("A)")[1].split("B)")[0].strip(),
                        text.split("B)")[1].split("C)")[0].strip(),
                        text.split("C)")[1].split("D)")[0].strip(),
                        text.split("D)")[1].split("Correct:")[0].strip()
                    ]
                    st.session_state.mcq_correct = text.split("Correct: ")[1].strip()[0] # Gets 'A', 'B', etc.
                except:
                    st.error("Format error. Please generate again.")

            # Display UI if question exists
            if "mcq_q" in st.session_state and st.session_state.mcq_q:
                st.write(f"**{st.session_state.mcq_q}**")
                
                # Create a selection list
                options = ["A", "B", "C", "D"]
                choice = st.radio("Select your answer:", options, format_func=lambda x: f"{x}: {st.session_state.mcq_options[options.index(x)]}")
                
                if st.button("Submit Answer"):
                    if choice == st.session_state.mcq_correct:
                        st.success("Correct!")
                    else:
                        st.error(f"Wrong. The correct answer was {st.session_state.mcq_correct}.")

        elif practice_option == "Flashcards":
            if st.button("Generate Flashcard"):
                prompt = (f"Based on these notes: {st.session_state.content}, create a study flashcard. "
                          "Format exactly as:\nFront: [Concept/Term]\nBack: [Detailed explanation]")
                response = client.chat_completion(messages=[{"role": "user", "content": prompt}])
                text = response.choices[0].message.content
                
                try:
                    st.session_state.fc_front = text.split("Front: ")[1].split("Back:")[0].strip()
                    st.session_state.fc_back = text.split("Back: ")[1].strip()
                    st.session_state.show_back = False # Hide answer by default
                except:
                    st.error("Could not generate card. Please try again.")

            if "fc_front" in st.session_state and st.session_state.fc_front:
                st.subheader("Front:")
                st.write(f"### {st.session_state.fc_front}")
                
                # Logic to reveal the back
                if st.button("Flip Card"):
                    st.session_state.show_back = True
                
                if st.session_state.get("show_back", False):
                    st.subheader("Back:")
                    st.info(st.session_state.fc_back)

        