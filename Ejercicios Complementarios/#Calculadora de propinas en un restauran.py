#Calculadora de propinas en un restaurante

monto_inicial=float(input("Ingrese el monto de la cuenta:$"))
propina_10=float(monto_inicial*0.10)
print(f"Propina sugerida(10%):${propina_10:.2f}")
monto_total_10=monto_inicial+propina_10
print(f"Total a pagar(10%):${monto_total_10:.2f}")
propina_15=float(monto_inicial*0.15)
print(f"Propina sugerida(15%):${propina_15:.2f}")
monto_total_15=monto_inicial+propina_15
print(f"Total a pagar(15%):${monto_total_15:.2f}")
