
def get_final_balance(df):
    # Calcula el balance final que es igual a la suma de los montos de credito menos la suma de los montos de debito
    sum_credit = df[df['tipo'] == 'Crédito']['monto'].sum()
    sum_debit = df[df['tipo'] == 'Débito']['monto'].sum()
    final_balance = sum_credit - sum_debit
    return final_balance
    
def get_max_transaction(df):
    # Halla la mayor monto de transacción. Con este dato, se halla si hay mas de una transaccion con el monto maximo
    max_amount = df['monto'].max()
    max_transaction = df[df["monto"] == max_amount]
    return max_transaction
    
def credit_count(df):
    # Cuenta todas las transacciones de tipo crédito
    credit_count = df[df['tipo'] == 'Crédito'].shape[0]
    return credit_count

def debit_count(df):
    # Cuenta todas las transacciones de tipo débito
    debit_count = df[df['tipo'] == 'Débito'].shape[0]
    return debit_count