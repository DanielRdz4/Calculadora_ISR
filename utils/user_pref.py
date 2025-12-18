#Store user preferences

import json

filename = "user_pref.json"

def get_tax_regime(msg):
    """Safely obtains user's tax regime"""
    tax_regimes = {'R','S','A'}
    while True:
        tax_regime = input(msg).strip().upper()
        if tax_regime in tax_regimes:
            return tax_regime
        print("Respuesta inválida, intente de nuevo")

def get_monthly_income(msg:str) -> int:
    """Safetely converts user input form stringo to int"""
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Respuesta inválida, intente de nuevo")


def get_user_pref():
    """Stores user's preferences"""
    tax_regime= get_tax_regime("Régimen fiscal actual: R = RESICO, S= Sueldos y salarios, A = Actividades empresariales")
    monthly_income = int(input("Ingreso mensual (sin centavos): "))

    user_pref = {
        'tax_regime': tax_regime,
        'monthly_income': monthly_income
    }
    return user_pref
