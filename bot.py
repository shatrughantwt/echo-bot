import nltk
import logging
from datetime import datetime
from nltk.chat.util import Chat, reflections
from rich.console import Console
from rich.prompt import Prompt

nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

console = Console()

# --- Logging setup ---
logging.basicConfig(
    filename="conversations.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# --- Expanded patterns ---
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there! How may I assist you?"]],
    [r"my name is (.*)", ["Hello %1! How can I assist you today?"]],
    [r"(.*) your name?", ["I am EchoBot, your friendly rule-based chatbot!"]],
    [r"how are you?", ["I'm just a bot, but I'm doing well. How about you?"]],
    [r"what (can|do) you do", ["I match patterns in your text and reply — I'm rule-based, not AI-powered (yet)."]],
    [r"what time is it", [f"It's {datetime.now().strftime('%H:%M:%S')} right now."]],
    [r"what.s the date|today.s date", [f"Today is {datetime.now().strftime('%B %d, %Y')}."]],
    [r"tell me a joke", [
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why do programmers prefer dark mode? Because light attracts bugs."
    ]],
    [r"(.*) (help|assist) (.*)", ["Sure! How can I assist you with %3?"]],
    [r"thank(s| you)", ["You're welcome!", "Anytime!"]],
    [r"who (made|created) you", ["I was built by Boruto as a rule-based NLP chatbot project."]],
    [r"bye|exit|quit", ["Goodbye! Have a great day!", "See you later!"]],
    [r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase?", "Could you please elaborate?"]]
]

class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input):
        return self.chat.respond(user_input)

def chat_with_bot():
    console.print("[bold cyan]Hello, I am EchoBot! Type 'exit' to end the conversation.[/bold cyan]")
    bot = RuleBasedChatbot(pairs)

    while True:
        user_input = Prompt.ask("[bold green]You[/bold green]")
        logging.info(f"User: {user_input}")

        if user_input.lower() in ("exit", "quit", "bye"):
            console.print("[bold yellow]Chatbot: Goodbye![/bold yellow]")
            logging.info("Chatbot: Goodbye!")
            break

        response = bot.respond(user_input)
        console.print(f"[bold magenta]Chatbot:[/bold magenta] {response}")
        logging.info(f"Chatbot: {response}")

if __name__ == "__main__":
    chat_with_bot()