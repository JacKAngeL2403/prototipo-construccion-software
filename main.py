import tkinter as tk
import winsound
import threading
import time

class YouAreAnIdiotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Universitario - Asignación de Notas")
        self.root.geometry("480x320")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)

        # Pantalla inicial "trampa"
        self.lbl = tk.Label(
            root,
            text="SISTEMA DE ASIGNACIÓN AUTOMÁTICA",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.lbl.pack(pady=40)

        self.btn = tk.Button(
            root,
            text="OBTENER NOTA 20 AQUÍ SOBRINO :)",
            font=("Arial", 11, "bold"),
            bg="#008CBA",
            fg="white",
            padx=15,
            pady=10,
            cursor="hand2",
            command=self.lanzar_meme
        )
        self.btn.pack(pady=10)

    def sonar_melodia(self):
        # Ritmo de la melodía "You are an idiot! Ha ha ha ha ha ha ha!"
        melodia = [
            (659, 200), (659, 200), (659, 200), (523, 200), (659, 200), (784, 400), (392, 400),
            (523, 150), (587, 150), (659, 150), (698, 150), (784, 150), (880, 300)
        ]
        for _ in range(4):  # Repite la secuencia
            for freq, dur in melodia:
                try:
                    winsound.Beep(freq, dur)
                except:
                    pass

    def parpadear_blanco_negro(self, popup, lbl_top, lbl_main, lbl_bot):
        # Efecto estroboscópico clásico (Blanco / Negro)
        for i in range(40):
            if not popup.winfo_exists():
                break
            if i % 2 == 0:
                bg_color, fg_color = "black", "white"
            else:
                bg_color, fg_color = "white", "black"

            popup.configure(bg=bg_color)
            lbl_top.configure(bg=bg_color, fg=fg_color)
            lbl_main.configure(bg=bg_color, fg=fg_color)
            lbl_bot.configure(bg=bg_color, fg=fg_color)
            time.sleep(0.12)

    def lanzar_meme(self):
        # Iniciar melodía en segundo plano
        threading.Thread(target=self.sonar_melodia, daemon=True).start()

        # Ventana estilo estético idéntico a la referencia
        popup = tk.Toplevel(self.root)
        popup.title("you are an idiot!")
        popup.geometry("450x300")
        popup.resizable(False, False)

        lbl_top = tk.Label(popup, text="☺  ☺  ☺", font=("Arial", 28), bg="black", fg="white")
        lbl_top.pack(pady=10)

        lbl_main = tk.Label(popup, text="you are an idI0t!", font=("Times New Roman", 26, "bold"), bg="black", fg="white")
        lbl_main.pack(expand=True)

        lbl_bot = tk.Label(popup, text="☺  ☺  ☺", font=("Arial", 28), bg="black", fg="white")
        lbl_bot.pack(pady=10)

        # Iniciar el parpadeo
        threading.Thread(target=self.parpadear_blanco_negro, args=(popup, lbl_top, lbl_main, lbl_bot), daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouAreAnIdiotApp(root)
    root.mainloop()