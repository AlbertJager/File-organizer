from pathlib import Path 
from collections.abc import Iterator
import argparse



extensions = {
    # Documents
    ".txt": "texts",
    ".pdf": "documents",
    ".doc": "documents",
    ".docx": "documents",

    # Images
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".gif": "images",
    ".webp": "images",

    # Videos
    ".mp4": "videos",
    ".mkv": "videos",
    ".avi": "videos",
    ".mov": "videos",

    # Audio
    ".mp3": "audio",
    ".wav": "audio",
    ".flac": "audio",

    # Spreadsheets
    ".csv": "spreadsheets",
    ".xls": "spreadsheets",
    ".xlsx": "spreadsheets",

    # Archives
    ".zip": "archives",
    ".rar": "archives",
    ".7z": "archives",
    ".tar": "archives",
    ".gz": "archives",

    # Code
    ".py": "code",
    ".js": "code",
    ".html": "code",
    ".css": "code",
}


def scan_directory(directory: Path) -> Iterator[Path]:
    '''Generator that scans the directory and return files, otherwise raises FileNotFoundError'''
    try:
        for file in directory.iterdir():
            if file.is_file():
                yield file
    except FileNotFoundError as e:
        print(f"The path '{e.filename}' is not found.")
    except NotADirectoryError as e:
        print(f"The path '{e.filename}' is not a directory.")
    

def categorize_file_by_extension(path: Path, file: Path) -> Path:
    '''Returns a category corresponding to the file'''
    if file.suffix in extensions:
        category = path / extensions[file.suffix.lower()]
    else:
        category = path / "other"
    category.mkdir(exist_ok=True)
    return category 


def move_into_category(file: Path, category: Path) -> None:
    '''Moves the file into the corresponding category'''
    file.move_into(category)
    print(f"File '{file.name}' was successfully moved into {category}")


def organize(path: Path) -> None:
    '''Organizes the directory by categorizing files by extension and moving them into folder'''
    total = 0
    for file in scan_directory(path):
        category = categorize_file_by_extension(path, file)

        move_into_category(file, category)
        total += 1

    print(f"\nTotal files moved: {total}\n")


def get_path() -> Path:
    parser = argparse.ArgumentParser(description="Organize files by their extensions.")
    parser.add_argument("path", help="Directory to organize")
    args = parser.parse_args()
    path = Path(args.path.strip())
    return path


if __name__ == "__main__":
    organize(get_path())
    
