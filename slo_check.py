import json

# V datoteki so zapisane funkcije, na podlagi katerih bo deloval program 'Slovenskega Spotla'
# Sprva skritega artista nastavim na 'Big Foot Mamo', kasneje ga bo naključno generirala funkcija
danasnji_artist = "Big Foot Mama"

# Zaenkrat črpam podatke iz testne .json datoteke
json_file = "test.json"

# funkcija naloži .json datoteko in vrne njeno vsebino
def nalozi_json(json_file):
    with open(json_file, "r", encoding='utf-8') as file:
        data = json.load(file)
    print(data)
    return data

# vsebina .json datoteke bo od zdaj naprej shranjena pod spremenljivko 'data'
data = nalozi_json(json_file)


# uporabnik skuša uganiti skritega glasbenika/skupino tistega dne, funkcija vrne True ali False
def preveri_osebo(oseba):
    if oseba == danasnji_artist:
        return True
    else:
        return False

# funkcija vrne seznam v katerem se nahajajo podatki 'danasnjega_artista'
def podatki_artista(danasnji_artist):
    dnevni_artist = []
    for atributi in data[danasnji_artist]:
        dnevni_artist.append(data[danasnji_artist][atributi])
    return dnevni_artist

# vrne seznam z atributi osebe
def napacna_oseba(oseba):
    podatki_osebe = []
    for atributi in  data[oseba]:
        podatki_osebe.append(data[oseba][atributi])
    return podatki_osebe

# vrne seznam, kjer so pari atributov 'danasnjega_artista' in napačno ugotovljene osebe (pride prav v naslednji funkciji),
# ko atribute med sabo primerjamo
def pari_atributov(oseba):
    pari = []
    for i, j in zip(podatki_artista(danasnji_artist), napacna_oseba(oseba)):
        pari.append((i, j))
    return pari

# funkcija v primeru, da je oseba, ki jo je uporabnik uganil napačna, preveri kateri podatki 
# osebe so podobni ali enaki podatkom 'danasnjega_artista' in vrne seznam, ki za vsak atribut posebej pove
# kako blizu je pravilnemu odgovoru

def primerjaj_atribute(oseba):
    seznam_blizu_dalec = []

    atributi = pari_atributov(oseba)
    album_art, album_oseba = atributi[0]
    spol_art, spol_oseba = atributi[1]
    zvrst_art, zvrst_oseba = atributi[2]
    clani_art, clani_oseba = atributi[3]

    if abs(album_art - album_oseba) <= 10:
        seznam_blizu_dalec.append("Letnica je blizu")
    if 10 < abs(album_art - album_oseba):
        seznam_blizu_dalec.append("Napačna letnica")
    if spol_art == spol_oseba:
        seznam_blizu_dalec.append("Enak spol")
    if spol_art != spol_oseba:
        seznam_blizu_dalec.append("Drugačen spol")
    if zvrst_art == zvrst_oseba:
        seznam_blizu_dalec.append("Enaka zvrst")
    if zvrst_art != zvrst_oseba:
        seznam_blizu_dalec.append("Drugačna zvrst")
    if clani_art == clani_oseba:
        seznam_blizu_dalec.append("Enako št članov")
    if clani_art != clani_oseba:
        seznam_blizu_dalec.append("Drugačno št članov")
    return seznam_blizu_dalec
