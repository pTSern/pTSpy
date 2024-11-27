@echo off
REM List of required libraries
set LIBS=requests numpy pandas pyinstaller minify-html

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b 1
)

REM Loop through each library and check if it is installed
for %%L in (%LIBS%) do (
    python -c "import %%~L" >nul 2>&1
    if %errorlevel% neq 0 (
        echo Installing missing library: %%L
        pip install %%L
    ) else (
        echo Library %%L is already installed.
    )
)

echo All libraries are installed.

python -m PyInstaller --onefile --name pTSpy pTSpy.py