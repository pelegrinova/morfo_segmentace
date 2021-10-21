import csv
import re


# načtení textu určeného k segmentaci
with open("něco.txt", encoding="UTF-8") as soubor:
    text_k_segmentaci = soubor.read().lower().replace("\n", " ").strip()

# načtení morfologického slovníku
with open("můj_slovník.csv", encoding="UTF-8") as soubor:
    obsah_slovniku = csv.reader(soubor, delimiter=";")
    slova_ze_slovniku = set()
    for polozka in obsah_slovniku:
        slova_ze_slovniku.add(polozka[0])


def uprava_textu(text):
    # odstranění interpunkce a znaků - a co mazání řádků ???
    znaky = [",", ".", "!", "?", "'", "\"", "<", ">", "-", "–", ":", ";", "„", "“", "=", "%", "&", "#", "@", "/", "\\", "+", "(", ")", "[", "]", "§"]

    for znak in znaky:
        text = text.replace(znak, "")

    # odstranění číslic
    text = re.sub(r"[0-9]+", "", text)

    # odstranění mezer
    text = re.sub(r"\s{2,}", " ", text)

    # rozdělení textu na slova
    text_na_slova = text.split(sep=" ")

    # substituce grafiky tak, aby odpovídala realizaci hlásek
    text_na_slova_foneticky = []
    for slovo in text_na_slova:  # pokud uniq slova, musí se tu přepsat ta proměnná text_na_slova_uniq
        slovo = slovo.replace("pouč", "po@uč")  # joojoo, tohle je prasárna a vím o tom; třeba vyřešit
        slovo = slovo.replace("nauč", "na@uč")
        slovo = slovo.replace("douč", "do@uč")
        slovo = slovo.replace("přeuč", "pře@uč")
        slovo = slovo.replace("přiuč", "při@uč")
        slovo = slovo.replace("vyuč", "vy@uč")
        slovo = slovo.replace("pouka", "po@uka")
        slovo = slovo.replace("pouká", "po@uká")
        slovo = slovo.replace("poukl", "po@ukl")
        slovo = slovo.replace("poulič", "po@ulič")
        slovo = slovo.replace("poum", "po@um")
        slovo = slovo.replace("poupr", "po@upr")
        slovo = slovo.replace("pouráž", "po@uráž")
        slovo = slovo.replace("pousm", "po@usm")
        slovo = slovo.replace("poust", "po@ust")
        slovo = slovo.replace("poute", "po@ute")
        slovo = slovo.replace("pouvaž", "po@uvaž")
        slovo = slovo.replace("pouzen", "po@uzen")
        slovo = slovo.replace("douč", "do@uč")
        slovo = slovo.replace("douprav", "do@uprav")
        slovo = slovo.replace("doužív", "do@užív")
        slovo = slovo.replace("douzov", "do@uzov")
        slovo = slovo.replace("doupřesn", "do@upřesn")
        slovo = slovo.replace("doudit", "do@udit")
        slovo = slovo.replace("doudí", "do@udí")
        slovo = slovo.replace("eufemism", "Efemism")
        slovo = slovo.replace("eufor", "Efor")
        slovo = slovo.replace("euro", "Ero")
        slovo = slovo.replace("eutan", "Etan")
        slovo = slovo.replace("farmaceut", "farmacEt")
        slovo = slovo.replace("feud", "fEd")
        slovo = slovo.replace("koloseu", "KolosE")
        slovo = slovo.replace("koreu", "korE")
        slovo = slovo.replace("leuk", "lEk")
        slovo = slovo.replace("linoleu", "linolE")
        slovo = slovo.replace("mauzoleu", "mauzolE")
        slovo = slovo.replace("muzeu", "muzE")
        slovo = slovo.replace("neutral", "nEtral")
        slovo = slovo.replace("neutrál", "nEtrál")
        slovo = slovo.replace("pneum", "pnEm")
        slovo = slovo.replace("pseudo", "psEdo")
        slovo = slovo.replace("terapeut", "terapEt")
        slovo = slovo.replace("eufon", "Efon")
        slovo = slovo.replace("eunuch", "Enuch")
        slovo = slovo.replace("eunuš", "Enuš")
        slovo = slovo.replace("zeugm", "zEgm")
        slovo = slovo.replace("jubileu", "jubilE")
        # části
        slovo = slovo.replace("ie", "ije")
        slovo = slovo.replace("ii", "iji")
        slovo = slovo.replace("ií", "ijí")
        slovo = slovo.replace("dě", "ďe")
        slovo = slovo.replace("tě", "ťe")
        slovo = slovo.replace("ně", "ňe")
        slovo = slovo.replace("mě", "MŇE")
        slovo = slovo.replace("ě", "JE")
        slovo = slovo.replace("x", "KS")
        slovo = slovo.replace("ch", "X")
        slovo = slovo.replace("q", "KW")
        slovo = slovo.replace("ou", "O")
        slovo = slovo.replace("au", "A")
        # odstranění "@"
        slovo = slovo.replace("@", "")
        text_na_slova_foneticky.append(slovo)

    text_na_slova_uniq_foneticky = set(text_na_slova_foneticky)

    text_na_slova_foneticky = " ".join(text_na_slova_foneticky)

    # výsledek uložím do souboru zvlášť
    ulozeni_substituovaneho_textu(text_na_slova_foneticky)

    return text_na_slova_foneticky, text_na_slova_uniq_foneticky


def ulozeni_substituovaneho_textu(text):
    # uložení "foneticky" upraveného textu
    with open("foneticky_přepsané_něco.txt", mode="w", encoding="UTF-8") as soubor:
        print(text, file=soubor)


def segmentace_manualni(slova):
    print(len(slova))  # vypíše počet slov, které je třeba nasegmentovat (obvykle neradostné číslo)

    # segmentace slova + vytváření slovníku
    with open("můj_slovník.csv", "a", encoding="UTF-8") as csvfile:
        vysledek_segmentace = csv.writer(csvfile, delimiter=';', lineterminator='\n')
        for polozka in slova:
            zpracovane = input(f"{polozka}: ")
            dvojice = (polozka, zpracovane)
            print(dvojice)
            if zpracovane == "šlus bus":
                break
            vysledek_segmentace.writerow(dvojice)


# takhle asi neee :D ale já nevíím jak :D
# spustím úpravu textu
text_k_segmentaci_substituovany, text_na_slova_uniq_foneticky = uprava_textu(text_k_segmentaci)

# porovnání slov k segmentaci se slovy ve slovníku (zda už některé z nich ve slovníku nejsou segmentované)
slova_k_segmentaci = text_na_slova_uniq_foneticky - slova_ze_slovniku

# spustím segmentování samotné (a rozšiřování slovníku, ale je tam chybaaa - anebo není? ověřit, jestli se to fakt zapisuje dobře do toho souboru)
segmentace_manualni(slova_k_segmentaci)
