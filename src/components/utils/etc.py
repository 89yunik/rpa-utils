from os import system, listdir, path, remove
from typing import List
from time import time

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

def delete_expired_files(directory:str, expiration_period:int):
    current_time:float = time()
    for filename in listdir(directory):
        filepath:str = path.join(directory, filename)

        modification_time:int = path.getmtime(filepath)

        if (current_time - modification_time) > (expiration_period * 24 * 3600): remove(filepath)