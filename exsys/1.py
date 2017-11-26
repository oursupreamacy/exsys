import sys
import re

#                   Пресеты
preset_add = re.compile('^[(]\w+[,]\s\w+[)]$')  # (Steve, Apples)
preset_search = re.compile('^[(]\w[,]\s\w+[)]$')  # (X, Apples)
preset_search2 = re.compile('^[(]\w+[,]\s\w[)]$')  # (Steve, X)


def add(string):
    with open('База_знаний.txt', 'a') as bz:
        bz.write(string + '\n')


def search(string):
    with open('База_знаний.txt', 'r') as bz:
        for line in bz:
            if string[2:] in line:
                splited = line.split(',')
                stripped = splited[0]
                a = stripped.strip()
                b = a.strip('(')
                print(b)


def search2(string):
    with open('База_знаний.txt', 'r') as bz:
        string_spl = string.split(',')
        for line in bz:
            if string_spl[0] in line:
                splited = line.split(',')
                stripped = splited[1]
                a = stripped.strip()
                b = a.strip(')')
                print(b)


def condition(cond, res):
    reslist = []
    with open('База_знаний.txt', 'r') as bz:
        cond_spl = cond.split(',')
        for line in bz:
            if cond_spl[0] in line:
                splited = line.split(',')
                stripped = splited[1]
                a = stripped.strip()
                b = a.strip(')')
                reslist.append(b)
    with open('База_знаний.txt', 'a') as bz:
        res_splt = res.split(',')
        for item in reslist:
            bz.write(res_splt[0] + ',' + ' ' + item + ')' + '\n')
            print(res_splt[0] + ',' + ' ' + item + ')')


def condition2(cond, res):
    with open('База_знаний.txt', 'r+') as bz:
        for line in bz:
            if cond in line:
                bz.write(res)


def condition3(cond, res):
    with open('База_знаний.txt', 'r+') as bz:
        cond_splt = cond.split(',')
        for line in bz:
            if cond_splt[1] in line:
                res_splt = res.split(',')
                splited = line.split(',')
                bz.write(splited[0] + ',' + res_splt[1] + '\n')
                print(splited[0] + ',' + res_splt[1])


if __name__ == '__main__':
    if sys.argv[1] == 'add' and preset_add.match(sys.argv[2]):
        add(sys.argv[2])
    elif sys.argv[1] == 'add' and not preset_add.match(sys.argv[2]):
        print('Неверно введен предикат')
    elif sys.argv[1] == 'search' and preset_search.match(sys.argv[2]):
        search(sys.argv[2])
    elif sys.argv[1] == 'search' and preset_search2.match(sys.argv[2]):
        search2(sys.argv[2])
    elif sys.argv[1] == 'if' and preset_search.match(sys.argv[2]) and preset_search.match(sys.argv[3]):
        condition3(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'if' and preset_search2.match(sys.argv[2]) and preset_search2.match(sys.argv[3]):
        condition(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'if' and preset_add.match(sys.argv[2]) and preset_add.match(sys.argv[3]):
        condition2(sys.argv[2], sys.argv[3])
    
