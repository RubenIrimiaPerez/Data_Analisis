import json
import pandas as pd
from datetime import datetime

# Función para convertir el salario de dólares a euros y aplicar el aumento del 10% para empleados menores de 30 años
def subida_salario(emp):
    salario = float(emp['salary'].replace('$', '').replace(',', ''))
    if emp.get('age', 0) < 30:
        salario *= 1.1
    return f"{salario:.2f}€"

# Cargar el JSON desde el archivo
with open('employees.json') as f:
    data = json.load(f)

# Filtrar empleados que no son del proyecto 'GRONK'
data = [emp for emp in data if emp.get('proyect') != 'GRONK']

# Modificar el salario y agregar el símbolo de euro
for emp in data:
    emp['salary'] = subida_salario(emp)

# Crear un DataFrame con los datos y modificarlos
df = pd.DataFrame(data)

# Generar el nombre del archivo Excel con el formato deseado
current_date = datetime.now()
file_name = f"pagos-empleados-{current_date.month}-{current_date.year}.xlsx"

# Guardar el DataFrame en un archivo Excel
df.to_excel(file_name, index=False)

print(f"Archivo Excel '{file_name}' generado correctamente.")
