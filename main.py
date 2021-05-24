# ------------------------- #
# Cover Letter Generator    #
# Made By: Shaishav Shah    #
# ========================= #

# Imports
from docxtpl import DocxTemplate
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
    for index in range(len(templates)):
        print("{}. {}".format(index+1, templates[index]))
    accepted_values = list(range(1, len(templates)+1))
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
            return userChoice - 1
    
def gatherInfo():
    UserInfo = BasicInfo()
    return UserInfo.gather_data()

def processingDoc(choice, data):
    name = templateNames[choice]
    doc = DocxTemplate(name)
    doc.render(data)
    doc.save('{}_{}_CoverLetter.docx'.format(data.get('company_name','Company'), data.get('position_name','Position')))


def main():
    choice = menu()
    data = gatherInfo()
    processingDoc(choice, data)
              
main()