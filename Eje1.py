# 1- Càlcul de la factura de consum de l’aigua

def calcul_factura(consum):
    preu: int = 6
    if consum >50 and consum < 200:
        for litre in range(50,consum):
            preu+=1*0.1
    else:
        for litre in range(200, consum):
            preu+=1*0.3
    return print("El teu consum es ", round(preu, 2), "€")

consum = int(input("Introdueix els teus llitres d'aigua consumits "))

calcul_factura(consum)