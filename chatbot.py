# kui on teada mis toote kohta allahindlus on, siis lõpptabelisse läheb juba allahindlusega hhind
# kui pole teada, mis toote kohta allahindlus, siis protsentuaalselt sama palju kui palju eest ta maksab
# ala maksab 60% tsekist, saab 60% allahindlusest ka
# sisend tuleb kujul
# tooted = [(jrk nr (int), "nimetus" (str), kogus (int), hind (float)), ()...]
tooted = [(1, "Kartulikrõps Lays Roheline", 1,4.77), (2, "Jäätis Limpa", 3, 0.69), (3, "Tualettpabeer Zewa", 1, 12.55)]

# chatboti töökirjeldus
# -----
# Kas soovid kogu tšeki protsentideks jaotada või eseme kaupa?
# 1) Protsendid - Kas jaotad inimeste vahel protsendid erinevalt? Jah / Ei
# 1.1) Jah - Sisesta inimeste nimed komadega ning nende taha
# mis protsendi soovid anda talle maksmiseks
# 1.2) Ei - Sisesta inimeste nimed komadega (siit saab inimeste arvu)
# -> return summa(kokku summa rida või liida kõik tooted kokku) / inimestega
# 1.1.1) KONTROLL kas protsendid = 1, kui ei siis uuesti 1.1, kellele mis protsent

# 2) Eseme kaupa, küsi inimeste nimed komadega enne
# -> näita nimekiri ja vali järjekorra nr järgi, komasid ei pea panema
# 2.1) Iga sisestatud nime kohta panna nimekiri mis valitakse nt ilma komadeta ning järgmise
# nime jaoks nimekirjast eelmised eemaldatakse, kui midagi jääb peale tsüklit üle, saab valida
# eraldi et nimi ja numbrid mis veel talle lisada jne kuni rohkem elemente pole
# 2.1.1) Kui kõik on sisestatud, kokkuvõte et mis kellel ja mis summa kokku igal
# 2.1.1) Küsimus - kas kõik sobib? jah / ei
# 2.1.1.1) Jah - prinditakse ja võimaldadakse kokkuvõte alla laadida
# et palju kes ja mis protsendid maksab siis
# 2.1.1.2) Ei - Sisestada kellelt mis element ära võtta, kellele lisada.
# "Kadri", 4 3 6 2, "Mia" ehk Kadrilt 4 3 6 2 Miale -> tsükkel 2.1.1 juurde kas sobib
# ja kui muid muutusi siis kuni inimene ütleb jah sobib

