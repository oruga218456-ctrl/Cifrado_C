import os,sys,time

def Limpiar_pantalla(): os.system('cls')
def T(tiempo: float): time.sleep(tiempo)

def escribir(texto="", velocidad=0.05):
    
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        T(velocidad)
    print()
        
def M(titulo=""): escribir(f'===== {titulo.upper()} =====')

def S(salto: int):
    
    for i in range(salto):
        print()