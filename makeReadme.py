# To use, paste at bottom of mathgen.py code, change line variable and remove all table rows in README.md except for the top 2 and run mathgen.py
# NOTE: not anymore. but still leaving this comment in.
from mathgenerator.mathgen import *

def array2markdown_table(string):
    string = string.replace("[[", "<table><tr><td>")
    string = string.replace("[", "<tr><td>")
    string = string.replace(", ", "</td><td>")
    string = string.replace("]]", "</td></tr></table>")
    string = string.replace("]", "</td></tr>")
    string = string.replace(" ", "")
    string = string.replace("\n", "")
    return string


wList = getGenList()
lines = []
with open('mathgenerator/mathgen.py', 'r') as f:
    lines = f.readlines()

allRows = []
# get the first line of the functions in mathgen.py
line = lines.index('# Funcs_start - DO NOT REMOVE!\n') + 1
for item in wList:
    myGen = item[2]
    # NOTE: renamed 'sol' to 'solu' to make it look nicer
    prob, solu = myGen()
    prob = str(prob).rstrip("\n")
    solu = str(solu).rstrip("\n")
    # edge case for matrixMultiplication
    if item[0] == 46:
        prob, solu = myGen(10, 4)
        prob = str(prob).rstrip("\n")
        solu = str(solu).rstrip("\n")
        prob = array2markdown_table(prob)
        solu = array2markdown_table(solu)

    instName = lines[line]
    # NOTE: renamed 'def_name' to 'func_name' because it suits it more
    func_name = instName[:instName.find('=')].strip()
    row = [myGen.id, myGen.title, prob, solu, func_name]
    print('added', item[1],'-', func_name, 'to the README.md')
    line += 1
    if line > len(lines):
        break
    allRows.append(row)

with open('README.md', "r") as g:
    lines = g.readlines()

    line = lines.index('[//]: # list start\n')
    lines = lines[:line + 1]

    for row in allRows:
        tableLine = "| " + str(row[0]) + " | " + str(row[1]) + " | " + str(
            row[2]) + " | " + str(row[3]) + " | " + str(row[4]) + " |\n"
        lines.append(tableLine)

with open('README.md', "w") as g:
    g.writelines(lines)

print("New README.md table generated")
