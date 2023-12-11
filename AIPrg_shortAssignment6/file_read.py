import os

pwd = os.getcwd()
pwd = pwd + '/NSCCAI/AIPrg_shortAssignment6'
print(f'pwd is: {pwd}')

source_file_path = os.path.join(pwd, 'source_file.txt')
prohibited_syntax_file_path = os.path.join(pwd, 'prohibited_syntax.txt')

with open(source_file_path, 'r') as f:
    source_file = f.read().splitlines()
    print(f'source_file content is: {source_file}')

print('\n')

with open(prohibited_syntax_file_path, 'r') as f:
    prohibited_syntax = f.read().splitlines()
    print(f'prohibited_syntax_file content is: {prohibited_syntax}')

print(type(source_file), type(prohibited_syntax), '\n')

source_file_res = []
for i in range(len(source_file)):
    ele = source_file[i]
    for j in range(len(prohibited_syntax)):
        sub_ele = prohibited_syntax[j]
        if sub_ele.lower() in ele.lower():
            source_file_res.append(ele.replace(sub_ele, '***'))

print(f'new source_file_res content is: {source_file_res}')
