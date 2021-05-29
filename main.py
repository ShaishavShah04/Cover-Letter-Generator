# ------------------------- #
# Cover Letter Generator    #
# Made By: Shaishav Shah    #
# ========================= #

# Imports
from docxtpl import DocxTemplate
from docx2pdf import convert
import os
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
    

def processingDoc(choice, Data, form_info):
    name = Data.getTemplatePaths()[choice]
    doc = DocxTemplate(name)
    doc.render(form_info)
    path = os.path.join( os.getcwd() ,"outputs", "temporary.docx")
    if not os.path.exists(os.path.join(os.getcwd(), "outputs")):
        os.mkdir(os.path.join(os.getcwd(), "outputs"))
    doc.save(path)
    return path

def docx_to_pdf(old_path, form_info):
    if os.path.exists(old_path):
        name_to_save = '{}_{}_CoverLetter.pdf'.format(form_info.get('company_name','Company'), form_info.get('position_name','Position'))
        convert(old_path, os.path.join(os.getcwd(), "outputs", name_to_save ))
        os.remove(old_path)

def again():
    userChoice = input("\nDo you want to generate another cover letter? [Y/N]: ")
    if not userChoice.lower() == "y":
        exit()
    

def main():
    DataClass = BasicInfo()
    while True:
        choice = menu(DataClass)
        data = DataClass.gather_data()
        old_path = processingDoc(choice, DataClass, data)
        docx_to_pdf(old_path, data)
        DataClass.reset()
        again()

main()