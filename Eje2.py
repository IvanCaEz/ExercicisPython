# 2- Màquina de venda de bitllets de metro


def seleccionar_bitllet():
    preus = "1-Bitllet senzill............2,20€ (1a zona)\n2-TCasual.................11,35€ (1a zona)\n3-TUsual(TMes)......................20,00€ (1a zona)\n4-Targeta T-70/90 FM/FN general..........31,75€ (1a zona)\n5-TJove...................40,00€ (Totes les zones)\n"
    preu_final = 0.0
    seleccio_valida = False
    zona_valida = False
    print("\nSelecciona un titol\n")
    print(preus)
    while seleccio_valida == False:
        try:
            seleccio = int(input())
            if seleccio in range (1,6): 
                seleccio_valida = True
                match seleccio:
                    case 1: preu_final = 2.2
                    case 2: preu_final = 11,35
                    case 3: preu_final = 20.0
                    case 4: preu_final = 31.75
                    case 5: preu_final = 40.0
                if seleccio != 5:
                    while zona_valida == False:
                        try:
                            zones = int(input("Selecciona les zones: 1, 2 o 3\n"))
                            if zones in range (1,4):
                                zona_valida = True
                                print("Carregant plataforma de pagaments...")
                                match zones:
                                    case 2: preu_final *=1.35
                                    case 3: preu_final *=1.89   
                            else: 
                                print("Selecciona una zona vàlida")
                        except ValueError:
                                print("Selecciona una zona vàlida")
            else: 
                print("Selecciona un titol vàlid")
        except ValueError:
            print("Selecciona un titol vàlid")
    return round(preu_final, 2), seleccio

def comprar_bitllet(preu: float, seleccio: int): 
    bitllets = {1: "Bitllet senzill", 2: "TCasual", 3: "TUsual", 4:"Targeta T-70/90 FM/FN general", 5: "TJove"}
    print(f"El preu final de la {bitllets[seleccio]} és: {preu}€")
    diners_valids = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
    diners_usuari = 0.0
    while diners_usuari < preu: 
        try:
            diners = float(input("Entra els diners "))
            while diners not in diners_valids: 
                diners = float(input("Entra una quantitat vàlida "))
            else:
                diners_usuari += diners
                if diners_usuari == preu:
                    print("Carregant bitllet...\nGràcies per la teva compra!")
                elif diners_usuari < preu: 
                    print("Falten {}€".format(round(preu-diners_usuari, 2)))
                else: 
                    print("Carregant bitllet...\nGràcies per la teva compra!")
                    print("Aqui tens el canvi {}".format(round(abs(preu-diners_usuari), 2)))
        except ValueError: print("Entra una quantitat vàlida")  

def __init__():
    comprar = True
    while comprar:
        bitllet = seleccionar_bitllet()
        comprar_bitllet(bitllet[0], bitllet[1])
        if str(input("Vols continuar comprant? ")) != "si": 
            comprar = False
            print("Bon viatge!")
        else: comprar = True

__init__()