# AI-project-24
Poetšekilt soetatud asjade pildilt sisselugemine ning juturobotiga soetatud asjade ära jagamine mitme inimese vahel.

Autorid: Anne-Mari Kasemetsa, Stina Maripuu

## Programmi kirjeldus

Programm laseb kasutajal laadida üles pildi, küsib kasutajalt kelle vahel ta soovib mis tooted jaotada ja arvutab automaatselt ära, kes kellele kui palju võlgu on.
Programm kasutab Tesseract-OCR-i, et tuvastada tehisintellekti abil tšekil olev tekst

## Jooksutamise juhend

### Vajalikud package'id:
Kontrollida, et arvutis, kus programmi jooksutada on olemas python, openssl ja anaconda:

``` python --version ```

``` openssl --version ```

``` anacoda3 --version ```

Kui openssl puudub, saab alla laadida selle tutoriali jargi: https://bonguides.com/how-to-install-openssl-in-windows-10-11/

### **Programmi jooksutamiseks on vaja alla laadida Tesseract-OCR**

Tesseracti alla laadimise juhend: https://www.youtube.com/watch?v=HNCypVfeTdw

Tesseracti github: https://github.com/tesseract-ocr

### Installi pytesseract

Et kood kasutab ja impordib **pytesseract**, siis et see töötaks tuleb kas conda või pip-i abil installida pytesseract.

1. Vaata, mis on IDE-s Python interpreter (siin PyCharm näide): 

    *File -> Settings -> Project: AI-project-24 -> Python interpreter*

2. kui su interpreter on anaconda, siis installi pytesseract conda kaudu
    ```conda install pytesseract```
   
   vajadusel enne seda ```conda activate "path to conda file nt C:\Users\Zenbook\Anaconda3"```
   
   ja   ```conda config --add channels conda-forge```

4. kui su interpreter ei ole anaconda vaid muu python, siis pip-i kaudu
   
   ```pip install pytesseract```

pytesseracti kasutamise juhend: https://pypi.org/project/pytesseract/

### Eesti keel pytesseractis

mugavamaks kasutamiseks alla laadida ka **eesti keel pytesseractis**

Juhend:

1. Download the Estonian language data file (est.traineddata) from the official Tesseract repository or from a trusted source: https://github.com/tesseract-ocr/tessdata/blob/main/est.traineddata 
2. Place the downloaded file in the Tesseract tessdata (example C:\Program Files\Tesseract-OCR\tessdata) directory:

**proovi, et fail tesseractproov.py töötab**
**NB! koodis on vaja ilmselt enda tesseract faili path asendada**


## GUI lehtede kiire kirjeldus

1. **esimesel lehel küsitakse, kas laadida pilt üles või valida olemasolev fail**

   Olemasolevad failid on: "tsekk1.jpg", "tsekk2.jpg" jne kuni "tsekk7.jpg"

   Kui soovida lihtsalt programmi töötamist testida, siis saab valida olemasoleva faili ning kiirelt kogu programm läbi jooksutada
3. **Peale faili üleslaadimist või olemasoleva faili valimist avaneb koheselt seesama pilt**
4. **Etteilmunud pildi peal tuleb hiirega kropeerida pilt sobivaks, et pildile jääks ainult tšekk ja mitte tausta**

   Koperimine käib hiirega - vaja teha ainult kaks liigutust: vajuta alla hiir pildi vasakul üleval nurgas

   ning lase lahti pildi paremal all nurgas. Kui toimis siis ilmub ekraanile kopeeritud pilt
6. **NB! Kui kropeeritud pilt on ette ilmunud, siis PEAB VAJUTAMA 'S' tähe nuppu**
7. **Peale 'S' nupu vajutamist salvestatakse kropeeritud pilt ära ning ilmub uus leht**
8. **Uuel lehel saab näha kropeeritud pilti**

   vajadusel saab keerata pilti õigetpidi või minna uuesti kropeerimise juurde

   kui kropeeritud pilt sobib, siis vajutada nuppu 'Liigu edasi'
9. **Tekib ette uus leht, sellel lehel tuleb sisestada:**
   
   Vali kõik tooted, mis lähevad ühele inimesele, ning kirjuta tema nimi

   Kui kõik selle inimese tooted on valitud ja nimi kirjutatud, siis vajuta 'salvesta'
   
   Korda kõikide inimestega, kelle vahel tahad jagada ning tooted saavad otsa

10. **Kui vajutada nuppu 'Arvuta tulemus', siis avaneb viimane leht, kus on arvutatud iga inimese puhul palju ta peab kellele maksma**

   Tekib ette jaotus, kes kui palju kellele võlgu on.
   Tulemust on võimalik alla laadida tekstifailina.

Näidisvideo: https://drive.google.com/file/d/1zamEWNwFbL3AnXjg97mqFZPmso6fGG8A/view?usp=sharing 

