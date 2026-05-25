#Presupuestos Hospital

Presupuesto = float(input("Ingrese el Presupuesto del hospital: "))

Presupuesto_Urgencias = Presupuesto * 0.37
Presupuesto_Pediatria = Presupuesto * 0.42
Presupuesto_Traumatologia = Presupuesto * 0.21

print("El presupuesto de las diferentes areas del hospital: ")
print("Presupuesto Area Urgencias: $",Presupuesto_Urgencias, "(37%)")
print("Presupuesto Area Pediatria: $",Presupuesto_Pediatria, "(42%)")
print("Presupuesto Area Traumatologia: $",Presupuesto_Traumatologia, "(21 %)")