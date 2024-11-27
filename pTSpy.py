from b64 import encode_file_to_base64, read_input, convert_base64_to_format, clear_terminal
from minify_html import minify
from spy import spy

while_runner = True
while while_runner:
    opt = read_input(0, 4, 'Base64 Program\n[0] - Base64 Decoder\n[1] - Base64 Encoder\n[2] - Aplovin Spy\n[3] - Minify\n[4] - Exit\n---------------------------------------\nOption: ')

    if opt == 0:
        t = read_input(0, 1, 'Type: \n\t[0] - Read File\n\t[1] - Raw Data\nInput: ')
        tell = 'File Name: ' if (t == 0) else 'Base64 Data: '
        fn = input(tell)
        convert_base64_to_format(fn, t)
        clear_terminal()
    if opt == 1:
        fn = input("File Name: ")
        encode_file_to_base64(fn)
        clear_terminal()
    if opt == 2:
        spy()
        clear_terminal()
    if opt == 3:
        minify()
    if opt == 4:
        clear_terminal()
        while_runner = False
