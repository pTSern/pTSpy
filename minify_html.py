
from utils import install_pkg, uid

install_pkg('minify_html')

import minify_html

def minify():
    fn = input('File Name: ')
    u = uid()
    try:
        with open(fn + '.html', "r") as f:
            html_data = f.read()
            minified = minify_html.minify(html_data, minify_js=True, remove_processing_instructions=True)
            op = fn + u + '.html'
            print(u)
            with open(op, 'w') as gf:
                gf.write(minified)
    except FileNotFoundError:
        print(f"Error: The file {fn}.html does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
