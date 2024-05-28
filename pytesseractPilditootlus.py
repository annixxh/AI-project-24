import pytesseract
import cv2
import re

# NB! MUUTA OMA ARVUTIS OLEVA TESSERACT PATHIGA
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def tootle_pilti_pytesseractiga():
    tekst1 = """Kilekott MAXIMA EPI
0.10A
Pet pudel 1,5] 0.08 N
Vesi AURA Fruit 0.94 A
J hkel FAZ
azeri Hele peenleib, 0.83 A
Spagetid BIG 4009 0.39 A
Keeduvorst Doktori NÕO 250g 1.16 4
Kodujuust EKSTRA 6% 0.84 A
Mandariin väike, ka
1.09 X 1.316 KG 1.43 4
Allahindlus -0.13 4
Kohup.kreem FARMI vaarika 0.57 A
Kohup.kreem FARMI vaarika 0.57 4
Kohup.kreem FARMI vaarika 0.57 4
Kodujuust EKSTRA 6% 0.84 A
Majonees Provansaal JAANI 40% 2.274
Hapukoor ARMAS 20% 500g 0.63 A
Hapukoor ARMAS 20% 500g 0.63 A
Või ARMAS 82% 1809 0.95 A
Või ARMAS 82% 1609 0.95 4
Või ARMAS 82% 1809 0.95 4"""
    img = cv2.imread('kropeeritud.png')
    tekst = pytesseract.image_to_string(img, lang="est")
    print("Pildilt loetud tekst on: ")
    print(tekst)
    # Split the input text into lines
    lines = tekst.split("\n")  # todo muuta siin tekst1 ära
    print(lines)

    # Initialize the list to hold the parsed data
    parsed_list = []
    # i = 1
    # for el in lines:
    #     osad = el.split(" ")
    #     price = 0
    #     name = ""
    #     print("Hetkene line: ", osad)
    #     # print(osad[-1], osad[-2])
    #     if len(osad)==1 or osad[0]=='':
    #         print("tyhi element")
    #         continue
    #     if '€' in osad[-1] or osad[-1].isnumeric():
    #         print("Viimane element on hind")
    #         price = float(osad[-1][1:])
    #         name = osad[0:-1]
    #         parsed_list.append([i, name, price])
    #         continue
    #     elif '€' in osad[-2] or osad[-2].isnumeric():
    #         print("Eelviimane element on hind")
    #         price = float(osad[-2])
    #         name = osad[0:-2]
    #         parsed_list.append([i, name, price])
    #         continue
    #     else:
    #         print("Ei leidnud hinda")
    #         continue
    # print("Nyyd siin")
    # print(parsed_list)
    #Helper function to extract price and name
    def extract_price_name(parts):
        if len(parts) < 2:
            print("here")
            return None, None
        try:
            price = float(parts[-2])
            name = " ".join(parts[:-2]).strip()
            print("price", price)
            print("name", name)
            return name, price
        except ValueError:
            print(type(parts[-2]))
            print("valueerroris")
            return None, None

    # Iterate over the lines and parse the data
    index = 1
    buffer = []
    for i, line in enumerate(lines):
        if line.strip() == "":
            continue
        parts = line.rsplit(' ', 2)
        print("parts")
        print(parts)
        name, price = extract_price_name(parts)
        if line.startswith("Allahindlus"):
            # Remove the discount from the previous entry
            if parsed_list:
                discount = float(parts[-2])
                parsed_list[-1][2] += discount
        elif name is not None and price is not None:
            if buffer:
                name = " ".join(buffer) + " " + name
                buffer = []
            parsed_list.append([index, name, price])
            index += 1
        else:
            buffer.append(line.strip())

    # Handle any remaining buffered lines
    if buffer:
        parts = buffer[-1].rsplit(' ', 2)
        name, price = extract_price_name(parts)
        if name is not None and price is not None:
            buffer.pop()
            name = " ".join(buffer) + " " + name
            parsed_list.append([index, name, price])
    print(parsed_list)
    return parsed_list
