import tkinter as tk
import winsound
import threading
import time
import os

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
            text="OBTENER NOTA 20 AQUÍ",
            font=("Arial", 11, "bold"),
            bg="#008CBA",
            fg="white",
            padx=15,
            pady=10,
            cursor="hand2",
            command=self.lanzar_meme
        )
        self.btn.pack(pady=10)

    def sonar_musica(self):
        archivo_wav = "sonido.wav"
        # Si existe el archivo de audio real, lo reproduce en bucle
        if os.path.exists(archivo_wav):
            try:
                winsound.PlaySound(
                    archivo_wav,
                    winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
                )
            except Exception:
                self.sonar_beeps_fallback()
        else:
            # Si no está el archivo .wav, reproduce los pitidos retro
            self.sonar_beeps_fallback()

    def sonar_beeps_fallback(self):
        melodia = [
            (659, 200), (659, 200), (659, 200), (523, 200), (659, 200), (784, 400), (392, 400),
            (523, 150), (587, 150), (659, 150), (698, 150), (784, 150), (880, 300)
        ]
        for _ in range(4):
            for freq, dur in melodia:
                try:
                    winsound.Beep(freq, dur)
                except Exception:
                    pass

    def parpadear_blanco_negro(self, popup, lbl_top, lbl_main, lbl_bot):
        # Efecto estroboscópico clásico (Blanco / Negro)
        for i in range(40):
            if not popup.winfo_exists():
                # Al cerrar la ventana, detiene la música
                try:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                except Exception:
                    pass
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
        # Iniciar reproducción de audio en segundo plano
        threading.Thread(target=self.sonar_musica, daemon=True).start()

        # Ventana estilo meme
        popup = tk.Toplevel(self.root)
        popup.title("you are an idiot!")
        popup.geometry("450x300")
        popup.resizable(False, False)

        lbl_top = tk.Label(popup, text="☺  ☺  ☺", font=("Arial", 28), bg="black", fg="white")
        lbl_top.pack(pady=10)

        lbl_main = tk.Label(popup, text="te la creiste :b!", font=("Times New Roman", 26, "bold"), bg="black", fg="white")
        lbl_main.pack(expand=True)

        lbl_bot = tk.Label(popup, text="☺  ☺  ☺", font=("Arial", 28), bg="black", fg="white")
        lbl_bot.pack(pady=10)

        # Iniciar parpadeo de colores
        threading.Thread(
            target=self.parpadear_blanco_negro,
            args=(popup, lbl_top, lbl_main, lbl_bot),
            daemon=True
        ).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouAreAnIdiotApp(root)
    root.mainloop()