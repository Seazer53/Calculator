import tkinter
import math


def hesap_makinesi():  # Hesaplama bitene kadar sürecin devamını sağlayan fonksiyon.
    icerik = labelinput.get()
    islem = str(icerik)
    islem_listesi = islem_listeleme(islem)
    islem_sonucu = -1

    parantez_var = False
    trigonometri_var = False
    logaritma_var = False

    print(islem_listesi)

    rakamlar = "0123456789"
    isaretler = "(+-*/^#)"

    if islem[0] not in rakamlar and islem[0] not in isaretler and islem[0] != "l":
        liste = trigonometrik_liste(islem)
        trigonometri_var = True
        islem_sonucu = trigonometri(liste)

    elif islem[0] not in rakamlar and islem[0] not in isaretler and islem[0] == "l":
        logaritma_var = True
        logaritma_liste = logaritmik_liste(islem)
        islem_sonucu = logaritma(logaritma_liste)

    while len(islem_listesi) >= 1 and trigonometri_var is not True and logaritma_var is not True:
        if "(" in islem_listesi and ")" in islem_listesi:
            parantez_var = True
            a_parantez = islem_listesi.index("(")
            k_parantez = islem_listesi.index(")")
            parantez_ici_liste = parantez_ici_listele(a_parantez, k_parantez, islem_listesi)

            print(parantez_ici_liste)

            duzenlenmis_liste = liste_duzenleyici(parantez_ici_liste)

            if len(duzenlenmis_liste) == 1:
                yeni_liste = parantez_ici_temizle(a_parantez, k_parantez, islem_listesi, duzenlenmis_liste[0])

            else:
                parantez_ici_sonuc = islem_onceligi(duzenlenmis_liste, parantez_var)
                yeni_liste = parantez_ici_temizle(a_parantez, k_parantez, islem_listesi, parantez_ici_sonuc)
                print(islem_listesi)

        else:
            if parantez_var is True:
                duzenli_liste = liste_duzenleyici(yeni_liste)
                islem_sonucu = islem_onceligi(duzenli_liste, parantez_var)

                if len(yeni_liste) <= 1:
                    break

            elif parantez_var is False:
                duzenli_liste = liste_duzenleyici(islem_listesi)
                islem_sonucu = islem_onceligi(duzenli_liste, parantez_var)

                if len(islem_listesi) <= 1:
                    break

    print(islem_sonucu)
    sonuc.configure(text="İşlem Sonucu: " + str(islem_sonucu))


def islem_listeleme(input):  # Bu fonksiyon girilen inputtaki sayilari ve operatörleri ayırarak liste haline getirir.
    operatorler = "^(*/+-)#"
    liste_islem = []
    sayi = ""
    operator = ""
    sayac = 0

    for x in input:
        if x not in operatorler:
            sayi += x
            sayac += 1

        elif x in operatorler:
            if sayi != "":
                liste_islem.append(sayi)
                sayi = ""

            operator += x
            liste_islem.append(operator)
            operator = ""
            sayac += 1

        if sayac == len(input) and sayi != "":
            liste_islem.append(sayi)

    return liste_islem


def trigonometrik_liste(input):  # Bu fonksiyon trigonometrik ifade ile büyüklüğünü ayırarak liste haline getirir.
    rakamlar = "0123456789"
    trigonometrik_operator = ""
    derece = ""
    liste = []

    for l in input:
        if l not in rakamlar:
            trigonometrik_operator += l

        else:
            derece += l

    liste.append(trigonometrik_operator)
    liste.append(float(derece))

    return liste


def logaritmik_liste(input):  # Bu fonksiyon logaritmik fonksiyon ile değerini ayırarak liste haline getirir.
    rakamlar = "0123456789"
    logaritma = ""
    degeri = ""
    liste = []

    for j in input:
        if j not in rakamlar:
            logaritma += j

        else:
            degeri += j

    liste.append(logaritma)
    liste.append(int(degeri))

    return liste


def parantez_ici_listele(a, b, liste):
    parantez_ici = liste[a+1:b]
    return parantez_ici


def parantez_ici_temizle(ilk, son, liste, sonuc1):
    for x in range(son-ilk+1):
        liste.pop(ilk)

    liste.insert(ilk, str(sonuc1))
    return liste


def kuvvet_alma(liste,parantez_var):
    kare = liste.index("^")
    sayi = liste[kare - 1]
    us = liste[kare + 1]
    sonuc = 1

    if float(sayi) < 0:
        if int(us) < 0:
            for x in range(int(us) * (-1)):
                sonuc *= float(sayi)

            sonuc = 1 / sonuc

        elif int(us) == 0:
            sonuc = 1

        else:
            for x in range(int(us)):
                sonuc *= float(sayi)

        if int(us) % 2 == 0 and parantez_var is True:
            sonuc *= -1

    elif float(sayi) == 0:
        if int(us) == 0:
            sonuc = "Tanımsız"
            liste.clear()
            liste.append(sonuc)
            return liste

        else:
            sonuc = 0
            liste.clear()
            liste.append(sonuc)

            return liste

    else:
        if int(us) < 0:
            for x in range(int(us) * (-1)):
                sonuc *= float(sayi)

            sonuc = 1 / sonuc
            liste.insert(liste.index(sayi), sonuc)

            for i in range(3):
                liste.pop(kare)

        elif int(us) == 0:
            sonuc = 1
            liste.clear()
            liste.append(sonuc)

            return liste

        elif int(us) > 0:
            for x in range(int(us)):
                sonuc *= float(sayi)

            liste.insert(liste.index(sayi), sonuc)

            for i in range(3):
                liste.pop(kare)

    return liste


def karekok_alma(liste):
    y = 1
    karekok_index = liste.index("#")
    x = int(liste[karekok_index + 1])

    for i in range(5):
        y = (x / y + y) / 2

    liste.insert(liste.index("#"), str(y))

    for k in range(2):
        liste.pop(karekok_index + 1)

    return liste


def trigonometri(liste):  # Trigonometrik listede verilen ifadenin sonucu hesaplayıp döner.
    sonuc = 0

    for x in liste:
        if x == "sin":
            derece = float(liste[liste.index("sin") + 1])
            radyan = math.radians(derece)
            sonuc = math.sin(radyan)
            break

        elif x == "cos":
            derece = float(liste[liste.index("cos") + 1])

            if derece == 90:
                sonuc = 0
                break

            else:
                radyan = math.radians(derece)
                sonuc = math.cos(radyan)
                break

        elif x == "tan":
            derece = float(liste[liste.index("tan") + 1])

            if derece == 90:
                sonuc = "Sonsuz"
                break
            else:
                radyan = math.radians(derece)
                sonuc = math.tan(radyan)
                break

        elif x == "cot":
            derece = float(liste[liste.index("cot") + 1])

            if derece == 0:
                sonuc = "Sonsuz"
                break

            elif derece == 90:
                sonuc = 0
                break

            else:
                radyan = math.radians(derece)
                sonuc = 1 / math.tan(radyan)
                break

    return sonuc


def logaritma(liste):  # Logaritmik listedeki ifadenin sonucunu hesaplayıp döner.
    deger = liste[liste.index("log") + 1]
    sonuc = math.log10(float(deger))

    return sonuc


def liste_duzenleyici(liste):  # Verilen listede işaret düzenlemelerini yapıp listeyi geri döner.(--'nin + olması gibi)
    if "-" == liste[0]:
        sayi = 0 - float(liste[1])

        for i in range(2):
            liste.pop(0)

        liste.insert(0, sayi)

    a = 0

    for i in liste:
        if a >= len(liste)-1:
            break

        if i == "^" and liste[a + 1] == "-":
            us_index = a

            if liste[us_index - 2] == "-":
                taban = float(liste[us_index - 1]) * (-1)

                liste.insert(us_index - 2, str(taban))

                for q in range(2):
                    liste.pop(us_index - 1)

                liste.insert(liste.index(str(taban)), "+")

            if "^" in liste:
                if liste[us_index + 1] == "-":
                    eksi_us = 0 - int(liste[us_index + 2])

                    liste.insert(us_index + 1, str(eksi_us))

                    for n in range(2):
                        liste.pop(us_index + 2)

        if i == "*" and liste[a + 1] == "-":
            carpim_index = a
            eksi_sayi = 0 - float(liste[carpim_index + 2])

            liste.insert(carpim_index + 1, str(eksi_sayi))

            for c in range(2):
                liste.pop(carpim_index + 2)

        if i == "/" and liste[a + 1] == "-":
            bolum_index = a
            negatif_sayi = 0 - float(liste[bolum_index + 2])

            liste.insert(bolum_index + 1, str(negatif_sayi))

            for b in range(2):
                liste.pop(bolum_index + 2)

        if i == "+" and liste[a + 1] == "-":
            toplam_index = a
            negatif_sayi2 = 0 - float(liste[toplam_index + 2])

            liste.insert(toplam_index + 1, str(negatif_sayi2))

            for m in range(2):
                liste.pop(toplam_index + 2)

        if i == "-" and liste[a + 1] == "-":
            fark_index = a
            pozitif_sayi = float(liste[fark_index+ 2]) * (-1)

            liste.insert(fark_index + 1, str(pozitif_sayi))

            for z in range(2):
                liste.pop(fark_index + 2)

        if sayi_mi(liste[a]) == True and sayi_mi(liste[a + 1]) == True:
            liste.insert(liste.index(liste[a + 1]), "+")

        else:
            a += 1

    return liste


def sayi_mi(s):  # Bu fonksiyon verilen parametrenin sayı olup olmadığını kontrol eder.
    try:
        float(s)
        return True

    except ValueError:
        return False


def islem_onceligi(liste, parantez):
    sonuc = ""

    while True:
        if len(liste) <= 1:
            break
        else:
            if "^" in liste:
                sonuc_listesi = kuvvet_alma(liste, parantez)
                sonuc = sonuc_listesi[0]

            elif "#" in liste:
                sonuc_listesi = karekok_alma(liste)
                sonuc = sonuc_listesi[0]

            elif "*" in liste:
               carp_index = liste.index("*")
               sonuc = float(liste[carp_index - 1]) * float(liste[carp_index + 1])

               for i in range(3):
                   liste.pop(carp_index - 1)

               liste.insert(carp_index - 1, str(sonuc))

            elif "/" in liste:
                bol_index = liste.index("/")
                sonuc = float(liste[bol_index - 1]) / float(liste[bol_index + 1])

                for i in range(3):
                   liste.pop(bol_index - 1)

                liste.insert(bol_index - 1, str(sonuc))

            elif "-" in liste:
                cikar_index = liste.index("-")
                sonuc = float(liste[cikar_index - 1]) - float(liste[cikar_index + 1])

                for i in range(3):
                    liste.pop(cikar_index - 1)

                liste.insert(cikar_index - 1, str(sonuc))

            elif "+" in liste:
                topla_index = liste.index("+")
                sonuc = float(liste[topla_index - 1]) + float(liste[topla_index + 1])

                for i in range(3):
                    liste.pop(topla_index - 1)

                liste.insert(topla_index - 1, str(sonuc))

    return sonuc


def girdi():
    islem = labelinput.get()
    sonuc.configure(text=str(islem))


def temizle():
    sonuc.configure(text="")
    labelinput.delete(0, "end")


window = tkinter.Tk()
window.title("Hesap Makinesi")
window.geometry("300x200")

label = tkinter.Label(window, text="İşlem:")
labelinput = tkinter.Entry(window)
button = tkinter.Button(window, text="Hesapla",command=hesap_makinesi)
button2 = tkinter.Button(window, text="Temizle", command=temizle)
sonuc = tkinter.Label(window, text="")

label.pack()
labelinput.pack(pady=10)
button.pack(padx=10)
button2.pack(pady=10)
sonuc.pack()

window.mainloop()
