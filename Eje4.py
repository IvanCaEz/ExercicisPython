# 4- Proporció àuria

def fibo(elements: int):
    num_anterior = 0
    next_num = 1
    help_num = 0
    contador = 1
    
    while contador <= elements:
        help_num = next_num
        next_num = num_anterior+next_num
        num_anterior = help_num
        print(num_anterior)
        contador+=1
        

def fibo_recursive(elements: int) -> int:
    if elements in (1,2):
        return 1
    else: 
        return fibo_recursive(elements-1) + fibo_recursive(elements-2)
    
    
def __init__():
    elements = int(input("Quants elements vols la seqüència? "))
    # fibo(elements)
    print(fibo_recursive(elements))


__init__()

