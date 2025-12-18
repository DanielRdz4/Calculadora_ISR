#Main script
from pathlib import Path
from utils.paths import DATA_DIR
from utils.user_pref import get_user_pref, save_preferences

def data_dir_exists():
    """Ensures local 'data' directory existence"""
    DATA_DIR.mkdir(parents=True ,exist_ok=True)

def main():
    """Main script"""
    data_dir_exists()
    user_preferences = get_user_pref()
    save_preferences(user_preferences)
    
    
if __name__ == "__main__":
    main()