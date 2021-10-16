import os

def find_files_1(suffix, path, file_list):
    
    dir_items_list = os.listdir(path)

    filestring = ''
    new_files = ''

    for i in range(len(dir_items_list)):
        item = dir_items_list[i]
        item_path = os.path.join(path, item)
            
        if os.path.isdir(item_path):

            find_files_1(suffix, item_path, file_list)

        if os.path.isfile(item_path) and item_path.endswith(suffix):
                if filestring is '':
                    new_files = item
                else:
                    new_files = filestring + ", " + item
             
    if new_files is not '':
        file_list.append(new_files)
        return file_list

file_list = []
path = "./testdir"
print(find_files_1('.c', path, file_list))


