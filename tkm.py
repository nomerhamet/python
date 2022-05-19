import random

while True:
    secenekler =["tas","kagit","makas"]

    bilgisayar = random.choice(secenekler)
    oyuncu = None # tas kagit makas harici kabul etmez

    while oyuncu not in secenekler:
        oyuncu = input("tas , kagit ya da makas ?: ").lower()

    if oyuncu == bilgisayar:
        print("bilgisayar: ",bilgisayar)
        print("oyuncu: ", oyuncu)
        print("Berabere!")
    elif oyuncu == "tas" :
        if bilgisayar == "kagit":
            print("bilgisayar: ",bilgisayar)
            print("oyuncu: ", oyuncu)
            print("Kaybettin!")
        if bilgisayar == "makas":
            print("bilgisayar: ",bilgisayar)
            print("oyuncu: ", oyuncu)
            print("Kazandin!")
    elif oyuncu == "makas" :
        if bilgisayar == "tas":
            print("bilgisayar: ",bilgisayar)
            print("oyuncu: ", oyuncu)
            print("Kaybettin!")
        if bilgisayar == "kagit":
            print("bilgisayar: ",bilgisayar)
            print("oyuncu: ", oyuncu)
            print("Kazandin!")        
    elif oyuncu == "kagit" :
        if bilgisayar == "tas":
            print("bilgisayar: ",bilgisayar)
            print("oyuncu: ", oyuncu)
            print("Kaybettin!")
        if bilgisayar == "makas":
            print("bilgisayar: ",bilgisayar)
            print("oyuncu: ", oyuncu)
            print("Kazandin!")                
    tekrar_oyna = input("Tekrar oyna? (E/H): ").lower()

    if tekrar_oyna != "e" :
        break
    
print("Bye!")