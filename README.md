# AI-project-24
Poetšekilt soetatud asjade pildilt sisselugemine ning juturobotiga soetatud asjade ära jagamine mitme inimese vahel.

Programmi kirjeldus

Jooksutamise juhend

vajalik Pythoni olemasolu arvutis

vajalik importida pytesseract, samuti on jooksutamiseks vaja alla laadida tesseracti
https://www.youtube.com/watch?v=HNCypVfeTdw tutorial selle jaoks
NB! pytesseract tuleks installida conda cmd-l (conda install pytesseract, vajadusel enne seda conda activate "path to conda file nt C:\Users\Zenbook\Anaconda3", ja:  conda config --add channels conda-forge)

mugavamaks kasutamiseks alla laadida ka eesti keel pytesseractis
1. Download Estonian Language Data
Download the Estonian language data file (est.traineddata) from the official Tesseract repository or from a trusted source:

Estonian language data on GitHub
Place the downloaded file in the Tesseract tessdata directory:

If you installed Tesseract using the default settings, the tessdata directory is likely located at C:\Program Files\Tesseract-OCR\tessdata on Windows.

pytesseracti jooksutamiseks vajalik OpenSSL olemasolu
vajadusel alla laadida selle tutoriali jargi https://bonguides.com/how-to-install-openssl-in-windows-10-11/

(step-by-step installation ja commandid jooksutamiseks)

GUI lehtede kiire kirjeldus
nt esimesel lehel - kaks nuppu, kui saad pildi üles laetud, siis kohe tekib ette see pilt ning sul on vaja kropeerida
kropeerimisel ei teki värvilist ruutu pildi peale, aga kropeerimiseks on vaja teha ainult kaks liigutust: vajuta alla hiir pildi vasakul üleval nurgas
ning lase lahti pildi paremal all nurgas. Sellisel juhul tekib ette kropeeritud pilt. 
NB! PEAD vajutama tähte 's', et kropeeritud pilt salvestuks ning et liikuda edasi
vastasel juhul edasi liikuda ei saa

