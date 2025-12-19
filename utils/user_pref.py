#User preferences management functions
import json
from pathlib import Path
from utils.paths import DATA_DIR
filename = "user_data.json"
user_pref_path = DATA_DIR / filename
UMA = 41_273.52
UMA_limit = 5 * UMA


def get_tax_regime(msg):
    """Safely obtains user's tax regime"""
    tax_regimes = {'R','S','A'}
    while True:
        tax_regime = input(msg).strip().upper()
        if tax_regime in tax_regimes:
            return tax_regime
        print("Respuesta inválida, intente de nuevo")

def get_float(msg:str) -> float:
    """Safetely converts user input form stringo to int"""
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Respuesta inválida, intente de nuevo")

def get_deductions(monthly_income,msg: str) -> float:
    """Ensures that total deductions are coherent with income"""

    while True:
        try:
             deductions = float(input(msg))

             if deductions > monthly_income:
                 print("Las deducciones no pueden superar los ingresos, intente de nuevo")
             elif deductions > UMA_limit:
                 print(
                     f"Las deducciones no pueden superar 5 UMAS: ({UMA_limit:,.2f}), intente de nuevo"
                 )
             else:
                return deductions
        
        except ValueError:
            print("Respuesta inválida, intente de nuevo")
    
def get_user_pref():
    """Stores user's preferences"""

    
    tax_regime= get_tax_regime("Régimen fiscal actual |R = RESICO, S= Sueldos y salarios, A = Actividades empresariales|: ")
    user_pref = {
            'tax_regime': tax_regime,
            'monthly_income': 0.0,
            'deductions': 0.0,
            }
    user_pref["monthly_income"]=get_float("Ingreso total mensual (MXN): ")

    if tax_regime != 'R':
        user_pref["deductions"] = get_deductions(user_pref["monthly_income"],"Deducciones totales del mes (MXN): ")


    save_preferences(user_pref)
    return user_pref

def save_preferences(user_pref):
    """Makes json file with user preferences"""

    DATA_DIR.mkdir(parents=True ,exist_ok=True) #Ensures that local 'data' dir exists
    with user_pref_path.open("w", encoding="utf-8") as f:
        json.dump(user_pref, f, indent= 4)

def load_preferences():
    """Loads user preferences for accesing data"""
    with user_pref_path.open("r",encoding="utf-8") as f:
        return json.load(f)

def fetch_user_pref():
    """Looks for existing user preferences"""
    if user_pref_path.is_file():
       
        while True:
            keep_delete = input("¿Desea utulizar las preferencias existentes? (S/N): ").strip().upper()
            if keep_delete == 'S':
                return load_preferences()

            elif keep_delete == 'N':
                user_pref_path.unlink()
                user_pref=get_user_pref()
                return user_pref
            
            else:
                print("Valor inválido, intente de nuevo")

    #If the file does not exist
    return get_user_pref()
