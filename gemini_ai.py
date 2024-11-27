
import os
import google.generativeai as genai
import json

from utils import uid, today, create_folder, read_input, clear_terminal, no_null_input, selection_input, md_to_html, AL, SL, ST, LL, short_str

GAK = "GEMINI_API_KEY"
GAK_F = os.path.join(os.path.expanduser('~'), '.config/') + GAK + ".cfg"

SFS = os.path.join(os.path.expanduser('~'), '.config/')

class GEMINI_API_DATA:
    def __init__(self):
        self.api_key = ""
        self.save_to_file = True
        self.format = 'html'

    def from_json(self, jsdata):
        self.api_key = jsdata['api_key']
        self.save_to_file = jsdata['save_to_file']
        self.format = jsdata['format']

    def to_json(self):
        obj = {
            "api_key": self.api_key,
            "save_to_file": self.save_to_file,
            "format": self.format
        }
        return json.dumps(obj)

    def set(self, api_key, save_to_file, format):
        self.api_key = api_key
        self.save_to_file = save_to_file
        self.format = format.lower()

    def save(self, path):
        with open(path, 'w') as f:
            f.write(self.to_json())

    def log(self):
        logger = f"""

        {SL}{SL} [ CONFIG ] {SL}{SL}
        {ST} API KEY:          {self.api_key}
        {ST} IS SAVE TO FILE:  {self.save_to_file}
        {ST} FILE FORMAT:      {self.format}
        {SL}{SL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{SL}{SL}

        """
        print(logger)

gid_inst = GEMINI_API_DATA()

def configure_api_key(initial_key=None):
    if initial_key:
        print(f"\nGet your API at: https://aistudio.google.com/app/apikey\n")
        key = input(f"GEMINI API KEY ({initial_key}): ")
        gkey = key if len(key) > 0 else initial_key
    else:
        gkey = no_null_input(f"GEMINI_API_KEY: ")

    save = selection_input(['0', '1', 'Y', 'Yes', 'N', "No"], f"Save response to file? (Y/N): ")
    is_save = save in ['1', 'Y', 'YES']
    format = selection_input(['html', 'md'], 'Select your output format (html/md): ', True) if is_save else gid_inst.format
    os.environ[GAK] = gkey
    gid_inst.set(gkey, is_save, format)
    gid_inst.save(GAK_F)

def gak_getter():
    try:
        with open(GAK_F, 'r') as gak_f:
            jsdata = json.loads(gak_f.read())
            gid_inst.from_json(jsdata)
            os.environ[GAK] = gid_inst.api_key
    except:
        configure_api_key()

    genai.configure(api_key=gid_inst.api_key)
    print()

def ai_gen():

    gak_getter()

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = input("Your Prompt: ")
    try:
        response = model.generate_content(prompt)
        print(SL)
        r_msg = response.text
        print(r_msg)
        print(SL)

        now = today()
        path = SFS + "GEMINI"
        create_folder(path)
        create_folder(f"{path}\\{now}")
        if gid_inst.save_to_file:
            fnp = f"{path}\\{now}\\{short_str(prompt, 20)}_{uid()}"
            with open(fnp + '.md', 'w') as f:
                prompt_box = f"""
<h2 style="text-align: center;">YOUR PROMPT</h2>
<div style="border: 1px solid white; padding: 10px; rx: 30px; ry: 30px; background-color: black; color: white; display: flex; justify-content: flex-start; align-items: flex-start; text-align: left;">
{prompt}
</div>

---

{r_msg}
"""
                f.write(prompt_box)
                if gid_inst.format.lower() == 'html':
                    md_to_html(fnp + '.md', fnp + '.html', False)
                print(f"Saved your request at: '{fnp}.{gid_inst.format}'")

    except Exception as e:
        print("An Error Occurred: ", e)

msg = f"""
{SL} GEMINI-AI {SL}
 [1] > ASK
 [2] > Change Config
 [3] > Clear Console
 [0] > EXIT
{SL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{AL}{SL}
 {ST} > OPTION: """

def infinite_request():
    break_point = True
    clear_terminal()

    while break_point:
        opt = read_input(0, 3, msg)

        match opt:
            case 1:
                ai_gen()
            case 2:
                gid_inst.log()
                configure_api_key(gid_inst.api_key)
            case 3:
                clear_terminal()
            case 0:
                clear_terminal()
                break_point = False

