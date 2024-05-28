import pytesseract
import cv2
import re

# NB! MUUTA OMA ARVUTIS OLEVA TESSERACT PATHIGA
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def tootle_pilti_pytesseractiga():

    img = cv2.imread('kropeeritud.png')
    tekst = pytesseract.image_to_string(img, lang="est")
    #print(tekst)
    # Split the input text into lines
    lines = tekst.split("\n") ####muuta siin tekst1 ära

    # Initialize the list to hold the parsed data
    parsed_list = []

    # Helper function to extract price and name
    def extract_price_name(parts):
        if len(parts) < 2:
            return None, None
        try:
            price = float(parts[-2])
            name = " ".join(parts[:-2]).strip()
            return name, price
        except ValueError:
            return None, None

    # Iterate over the lines and parse the data
    index = 1
    buffer = []
    for i, line in enumerate(lines):
        if line.strip() == "":
            continue
        parts = line.rsplit(' ', 2)
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

# Sa void need alumised meetodid teha ka chatbot.py-s, vaata ise kuidas tahad
