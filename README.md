# File Organizer

A simple Python CLI application that organizes files in a directory by their file extensions. It automatically creates category folders and moves files into the appropriate folder.

## Features

* Scans a specified directory
* Categorizes files by extension
* Automatically creates category folders
* Moves files into their corresponding categories
* Places unknown or extensionless files into `other/`
* Supports command-line usage with `argparse`
* Uses `pathlib` for filesystem operations

## Requirements

* Python 3.14+

The project uses only Python's standard library, so no external packages are required.

## Usage

Run the program from the terminal:

```bash
python organizer.py "C:\Users\user\Desktop\files"
```

To see the available command-line options:

```bash
python organizer.py --help
```

## Example

### Before

```text
files/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── script.py
└── unknown.xyz
```

### After

```text
files/
├── images/
│   └── photo.jpg
├── documents/
│   └── resume.pdf
├── audio/
│   └── song.mp3
├── code/
│   └── script.py
└── other/
    └── unknown.xyz
```

## Supported Categories

* **Documents:** `.txt`, `.pdf`, `.doc`, `.docx`
* **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
* **Videos:** `.mp4`, `.mkv`, `.avi`, `.mov`
* **Audio:** `.mp3`, `.wav`, `.flac`
* **Spreadsheets:** `.csv`, `.xls`, `.xlsx`
* **Archives:** `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
* **Code:** `.py`, `.js`, `.html`, `.css`
* **Other:** unknown or extensionless files

## Technologies

* Python
* `pathlib`
* `argparse`
* Generators
* Type hints
* Exception handling