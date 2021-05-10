# ------------------------- #
# Cover Letter Generator    #
# Made By: Shaishav Shah    #
# ========================= #

# Imports
from docxtpl import DocxTemplate
import datetime
from docx2pdf import convert
# Data
from data import *

# Functions

def menu():
    """Prompts the user for the template which they want

    Returns:
        str: a string object which can be used as a key for the template data
    """ 
    print("What template would you like to choose:")
    for index in range(len(templateNames)):
        print("{}. {}".format(index+1, templateNames[index]))
    accepted_values = list(range(1, len(templateNames)+1))
    while True:
        try:
            userChoice = int(input("> "))
            if not userChoice in accepted_values:
                raise Exception("Not a valid choice!")
        except ValueError:
            print("Enter a valid number!")
        except:
            print("Input a valid choice!")
        else:
            return templateNames[userChoice-1]
    
def gatherInfo():
    pass


def main():
    print(menu())            

main()