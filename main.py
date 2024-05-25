import cv2
import imageio
import numpy as np
import pilditootlus
import tkinter as tk
from PIL import Image, ImageTk
import os
import imagecrop
from tkinter import ttk, filedialog, messagebox


# 1. Sisestad pildi või otsid nime järgi pildi nime
# 2. kasutaja kropeerib pildi sobivaks
# 2. programm loeb sisse kropeeritud pildi ning küsib, mida teha (kuidas jagada) - juturobot
# 3. programm loeb pildi pealt tooted ning nende hinnad
# 4. vastavalt kasutaja soovile jaotab programm automaatselt ära, kes kui palju peab maksma

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
#                    ESIMENE LEHT
# kas laadida pilt üles või otsida nime järgi
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
    button_upload.place(x=200, y=250)

    # vali fail nupp käivitab meetodi kusi_pildi_nime, mis tekitab uued elemendid ja küsib kasutajalt failinime
    # meetod check_and_prooceed kontrollib, kas vastuseks saadi Image, kui jah siis liigub teisele lehele
    button_choose = tk.Button(frame, text="Vali fail",
                              command=lambda: check_and_proceed(lambda: kusi_pildi_nime(frame), frame))
    button_choose.place(x=350, y=250)

    label_instruction2 = tk.Label(frame,
                                  text="Kui laed üles pildi/leiad faili, siis tuleb ette see pilt.\n"
                                       "Sellel pildid pead sa hiirega alustades ühest nurgast kropeerima pilti, \n et jääks peale ainult tšekk ja mitte tausta. \n"
                                       "Kui oled kropeerinud ning uus pilt ilmub ette, siis vajuta 's' tähte")
    label_instruction2.place(x=100, y=300)


###########################################################
#                     TEINE LEHT
# kasutaja peab croppima pildi õigeks suuruseks
# liigub edasi, kui pilt on cropitud
###########################################################
mouse_pressed = False
starting_x = starting_y = ending_x = ending_y = -1
cropped = None
img_dup = None


def show_second_page(frame, image):
    algne = image
    print(image)
    print(f"Esimesel lehel leitud pildi tyyp: {type(image)}")
    image_array = np.array(image)
    image = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    print(f"pildi tyyp nyyd: {type(image)}")

    # cropping the image

    img = image
    img_dup = np.copy(img)
    mouse_pressed = False
    cropped = None
    # defining starting and ending point of rectangle (crop image region)
    starting_x = starting_y = ending_x = ending_y = -1

    # funktsioon, mille abil kasutaja klikkimise ja hiire liigutamise peale kropeeritakse pilt
    def mousebutton(event, x, y, flags, param):
        global img_dup, starting_x, starting_y, ending_x, ending_y, mouse_pressed, cropped
        global mouse_pressed
        # if left mouse button is pressed then takes the cursor position at starting_x and starting_y
        if event == cv2.EVENT_LBUTTONDOWN:
            mouse_pressed = True
            starting_x, starting_y = x, y
            img_dup = np.copy(img)

        elif event == cv2.EVENT_MOUSEMOVE:
            if mouse_pressed:
                img_dup = np.copy(img)
                cv2.rectangle(img_dup, (starting_x, starting_y), (x, y), (0, 255, 0), 1)
        # final position of rectangle if left mouse button is up then takes the cursor position at ending_x and ending_y
        elif event == cv2.EVENT_LBUTTONUP:
            print("Lbuttonupis")
            mouse_pressed = False
            ending_x, ending_y = x, y
            cropped = img[starting_y:ending_y, starting_x:ending_x]
            cv2.imshow('cropped', cropped)
            print("cropped type in lbuttonup: ", type(cropped))
            imageio.imwrite("kropeeritud.png", cropped)
            print("salvestatud")

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 800, 600)
    cv2.setMouseCallback('image', mousebutton)

    while True:
        cv2.imshow('image', img_dup)
        k = cv2.waitKey(1)
        if k == ord('s'):
            print("cropped type after s: ", type(cropped))
            print("Sain kommandi")
            print("Cropped image on olemas")
            cropped = imageio.v2.imread("kropeeritud.png")
            cv2.destroyWindow('image')
            break
        elif k == 27:
            break
    cv2.destroyAllWindows()
    print("Nyyd siin")
    print("cropped type: ", type(cropped))

    # kui saadi kätte kropeeritud pilt, siis läheb uuele lehele
    # ja küsib, kas see kropeering sobib, kui ei siis tagasi teisele lehele ja uuesti kropeering
    if cropped is not None:
        print("Kropeeritud pilt olemas, liigume küsimise lehele")
        kusi_kas_sobib(frame, cropped, algne)


def kusi_kas_sobib(frame, cropped, algne):
    for widget in frame.winfo_children():
        widget.destroy()

    label_title = tk.Label(frame, text="Kropeeritud pilt: ", font=("Helvetica", 16))
    label_title.place(x=230, y=50)

    image = imageio.v2.imread("kropeeritud.png")
    print("Crop img: ", type(image))

    # Convert the image to a PIL Image object
    pil_image = Image.fromarray(image)

    # Resize the image to fit within a maximum width and height
    max_width = 400
    max_height = 400
    resized_image = resize_image(pil_image, max_width, max_height)

    # Convert the resized PIL Image to a Tkinter PhotoImage object
    tk_image = ImageTk.PhotoImage(resized_image)

    pic = tk.Label(frame, image=tk_image)
    pic.place(x=50, y=100)
    pic.image = tk_image

    label_instruction = tk.Label(frame,
                                 text="Kas kropeeritud pilt sobib, või soovid uuesti kropeerida?")
    label_instruction.place(x=150, y=520)

    button_edasi = tk.Button(frame, text="Liigu edasi",
                             command=lambda: show_third_page(frame, image))
    button_edasi.place(x=150, y=550)

    button_uuesti = tk.Button(frame, text="Kropeeri uuesti",
                              command=lambda: show_second_page(frame, algne))
    button_uuesti.place(x=250, y=550)

    button_keera = tk.Button(frame, text="Keera pilti (90)",
                             command=lambda: turn_image(frame, pic))
    button_keera.place(x=350, y=550)

rotation_angle = 0
def turn_image(frame, pic):
    global rotation_angle
    rotation_angle += 90

    img = imageio.v2.imread("kropeeritud.png")
    rotated = np.rot90(img)
    imageio.v2.imwrite("kropeeritud.png", rotated)
    print("Pilti keerati 90 kraadi paremale ja salvestati ara")

    image = imageio.v2.imread("kropeeritud.png")
    print("Crop img: ", type(image))

    # Convert the image to a PIL Image object
    pil_image = Image.fromarray(image)

    # Resize the image to fit within a maximum width and height
    max_width = 400
    max_height = 400
    resized_image = resize_image(pil_image, max_width, max_height)

    # Convert the resized PIL Image to a Tkinter PhotoImage object
    tk_image = ImageTk.PhotoImage(resized_image)

    pic.config(image=tk_image)
    pic.image = tk_image


def resize_image(image, max_width, max_height):
    width, height = image.size
    if width > max_width or height > max_height:
        ratio = min(max_width / width, max_height / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        return image.resize((new_width, new_height), Image.ANTIALIAS)
    return image


def show_third_page(frame, cropped):
    for widget in frame.winfo_children():
        widget.destroy()
    label_title = tk.Label(frame, text="Kolmas leht: ", font=("Helvetica", 16))
    label_title.place(x=150, y=100)


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
