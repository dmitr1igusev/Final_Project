#Dmitrii Gusev
#05/09/2024
#Final Project
import tkinter as tk
from tkinter import messagebox

from deck_cards_lib.flashcard_deck import Deck
from deck_cards_lib.flashcard_deck import FlashCard


class FlashCardApp(Deck):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.decks = []
        self.current_deck_index = -1

        self.main_menu()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.master, text="Flash Cards App", font=("Helvetica", 18)).pack()
        tk.Button(self.master, text="Create New Deck", command=self.create_new_deck).pack()
        tk.Button(self.master, text="Select Existing Deck", command=self.select_existing_deck).pack()
        tk.Button(self.master, text="Exit", command=self.master.destroy).pack()

    def create_new_deck(self):
        self.clear_window()
        tk.Label(self.master, text="Enter Deck Name:").pack()
        self.deck_name_entry = tk.Entry(self.master)
        self.deck_name_entry.pack()
        tk.Button(self.master, text="Create Deck", command=self.save_new_deck).pack()

    def save_new_deck(self):
        deck_name = self.deck_name_entry.get()
        if deck_name:
            self.decks.append(Deck(deck_name))
            self.current_deck_index = len(self.decks) - 1
            self.edit_deck()
        else:
            messagebox.showerror("Error", "Please enter a valid deck name.")

    def select_existing_deck(self):
        self.clear_window()
        tk.Label(self.master, text="Select Deck:").pack()
        self.deck_selection = tk.StringVar()
        self.deck_selection.set("Select Deck")
        for deck in self.decks:
            tk.Radiobutton(self.master, text=deck.name, variable=self.deck_selection, value=deck.name).pack()
        tk.Button(self.master, text="Select", command=self.load_selected_deck).pack()
        tk.Button(self.master, text="Back to Main Menu", command=self.main_menu).pack()

    def load_selected_deck(self):
        deck_name = self.deck_selection.get()
        if deck_name:
            for i, deck in enumerate(self.decks):
                if deck.name == deck_name:
                    self.current_deck_index = i
                    self.edit_deck()
                    return
        else:
            messagebox.showerror("Error", "Please select a deck.")

    def edit_deck(self):
        self.clear_window()
        tk.Label(self.master, text=f"Deck: {self.decks[self.current_deck_index].name}", font=("Helvetica", 16)).pack()
        tk.Button(self.master, text="Add Card", command=self.add_card).pack()
        tk.Button(self.master, text="Edit Card", command=self.edit_card).pack()
        tk.Button(self.master, text="Delete Card", command=self.delete_card).pack()
        tk.Button(self.master, text="View Cards", command=self.view_cards).pack()
        tk.Button(self.master, text="Study Mode", command=self.study_mode).pack()
        tk.Button(self.master, text="Close Deck", command=self.close_deck).pack()

    def add_card(self):
        self.clear_window()
        tk.Label(self.master, text="Enter Side 1:").pack()
        self.side1_entry = tk.Entry(self.master)
        self.side1_entry.pack()
        tk.Label(self.master, text="Enter Side 2:").pack()
        self.side2_entry = tk.Entry(self.master)
        self.side2_entry.pack()
        tk.Button(self.master, text="Add Card", command=self.save_card).pack()

    def save_card(self):
        side1 = self.side1_entry.get()
        side2 = self.side2_entry.get()
        if side1 and side2:
            self.decks[self.current_deck_index].add_card(FlashCard(side1, side2))
            self.edit_deck()
        else:
            messagebox.showerror("Error", "Please fill in both sides of the card.")

    def edit_card(self):
        self.clear_window()
        tk.Label(self.master, text="Select Card to Edit:").pack()
        self.card_selection = tk.StringVar()
        self.card_selection.set("Select Card")
        for i, card in enumerate(self.decks[self.current_deck_index].cards):
            tk.Radiobutton(self.master, text=f"{card.side1} - {card.side2}", variable=self.card_selection,
                           value=i).pack()
        tk.Button(self.master, text="Edit", command=self.modify_selected_card).pack()
        tk.Button(self.master, text="Back", command=self.edit_deck).pack()

    def modify_selected_card(self):
        index = int(self.card_selection.get())
        selected_card = self.decks[self.current_deck_index].cards[index]
        self.clear_window()
        tk.Label(self.master, text="Enter New Side 1:").pack()
        self.new_side1_entry = tk.Entry(self.master)
        self.new_side1_entry.insert(tk.END, selected_card.side1)
        self.new_side1_entry.pack()
        tk.Label(self.master, text="Enter New Side 2:").pack()
        self.new_side2_entry = tk.Entry(self.master)
        self.new_side2_entry.insert(tk.END, selected_card.side2)
        self.new_side2_entry.pack()
        tk.Button(self.master, text="Save Changes", command=lambda: self.save_modified_card(index)).pack()
        tk.Button(self.master, text="Back", command=self.edit_card).pack()

    def save_modified_card(self, index):
        new_side1 = self.new_side1_entry.get()
        new_side2 = self.new_side2_entry.get()
        if new_side1 and new_side2:
            self.decks[self.current_deck_index].modify_card(index, FlashCard(new_side1, new_side2))
            self.edit_deck()
        else:
            messagebox.showerror("Error", "Please fill in both sides of the card.")

    def delete_card(self):
        self.clear_window()
        tk.Label(self.master, text="Select Card to Delete:").pack()
        self.card_selection = tk.StringVar()
        self.card_selection.set("Select Card")
        for i, card in enumerate(self.decks[self.current_deck_index].cards):
            tk.Radiobutton(self.master, text=f"{card.side1} - {card.side2}", variable=self.card_selection,
                           value=i).pack()
        tk.Button(self.master, text="Delete", command=self.remove_selected_card).pack()
        tk.Button(self.master, text="Back", command=self.edit_deck).pack()

    def remove_selected_card(self):
        index = int(self.card_selection.get())
        self.decks[self.current_deck_index].remove_card(index)
        self.edit_deck()

    def view_cards(self):
        self.clear_window()
        tk.Label(self.master, text="Deck Cards:").pack()
        for card in self.decks[self.current_deck_index].cards:
            tk.Label(self.master, text=f"{card.side1} - {card.side2}").pack()
        tk.Button(self.master, text="Back to Deck", command=self.edit_deck).pack()

    def study_mode(self):
        self.start_review_mode()

    def close_deck(self):
        self.current_deck_index = -1
        self.main_menu()

    def start_review_mode(self):
        self.clear_window()
        self.current_card_index = 0
        self.review_cards()

    def review_cards(self):
        if self.current_card_index < len(self.decks[self.current_deck_index].cards):
            card = self.decks[self.current_deck_index].cards[self.current_card_index]
            self.clear_window()
            tk.Label(self.master,
                     text=f"Card {self.current_card_index + 1} of {len(self.decks[self.current_deck_index].cards)}",
                     font=("Helvetica", 14)).pack()
            tk.Label(self.master, text=card.side1, font=("Helvetica", 12)).pack()
            tk.Button(self.master, text="Show Answer", command=lambda: self.show_answer(card)).pack()
        else:
            tk.Button(self.master, text="Back to Deck", command=self.edit_deck).pack()

    def show_answer(self, card):
        self.clear_window()
        tk.Label(self.master,
                 text=f"Card {self.current_card_index + 1} of {len(self.decks[self.current_deck_index].cards)}",
                 font=("Helvetica", 14)).pack()
        tk.Label(self.master, text=card.side1, font=("Helvetica", 12)).pack()
        tk.Label(self.master, text=card.side2, font=("Helvetica", 12)).pack()
        tk.Button(self.master, text="Next Card", command=self.next_review_card).pack()

    def next_review_card(self):
        self.current_card_index += 1
        self.review_cards()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()


def main():
    try:
        root = tk.Tk()
        root.title("Flash Cards App")
        root.geometry("400x300")
        app = FlashCardApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    main()
