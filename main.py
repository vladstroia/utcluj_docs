from docxtpl import DocxTemplate
import pandas as pd

df = pd.read_csv('tabel_materii.csv', dtype=str)
df.applymap(lambda x: x.strip() if isinstance(x, str) else x)


doc = DocxTemplate("template-fisa-disciplinei.docx")


def generateData(df):
    fisa = {}
    fisa["p1_2"] = df['facultate']
    fisa["p1_3"] = df['nume_catedra']
    fisa["p1_8"] = df['nrcrt']
    fisa["p2_1"] = df['nume_disciplina']
    fisa["p2_2"] = ""
    fisa["p2_3"] = ""
    fisa["p2_4"] = df['an']
    fisa["p2_5"] = df['sem']
    fisa["p2_6"] = df['examen']
    fisa["p2_7_a"] = df['categdisc']  # categorie formtiva
    fisa["p2_7_b"] = df['obligativ']  # optionalitate
    fisa["p3_1"] = df['numarore']  # numar ore pe saptamana
    if "CURS" in df:
        fisa["p3_2"] = df['CURS']  # curs
    else:
        fisa["p3_2"] = ""
    if "SEMINAR" in df:
        fisa["p3_3_a"] = df['SEMINAR']
    else:
        fisa["p3_3_a"] = ""
    if "LABORATOR" in df:
        fisa["p3_3_b"] = df['LABORATOR']
    else:
        fisa["p3_b"] = ""
    if "PROIECT" in df:
        fisa["p3_3_c"] = df['PROIECT']
    else:
        fisa["p3_3_c"] = ""

    fisa["p3_4"] = df['orestudindiv']  # numar de ore pe semenstru ?
    fisa["p3_5"] = ""
    fisa["p3_6_a"] = ""
    fisa["p3_6_b"] = ""
    fisa["p3_6_c"] = ""
    fisa["p3_7_a"] = ""
    fisa["p3_7_b"] = ""
    fisa["p3_7_c"] = ""
    fisa["p3_7_d"] = ""
    fisa["p3_7_e"] = ""
    fisa["p3_7_f"] = ""
    fisa["p3_8"] = ""
    fisa["p3_9"] = ""
    fisa["p3_10"] = ""

    return fisa


i = 0

# variabila asta zice la cate linii din tabel sa se uite python
# numarul de linii e mereu mai mare decat numarul de fise pe care le
# genereaza pt ca majoritatea disciplinelor au mai multe linii in tabel
nrLinii = 20
while i < nrLinii:
    materie = {}
    while True:
        # rand contine un rand din tabel
        rand = df.loc[[i]]
        for item in rand:
            # ne intereseaza daca suntem la coloana care ne zice
            # daca e vorba de nr de ore de curs, seminar, laborator, proiect
            if item == 'formapred':
                materie[rand['formapred'].values[0].strip()
                        ] = rand["numarore"].values[0]
            else:
                # daca suntem la o alta coloana, adaugam in dictionarul materie
                materie[item] = rand[item].values[0]
        if df['nrcrt'][i + 1] != df['nrcrt'][i]:
            break
        else:
            i += 1
    # acum avem un dictionar cu toate datele despre o materie
    print(materie)
    # generam fisierul docx
    doc.render(generateData(materie))
    # salvam fisierul docx
    doc.save(f"./files/curs_{materie['nrcrt'].replace('.','_')}.docx")

    i += 1
