 # ==========================================================
# DecodeBot - Intelligent Rule-Based AI Assistant
# Developed by: Ayesha Zaib Warraich
# Course: Artificial Intelligence
# BS Artificial Intelligence – University of Agriculture Faisalabad
# ==========================================================

import datetime
import random

def show_help():
    print("\n📋 Available Commands")
    print("-" * 30)
    print("👋 hi / hello / hey")
    print("🤖 what is ai")
    print("🐍 what is python")
    print("📚 study tips")
    print("💪 motivate me")
    print("😂 tell me a joke")
    print("📅 date")
    print("⏰ time")
    print("📆 day")
    print("👨‍💻 who created you")
    print("❓ help")
    print("👋 bye")
def motivate():
    quotes = [
        "Success is built one small step at a time.",
        "Practice makes progress.",
        "Believe in yourself and keep learning.",
        "Every expert was once a beginner.",
        "Dream big. Start small. Stay consistent."
    ]

    print("\n💡", random.choice(quotes))
def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer visit the doctor? It caught a virus!",
        "Why was the keyboard tired? It worked all day!",
        "Why don't programmers like nature? Too many bugs!",
        "Why was the computer cold? It forgot to close Windows!"
    ]

    print("\n😂", random.choice(jokes))    
def show_title():
    print("\n" + "=" * 65)
    print("          🤖 DECODEBOT – AI ASSISTANT")
    print("=" * 65)
    print("     Intelligent Rule-Based Chatbot using Python")
    print("=" * 65)
def study_tips():
    print("\n📚 Study Tips")
    print("- Study for 45 minutes.")
    print("- Take a 10-minute break.")
    print("- Revise before sleeping.")
    print("- Practice coding every day.")
    print("- Solve problems instead of only reading.")
show_title()

print("\nWelcome to DecodeBot!")

now = datetime.datetime.now()

print(f"\n📅 Date : {now.strftime('%d %B %Y')}")
print(f"⏰ Time : {now.strftime('%I:%M %p')}")

name = input("\nEnter your name: ")

hour = datetime.datetime.now().hour

if hour < 12:
    greeting = "🌅 Good Morning"

elif hour < 17:
    greeting = "☀️ Good Afternoon"

else:
    greeting = "🌙 Good Evening"

print(f"\n{greeting}, {name}! 👋")
print("Type 'help' to see all commands.")

while True:

    user = input(f"\n{name}: ").lower().strip()
    if user in [
        "bye",
        "exit",
        "quit",
        "close"
    ]:
        print("\n🤖 DecodeBot: Goodbye! Have a wonderful day.")
        break  
    elif user in ["hi", "hello", "hey"]:
        print(f"\n🤖 Hello {name}! How can I help you today?")

    elif user == "help":
        show_help()
    elif user in [
        "what is ai",
        "define ai",
        "explain ai",
        "tell me about ai",
        "ai"
    ]:
        print("\n🤖 Artificial Intelligence (AI) enables computers to perform tasks that normally require human intelligence, such as learning, reasoning, problem-solving, and decision-making.")
    
    elif user in [
        "machine learning",
        "what is machine learning",
        "define machine learning",
        "ml"
    ]:
        print("\n🤖 Machine Learning is a branch of AI where computers learn from data and improve their performance without being explicitly programmed.")

    elif user in [
        "deep learning",
        "what is deep learning",
        "define deep learning",
        "dl"
    ]:
        print("\n🤖 Deep Learning is a type of Machine Learning that uses neural networks to solve complex tasks like image recognition and speech processing.")

    elif user in [
        "what is chatbot",
        "chatbot",
        "define chatbot"
    ]:
        print("\n🤖 A chatbot is a computer program that communicates with users through text or voice to answer questions and provide assistance.")
    
    elif user in [
        "what is generative ai",
        "generative ai",
        "gen ai"
    ]:
    
        print("\n🤖 Generative AI creates new content such as text, images, music, videos, and computer code based on user prompts.")

    elif user == "study tips":
        study_tips()
    elif user == "motivate me":
        motivate()
    elif user == "tell me a joke":
        tell_joke()    
    elif user in ["today", "date"]:
        print("\n📅", datetime.datetime.now().strftime("%d %B %Y")) 
    elif user == "time":
        print("\n⏰", datetime.datetime.now().strftime("%I:%M %p"))     
    elif user == "day":
        print("\n📆 Today is", datetime.datetime.now().strftime("%A"))  
    elif user in [
    "who created you",
    "creator",
    "who made you"
]:
       print("\n🤖 I was created by Ayesha Zaib Warraich as an Artificial Intelligence course project.")     
    else:
        print("\n🤖 Sorry, I don't understand that.")