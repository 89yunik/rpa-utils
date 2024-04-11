from components.utils.error_handling import error_handler
from components.utils.etc import close_programs
from config import *

@error_handler()
def rpa_main(): 
    close_programs([])

if __name__=="__main__": rpa_main()