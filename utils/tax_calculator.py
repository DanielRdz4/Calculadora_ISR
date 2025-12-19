#Script that calculates the ISR for the given user data

# R= RESICO, S= Sueldos y salarios, A = Actividades empresariales
from utils.tax_rates import SA_rates, RESICO_rates

def calculate_tax_SA(income, deductions):
    """Calculates tax rate for ASALARIADOS and Act. Empresarial"""
    for inf, sup, base, rate in SA_rates:
        if inf <= income <= sup:
            difference = income - inf
            gross_ISR = base + difference * rate / 100
            ISR = gross_ISR - deductions
            print(f"{inf},{sup},{base},{rate}")
            return ISR
        
def calculate_tax_R(income):
    for inf, sup, rate in RESICO_rates:
        if inf <= income <= sup:
            ISR = income * rate / 100
            return ISR

def calculate_ISR(user_pref):
    """Calculates ISR"""
    regime = user_pref["tax_regime"]
    income = user_pref["monthly_income"]
    deductions = user_pref["deductions"]

    if regime == 'R':
        return calculate_tax_R(income)
    
    return calculate_tax_SA(income, deductions)