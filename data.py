import datetime

class BasicInfo:
  def __init__(self):
    self.data = {}
  
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


templates = ['Casual Template']
templateNames = ['templates\casual_admin_template.docx']