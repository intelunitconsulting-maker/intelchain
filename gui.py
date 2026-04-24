import customtkinter as ctk
import tkinter as tk
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

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(pady=(70, 20))

        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack()

        ctk.CTkLabel(title_frame, text="Intel",
                     font=("Arial", 38, "bold"),
                     text_color="white").pack(side="left")

        ctk.CTkLabel(title_frame, text="Chain",
                     font=("Arial", 38, "bold"),
                     text_color="#3b82f6").pack(side="left")

        ctk.CTkLabel(header,
                     text="OSINT Evidence Sealing",
                     font=("Arial", 14),
                     text_color="gray").pack()

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True)

        scroll = ctk.CTkScrollableFrame(
            container,
            corner_radius=12,
            fg_color="#0e1624"
        )
        scroll.pack(padx=40, pady=20, fill="both", expand=True)

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

        ctk.CTkLabel(scroll, text="URL (optional)", anchor="w").pack(
            padx=20, pady=(15, 5), fill="x"
        )

        self.url_entry = ctk.CTkEntry(scroll)
        self.url_entry.pack(padx=20, fill="x")

        self.run_btn = ctk.CTkButton(
            scroll,
            text="Generate Evidence",
            height=55,
            font=("Arial", 16, "bold"),
            fg_color="#2563eb",
            hover_color="#1e40af",
            command=self.run_chain
        )
        self.run_btn.pack(pady=30, padx=20, fill="x")

        self.status = ctk.CTkLabel(scroll, text="", text_color="green")
        self.status.pack()

        self.open_btn = ctk.CTkButton(
            scroll,
            text="Open Evidence",
            fg_color="#1f2937",
            hover_color="#374151",
            state="disabled",
            command=self.open_folder
        )
        self.open_btn.pack(pady=20)

    def select_file(self):
        top = ctk.CTkToplevel(self)
        top.title("Select File")
        top.geometry("600x400")

        current_path = "/"

        path_label = ctk.CTkLabel(top, text=current_path)
        path_label.pack(pady=5)

        frame = ctk.CTkFrame(top)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        listbox = tk.Listbox(
            frame,
            bg="#1a1a1a",
            fg="white",
            selectbackground="#2563eb",
            activestyle="none",
            font=("Arial", 11)
        )
        listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
        listbox.config(yscrollcommand=scrollbar.set)

        def refresh(path):
            nonlocal current_path
            current_path = path
            path_label.configure(text=path)
            listbox.delete(0, "end")

            try:
                files = os.listdir(path)

                dirs = [f for f in files if os.path.isdir(os.path.join(path, f))]
                files_only = [f for f in files if os.path.isfile(os.path.join(path, f))]

                for d in sorted(dirs):
                    listbox.insert("end", d)

                for f in sorted(files_only):
                    listbox.insert("end", f)

            except Exception as e:
                print(e)

        def open_selected():
            if not listbox.curselection():
                return

            selection = listbox.get(listbox.curselection())
            full_path = os.path.join(current_path, selection)

            if os.path.isdir(full_path):
                refresh(full_path)
            else:
                self.file_entry.delete(0, "end")
                self.file_entry.insert(0, full_path)
                top.destroy()

        def go_back():
            parent = os.path.dirname(current_path)
            refresh(parent)

        listbox.bind("<Double-Button-1>", lambda e: open_selected())

        btn_frame = ctk.CTkFrame(top, fg_color="transparent")
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="⬅ Back", command=go_back).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Open", command=open_selected).pack(side="left", padx=5)

        refresh(current_path)

    def run_chain(self):
        global last_output

        file = self.file_entry.get()
        url = self.url_entry.get() or None

        if not file or not os.path.exists(file):
            self.status.configure(text="Invalid file", text_color="red")
            return

        self.run_btn.configure(state="disabled")
        self.open_btn.configure(state="disabled", fg_color="#1f2937")

        self.status.configure(text="Processing evidence...", text_color="orange")
        self.update()

        try:
            last_output = run_intelchain(file, url)

            self.status.configure(
                text="✔ Evidence successfully generated",
                text_color="green"
            )

            self.open_btn.configure(
                state="normal",
                fg_color="#2563eb",
                hover_color="#1e40af"
            )

        except Exception as e:
            self.status.configure(text=str(e), text_color="red")
            print(e)

        finally:
            self.run_btn.configure(state="normal")

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
