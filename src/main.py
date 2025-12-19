#Main script
from utils.paths import DATA_DIR
from utils.user_pref import fetch_user_pref, get_user_pref, save_preferences
from utils.tax_calculator import calculate_ISR

def main():
    """Main script"""
    user_pref=fetch_user_pref()
    ISR = calculate_ISR(user_pref)
    print(f"{ISR:,.2f}")
    
if __name__ == "__main__":
    main()