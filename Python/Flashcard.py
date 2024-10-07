class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardDeck:
    def __init__(self):
        self.cards = []

    def add_card(self, question, answer):
        self.cards.append(Flashcard(question, answer))

    def study(self):
        if not self.cards:
            print("No cards in the deck!")
            return

        for card in self.cards:
            print("\nQuestion:", card.question)
            input("Press Enter to see the answer...")
            print("Answer:", card.answer)
            input("Press Enter for the next card...")

# Example usage
deck = FlashcardDeck()

# Adding some sample flashcards
deck.add_card("What is the capital of France?", "Paris")
deck.add_card("What is 2 + 2?", "4")
deck.add_card("Who wrote 'Romeo and Juliet'?", "William Shakespeare")

# Start studying
deck.study()
