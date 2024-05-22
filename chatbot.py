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
# 1.1) Jah -
# 1.2) Ei - Sisesta inimeste arv -> return summa(kokku summa rida või liida kõik tooted kokku) / inimestega