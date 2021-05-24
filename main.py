# ------------------------- #
# Cover Letter Generator    #
# Made By: Shaishav Shah    #
# ========================= #

# Imports
from docxtpl import DocxTemplate
from docx2pdf import convert
# Data
from data import BasicInfo

# Functions

def menu(Data):
    """Prompts the user for the template which they want

    Returns:
        str: a string object which can be used as a key for the template data
    """ 
    print("\nWhat template would you like to choose:\n")
    templates = Data.getTemplateNames()
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
    

def processingDoc(choice, data):
    name = data.getTemplatePaths()[choice]
    doc = DocxTemplate(name)
    doc.render(data)
    doc.save('{}_{}_CoverLetter.docx'.format(data.get('company_name','Company'), data.get('position_name','Position')))

def again():
    userChoice = input("\nDo you want to generate another cover letter? [Y/N]: ")
    if not userChoice.lower() in {"y",""}:
        exit()
    

def main():
    Data = BasicInfo()
    while True:
        choice = menu(Data)
        data = Data.gather_data()
        processingDoc(choice, data)
        Data.reset()

main()