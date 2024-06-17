import os
import glob

fileEnding = '.js'


def get_js_files(directory):
    pattern = os.path.join(directory, '*' + fileEnding)
    js_files = glob.glob(pattern)
    return js_files

def merge_js_files(files, output_file):
    merged_content = ''

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            merged_content += f.read() + '\n'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(merged_content)

if __name__ == '__main__':
    egopath = os.path.dirname(os.path.abspath(__file__))
    parentpath = egopath
    if parentpath.endswith(fileEnding.lstrip('.')):
        parentpath = os.path.dirname(parentpath)
    folder_name = os.path.basename(parentpath)

    files_to_merge = get_js_files(egopath)
    output_file = folder_name + " All_" + fileEnding
    if (egopath + "\\" + output_file in files_to_merge):
        files_to_merge.remove(egopath + "\\" + output_file)
    
    merge_js_files(files_to_merge, egopath + "\\" + output_file)
