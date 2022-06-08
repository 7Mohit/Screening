def replace_file_content(file_name, original_txt, replace_txt):
    with open(file_name, 'r') as fr:
        data = fr.read()
        data = data.replace(original_txt, replace_txt)
    with open(file_name, 'w') as fw:
        fw.write(data)

if __name__=='__main__':
    print('Input the filename original txt and replacement text.\
         Input values space separated:')
    filename, org_txt, rep_txt = input().split()
    replace_file_content(filename, org_txt, rep_txt)