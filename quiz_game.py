import tkinter as tk
from tkinter import messagebox

class Quiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("600x400")
        self.configure(bg="#ADD8E6")
        
        
        self.instructions_label = tk.Label(self, text="Welcome to Quiz game!", font=("Arial", 16), bg="#ADD8E6")
        self.instructions_label.pack(pady=20)

        self.name_label = tk.Label(self, text="Enter your name:", font=("Arial", 12), bg="lightblue")
        self.name_label.pack()

        self.name_entry = tk.Entry(self, font=("Arial", 12))
        self.name_entry.pack()

        self.start_button = tk.Button(self, text="Start Game", font=("Arial", 14), command=self.start_game, bg="green", fg="white")
        self.start_button.pack(pady=10)

        self.questions = {
            "Who is the Prime Minister of India? ": ["modi", "narendra modi",'narendra'],
            "What is the capital of France? ": ["paris"],
            
        }

        self.current_question_index = 0
        self.correct_answers = 0

    def start_game(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return

        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()
        self.instructions_label.config(text=f"Welcome, {name}! Answer the following questions:")

        self.ask_question()

    def ask_question(self):
        question = list(self.questions.keys())[self.current_question_index]
        

        self.question_label = tk.Label(self, text=question, font=("Arial", 12), bg="lightblue")
        self.question_label.pack()

        self.answer_entry = tk.Entry(self, font=("Arial", 12))
        self.answer_entry.pack()

        self.submit_button = tk.Button(self, text="Submit Answer", font=("Arial", 12), command=self.check_answer)
        self.submit_button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answers = self.questions[list(self.questions.keys())[self.current_question_index]]
        print('values',correct_answers)
        if user_answer in correct_answers:
            self.correct_answers += 1
            messagebox.showinfo("Correct", "Good job! Your answer is correct.")
        else:
            messagebox.showinfo("Incorrect", "Sorry, your answer is incorrect. Game over.")
            self.end_game()
            return

        self.current_question_index += 1
        self.question_label.pack_forget()
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()

        if self.current_question_index < len(self.questions):
            self.ask_question()
        else:
            self.end_game()

    def end_game(self):
        messagebox.showinfo("Game Over", f"Thank you for playing! You answered {self.correct_answers} out of {len(self.questions)} questions correctly.")
        self.destroy()


hangman_game = Quiz()
hangman_game.mainloop()

