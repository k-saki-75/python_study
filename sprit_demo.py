import re

def strip_demo(str):

    for age in str:
        strip_str = re.sub(r"^\s+|\s+$|EG", "", age)
        print(strip_str)
        


str_demo = [' spam ', '  spam  ', ' spam', 'spam ', 'spam', ' spam spam ']
args = ['EspamG', 'EspamG', 'EGspamEG', ' EspamG ', 'Espam', 'spamE','spam', 'EspamEspamE']
strip_demo(str_demo)
strip_demo(args)