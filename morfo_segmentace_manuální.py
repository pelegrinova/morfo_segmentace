import csv
import re

cisla = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "slouč"] #"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "slouč"

for cislo in cisla:

    # načtení textu určeného k segmentaci
    with open(f"stud_{cislo}.txt", encoding="UTF-8") as soubor:
        text = soubor.read().lower().replace("\n", " ").strip()
    
    # odstranění interpunkce a znaků - a co mazání řádků ???
    znaky = [",", ".", "!", "?", "'", "\"", "<", ">", "-", "–", ":", ";", "„", "“", "=", "%", "&", "#", "@", "/", "\\", "+", "(", ")", "[", "]", "§"]

    for znak in znaky:
        text = text.replace(znak, "")

    # odstranění číslic
    text = re.sub(r"[0-9]+", "", text)

    # odstranění (max 4) mezer po odstraněných znacích # --> while dvě mezery, replace :)
    text = re.sub(r"\s{2,}", " ", text)

    # rozdělení textu na slova; na unikátní slova
    text_na_slova = text.split(sep=" ") # když to nepůjde, ať si vyserou oko a upraví si to sami !!! UWAGA udělat z toho set
    #text_na_slova_uniq = set(text_na_slova)


    # "fonetický" přepis
    text_na_slova_foneticky = []
    for slovo in text_na_slova:
        slovo = slovo.replace("pouč", "po@uč")
        #slovo = slovo.replace("nauč", "na@uč")  
        #slovo = slovo.replace("douč", "do@uč")
        #slovo = slovo.replace("přeuč", "pře@uč")
        #slovo = slovo.replace("přiuč", "při@uč")
        #slovo = slovo.replace("vyuč", "vy@uč")
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
        #slovo = slovo.replace("ii", "iji")
        #slovo = slovo.replace("ií", "ijí")
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

    # uložení "foneticky" upraveného textu
    with open(f"foneticky_přepsaný_stud_{cislo}.txt", mode="w" ,encoding="UTF-8") as soubor:
        print(text_na_slova_foneticky, file=soubor)

    ##### tuhle část jenom pokud by někdo chtěl využít už ten můj morfo-slovník
    # načtení morfologického slovníku
    with open("můj_slovník.csv", encoding="UTF-8") as soubor:
        obsah_slovniku = csv.reader(soubor, delimiter=";")

        slova_ze_slovniku = set()
        for polozka in obsah_slovniku:
            slova_ze_slovniku.add(polozka[0])

    # porovnání slov k segmentaci se slovy ve slovníku (zda už některé z nich ve slovníku nejsou segmentované)
    slova_k_segmentaci = list(text_na_slova_uniq_foneticky - slova_ze_slovniku)
    print(len(slova_k_segmentaci))

    ##### konec části s porovnáváním mojeho slovníku

    # segmentace slova + vytváření slovníku
    with open("nový_slovník.csv", "a", encoding="UTF-8") as csvfile:  # nemám ale vyřešené, jak tohle budu přidávat do slovníku všeho
        vysledek_segmentace = csv.writer(csvfile, delimiter=';', lineterminator='\n')
        for polozka in slova_k_segmentaci:
            zpracovane = input(f"{polozka}: ")
            dvojice = (polozka, zpracovane)
            if zpracovane == "šlus bus":
                break
            vysledek_segmentace.writerow(dvojice)

