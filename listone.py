#listone idea matteo prendi da web il listone o excel ed estrae random per reparto

import random
import pandas as pd
def estrattore(listone):
    random.seed()
    scelto=random.choices(listone['Nome'] +' '+ listone['Ruolo'])
    print(scelto)
file_path=r'C:\Users\Utente\Desktop\Quotazioni_Fantacalcio_Stagione_2023_24.xlsx'
listone=pd.read_excel(file_path)
estrattore(listone)