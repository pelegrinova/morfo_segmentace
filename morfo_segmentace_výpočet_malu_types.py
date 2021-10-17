import csv
from decimal import Decimal
from collections import Counter
from locale import LC_NUMERIC
from locale import setlocale

## nastavení "lokality"
setlocale(LC_NUMERIC, "cs_CZ.UTF-8")


cisla = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "slouč"]

for cislo in cisla:

    ## načtení segmentovaného textu
    with open(f"vysledek_segmentace_stud_{cislo}.txt", encoding="UTF-8") as soubor:
        segmentovany_text = soubor.read().strip().split(sep=" ")

    # převod textu v tokens na text v types
    def token_to_types(text):
        text_types = []

        for slovo in text:
            if slovo not in text_types:
                text_types.append(slovo)

        return text_types

    segmentovany_text_types = token_to_types(segmentovany_text)

    ## přípravné výpočty
    # výpočet délky konstruktu v konstituentech
    delka_slov_v_morfech = []
    for slovo in segmentovany_text_types:
        delka_slova_v_morfech = slovo.count("-") + 1
        delka_slov_v_morfech.append(delka_slova_v_morfech)

    # výpočet délky konstruktu v subkonstituentech
    nesegmentovany_text = []
    for segmentovane_slovo in segmentovany_text_types:
        hole_slovo = segmentovane_slovo.replace("-", "")
        nesegmentovany_text.append(hole_slovo)

    delka_slov_ve_fonemech = []
    for slovo in nesegmentovany_text:
        delka_slova_ve_fonemech = len(slovo)
        delka_slov_ve_fonemech.append(delka_slova_ve_fonemech)

    # počítadlo frekvencí
    def pocitadlo(soubor):
        frekvence = Counter(soubor)
        return frekvence

    # počet x-konstituentových konstruktů
    frekvence_morfu = pocitadlo(delka_slov_v_morfech)

    # slovník: klíč = x-konstituentový konstrukt, hodnota = součet délek všech takových konstruktů (dvou-morfémové slovo, součet délek všech dvou-morfémových slov)
    soucty_delek_x_morfovych_slov = {}
    for i, klic in enumerate(delka_slov_v_morfech):
        if klic not in soucty_delek_x_morfovych_slov:
            soucty_delek_x_morfovych_slov[klic] = 0
        soucty_delek_x_morfovych_slov[klic] += delka_slov_ve_fonemech[i]

    print(soucty_delek_x_morfovych_slov)

    # slovník: klíč = x-konstituentový konstrukt, hodnota = (součet délek všech takových konstruktů, počet takových konstuktů)
    slovnik_data_pro_mal = {}
    for klic in soucty_delek_x_morfovych_slov:
        slovnik_data_pro_mal[klic] = (soucty_delek_x_morfovych_slov[klic], frekvence_morfu[klic])

    print(dict(sorted(slovnik_data_pro_mal.items()))) # seřazený slovník podle klíčů, pozor na seřazování slovníku - ošemetné, pro zobrazení či tahání infa ale stačí

    ## funkce s výpočtem MALu
    def vypocet_mal(data):
        vysledek = []
        for klic in sorted(data): # tahá ze seřazeného seznamu klíčů, ale nic nepřepisuje !
            if klic == 0:
                pass
            else:
                prumer = round(Decimal(str(data[klic][0] / (data[klic][1] * klic))), 2)
                mezivysledek_carka = (klic, data[klic][1], f"{prumer:n}") # to f"..." dělám proto, aby se převedly korektně desetinné tečky na desetinné čárky
                vysledek.append(mezivysledek_carka)
        return vysledek

    vysledek_data = vypocet_mal(slovnik_data_pro_mal)
    print(vysledek_data)
    print(segmentovany_text_types)

    # uložení výsledků do tabulky
    with open(f"data_S_M_F_types_stud_{cislo}.csv", "x", encoding="UTF-8") as csvfile:
        vysledek_mal = csv.writer(csvfile, delimiter=';', lineterminator='\n')
        vysledek_mal.writerow(["construct", "frq", "mean of constituent"])
        for i in vysledek_data:
            vysledek_mal.writerow([i[0], i[1], i[2]])
