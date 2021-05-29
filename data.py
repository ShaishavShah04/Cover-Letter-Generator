import datetime, os

class BasicInfo:
  def __init__(self):
    self.data = {}
    self.templates = []
    self.templatePaths = []
    self.scanFiles()

  # Setter Methods

  def scanFiles(self):
    for filename in os.listdir('./templates'):
      name, ext = os.path.splitext(filename)
      if ext == ".docx" or ext == ".doc":
        self.templates.append(name)
        self.templatePaths.append(os.path.join(os.getcwd(),"templates", filename))

  def gather_data(self):
    
    data_list = {'date': datetime.datetime.today().strftime('%m/%d/%Y'),
                 'company_name': None,
                 'company_street_address':None,
                 'city': None,
                 'state':None,
                 'postal_code': None,
                 'position_name': None
    }
    for key in data_list.keys():
      if data_list.get(key, None) == None:
        data_list[key] = input('What is the {}: '.format(key))
  
    return data_list

  def reset(self):
    self.data = {}

  # Getter Methods

  def getTemplateNames(self):
    return self.templates

  def getTemplatePaths(self):
    return self.templatePaths
