from os import system
from typing import List

def close_program(program:str):
    try: system(f'taskkill /f /im {program}')
    except: pass

def close_programs(programs:List[str]):
    for program in programs: close_program(program=program)

