#Main script
from pathlib import Path

def data_dir_exists():
    """Ensures local dir 'data' existence"""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

def main():
    data_dir_exists()
    

if __name__ == "__main__":
    main()