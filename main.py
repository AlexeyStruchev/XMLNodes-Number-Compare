# The utility checks if quantity of nodes in files of different languages is different or not.
# It is assumed that nodes number in files of different languages should be equal.
# If nodes number is different it is a sign of a defect.

from compare_xml_functions import *

# file template can be a file name of any language
# absolute path to folder example = r'C:\Users\user\Documents\Ixml\26167\CCS_Feed_26167_210111_0815'
file_template = 'Standard_file_en_1_of_1'
# The first language in langs variable list must be equal the language in file template
langs = ('en', 'es')
folder = r'xml_examples'
# Nodes which are going to be compared
xpath_nodes = [
    '/Feed',
    '/Feed/Product',
    '/Feed/Product/CustomerSKUID'
]

compare_xml_files_by_nodes(file_template, langs, folder)
