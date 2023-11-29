import os

pwd = os.getcwd() + '/NSCCAI/AIPrg_shortAssignment6'

source_file = pwd + '/source_file.txt'
prohibited_syntax_file = pwd + '/prohibited_syntax.txt'

with open(source_file, 'r') as f:
    source = f.read().splitlines()
    print(f'source_file content is: {source}')

print('\n')

with open(prohibited_syntax_file, 'r') as f:
    prohibited_syntax = f.read().splitlines()
    print(f'prohibited_syntax_file content is: {prohibited_syntax}')


print(type(source), type(prohibited_syntax), '\n')

for i in range(len(prohibited_syntax)):
    prohibited_syntax[i] = prohibited_syntax[i].split(' ')
    print(f'line {i+1} is: {prohibited_syntax[i]}')