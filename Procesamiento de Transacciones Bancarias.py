# Importa la libreria pandas para analizar y manipular los datos
import pandas as pd

# Lee el archivo CSV "Transacciones Bancarias"
df = pd.read_csv("Transacciones Bancarias.csv")

# Calcula el balance final restando la suma del monto de los dataframe tipo crédito y la suma del monto de los dataframe tipo débito
balance_final = df[df['tipo'] == 'Crédito']['monto'].sum() - df[df['tipo'] == 'Débito']['monto'].sum()
# Halla el monto máximo
mayor_monto = df['monto'].max()
# Almacena en un dataframe los montos que sean iguales que el mayor monto
mayor_transaccion = df[df["monto"] == mayor_monto]
# Cuenta el número de transacciones de tipo Crédito y Débito
conteo_credito = df[df['tipo'] == 'Crédito'].shape[0]
conteo_debito = df[df['tipo'] == 'Débito'].shape[0]

# Título del reporte
print("Reporte de Transacciones\n---------------------------------------------")
# Imprime la variable balance_final hallada anteriormente
print(f"Balance Final: {balance_final}")
# Imprime las filas de mayor_transaccion, pues puede que haya más de una transacción que contenga el monto máximo
for _, row in mayor_transaccion.iterrows():
    print(f"Transacción de Mayor Monto: ID {row['id']} - {row['monto']}")
# Imprime la variables conteo_credito y conteo_debito
print(f"Conteo de Transacciones: Crédito: {conteo_credito} Débito: {conteo_debito}")

# Mantiene abierto el terminal hasta que el usuario haya decidido terminar con la lectura del reporte
input("\nPresionar Enter para salir...")