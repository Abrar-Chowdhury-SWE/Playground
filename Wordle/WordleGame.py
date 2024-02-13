import random
import tkinter as tk
from tkinter import messagebox

# Predefined list of words
word_list = ["abrar"]

class WordleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Bangla Wordle")

        self.target_word = self.choose_random_word()
        self.attempts = 0
        self.max_attempts = 5
        self.guesses = []

        self.create_widgets()

    def choose_random_word(self):
        return random.choice(word_list)

    def check_guess(self, user_guess):
        correct_positions = sum(1 for a, b in zip(self.target_word, user_guess) if a == b)
        correct_letters = set(self.target_word) & set(user_guess)
        correct_positions_letters = set([user_guess[i] for i in range(len(user_guess)) if user_guess[i] == self.target_word[i]])
        correct_wrong_positions_letters = correct_letters - correct_positions_letters

        return correct_positions, correct_positions_letters, correct_wrong_positions_letters

    def check_button_click(self):
        user_guess = self.entry.get().lower()

        if self.attempts < self.max_attempts:
            correct_positions, correct_positions_letters, correct_wrong_positions_letters = self.check_guess(user_guess)
            self.guesses.append((user_guess, correct_positions_letters, correct_wrong_positions_letters))
            self.display_guesses()

            self.attempts += 1

            if correct_positions == 5:
                messagebox.showinfo("Yessir!", f"You guessed the word '{self.target_word}' correctly.")
                self.master.destroy()
            elif self.attempts == self.max_attempts:
                messagebox.showinfo("Game Over", f"Sorry, dumbo. The correct word was '{self.target_word}'.")
                self.master.destroy()

    def display_guesses(self):
     for i, (guess, correct_positions_letters, correct_wrong_positions_letters) in enumerate(self.guesses):
        for j, letter in enumerate(guess):
            if letter in correct_positions_letters:
                color = "green" if guess[j] == self.target_word[j] else "yellow"
            elif letter in correct_wrong_positions_letters:
                color = "yellow"
            else:
                color = "gray"
            self.labels[i][j].config(text=letter, bg=color)

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.master, text="Bangla Wordle", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=5, pady=10)

        # Labels for displaying guesses
        self.labels = [[tk.Label(self.master, text="", width=3, height=2, relief="ridge") for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                self.labels[i][j].grid(row=i + 1, column=j, padx=2, pady=2)

        # Entry for user input
        self.entry = tk.Entry(self.master)
        self.entry.grid(row=6, column=0, columnspan=5, pady=10)

        # Check Guess button
        check_button = tk.Button(self.master, text="Check Guess", command=self.check_button_click)
        check_button.grid(row=7, column=0, columnspan=5, pady=10)

# Create the Tkinter window
root = tk.Tk()
game = WordleGame(root)
root.mainloop()

# Run the Tkinter 