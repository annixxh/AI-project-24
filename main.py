import cv2
import imageio
import numpy as np
import pilditootlus
import tkinter as tk
from PIL import Image, ImageTk
import pytesseractPilditootlus

# 1. Sisestad pildi või otsid nime järgi pildi nime                                             # todo DONE
# 2. kasutaja kropeerib pildi sobivaks                                                          # todo DONE
# 2. programm loeb sisse kropeeritud pildi ning küsib, mida teha (kuidas jagada) - juturobot    # todo poolik
# 3. programm loeb pildi pealt tooted ning nende hinnad                                         # todo VAJA TEHA
# 4. vastavalt kasutaja soovile jaotab programm automaatselt ära, kes kui palju peab maksma     # todo VAJA TEHA

###########################################################
# GUI käivitamine
###########################################################


# todo NBNBNBNB! Et pytesseract töötaks peab võibolla pytesseractPilditootlus.py failis ->
# todo -> muutma ära tesseracti pathi enda arvutis oleva pathiga

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
# todo see leht on täiesti tehtud
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
# todo see leht on täiesti tehtud
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
    # kood võetud siit: https://www.engineerknow.com/2022/12/crop-image-simple-app-using-cv2-numpy.html
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


###########################################################
#                     VAHELEHT
# küsib, kas kropeeritud pilt sobib, võimalik minna tagasi kropeerima
# või pöörata pilti. Liigub edasi, kui pilt sobib.
# todo see leht on täiesti tehtud
###########################################################


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
                             command=lambda: show_third_page(frame))
    button_edasi.place(x=150, y=550)

    button_uuesti = tk.Button(frame, text="Kropeeri uuesti",
                              command=lambda: show_second_page(frame, algne))
    button_uuesti.place(x=250, y=550)

    button_keera = tk.Button(frame, text="Keera pilti (90)",
                             command=lambda: turn_image(frame, pic))
    button_keera.place(x=350, y=550)


###########################################################
#                     KOLMAS LEHT
# Küsib kasutajalt, kelle vahel jaotada tšekilt leitavad tooted
# Lisaks, millised tooted peaks kellele minema
# pildi pealt saadakse tekst kätte, vaja leida sellest tekstist n.ö õiged tooted üles
#
# TODO lõpetada see GUI leht
# TODO sellel lehel:
# küsida kasutajalt mis tooted kellele maksta ning lisaks kes kui palju maksis
# luua vajalikud variablid, kus need hoidakse (pead ilmselt global tegema, vt save_inimesed()
# viidata õigetele meetoditele, et arvutusloogika toimiks ning jõuaks tagasi siia main.py-sse ka
# NB! sa võid muuta kõiki meetodeid mis on seotud show_third_page() ja pytesseractPilditootlus.py failis
# aga proovi mitte muuta meetodeid mis on seotud esimeste lehtedega PLS, muidu katki :))
# vaata eelmise lehtede ülesehitust, kui tahad lisada GUI-le lable'id jne
# vt märget 'kropeeritud.png' kohta selle meetodi all
# sinul ei tohiks vaja minna mingit pildi n.ö üleslaadimis või teisendus paska
# aka sa peaks saama kõik kätte cv2.imread('kropeeritud.png')ga
# peamine arvutus peaks olema võimalik pytesseractPilditootlus failis
# TODO pytesseractPilditootlus.py failis:
# leida saadud tekstist õiged read üles ning nendest eraldada summad, lisada need summad õigetele inimestele
# mingi arvutusloogika, mille järgi arvutatakse ära kellele mis summa läheb (arvestades ka palju keegi algselt maksis)
###########################################################

# inimesed = [] # nt inimesed = [Stina, Anni] ehk kelle vahel jagada
# jaotus = {} # nt {Stina: 5.20, Anni: 6.99}  ehk see mis siis lopuks keegi peab tagasi maksma
# maksmised = {} # nt {Stina: 12.00, Anni: 0.00} ehk see palju keegi maksis
items = []
selections = {}
name_totals = {}
def show_third_page(frame):
    global items, selections, name_totals

    def create_checklist(frame):
        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        check_vars = []
        for item in items:
            var = tk.IntVar()
            check_vars.append(var)
            check_text = f"{item[1]} - {item[2]:.2f}€"
            check = tk.Checkbutton(scrollable_frame, text=check_text, variable=var)
            check.pack(anchor='w')

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return check_vars

    def save_selection():
        entry_value = entry_kysimus.get()
        selected_items = [items[i] for i, var in enumerate(check_vars) if var.get() == 1]
        selections[entry_value] = selected_items
        print("Selected items:", selected_items)
        print("Selections:", selections)

        # Remove selected items from the items list
        global items
        items = [item for i, item in enumerate(items) if not check_vars[i].get()]

        # Refresh the checklist display
        show_third_page(frame)

    for widget in frame.winfo_children():
        widget.destroy()


    label_title = tk.Label(frame, text="Kelle vahel mida jagame?", font=("Helvetica", 16))
    label_title.place(x=150, y=100)

    # leiab pildilt pytesseractiga teksti
    # NB! Failis pytesserractPilditootlus on vaja muuta tesseract path oma arvutis olevaks pathiks
    #teksti_read = pytesseractPilditootlus.tootle_pilti_pytesseractiga()
    #print("Pildilt loetud tekst on: ")
    #print(teksti_read)



    teksti_read = pytesseractPilditootlus.tootle_pilti_pytesseractiga()
    print("Pildilt loetud tekst on: ")
    print(teksti_read)
    if not items:
        if len(selections) > 0:
            for widget in frame.winfo_children():
                widget.destroy()
            viimasele_lehele(frame)
        else:
            items = teksti_read
            selections = {}
            name_totals = {}
    if items:

        lable_kysimus = tk.Label(frame, text="Kelle vahel soovid summad jagada?")
        lable_kysimus.place(x=150, y=150)

        entry_kysimus = tk.Entry(frame)
        entry_kysimus.place(x=150, y=200)

        save_button = tk.Button(frame, text="Save", command=save_selection)
        save_button.place(x=300, y=200)

        checklist_frame = tk.Frame(frame)
        checklist_frame.place(x=150, y=250)
        check_vars = create_checklist(checklist_frame)

    #button_vastuse_juurde = tk.Button(frame, text="Arvuta vastus", command=lambda: viimasele_lehele(frame))
    #button_vastuse_juurde.place(x=200, y=525)

    # show_selected_button = tk.Button(frame, text="Show Selected", command=show_selected)
    # show_selected_button.place(x=150, y=450)

    # TODO lable ja küsimus, kellele mis toode läheb või siis checkboxid
    # TODO lable ja küsimus, kes palju maksis

    # TODO mida veel teha vaja, et koik siin tootaks:
    # märkus: variable 'cropped' ei ole enam vaja, kuna alati programmi jooksutamisel tekib fail 'kropeeritud.png'
    # mis igal uuel jooksutamisel kirjtatakse üle, seega var cropped asemel saame igal pool kasutada lihtsalt
    # 'kropeeritud.png' ja see töötab (plus seda lihtsam cv2.imread('kropeeritud.png') kaudu üles laadida)
    # TODO luua ja panna inimesed kelle vahel jagada mingi dicti või listi, kus on lisaks ka nendele antud summa jne
    #    vt selle meetodi yles, need variablid luua ja neid rakendada loogikas kuidagi
    # TODO (pytesseractPilditootlus.py failis) töödelda pytesseracti antud tekste ja leida õiged tooted sealt üles
    #   + selle toote summa ja designeerida õigele inimesele
    # TODO arvutusloogika, et viimasel lehel esitleda, kes kui palju kellele maksma peab
    # TODO viimase lehe GUI

###########################################################
#                     NELJAS LEHT
# Näitab kasutajale kõikide inimeste puhul palju nad kellele võlgu on
# Võibolla võimalik minna tagasi algusesse?
# TODO täiesti tegemata
# vaata ka viimasele_lehele() abimeetodit
# (buttoni vajutades toimuvad arvutused ja viib viimasele lehele, kus esitletakse arvutuste tulemused)
# sellel lehel lihtsalt näidata tulemusi, rohkem eriti ei ole
# lisasin lehe alla nupu, et minna tagasi algusesse
###########################################################

def show_fourth_page(frame):
    global selections, name_totals

    for widget in frame.winfo_children():
        widget.destroy()

    label_title = tk.Label(frame, text="Tšekk jaotati nii: ", font=("Helvetica", 16))
    label_title.place(x=150, y=20)
    print("Nüüd neljanda lehe juures")

    y_position = 60  # Starting position for displaying information
    for name, items in selections.items():
        total = sum(item[2] for item in items)
        name_label = tk.Label(frame, text=f"{name} - Kogu summa: {total:.2f}€", font=("Helvetica", 14))
        name_label.place(x=150, y=y_position)
        y_position += 30

        for item in items:
            item_label = tk.Label(frame, text=f"{item[1]} - {item[2]:.2f}€")
            item_label.place(x=170, y=y_position)
            y_position += 20


        y_position += 10  # Add some space between different names

    button_algusesse = tk.Button(frame, text="Tagasi algusesse", command=lambda: tagasi_algusesse(frame))
    button_algusesse.place(x=200, y=550)

    print("Nüüd neljanda lehe juures")
    # vastused = mingimeetod() VOI SIIS pane show_fourth_page(frame, vastused)
    # TODO esitleda vastused



###########################################################
#                  ABIMEETODID
# seletused meetoditele sees, mitte väljas
###########################################################

# TODO
def viimasele_lehele(frame):
    # TODO voibolla vaja global muutujaid teha
    # seda meetodit ei ole tegelt vaja, kui teha koik vajalik show_third_page() meetodis ara
    # aga siin voib valja kutsuda meetodid, mis koik vajaliku ara arvutab
    # ja siis kui olemas siis liigub edasi neljandale lehele

    # NAITEKS
    # vastus = mingimeetod(jaotus, maksmised)
    # if vastus is not {}:
    #     print("Kõik vajalik arvutatud")
    #     print("Liigume viimasele lehele")
    #     show_fourth_page(frame)
    # praegu laheb niisama edasi
    show_fourth_page(frame)
    print("Calculating the final result...")
    print("Selections by each person:")
    for person, items in selections.items():
        print(f"{person}:")
        for item in items:
            name, price, a = item[1], item[2], item[0]
            price = float(price)
            print(f"  {name} - {price:.2f}€")


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
    #####################################################
    # Abimeetod, mis aitab ette antud pildi suurust kohandada kindla suuruse järgi
    ####################################################
    width, height = image.size
    if width > max_width or height > max_height:
        ratio = min(max_width / width, max_height / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        return image.resize((new_width, new_height), Image.ANTIALIAS)
    return image


inimesed_algne_vastus = ""
def save_inimesed(entry):
    global inimesed_algne_vastus
    input_text = entry.get()
    print("Kelle vahel jagada on: ")
    print(inimesed_algne_vastus)
    inimesed_algne_vastus = input_text


def kusi_pildi_nime(frame):
    ###########################################################
    # Esimese lehe button_choose abimeetod
    # küsib kasutajalt failinime, nupu Enter vajutades kontrollib, kas see on olemas
    ###########################################################
    lable = tk.Label(frame, text="Sisesta palun faili nimi: ")
    lable.place(x=235, y=400)
    entry_field = tk.Entry(frame)
    entry_field.place(x=235, y=450)
    button_submit = tk.Button(frame, text="Enter", command=lambda: kas_leidus(frame, vastus=entry_field.get()))
    vastus = entry_field.get()
    print(f"sisestatud fail oli: {vastus}")
    button_submit.place(x=400, y=450)


def kas_leidus(frame, vastus):
    ###########################################################
    # Esimese lehe button_choose abimeetod
    # kontrollib, kas kasutaja sisestatud failinimi on olemas
    # tagastab saadud pildi või None
    ###########################################################
    kasleidus = pilditootlus.leia_pilt(vastus)
    if kasleidus is not None:
        text = tk.Label(frame, text=f"Pilt {vastus} leidus")
        text.place(x=210, y=500)
        img = pilditootlus.leia_pilt(vastus)
        proceed(frame, img)
    else:
        text = tk.Label(frame, text=f"Pilti {vastus} ei leidunud. Palun vaata, kas kirjapilt on õige!")
        text.place(x=170, y=500)


def check_and_proceed(action, frame):
    ###########################################################
    # Esimese lehe button_upload ja button_choose abimeetodid
    # kontrollib, kas on saadud kätte pilt
    # kui jah, siis liigub edasi teisele lehele
    # kui ei, siis jääb esimese lehe juurde
    ###########################################################
    result = action()
    if isinstance(result, Image.Image):
        print("A valid picture was found, going to the second page")
        print(f"Image size: {result.size}, mode: {result.mode}")
        show_second_page(frame, result)
    else:
        print("No valid image returned, staying on the first page.")


def proceed(frame, result):
    ###########################################################
    # Esimese lehe button_upload ja button_choose abimeetodid
    # liigub edasi teise lehe juurde
    ###########################################################
    print("A valid picture was found, going to the second page")
    print(f"Image size: {result.size}, mode: {result.mode}")
    show_second_page(frame, result)


# TODO
def tagasi_algusesse(frame):
    # TODO vaadata üle, et kõik ikkagi ära kustuks ning tuleks n.ö puhas esimene leht jälle ette
    print("Lähme tagasi esimesele lehele")
    for widget in frame.winfo_children():
        widget.pack_forget()
    show_first_page(rootglobal)


###########################################################
# GUI peameetod
###########################################################
rootglobal = None
def main():
    global rootglobal
    root = tk.Tk()
    root.title("Application")
    rootglobal = root
    show_first_page(root)
    root.mainloop()


if __name__ == "__main__":
    main()
