from os import system, listdir, path, remove
from typing import List, Sequence
from time import time
import random

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
        expiration_seconds = expiration_period * 24 * 3600
        if (current_time - modification_time) > expiration_seconds: remove(filepath)

def generate_random_string(character_set:Sequence, length:int):
    random_string = ''.join(random.choice(character_set) for _ in range(length))
    return random_string