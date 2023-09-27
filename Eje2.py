# 2- Màquina de venda de bitllets de metro

preus = "1-Bitllet senzill............2,20€ (1a zona)\n2-TCasual.................10,20€ (1a zona)\n3-TMes......................54,00€ (1a zona)\n4-TTrimestre..........145,30€ (1a zona)\n5-TJove...................105,00€ (1a zona)\n"

def seleccionar_bitllet():
    preu_final = 0.0
    seleccio_valida = False
    zona_valida = False
    print("Selecciona un titol\n")
    print(preus)
    while seleccio_valida == False:
        try:
            seleccio = int(input())
            if seleccio in range (1,6): 
                seleccio_valida = True
                match seleccio:
                    case 1: preu_final = 2.2
                    case 2: preu_final = 10.2
                    case 3: preu_final = 54.0
                    case 4: preu_final = 145.3
                    case 5: preu_final = 105.00
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
    return round(preu_final, 2)

def comprar_bitllet(preu: float): 
    print("El preu final és: ", preu, "€")
    diners_usuari = 0.0
    while diners_usuari < preu: 
        try:
            diners_usuari = float(input("Entra els diners\n"))
            if diners_usuari == preu:
                print("Carregant bitllet...\nGràcies per la teva compra!")
            elif diners_usuari < preu: 
                print("Falten {}€".format(round(diners_usuari-preu, 2)))
                preu -= diners_usuari
            else: 
                print("Carregant bitllet...\nGràcies per la teva compra!")
                print("Aqui tens el canvi {}".format(round(diners_usuari-preu, 2)))
        except ValueError: print("Entra una quantitat vàlida")  

comprar_bitllet(seleccionar_bitllet())
