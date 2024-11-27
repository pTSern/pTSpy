
from utils import remove_right_side

import base64
import time
import os

def clear_terminal():
    # Check the operating system
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix-like (Linux, macOS)
        os.system('clear')

def convert_base64_to_format(input_file: str, t):
    uid = str(time.time() * 1000)

    fnf = remove_right_side(input_file, '.') + '_' + uid + '_Out Put'

    if t == 0:
        with open(input_file, 'r') as file:
            base64_data = file.read().strip()
    else:
        base64_data = input_file

    if base64_data.startswith('data:'):
        header, data = base64_data.split(',', 1)
    else:
        raise ValueError("Input file must start with 'data:'")

    media_type = header.split(':')[1].split(';')[0]

    binary_data = base64.b64decode(data)

    if media_type.startswith('video/'):
        output_extension = media_type.split('/')[1]  # Get the file extension
        output_path = f"{fnf}.{output_extension}"
    elif media_type.startswith('image/'):
        output_extension = media_type.split('/')[1]  # Get the file extension
        output_path = f"{fnf}.{output_extension}"
    else:
        raise ValueError("Unsupported media type: {}".format(media_type))

    with open(output_path, 'wb') as fnf:
        fnf.write(binary_data)

    print(f"Converted {input_file} to {output_path}")

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

import mimetypes

def encode_file_to_base64(file_path):
    # Determine the MIME type based on the file extension
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        raise ValueError("Unsupported file type or cannot determine MIME type.")

    with open(file_path, "rb") as file:
        encoded_data = base64.b64encode(file.read()).decode('utf-8')

    data_uri = f"data:{mime_type};base64,{encoded_data}"

    output = remove_right_side(file_path, '.') + '.txt'

    with open(output, "w") as output:
        output.write(data_uri)

    print(f"Encoded data URI written to {output}")
    return data_uri

