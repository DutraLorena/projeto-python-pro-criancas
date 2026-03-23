import random
import tkinter as tk
from tkinter import messagebox


class KidsPythonProApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Aventura dos Números")
        self.root.geometry("760x520")
        self.root.configure(bg="#f7fbff")
        self.root.resizable(False, False)

        self.score = 0
        self.rounds = 0
        self.max_rounds = 10
        self.current_answer = 0
        self.current_mode = "sum"

        self.title_label = tk.Label(
            root,
            text="Aventura dos Números",
            font=("Arial", 24, "bold"),
            bg="#f7fbff",
            fg="#2457d6",
        )
        self.title_label.pack(pady=(20, 10))

        self.subtitle = tk.Label(
            root,
            text="Um jogo educativo em Python para crianças praticarem matemática!",
            font=("Arial", 12),
            bg="#f7fbff",
            fg="#334155",
        )
        self.subtitle.pack()

        self.top_frame = tk.Frame(root, bg="#f7fbff")
        self.top_frame.pack(pady=18)

        self.score_label = tk.Label(
            self.top_frame,
            text="Pontuação: 0",
            font=("Arial", 14, "bold"),
            bg="#dbeafe",
            fg="#1e3a8a",
            padx=14,
            pady=8,
        )
        self.score_label.grid(row=0, column=0, padx=10)

        self.round_label = tk.Label(
            self.top_frame,
            text=f"Rodada: 0/{self.max_rounds}",
            font=("Arial", 14, "bold"),
            bg="#dcfce7",
            fg="#166534",
            padx=14,
            pady=8,
        )
        self.round_label.grid(row=0, column=1, padx=10)

        self.mode_frame = tk.Frame(root, bg="#f7fbff")
        self.mode_frame.pack(pady=(0, 10))

        tk.Label(
            self.mode_frame,
            text="Escolha o desafio:",
            font=("Arial", 12, "bold"),
            bg="#f7fbff",
            fg="#0f172a",
        ).grid(row=0, column=0, padx=8)

        self.sum_button = tk.Button(
            self.mode_frame,
            text="Soma",
            command=lambda: self.set_mode("sum"),
            width=12,
            bg="#60a5fa",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
        )
        self.sum_button.grid(row=0, column=1, padx=5)

        self.sub_button = tk.Button(
            self.mode_frame,
            text="Subtração",
            command=lambda: self.set_mode("sub"),
            width=12,
            bg="#cbd5e1",
            fg="#0f172a",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
        )
        self.sub_button.grid(row=0, column=2, padx=5)

        self.question_card = tk.Frame(root, bg="white", bd=0, highlightthickness=2, highlightbackground="#bfdbfe")
        self.question_card.pack(padx=40, pady=10, fill="x")

        self.question_label = tk.Label(
            self.question_card,
            text="Clique em 'Nova pergunta' para começar!",
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#1e293b",
            pady=25,
        )
        self.question_label.pack()

        self.entry = tk.Entry(root, font=("Arial", 18), justify="center", width=12)
        self.entry.pack(pady=12)
        self.entry.bind("<Return>", lambda event: self.check_answer())

        self.feedback_label = tk.Label(
            root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f7fbff",
            fg="#0f172a",
        )
        self.feedback_label.pack(pady=5)

        self.button_frame = tk.Frame(root, bg="#f7fbff")
        self.button_frame.pack(pady=18)

        self.new_button = tk.Button(
            self.button_frame,
            text="Nova pergunta",
            command=self.new_question,
            width=16,
            bg="#22c55e",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
        )
        self.new_button.grid(row=0, column=0, padx=8)

        self.check_button = tk.Button(
            self.button_frame,
            text="Responder",
            command=self.check_answer,
            width=16,
            bg="#f59e0b",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
        )
        self.check_button.grid(row=0, column=1, padx=8)

        self.reset_button = tk.Button(
            self.button_frame,
            text="Reiniciar jogo",
            command=self.reset_game,
            width=16,
            bg="#ef4444",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
        )
        self.reset_button.grid(row=0, column=2, padx=8)

        self.tip_label = tk.Label(
            root,
            text="Dica: aperte Enter para responder mais rápido.",
            font=("Arial", 11),
            bg="#f7fbff",
            fg="#475569",
        )
        self.tip_label.pack(side="bottom", pady=20)

    def set_mode(self, mode: str):
        self.current_mode = mode
        if mode == "sum":
            self.sum_button.configure(bg="#60a5fa", fg="white")
            self.sub_button.configure(bg="#cbd5e1", fg="#0f172a")
            self.feedback_label.config(text="Modo soma ativado!")
        else:
            self.sub_button.configure(bg="#60a5fa", fg="white")
            self.sum_button.configure(bg="#cbd5e1", fg="#0f172a")
            self.feedback_label.config(text="Modo subtração ativado!")
        self.new_question()

    def new_question(self):
        if self.rounds >= self.max_rounds:
            self.finish_game()
            return

        if self.current_mode == "sum":
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            self.current_answer = a + b
            self.question_label.config(text=f"Quanto é {a} + {b}?")
        else:
            a = random.randint(5, 20)
            b = random.randint(1, a)
            self.current_answer = a - b
            self.question_label.config(text=f"Quanto é {a} - {b}?")

        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.entry.focus_set()

    def check_answer(self):
        if self.rounds >= self.max_rounds:
            self.finish_game()
            return

        typed = self.entry.get().strip()
        if typed == "":
            self.feedback_label.config(text="Digite uma resposta primeiro.", fg="#b45309")
            return

        if not typed.lstrip("-").isdigit():
            self.feedback_label.config(text="Use apenas números.", fg="#b91c1c")
            return

        answer = int(typed)
        self.rounds += 1

        if answer == self.current_answer:
            self.score += 10
            self.feedback_label.config(text="Muito bem! Você acertou! 🎉", fg="#15803d")
        else:
            self.feedback_label.config(
                text=f"Quase! A resposta certa era {self.current_answer}.",
                fg="#b91c1c",
            )

        self.score_label.config(text=f"Pontuação: {self.score}")
        self.round_label.config(text=f"Rodada: {self.rounds}/{self.max_rounds}")

        if self.rounds >= self.max_rounds:
            self.root.after(900, self.finish_game)
        else:
            self.root.after(900, self.new_question)

    def finish_game(self):
        if self.score >= 80:
            medal = "🏆 Excelente!"
        elif self.score >= 50:
            medal = "⭐ Muito bom!"
        else:
            medal = "👍 Continue praticando!"

        messagebox.showinfo(
            "Fim de jogo",
            f"Você terminou o desafio!\n\nPontuação final: {self.score}\n{medal}",
        )

    def reset_game(self):
        self.score = 0
        self.rounds = 0
        self.score_label.config(text="Pontuação: 0")
        self.round_label.config(text=f"Rodada: 0/{self.max_rounds}")
        self.feedback_label.config(text="Jogo reiniciado! Vamos brincar de novo.", fg="#1d4ed8")
        self.question_label.config(text="Clique em 'Nova pergunta' para começar!")
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = KidsPythonProApp(root)
    root.mainloop()
