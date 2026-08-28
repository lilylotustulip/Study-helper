# 📚 Study Helper

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B)](https://streamlit.io)

An AI-powered study companion that transforms your learning experience with intelligent summarization, interactive mind maps, and adaptive quizzes—powered by Meta's Llama 3.1.

## 🎯 What It Does

Study Helper makes learning smarter and faster by breaking down complex topics into digestible pieces and testing your understanding at every step.

### 📖 Learning Mode
Transform raw study material into structured knowledge:

- **📝 Summarize** — Get concise overviews of your uploaded texts or files to grasp topics quickly
- **🗺️ Mind Map** — Visualize key concepts and their relationships to see the big picture
- **❓ Understand** — Get auto-generated questions that deepen your understanding through active recall

### 🎓 Practice Mode
Test and reinforce what you've learned:

- **🎴 Flashcards** — Auto-generated flashcards for long-term memorization
- **📊 Multiple Choice** — Practice with MCQ exercises to identify knowledge gaps  
- **💬 Q&A** — Advanced free-response questions for deeper mastery

### 🌍 Multi-Language Support
Learn in your preferred language — Study Helper works across multiple languages.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | [Streamlit](https://streamlit.io) |
| **AI Engine** | Meta Llama 3.1 (via [Hugging Face Inference API](https://huggingface.co/inference-api)) |
| **Language** | Python 3.8+ |
| **Environment** | `python-dotenv` (secure API token management) |

---

## HOW TO WORK WITH IT
it is currently live here: [my study helper](https://study-apper-pwtavy3qh9d8xgecwen4mu.streamlit.app/)

## 📖 How to Use

### Step 1: Upload Your Study Material
- Paste text directly, or
- Upload a `.txt` file

### Step 2: Choose Your Mode

**Learning Mode:**
- Select a feature (Summarize, Mind Map, or Understand)
- Adjust settings if needed
- Get AI-generated insights instantly

**Practice Mode:**
- Select a practice type (Flashcards, MCQ, Q&A)
- Work through questions
- Track your progress

### Step 3: Learn & Retain
Study Helper generates content tailored to your material and learning style.

---

## 🌟 Features Highlight

| Feature | Benefit |
|---------|---------|
| **AI-Powered** | Uses state-of-the-art Llama 3.1 for accurate, context-aware content |
| **Multi-Mode Learning** | Combines active recall, visualization, and practice for better retention |
| **Language Agnostic** | Works in English, Spanish, French, German, and more |
| **No Ads** | Clean, distraction-free learning experience |
| **Open Source** | Free to use, modify, and extend |

---

## 📁 Project Structure

```
Study-helper/
├── studyhelper.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── main.py         
├── README.md             # This file
└── LICENSE               # MIT License
```

---

## 🧪 Example Workflow

1. Upload a textbook chapter on photosynthesis
2. Click **Summarize** → Get a 2-minute overview
3. Click **Mind Map** → See the key concepts visually connected
4. Click **Understand** → Answer generated questions about the topic
5. Switch to **Practice Mode** → Test yourself with flashcards and MCQs
6. Review weak areas with targeted Q&A

---

## 🔧 Configuration

### API Rate Limits
- Free Hugging Face tier: 3 requests/minute
- For higher limits, upgrade to a paid plan or use your own LLM

### Custom Prompts
You can modify the AI prompts by editing the prompt templates in `studyhelper.py` to customize the output style.

---

## 💡 Tips for Best Results

- **Keep inputs focused**: 500-2000 word excerpts work best
- **Read summaries first**: Get context before diving into mind maps
- **Use flashcards early**: Reinforce concepts while they're fresh
- **Practice regularly**: Spaced repetition improves retention
- **Combine modes**: Learning + Practice modes together maximize retention

---

## 🤝 Contributing

Contributions are welcome! Whether it's bug fixes, feature requests, or documentation improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## ⚠️ Limitations

- Requires internet connection (uses Hugging Face API)
- Dependent on API availability and rate limits
- Quality depends on input material clarity
- Large files may take longer to process

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io) — the fastest way to build data apps
- Powered by [Meta's Llama 3.1](https://www.llama.com/) via [Hugging Face](https://huggingface.co/)
- Inspired by spaced repetition and active recall learning techniques

---

## 💬 Feedback

Have questions or suggestions? Feel free to:
- Open an [Issue](https://github.com/lilylotustulip/Study-helper/issues)
- Start a [Discussion](https://github.com/lilylotustulip/Study-helper/discussions)
- Reach out on [GitHub](https://github.com/lilylotustulip)

---

**Happy studying!** 🚀📚
