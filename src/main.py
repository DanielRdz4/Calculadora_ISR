#Main script
from pathlib import Path
from utils.paths import DATA_DIR
from utils.user_pref import fetch_user_pref, get_user_pref, save_preferences

def main():
    """Main script"""
    user_pref=fetch_user_pref()
    save_preferences(user_pref)
    
if __name__ == "__main__":
    main()