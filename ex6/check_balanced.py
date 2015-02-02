from balanced_brackets import *

func_num = int(input())
check_str = ""
while check_str != 'exit':
    check_str = input()
    if check_str == 'exit': break
    print(check_str, end="\t:\t")
    if func_num == 1:
        print(is_balanced(check_str))
    elif func_num == 2:
        print(violated_balanced(check_str))
    else:
        print(match_brackets(check_str))
