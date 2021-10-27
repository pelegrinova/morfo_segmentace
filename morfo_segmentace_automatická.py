import csv

DICTIONARY_FILE = "můj_slovník.csv"
INPUT_FILE = "foneticky_přepsaný_stud.txt"
OUTPUT_FILE = "vysledek_segmentace_stud.txt"

# načtení morfologického slovníku jako slovníku (haha)
with open(DICTIONARY_FILE, encoding="UTF-8") as soubor:
    obsah_slovniku = csv.reader(soubor, delimiter=";")

    slovnik = {}
    for polozka in obsah_slovniku:
        slovnik[polozka[0]] = polozka[1]

# načtení textu/slov k segmentaci (a odstranění případné mezery na konci)
with open(INPUT_FILE, encoding="UTF-8") as soubor:
    slova_k_segmentaci = soubor.read().strip().split(sep=" ")

# autosegmentace
segmented_words = []
for original_word in slova_k_segmentaci:
    try:
        segmented_word = slovnik[original_word]
    except KeyError:
      print(
            f"POZOR! SLOVO {original_word} CHYBÍ VE SLOVNÍKU A TUDÍŽ"
            "NEBUDE SEGMENTOVÁNO!"
        )
        segmented_word = original_word
    segmented_words.append(segmented_word)
 
text_segmentovany_slouceny = " ".join(segmented_words)

# uložení výsledku segmentace do souboru
with open(OUTPUT_FILE, mode="x", encoding="UTF-8") as soubor:
    print(text_segmentovany_slouceny, file=soubor)
