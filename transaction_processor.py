# Importa la libreria pandas para analizar y manipular los datos
import pandas as pd
from main_functions import get_final_balance, get_max_transaction, credit_count, debit_count

try:
    # Lee el archivo 'Transacciones Bancarias' y procesa los datos como un dataframe en 'df'
    filename = 'Transacciones Bancarias.csv'
    df = pd.read_csv(filename)
    
    # Llama a las funciones que calculan el balance final, mayor transacción, conteo de creditos y conteo de debitos
    balance_final = round(get_final_balance(df), 2)
    mayor_transaccion = get_max_transaction(df)
    conteo_credito = credit_count(df)
    conteo_debito =  debit_count(df)

    # Título del reporte
    print("\nReporte de Transacciones\n---------------------------------------------")

    # Imprime la variable balance_final hallada anteriormente
    print(f"Balance Final: {balance_final}")

    # Imprime las filas de mayor_transaccion, pues puede que haya más de una transacción que contenga el monto máximo
    for _, row in mayor_transaccion.iterrows():
        print(f"Transacción de Mayor Monto: ID {row['id']} - {row['monto']}")

    # Imprime la variables conteo_credito y conteo_debito
    print(f"Conteo de Transacciones: Crédito: {conteo_credito} Débito: {conteo_debito}")

    # Mantiene abierto el terminal hasta que el usuario haya decidido terminar con la lectura del reporte
    input("\nPresionar Enter para salir...")

# Maneja el error cuando el archivo 'Transacciones Bancarias' no se encuentra en la carpeta
except FileNotFoundError:
    print("No se logró realizar la operación. Verificar que el archivo 'Transacciones Bancarias.csv' exista.")
