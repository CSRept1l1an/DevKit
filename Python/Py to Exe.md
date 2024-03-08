# Convert Python `.py` to Executable `.exe` File and Customize Icon

## Introduction
This guide explains how to convert a Python script (`.py`) into an executable file (`.exe`) using `pyinstaller`. Additionally, it covers the process of customizing the icon of the generated executable.

### Prerequisites
- Python installed
- `pyinstaller` module installed (`pip install pyinstaller`)
- Icon file (`.ico`) for customization (optional)

## Step-by-Step Instructions

### Step 1: Convert `.py` to `.exe`

1. Open your command prompt or terminal.
2. Navigate to the directory containing your Python script.
   ```bash
   cd path/to/your/script
3. Run `pyinstaller` with the following command:
    ```bash
    pyinstaller --onefile your_script.py
4. Once pyinstaller finishes, locate the executable file in the dist directory.

### Step 2: Change the Icon of the Executable
1. Prepare an icon file (`.ico`) that you want to use.
2. Place the icon file in the same directory as your Python script.
3. Modify the `pyinstaller` command to include the `--icon` option:
   ```bash
   pyinstaller --onefile --icon=your_icon.ico your_script.py
4. Run the modified `pyinstaller` command.
5. The generated executable will now have the specified icon.
