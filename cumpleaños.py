import pandas as pd
from datetime import datetime

# Ruta del archivo Excel
ruta_excel = r"C:\Users\rezts\Downloads\cumpleanios.xlsx"

# Cargar el archivo
df = pd.read_excel(ruta_excel)

# Convertir la columna Fecha a formato de fecha
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

# Obtener la fecha actual (mes y día)
hoy = datetime.now().strftime("%m-%d")

# Crear columna temporal para comparar
df['mm-dd'] = df['Fecha'].dt.strftime('%m-%d')

# Buscar cumpleaños de hoy
cumple_hoy = df[df['mm-dd'] == hoy]

if not cumple_hoy.empty:
    print("🎉 ¡Hoy hay cumpleaños! 🎂")
    for _, fila in cumple_hoy.iterrows():
        print(f"➡️ {fila['Nombre']} ({fila['Cargo']}) - {fila['Fecha'].strftime('%d/%m/%Y')}")
else:
    print("😔 Hoy no hay cumpleaños.")
