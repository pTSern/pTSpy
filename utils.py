
import math
import os
import datetime
import time
import sys
import subprocess

import markdown
from pygments.formatters import HtmlFormatter
from pathlib import Path

AL = '─'
SL = f"{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}"
LL = f"{SL}{SL}"
ST = '✦'

def clear_terminal():
    # Check the operating system

    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix-like (Linux, macOS)
        os.system('clear')

def is_pkg_ist(pn):
    try:
        __import__(pn)
        return True
    except ImportError:
        return False

def install_pkg(pn):
    if not is_pkg_ist(pn):
        print(f'Installing ' + pn + ' lib by pip ...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pn])

def uid():
    return str(math.floor( time.time() * 1000 ))

def remove_right_side(input_string, key):
    return input_string.split(key)[0]

def today():
    now = datetime.datetime.now()

    week = now.strftime("%A")
    moth = now.strftime("%B")
    day = now.strftime("%d")
    year = now.strftime("%Y")

    return f"{day}_{week}_{moth}_{year}"

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def read_input(min_val, max_val, msg):
    try:
        data = float(input(msg))  # Change to int(input(msg)) if you want integers only
    except ValueError:
        clear_terminal()
        print("Invalid input. Please enter a number.")
        return read_input(min_val, max_val, msg)

    if data > max_val or data < min_val:
        clear_terminal()
        print(f"Input must be between {min_val} and {max_val}. Please try again.")
        return read_input(min_val, max_val, msg)

    return data

def no_null_input(msg):
    data = input(msg)

    if len(data) <= 0:
        print(f"Can not leave this to be blank!!. Please try again")
        return no_null_input(msg)

    return data

def selection_input(lists, msg, upcase = True):
    fnl = list(map(str.upper, lists)) if upcase else lists
    data = input(msg)
    fnd = data.upper() if upcase else data

    if fnd not in fnl:
        print(f"{fnd} is not a valid selection, which are {fnl}. Please try again.")
        return selection_input(fnl, msg, False)

    return fnd

def md_to_html(input_file: str, output_file: str, remove_root = False):
    # Read the Markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(
        md_content, 
        extensions=['fenced_code', 'codehilite', 'tables', 'toc']
    )
    
    # Add custom CSS for beautification
    style = """
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; background: #f9f9f9; color: #333; }
        h1, h2, h3 { color: #007acc; }
        code { background: #f4f4f4; padding: 2px 4px; border-radius: 3px; }
        pre { background: #272822; color: #f8f8f2; padding: 10px; border-radius: 5px; overflow-x: auto; }
        pre code { color: inherit; background: none; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background: #f4f4f4; }
        a { color: #007acc; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .toc { margin-bottom: 20px; padding: 10px; background: #eef; border-radius: 5px; }
    </style>
    """
    
    # Include pygments style for syntax highlighting
    pygments_style = HtmlFormatter().get_style_defs('.codehilite')

    # Create the final HTML
    final_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Markdown to HTML</title>
        <style>{pygments_style}</style>
        {style}
    </head>
    <body>
        <div class="content">
            {html_content}
        </div>
    </body>
    </html>
    """

    # Write the HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
        if remove_root and os.path.exists(input_file):
            os.remove(input_file)

def short_str(msg, length = 10):
    return msg[:length].replace(' ', '_')
