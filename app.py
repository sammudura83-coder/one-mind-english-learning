import gradio as gr

def conversation(topic, message):
    replies = {
        "Daily Life": "That's interesting! Can you tell me more about your daily routine?",
        "University": "University life can be challenging. What subject are you studying?",
        "Travel": "Travel is a great way to learn. Which place would you like to visit?",
        "Job Interview": "Good answer! Try to explain your experience and skills more clearly."
    }
    return replies.get(topic, "Great! Let's practice English together.")

def grammar_check(text):
    corrections = {
        "i am agree": "I agree",
        "she go": "She goes",
        "he go": "He goes",
        "i has": "I have",
        "he have": "He has",
        "she have": "She has",
        "i goed": "I went",
        "i didn't went": "I didn't go"
    }

    result = text
    for wrong, correct in corrections.items():
        result = result.replace(wrong, correct)
        result = result.replace(wrong.capitalize(), correct)

    if result == text:
        return "No predefined correction found. Your sentence may be correct!"
    return f"Corrected sentence: {result}"

def vocabulary(word):
    words = {
        "participate": "To take part in an activity.",
        "efficient": "Working well without wasting time or resources.",
        "confident": "Feeling sure about yourself or your abilities.",
        "improve": "To make something better.",
        "opportunity": "A chance to do something.",
        "communicate": "To share information or ideas with others."
    }
    return words.get(word.lower().strip(), "Word not found in our demo dictionary. Try: participate, efficient, confident, improve, opportunity, communicate.")

def practice_plan(skill):
    plans = {
        "Speaking": "Practice a 2-minute conversation about your daily life. Learn 5 useful expressions.",
        "Grammar": "Write 5 sentences using the present tense and check their grammar.",
        "Vocabulary": "Learn 5 new English words and use each one in a sentence.",
        "Listening": "Listen to a short English video and write down 5 expressions."
    }
    return plans.get(skill, "Practice English for 15 minutes today!")

with gr.Blocks(title="ONE MIND English Learning") as app:

    gr.Markdown("# 🌱 ONE MIND")
    gr.Markdown("### Personalized English Learning Support for Korean University Students")
    gr.Markdown("Practice English through conversation, grammar, vocabulary, and personalized learning.")

    with gr.Tab("💬 Conversation"):
        topic = gr.Dropdown(
            ["Daily Life", "University", "Travel", "Job Interview"],
            label="Choose a topic",
            value="Daily Life"
        )
        message = gr.Textbox(label="Your message", placeholder="Write something in English...")
        chat_button = gr.Button("Practice Conversation")
        chat_output = gr.Textbox(label="Demo Response")
        chat_button.click(conversation, inputs=[topic, message], outputs=chat_output)

    with gr.Tab("✏️ Grammar"):
        sentence = gr.Textbox(label="Enter your English sentence")
        grammar_button = gr.Button("Check Grammar")
        grammar_output = gr.Textbox(label="Result")
        grammar_button.click(grammar_check, inputs=sentence, outputs=grammar_output)

    with gr.Tab("📚 Vocabulary"):
        word = gr.Textbox(label="Enter an English word")
        vocab_button = gr.Button("Learn Word")
        vocab_output = gr.Textbox(label="Meaning")
        vocab_button.click(vocabulary, inputs=word, outputs=vocab_output)

    with gr.Tab("🎯 My Practice"):
        skill = gr.Dropdown(
            ["Speaking", "Grammar", "Vocabulary", "Listening"],
            label="Choose your learning skill",
            value="Speaking"
        )
        plan_button = gr.Button("Get Practice Suggestion")
        plan_output = gr.Textbox(label="Your Practice Plan")
        plan_button.click(practice_plan, inputs=skill, outputs=plan_output)

    gr.Markdown("---")
    gr.Markdown("**Student Project Prototype | Seoul Christian University**")
    gr.Markdown("This prototype uses predefined demo responses and is not yet connected to a real AI model.")

app.launch(server_name="0.0.0.0", port=int(__import__("os").environ.get("PORT", 7860)))
