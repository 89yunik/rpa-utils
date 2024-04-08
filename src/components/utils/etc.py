from os import system
from typing import List

def close_program(program:str):
    try: system(f'taskkill /f /im {program}')
    except: pass

def close_programs(programs:List[str]):
    for program in programs: close_program(program=program)

def get_txt(txt_path:str)->List[str]:
    f = open(txt_path, 'r')
    data = f.readlines()
    f.close()
    return data

def update_txt(txt_path:str, data:List[str]):
    f = open(txt_path, 'w')
    f.writelines(data)
    f.close()