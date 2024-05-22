import os
import shutil
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# 1. Sisestad pildi
# 2. võibolla vaja image töötlust
# 2. programm loeb sisse pildi ning küsib, mida teha (kuidas jagada)
# 3. programm loeb pildi pealt tooted ning nende hinnad
# 4. vastavalt kasutaja soovile jaotab programm automaatselt ära, kes kui palju peab maksma
#
# pildi pealt character ja sõnade recognition - tesseract
#
# juturobot, küsib mida teha ning kui ei tea täpselt mida teha siis küsib üle
#
# Et pildilt arusaada, mis toodet kuhu jaotada, peab inimene ütlema tšeki pealt,
# kas toote järjekorranumbri või siis toote nimest vähemalt mingi osa.
#
# Kui juturobot ei leia täpselt, siis küsib üle, kuni saab õige

import tkinter as tk
from tkinter import ttk, filedialog, messagebox


import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Tkinter App")
        self.geometry("600x400")
        #self.resizable(False, False)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        self.create_first_page()
        self.create_second_page()
        self.create_third_page()
        self.create_fourth_page()

        # Force the notebook to display the first page
        self.after(0, lambda: self.notebook.select(0))

    def create_first_page(self):
        first_page = ttk.Frame(self.notebook)
        self.notebook.add(first_page, text="First Page")

        upload_button = ttk.Button(first_page, text="Lae pilt üles", command=self.upload_image)
        upload_button.pack(pady=10)

        search_button = ttk.Button(first_page, text="Otsi arvutist", command=self.search_computer)
        search_button.pack(pady=10)

        info_text = tk.Text(first_page, height=4, wrap='word')
        info_text.insert('1.0', "Poetšekilt summade jagamine inimeste vahel. Sisesta oma tšeki pilt ja leiame õiged võlgnikud üles!")
        info_text.config(state='disabled')
        info_text.pack(pady=10, padx=10, fill='x')

    def create_second_page(self):
        second_page = ttk.Frame(self.notebook)
        self.notebook.add(second_page, text="Second Page")

        self.canvas = tk.Canvas(second_page, width=400, height=300, bg='grey')
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.get_coordinates)

        rotate_button = ttk.Button(second_page, text="Pööra 90 kraadi", command=self.rotate_image)
        rotate_button.pack(pady=10)

        self.coordinates = []

    def create_third_page(self):
        third_page = ttk.Frame(self.notebook)
        self.notebook.add(third_page, text="Third Page")

        self.check_var1 = tk.IntVar()
        self.check_var2 = tk.IntVar()
        self.check_var3 = tk.IntVar()

        self.text_box1 = tk.Text(third_page, height=4, wrap='word')
        self.text_box1.insert('1.0', "Checkbox elements will appear here.")
        self.text_box1.config(state='disabled')
        self.text_box1.pack(pady=10, padx=10, fill='x')

        self.text_box2 = tk.Text(third_page, height=2, wrap='word')
        self.text_box2.pack(pady=10, padx=10, fill='x')

        input_label = tk.Label(third_page, text="Input:")
        input_label.pack(pady=5, padx=10, anchor='w')

        self.input_text = tk.Entry(third_page)
        self.input_text.pack(pady=5, padx=10, fill='x')

        submit_button = ttk.Button(third_page, text="Submit", command=self.submit_third_page)
        submit_button.pack(pady=10)

    def create_fourth_page(self):
        fourth_page = ttk.Frame(self.notebook)
        self.notebook.add(fourth_page, text="Fourth Page")

        self.info_text_box = tk.Text(fourth_page, height=10, wrap='word')
        self.info_text_box.insert('1.0', "Information will appear here.")
        self.info_text_box.config(state='disabled')
        self.info_text_box.pack(pady=10, padx=10, fill='x')

        button_frame = ttk.Frame(fourth_page)
        button_frame.pack(pady=10, padx=10, anchor='e')

        edit_button = ttk.Button(button_frame, text="Muuda", command=self.edit_info)
        edit_button.pack(side='left', padx=5)

        send_button = ttk.Button(button_frame, text="Saada tšekk", command=self.send_check)
        send_button.pack(side='left', padx=5)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Image Upload", f"Image uploaded: {file_path}")

    def search_computer(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Search Computer", f"File found: {file_path}")

    def get_coordinates(self, event):
        if len(self.coordinates) < 4:
            x, y = event.x, event.y
            self.coordinates.append((x, y))
            print(f"Coordinate: ({x}, {y})")

    def rotate_image(self):
        messagebox.showinfo("Rotate Image", "Image rotated 90 degrees!")

    def submit_third_page(self):
        checkboxes = [self.check_var1.get(), self.check_var2.get(), self.check_var3.get()]
        input_text = self.input_text.get()
        print(f"Checkboxes: {checkboxes}")
        print(f"Input: {input_text}")

    def edit_info(self):
        self.info_text_box.config(state='normal')

    def send_check(self):
        messagebox.showinfo("Send Check", "Check sent!")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
