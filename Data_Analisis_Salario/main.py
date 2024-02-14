import json
import pandas as pd
from datetime import datetime

# Función  salario
def subida_salario(emp):
    salario = float(emp['salary'].replace('$', '').replace(',', ''))
    if emp.get('age', 0) < 30:
        salario *= 1.1
    return f"{salario:.2f}€"

# Cargar el JSON
with open('employees.json') as f:
    data = json.load(f)

#  empleados no 'GRONK'
data = [emp for emp in data if emp.get('proyect') != 'GRONK']


for emp in data:
    emp['salary'] = subida_salario(emp)

df = pd.DataFrame(data)

# Generar Excel
current_date = datetime.now()
file_name = f"pagos-empleados-{current_date.month}-{current_date.year}.xlsx"


df.to_excel(file_name, index=False)

print(f"Archivo Excel '{file_name}' generado correctamente.")
