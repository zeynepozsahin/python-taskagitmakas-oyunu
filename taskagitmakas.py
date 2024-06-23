import random
can = 3
puan =0
x=random.randint(0,2)

oyun = ["tas","kagit","makas"]

while(can!=0):
    x =random.randint(0,2)
    bilgisayarHamle = oyun[x]
    hamle = İnput("Tas, kagit,makas?\n")
    if(bilgisayarHamle == hamle):
        print("Berabere!")
    elif(hamle=="tas"):
        if(bilgisayarHamle == "kagit"):
               can-=1
               print("Kaybettiniz,", can, "caniniz kaldi!")
        else:
            puan += 10
            print("Tebrikler! 10 puan kazandınız!")
    elif(hamle == "kagit"):
        if(bilgisayarHamle == "makas"):
               can-=1
               print("Kaybettiniz,", can, "caniniz kaldi!")
        else:
            puan += 10
            print("Tebrikler! 10 puan kazandınız!")  
    elif(hamle == "makas"):
        if(bilgisayarHamle == "tas"):
               can-=1
               print("Kaybettiniz,", can, "caniniz kaldi!")
        else:
            puan += 10
            print("Tebrikler! 10 puan kazandınız!")  


print("Oyun Bitti!",puan, "puan kazandiniz!")

        

