class Egyauto:
    def __init__(self, sor: str):
        adatok = sor.strip().split(" ")
        self.nap = int(adatok[0])
        self.idopontok = adatok[1]
        self.rendszam = adatok[2]
        self.dolgozo = int(adatok[3])
        self.km= int(adatok[4])
        self.kibe= int(adatok[5])

autok = []

def beolvas(fajlnev: str):
    with open(fajlnev,"r", encoding='utf-8' ) as f:
        for sor in f:
            autok.append(Egyauto(sor))
    f.close
    print("A file beolvasása kész!")

def utoljara():
    for i in range(len(autok)-1,0, -1):
        if autok[i].kibe == 0:
            print(autok[i].nap,". nap rendszám:",autok[i].rendszam)
            break
        
def adott_nap_kibe(keresett: int):   
    print(f"Forgalom a(z) {keresett}. napon")
    for i in range(0,len(autok)):
        if autok[i].nap == keresett:
            if autok[i].kibe == 0:
                 print(f"{autok[i].nap} {autok[i].rendszam} {autok[i].dolgozo} ki")
            if autok[i].kibe == 1:
                 print(f"{autok[i].nap} {autok[i].rendszam} {autok[i].dolgozo} be")

def utolso_nap_kint():
    utolso = []
    for i in range(0,len(autok)):
        if autok[i].kibe == 0:
           utolso.append(autok[i].rendszam) 
        if autok[i].kibe == 1:
           utolso.remove(autok[i].rendszam) 
    print(f"A hónap végén {len(utolso)} autót nem hoztak vissza! Melyek:")
    print(utolso)

rendszamok = []
def km():
    for i in autok:
        if i.rendszam not in rendszamok:
            rendszamok.append(i.rendszam)
    rendszamok.sort()
    #print(rendszamok)
    
    for rsz in rendszamok:
        megtett_km =[]
        for i in autok:
            if i.rendszam==rsz:
                megtett_km.append(i.km)
        kezdo_km=megtett_km[0]
        zaro_km=megtett_km[len(megtett_km)-1]
        megtettkmek=zaro_km-kezdo_km
        print(f"{rsz} {megtettkmek} km")

def szemely_max():
    k_km =0
    megtett_km =0
    leghosszabb_ut =0
    for rsz in rendszamok:
        for i in autok:
            if i.rendszam==rsz:
                if i.kibe==0:
                    k_km=i.km
                if i.kibe ==1:
                    megtett_km=i.km-k_km
                    if megtett_km>leghosszabb_ut:
                        leghosszabb_ut=megtett_km
                        keresett_dolgozo=i.dolgozo
                        keresett_auto=i.rendszam   

    print(f'Leghosszabb ut: {leghosszabb_ut} km, dolgozó: {keresett_dolgozo}, rendszám: {keresett_auto}')

def menetlevel(rszam: str):
    kiir=''
    for i in autok:
        if i.rendszam==rszam:
            if i.kibe==0:
               kiir+=f'{i.dolgozo}\t{i.nap}. {i.idopontok}\t{i.km} km \t'
            if i.kibe==1:
               kiir+=f'{i.nap}. {i.idopontok}\t{i.km} km\n'
    print(kiir)
    with open(f"{rszam}_menetlevel.txt", "w", encoding="utf-8") as w:  
            w.write(kiir)

beolvas("autok.txt")
utoljara()
keresettnap=int(input("Adjon meg egy napot: "))
adott_nap_kibe(keresettnap)
utolso_nap_kint()
km()
szemely_max()
keresett_rendszam="CEG304"
menetlevel(keresett_rendszam)