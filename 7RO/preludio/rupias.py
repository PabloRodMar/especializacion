import datetime

def calcRupias(dolares):
    rupias_300 = 0
    rupias_100 = 0
    rupias_50 = 0
    rupias_20 = 0
    rupias_5 = 0
    rupias_1 = 0
    while (dolares > 0):
        if dolares >= 300:
            rupias_300 += 1
            dolares -= 300
        elif dolares >= 100:
            rupias_100 += 1
            dolares -= 100
        elif dolares >= 50:
            rupias_50 += 1
            dolares -= 50
        elif dolares >= 20:
            rupias_20 += 1
            dolares -= 20
        elif dolares >= 5:
            rupias_5 += 1
            dolares -= 5
        elif dolares >= 1:
            rupias_1 += 1
            dolares -= dolares
        
    return rupias_300, rupias_100, rupias_50, rupias_20, rupias_5, rupias_1


##################################
nombre = input("¡Bienvenido a Hyrule, viajero! ¿Cómo te llamas?:\n")
fecha = datetime.date.today()
hora = datetime.datetime.now().strftime("%H:%M")
bienvenida = f"Bienvenido a las tierras sagradas de Hyrule, {nombre}. \nHoy es el día {fecha} del calendario hyliano, con hora local {hora}"
print(bienvenida)
##################################

##################################
dolares = float(input("Al igual que en tu mundo, en Hyrule todo funciona con dinero.\nAquí usamos rupias, pero aceptamos todo tipo de" \
" divisa.\nHe oído que usaís algo llamado dólares en vuestro mundo, ¿puedes decirme cuántos tienes?: "))
total_rupias = calcRupias(int(dolares * 10))
##################################

##################################
print(f"¡Listo! Tu total es de \n\n{total_rupias[0]} rupias doradas (300), {total_rupias[1]} rupias plateadas (100),\n{total_rupias[2]} rupias moradas (50), {total_rupias[3]} rupias rojas (20),\n{total_rupias[4]} rupias azules (5) y {total_rupias[5]} rupias rojas (1)\n")
print("Mucha suerte en tus aventuras y que la fuerza te acompañe, o algo asi")
##################################