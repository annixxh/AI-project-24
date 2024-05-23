import pilditootlus
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, filedialog, messagebox


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


###########################################################
# GUI käivitamine
###########################################################
def __init__(self, root):
    self.root = root
    self.root.title("Application")

    self.frame = tk.Frame(self.root, width=600, height=600)
    self.frame.pack()

    self.show_first_page()

    # Bind the Enter key to the get_user_input function
    self.root.bind('<Return>', self.get_user_input)


###########################################################
# ESIMENE LEHT, kas laadida pilt üles või otsida nime järgi
# liigub edasi, vaid kui on saadud Image tüüpi pilt vastuseks kummaltki nupult
###########################################################
def show_first_page(root):
    frame = tk.Frame(root, width=600, height=600)
    frame.pack()

    label_title = tk.Label(frame, text="Tšeki summade arvutamise AI", font=("Helvetica", 16))
    label_title.place(x=150, y=100)

    label_instruction = tk.Label(frame,
                                 text="Kas tahad üles laadida tšeki pilti või valida juba üles laetud faili nime?")
    label_instruction.place(x=100, y=200)

    # lae üles nupp käivitab meetodi lae_ules_pilt, mis on pilditootlus failis
    # meetod check_and_prooceed kontrollib, kas vastuseks saadi Image, kui jah siis liigub teisele lehele
    button_upload = tk.Button(frame, text="Lae üles",
                              command=lambda: check_and_proceed(pilditootlus.lae_ules_pilt, frame))
    button_upload.place(x=200, y=300)

    # vali fail nupp käivitab meetodi kusi_pildi_nime, mis tekitab uued elemendid ja küsib kasutajalt failinime
    # meetod check_and_prooceed kontrollib, kas vastuseks saadi Image, kui jah siis liigub teisele lehele
    button_choose = tk.Button(frame, text="Vali fail",
                              command=lambda: check_and_proceed(lambda: kusi_pildi_nime(frame), frame))
    button_choose.place(x=350, y=300)


###########################################################
# TEINE LEHT, kas laadida pilt üles või otsida nime järgi
# liigub edasi, vaid kui on saadud Image tüüpi pilt vastuseks kummaltki nupult
###########################################################
def show_second_page(frame, image):
    for widget in frame.winfo_children():
        widget.destroy()  # Clear the first page

    label_title = tk.Label(frame, text="Tšekk, mida analüüsin: ", font=("Helvetica", 14))
    label_title.place(x=200, y=50)

    print(image)
    print(f"Esimesel lehel leitud pildi tyyp: {type(image)}")

    # Create an object of tkinter ImageTk
    photo_image = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label_image = tk.Label(frame, image=photo_image)
    label_image.image = photo_image  # Keep a reference to the image to prevent it from being garbage collected
    label_image.pack(pady=20)


###########################################################
# Esimese lehe button_choose abimeetod
# küsib kasutajalt failinime, nupu Enter vajutades kontrollib, kas see on olemas
###########################################################
def kusi_pildi_nime(frame):
    lable = tk.Label(frame, text="Sisesta palun faili nimi: ")
    lable.place(x=235, y=400)
    entry_field = tk.Entry(frame)
    entry_field.place(x=235, y=450)
    button_submit = tk.Button(frame, text="Enter", command=lambda: kas_leidus(frame, vastus=entry_field.get()))
    vastus = entry_field.get()
    print(f"sisestatud fail oli: {vastus}")
    button_submit.place(x=400, y=450)


###########################################################
# Esimese lehe button_choose abimeetod
# kontrollib, kas kasutaja sisestatud failinimi on olemas
# tagastab saadud pildi või None
###########################################################
def kas_leidus(frame, vastus):
    kasleidus = pilditootlus.leia_pilt(vastus)
    if kasleidus is not None:
        text = tk.Label(frame, text=f"Pilt {vastus} leidus")
        text.place(x=210, y=500)
        img = pilditootlus.leia_pilt(vastus)
        proceed(frame, img)
    else:
        text = tk.Label(frame, text=f"Pilti {vastus} ei leidunud. Palun vaata, kas kirjapilt on õige!")
        text.place(x=170, y=500)


###########################################################
# Esimese lehe button_upload ja button_choose abimeetodid
# kontrollib, kas on saadud kätte pilt
# kui jah, siis liigub edasi teisele lehele
# kui ei, siis jääb esimese lehe juurde
###########################################################
def check_and_proceed(action, frame):
    result = action()
    if isinstance(result, Image.Image):
        print("A valid picture was found, going to the second page")
        print(f"Image size: {result.size}, mode: {result.mode}")
        show_second_page(frame, result)
    else:
        print("No valid image returned, staying on the first page.")


###########################################################
# Esimese lehe button_upload ja button_choose abimeetodid
# liigub edasi teise lehe juurde
###########################################################
def proceed(frame, result):
    print("A valid picture was found, going to the second page")
    print(f"Image size: {result.size}, mode: {result.mode}")
    show_second_page(frame, result)


###########################################################
# GUI peameetod
###########################################################
def main():
    root = tk.Tk()
    root.title("Application")
    show_first_page(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# class Application(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Python Tkinter App")
#         self.geometry("600x400")
#         # self.resizable(False, False)
#
#         self.notebook = ttk.Notebook(self)
#         self.notebook.pack(expand=True, fill='both')
#
#         self.create_first_page()
#         self.create_second_page()
#         self.create_third_page()
#         self.create_fourth_page()
#
#         # Force the notebook to display the first page
#         self.after(0, lambda: self.notebook.select(0))
#
#     def create_first_page(self):
#         # first_page = ttk.Frame(self.notebook)
#         # self.notebook.add(first_page, text="First Page")
#         #
#         # upload_button = ttk.Button(first_page, text="Lae pilt üles", command=self.upload_image)
#         # upload_button.pack(pady=10)
#         #
#         # search_button = ttk.Button(first_page, text="Otsi arvutist", command=self.prompt_for_filename)
#         # search_button.pack(pady=10)
#         #
#         # info_text = tk.Text(first_page, height=4, wrap='word')
#         # info_text.insert('1.0', "Poetšekilt summade jagamine inimeste vahel. Sisesta oma tšeki pilt ja leiame õiged võlgnikud üles!")
#         # info_text.config(state='disabled')
#         # info_text.pack(pady=10, padx=10, fill='x')
#         first_page = ttk.Frame(self.notebook)
#         self.notebook.add(first_page, text="First Page")
#
#         upload_button = ttk.Button(first_page, text="Lae pilt üles", command=pilditootlus.lae_ules_pilt())
#         upload_button.pack(pady=10)
#
#         # Define a function to handle the file search
#         def search_file():
#             filename = tk.simpledialog.askstring("File Name", "Enter the file name:")
#             if filename:
#                 pilditootlus.leia_pilt(filename)  # Call lae_pilt with the entered filename
#
#         search_button = ttk.Button(first_page, text="Otsi arvutist", command=search_file)
#         search_button.pack(pady=10)
#
#         info_text = tk.Text(first_page, height=4, wrap='word')
#         info_text.insert('1.0',
#                          "Poetšekilt summade jagamine inimeste vahel. Sisesta oma tšeki pilt ja leiame õiged võlgnikud üles!")
#         info_text.config(state='disabled')
#         info_text.pack(pady=10, padx=10, fill='x')
#
#     def prompt_for_filename(self):
#         filename = filedialog.askopenfilename(title="Kirjuta faili nimi: ", filetypes=[("Pildifailid", "*.jpg *.png")])
#         if filename:
#             pilditootlus.leia_pilt(filename)
#
#     def create_second_page(self):
#         second_page = ttk.Frame(self.notebook)
#         self.notebook.add(second_page, text="Second Page")
#
#         self.canvas = tk.Canvas(second_page, width=400, height=300, bg='grey')
#         self.canvas.pack(pady=10)
#         self.canvas.bind("<Button-1>", self.get_coordinates)
#
#         rotate_button = ttk.Button(second_page, text="Pööra 90 kraadi", command=self.rotate_image)
#         rotate_button.pack(pady=10)
#
#         self.coordinates = []
#
#     def create_third_page(self):
#         third_page = ttk.Frame(self.notebook)
#         self.notebook.add(third_page, text="Third Page")
#
#         self.check_var1 = tk.IntVar()
#         self.check_var2 = tk.IntVar()
#         self.check_var3 = tk.IntVar()
#
#         self.text_box1 = tk.Text(third_page, height=4, wrap='word')
#         self.text_box1.insert('1.0', "Checkbox elements will appear here.")
#         self.text_box1.config(state='disabled')
#         self.text_box1.pack(pady=10, padx=10, fill='x')
#
#         self.text_box2 = tk.Text(third_page, height=2, wrap='word')
#         self.text_box2.pack(pady=10, padx=10, fill='x')
#
#         input_label = tk.Label(third_page, text="Input:")
#         input_label.pack(pady=5, padx=10, anchor='w')
#
#         self.input_text = tk.Entry(third_page)
#         self.input_text.pack(pady=5, padx=10, fill='x')
#
#         submit_button = ttk.Button(third_page, text="Submit", command=self.submit_third_page)
#         submit_button.pack(pady=10)
#
#     def create_fourth_page(self):
#         fourth_page = ttk.Frame(self.notebook)
#         self.notebook.add(fourth_page, text="Fourth Page")
#
#         self.info_text_box = tk.Text(fourth_page, height=10, wrap='word')
#         self.info_text_box.insert('1.0', "Information will appear here.")
#         self.info_text_box.config(state='disabled')
#         self.info_text_box.pack(pady=10, padx=10, fill='x')
#
#         button_frame = ttk.Frame(fourth_page)
#         button_frame.pack(pady=10, padx=10, anchor='e')
#
#         edit_button = ttk.Button(button_frame, text="Muuda", command=self.edit_info)
#         edit_button.pack(side='left', padx=5)
#
#         send_button = ttk.Button(button_frame, text="Saada tšekk", command=self.send_check)
#         send_button.pack(side='left', padx=5)
#
#     def search_computer(self):
#         file_path = filedialog.askopenfilename()
#         if file_path:
#             messagebox.showinfo("Search Computer", f"File found: {file_path}")
#
#     def get_coordinates(self, event):
#         if len(self.coordinates) < 4:
#             x, y = event.x, event.y
#             self.coordinates.append((x, y))
#             print(f"Coordinate: ({x}, {y})")
#
#     def rotate_image(self):
#         messagebox.showinfo("Rotate Image", "Image rotated 90 degrees!")
#
#     def submit_third_page(self):
#         checkboxes = [self.check_var1.get(), self.check_var2.get(), self.check_var3.get()]
#         input_text = self.input_text.get()
#         print(f"Checkboxes: {checkboxes}")
#         print(f"Input: {input_text}")
#
#     def edit_info(self):
#         self.info_text_box.config(state='normal')
#
#     def send_check(self):
#         messagebox.showinfo("Send Check", "Check sent!")
#
#
# if __name__ == "__main__":
#     app = Application()
#     app.mainloop()
