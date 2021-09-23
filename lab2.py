key_word = ['auto', 'break', 'case', 'char', 'const',
            'continue', 'default', 'do','double', 'else', 'enum',
           'extern', 'float', 'for', 'goto', 'if','int', 'long',
          'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union',
            'unsigned', 'void', 'volatile', 'while']                                            #All the keywords in C and C++ are generated here
file_name = input("Please input the file name:")
level = input("Please input the level(1-4):")                                                   #Determine the name of the object file and the processing level
level = int(level)

with open(file_name) as C_object:
    lines = C_object.readlines()
                                                                                                #open the object file and read it line by line
def One(lines):
    count = 0
    store = []
    for line in lines:
            chars = ['(', ')', '{', '}', ':', ',', '<', '>', '=', '+', '-', '#', ';']

    for line in lines:

        if '//' in line:
            temp = line.index('//')
            line = line[:temp]

        if '/*' in line:
            a = lines.index(line)

            for new_line in lines[a:]:

                if '*/' not in new_line:
                    del lines[a]

                else:
                    del lines[a]
                    break

        while True:

            if '"' in line:
                first_subscript = line.index('"')
                last_subscript = line[first_subscript + 1:].index('"')
                line = line[:first_subscript] + line[first_subscript + last_subscript + 2:]

            else:
                break

        while True:
            if "'" in line:
                first_subscript = line.index("'")
                last_subscript = line[first_subscript + 1:].index("'")
                line = line[:first_subscript] + line[first_subscript + last_subscript + 2:]
            else:
                break

        # Converts special characters to Spaces, word segmentation

        for element in chars:
            line = line.replace(element, ' ')
            b = line.split()

        if 'else' in b and 'if' in b:

         # Consider esle if as a whole to pave the way for the following function processing

            store.append('elif')
            count += 2
        else:
            for word in b:
                if word in key_word:
                    count += 1
                    store.append(word)
    return store, count

def Two(store):

    case_num = []
    structure_num = 0
    while True:
        num = 0
        if 'default' in store:
            subscript = store.index('default')
            structure_num += 1

            # The number of SwitchCase structures is identified by the number of default

            for word in store[:subscript]:
                if word == 'case':
                    num += 1
            case_num.append(num)

             #dentify the number of cases in each group

            del store[:subscript + 1]
        else:
            break
    return case_num, structure_num

def  Three(store):

    if_else_num = 0
    list = []
    if_elif_num = 0


    for word in store:
        count = 0

        if word == 'if':
            if_else_num += 1

        if word == 'if' or word == 'elif':
            list.append(word)
        elif word == 'else':
            while True:
                temp = list.pop()
                if temp == 'elif':
                    count = 1
                elif temp == 'if':
                    break
        if count == 1:
            if_elif_num += 1


    for word in list:

    # Consider that there is no else in if else if structure

        if word == 'if':
            if_else_num -= 1
    return if_else_num, if_elif_num


     # Call and execute the function

store, total_num = One(lines)
case_nums , switch_nums = Two(store[:])
if_else_nums, if_elif_nums =  Three(store[:])
if level >= 1:
    print(f"total num:{total_num}")
if level >= 2:
    print(f"switch num:{switch_nums}")
    print("case num:", end = ' ')
    for case in case_nums:
        print(case, end = ' ')

if level >= 3:

    print('\n'f"if-else num:{if_else_nums - if_elif_nums}")
if level >= 4:

    print(f"if-elif_num:{if_elif_nums}")