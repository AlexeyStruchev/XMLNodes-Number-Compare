from lxml import etree



def add_list_to_list_of_lists(list_of_lists, list_name):
    list_of_lists.append(list_name)


def count_nodes(path_to_files, xmlpath, united_list):
    # make united list by different languages
    node_list = []
    for k, v in path_to_files.items():
        doc = open(v, 'r')
        docx = etree.parse(doc)
        root = docx.getroot()
        # count nodes in file
        node_count = len(root.xpath(xmlpath))
        node_list.append(node_count)
        doc.close()
    add_list_to_list_of_lists(united_list, node_list)


def count_nodes_many_files(langs_files_dict, nodes_):
    joined_list_ = []
    for node in nodes_:
        count_nodes(langs_files_dict, node, joined_list_)
    return joined_list_


def compare_nodes(init_dict):
    new_dict = {}
    for node_name, node in list(init_dict.items()):
        for num in node:
            if num != node[0]:
                new_dict.update({node_name: node})
        if sum(node) == 0:
            print('Check left node: ')
            print('\t', node_name)
    if new_dict == {}:
        print('\n', 'All downloads are equal! Nothing to compare!')
    else:
        print('Number of nodes is not equal: ')
        for i in new_dict.items():
            print('\t', i)


def create_files_dict(input_file_name_, langs_, folder_):
    file_ext_ = '.xml'
    files_dict_ = {}
    start_index = input_file_name_.find('_' + langs_[0] + '_') + 1
    end_index = start_index + 2
    for lang in langs_:
        file_name = input_file_name_[0:start_index] + lang + input_file_name_[end_index:]
        file_path = folder_ + '\\' + file_name + file_ext_
        files_dict_.update({lang: file_path})
    return files_dict_


def compare_xml_files_by_nodes(file_template_, langs_, folder_, xpath_nodes_):
    files_dict = create_files_dict(file_template_, langs_, folder_)
    joined_list = count_nodes_many_files(files_dict, xpath_nodes_)
    compare_nodes(dict(zip(xpath_nodes_, joined_list)))
