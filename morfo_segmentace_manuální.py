import csv

DICTIONARY_FILE = "můj_slovník.csv"
INPUT_FILE = "foneticky_přepsané_něco.txt"


def segmentace_manualni(slova):
    print(len(slova))  # vypíše počet slov, které je třeba nasegmentovat (obvykle neradostné číslo)

    # segmentace slova + vytváření slovníku
    with open(DICTIONARY_FILE, "a", encoding="UTF-8") as csvfile:
        vysledek_segmentace = csv.writer(csvfile, delimiter=';', lineterminator='\n')
        for polozka in slova:
            zpracovane = input(f"{polozka}: ")
            dvojice = (polozka, zpracovane)
            print(dvojice)
            if zpracovane == "šlus bus":
                break
            vysledek_segmentace.writerow(dvojice)


# načtení textu určeného k segmentaci
with open(INPUT_FILE, encoding="UTF-8") as soubor:
    text_k_segmentaci_substituovany = soubor.read().rstrip().split(sep=" ")

# načtení morfologického slovníku
with open(DICTIONARY_FILE, encoding="UTF-8") as soubor:
    obsah_slovniku = csv.reader(soubor, delimiter=";")
    slova_ze_slovniku = set()
    for polozka in obsah_slovniku:
        slova_ze_slovniku.add(polozka[0])

# takhle asi neee :D ale já nevíím jak :D
# spustím úpravu textu
text_na_slova_uniq_foneticky = set(text_k_segmentaci_substituovany)

# porovnání slov k segmentaci se slovy ve slovníku (zda už některé z nich ve slovníku nejsou segmentované)
slova_k_segmentaci = text_na_slova_uniq_foneticky - slova_ze_slovniku

# spustím segmentování samotné (a rozšiřování slovníku, ale je tam chybaaa - anebo není? ověřit, jestli se to fakt zapisuje dobře do toho souboru)
segmentace_manualni(slova_k_segmentaci)
