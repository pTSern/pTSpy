from b64 import encode_file_to_base64, convert_base64_to_format
from minify_html import minify
from spy import spy
from gemini_ai import infinite_request
from utils import clear_terminal, read_input, AL, SL, ST

msg = f"""
{SL} pTSpy {SL}
 [1] - Base64 Decoder
 [2] - Base64 Encoder
 [3] - Aplovin Spy
 [4] - Minify Html
 [5] - GEMINI AI
 [6] - Clear Console
 [0] - EXIT
{SL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{SL}
 {ST} > OPTION: """

while_runner = True
while while_runner:
    clear_terminal()
    opt = read_input(0, 6, msg)
    match(opt):
        case 1:
            t = read_input(0, 1, 'Type: \n\t[0] - Read File\n\t[1] - Raw Data\nInput: ')
            tell = 'File Name: ' if (t == 0) else 'Base64 Data: '
            fn = input(tell)
            convert_base64_to_format(fn, t)
            clear_terminal()
        case 2:
            fn = input("File Name: ")
            encode_file_to_base64(fn)
            clear_terminal()
        case 3:
            spy()
            clear_terminal()
        case 4:
            minify()
        case 5:
            infinite_request()
        case 0:
            while_runner = False
        case _:
            clear_terminal()
