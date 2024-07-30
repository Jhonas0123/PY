# Si tenemos un total de 3940 de estamina, y la estamina por ronda cuesta 14 es estamina, 
# cuanto de estamina gastamos en 50 rondas y con cuanto de estamina nos quedamos restando
# al total 

total = 3940
estamina_gastada = []
def gasto(estamina, rondas):
    gasto_total = estamina * rondas
    return gasto_total

gasto_total = gasto(14,50)

print(f"total de estamina gastada es {gasto_total} y
el monto restado menos la estamina gastada es {total - gasto_total}")
    
    
    
    



