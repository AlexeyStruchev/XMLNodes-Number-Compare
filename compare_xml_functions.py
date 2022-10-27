from lxml import etree


def add_list_to_list_of_lists(list_of_lists, list_name):
    list_of_lists.append(list_name)


def count_nodes(path_to_file_with_lang, node_path, united_list):
    # make united list by different languages
    nodes_in_file = []
    for lang, path_to_file_ in path_to_file_with_lang.items():
        doc = open(path_to_file_, 'r')
        xmldoc = etree.parse(doc)
        root = xmldoc.getroot()
        # count all nodes for a given node in a file
        node_count = len(root.xpath(node_path))
        nodes_in_file.append(node_count)
        doc.close()
    add_list_to_list_of_lists(united_list, nodes_in_file)


def count_nodes_many_files(langs_files_dict, nodes_):
    joined_list_ = []
    for node in nodes_:
        count_nodes(langs_files_dict, node, joined_list_)
    return joined_list_


def compare_nodes(node_names_with_number):
    result_dict = {}
    for node_name, node in list(node_names_with_number.items()):
        for num in node:
            # check for count difference of first node with other nodes
            if num != node[0]:
                result_dict.update({node_name: node})
    if result_dict == {}:
        print('\n', 'Xml nodes number is equal in provided files!')
    else:
        print('Number of nodes is not equal comparing to a file with "en" language: ')
        for node_path, nodes_count in result_dict.items():
            print('\t', 'Check nodes with path: {}. The difference per file is: {}'.format(node_path, nodes_count))


class File:
    @staticmethod
    def create_files_dict(input_file_name_, langs_, folder_, file_ext_):
        files_dict_ = {}
        start_lang_index = input_file_name_.find('_' + langs_[0] + '_') + 1
        end_lang_index = start_lang_index + 2
        for lang in langs_:
            file_name = input_file_name_[0:start_lang_index] + lang + input_file_name_[end_lang_index:]
            file_path = folder_ + '\\' + file_name + file_ext_
            files_dict_.update({lang: file_path})
        return files_dict_


def compare_xml_files_by_nodes(file_template_, langs_, folder_, nodes_, file_extension_):
    files_dict = File.create_files_dict(file_template_, langs_, folder_, file_extension_)
    nodes_count = count_nodes_many_files(files_dict, nodes_)
    compare_nodes(dict(zip(nodes_, nodes_count)))
