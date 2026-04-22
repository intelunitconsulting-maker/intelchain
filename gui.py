import customtkinter as ctk
from tkinter import filedialog
import subprocess
import os

from intelchain import run_intelchain

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

last_output = None


class IntelChainApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("IntelChain")
        self.geometry("900x600")

        # 🔷 HEADER
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(pady=(70, 20))

        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack()

        ctk.CTkLabel(
            title_frame,
            text="Intel",
            font=("Arial", 38, "bold"),
            text_color="white"
        ).pack(side="left")

        ctk.CTkLabel(
            title_frame,
            text="Chain",
            font=("Arial", 38, "bold"),
            text_color="#3b82f6"
        ).pack(side="left")

        ctk.CTkLabel(
            header,
            text="OSINT Evidence Sealing",
            font=("Arial", 14),
            text_color="gray"
        ).pack()

        # 🧠 CONTAINER
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True)

        # 🔥 SCROLLABLE FRAME
        scroll = ctk.CTkScrollableFrame(
            container,
            corner_radius=12,
            fg_color="#0e1624"
        )
        scroll.pack(padx=40, pady=20, fill="both", expand=True)

        # FILE
        ctk.CTkLabel(scroll, text="Select File", anchor="w").pack(
            padx=20, pady=(20, 5), fill="x"
        )

        file_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        file_frame.pack(padx=20, fill="x")

        self.file_entry = ctk.CTkEntry(file_frame)
        self.file_entry.pack(side="left", expand=True, fill="x", padx=(0, 10))

        ctk.CTkButton(
            file_frame,
            text="Browse",
            width=100,
            command=self.select_file
        ).pack(side="right")

        # URL
        ctk.CTkLabel(scroll, text="URL (optional)", anchor="w").pack(
            padx=20, pady=(15, 5), fill="x"
        )

        self.url_entry = ctk.CTkEntry(scroll)
        self.url_entry.pack(padx=20, fill="x")

        # 🔥 BOUTON PRINCIPAL
        self.run_btn = ctk.CTkButton(
            scroll,
            text="Generate Evidence",
            height=55,
            font=("Arial", 16, "bold"),
            fg_color="#2563eb",  # plus moderne
            hover_color="#1e40af",
            command=self.run_chain
        )
        self.run_btn.pack(pady=30, padx=20, fill="x")

        # STATUS
        self.status = ctk.CTkLabel(scroll, text="", text_color="green")
        self.status.pack()

        # OPEN BUTTON
        self.open_btn = ctk.CTkButton(
            scroll,
            text="Open Evidence",
            fg_color="gray",
            state="disabled",
            command=self.open_folder
        )
        self.open_btn.pack(pady=20)

    # 📂 FILE SELECT
    def select_file(self):
        file = filedialog.askopenfilename(initialdir="/")

        if file:
            self.file_entry.delete(0, "end")
            self.file_entry.insert(0, file)

    # 🚀 RUN
    def run_chain(self):
        global last_output

        file = self.file_entry.get()
        url = self.url_entry.get() or None

        if not file or not os.path.exists(file):
            self.status.configure(text="Invalid file", text_color="red")
            return

        # 🔒 désactive boutons
        self.run_btn.configure(state="disabled")
        self.open_btn.configure(state="disabled")

        self.status.configure(text="Processing evidence...", text_color="orange")
        self.update()

        try:
            last_output = run_intelchain(file, url)

            self.status.configure(
                text="✔ Evidence successfully generated",
                text_color="green"
            )

            self.open_btn.configure(state="normal")

        except Exception as e:
            self.status.configure(text=str(e), text_color="red")
            print(e)

        finally:
            self.run_btn.configure(state="normal")

    # 📁 OPEN FOLDER
    def open_folder(self):
        global last_output

        if not last_output:
            return

        try:
            win_path = subprocess.check_output(
                ["wslpath", "-w", last_output]
            ).decode().strip()

            subprocess.run(["explorer.exe", win_path])

        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = IntelChainApp()
    app.mainloop()
