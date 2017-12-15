import re
import os
import logging


FORMAT="%(asctime)s:%(message)s"
logging.basicConfig(level=logging.INFO, format = FORMAT)


def confirm(answer="OK to push to continue [Y/N]? "):
    """
    Ask user to enter Y or N (case-insensitive).
    :return: True if the answer is Y.
    :rtype: bool
    """
    while answer not in ["y", "n"]:
        answer = raw_input(answer + " [Y/N]").lower()
    return answer == "y"


def save_txt_fo_file (file, txt, rewrite = False):
    if ( not os.path.exists(file) or rewrite ):
        with open (file, 'w') as f:
            f.write (txt)
            logging.info ("Saved '%s' to '%s'" % (txt, file))
    else:
        save_txt_fo_file (file, txt, confirm ("Rewrite '%s'?" % file) )
    
    
def save_answ (number, answer, folder = 'answers'):
    if os.path.isdir(folder):
        file = os.path.join(folder, str(number) + "_answ.txt")
        save_txt_fo_file(file, answer)
    else:
        os.mkdir(folder)
        logging.info ("Created folder %s", folder)
        save_answ (number, answer, folder)