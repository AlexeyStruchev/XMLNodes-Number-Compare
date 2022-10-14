""" The utility checks if number of nodes in files of different languages is equal or not.
It is assumed that nodes number in files of different languages should be equal.
If nodes number is different it is a sign of a defect.
In order to correctly compare files there has to be at least two files by different languages each.
By default, the utility works with files attached to this project. To change default behavior create a folder
and place xml files there.
A file template is a file name with language inside the name. Language can be in any place of the file and consists of
two symbols: en - English, es - Spanish, etc. """

from compare_xml_functions import compare_xml_files_by_nodes

file_template = 'Standard_file_en_1_of_1'
file_ext = '.xml'
langs = ('en', 'es')  # The first language in langs variable list must be equal the language in file template
folder = r'xml_examples'
# Nodes which are going to be compared
nodes_to_compare = \
    [
        '/Feed',
        '/Feed/Product',
        '/Feed/Product/INTSKUID',
        '/Feed/Product/ManufacturerPN',
        '/Feed/Product/Manufacturer',
        '/Feed/Product/ProductName',
        '/Feed/Product/ProductName',
        '/Feed/Product/ProductTitle'
    ]

compare_xml_files_by_nodes(file_template, langs, folder, nodes_to_compare, file_ext)
