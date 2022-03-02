import sys

name = sys.path[0] + '/haypy.arm'

with open(name, 'r') as my_lang:
    data = my_lang.readlines()

arithmetic_operations = {'gum': '+', 'han': '-', 'bazh': '/', 'tvh': '//', 'bazm': '*', 'ast': '**', 'nsh': '=', 'hav': '==', 'poqr': '<', 'ph': '<=',
                         'mets': '>', 'mh': '>=', 'hch': '!=', 'mn': '%', '(': '(', ')': ')'}

booleans = {'True': 'Chishte', 'False': 'Sxale', 'None': 'Datark'}


keyword_dict = {'yev': 'and', 'Vorp': 'as','kangar': 'break', 'das': 'class', 'sharunaki': 'continue', 'sahm': 'def', 'jnj': 'del',
                'aylapes': 'elif', 'urish': 'else', 'bacari': 'except', 'verjapes': 'finally', 'ptuyt': 'for', 'ic': 'from',
                'ete': 'if', 'nerm': 'import', 'ka': 'in', 'nuyn': 'is', 'voch': 'not', 'kam': 'or', 'anc': 'pass', 'veradardz': 'return',
                'pordzel': 'try', 'minchder': 'while', 'hety':'with', 'ardyunq': 'print()', 'dir': 'popoxakan haytararel'}

all_page = []
variables = {}
variables['vars'] = []
values = {}

for i in data:
    all_page.append(i.split())


for k in all_page:
    try:
        if k[0] == 'dir' and k[2] == 'nsh':
            variables['vars'].append(k[1])
        if k[0] == 'dir' and k[2] == 'nsh':
            eval_list = []
            for j in k[3:]:
                if j in arithmetic_operations:
                    eval_list.append(arithmetic_operations[j])
                else:
                    eval_list.append(j)
            values[k[1]] = eval(''.join(eval_list))
        eval_list = []
        if k[0] != 'dir' and k[2] != 'nsh':
            for j in k:
                if j in arithmetic_operations:
                    eval_list.append(arithmetic_operations[j])
                else:
                    eval_list.append(j)
        if str(eval(''.join(eval_list))) in booleans:
            b = eval(''.join(eval_list))
            print(booleans[str(b)])
        else:
            print(eval(''.join(eval_list)))
    except:
        pass
    finally:
        try:
            if k[0] == 'ardyunq' and k[1] in values and len(k) == 2:
                print(values[k[1]])
            elif k[0] == 'ardyunq' and len(k) > 2:
                eval_list = []
                for i in k[1:]:
                    if i in arithmetic_operations:
                        eval_list.append(arithmetic_operations[i])
                    elif i in values:
                        eval_list.append(str(values[i]))
                    else:
                        eval_list.append(i)
                print(eval(''.join(eval_list)))
            elif k[0] == 'ardyunq' and len(k) > 2 and str(k[1]) not in values:
                print('Harcman Sxal!!! \nChka nshanakvats aydpisi popoxakan. \nXndrum enq stugel ev noric pordzel!!!!')
            elif k[0] == 'ardyunq' and k[1] not in values:
                print('Harcman Sxal!!! \nChka nshanakvats aydpisi popoxakan. \nXndrum enq stugel ev noric pordzel!!!!')
        except:
            pass
        finally:
            
            try:
               
                
                other_list = []
                if k[0] == 'ete' or k[0] == 'aylapes:':
                    eval_list = []
                    if k[0] == 'ete':
                        for i in k[1:]:
                            if i in arithmetic_operations:
                                eval_list.append(str(arithmetic_operations[i]))
                            elif i in values:
                                eval_list.append(str(values[i]))
                                
                            else:
                                eval_list.append(str(i))
                        if eval(''.join(eval_list)[:-1]):
                            print(booleans[str(eval(''.join(eval_list)[:-1]))])
                           
                        else:
                             print(booleans[str(False)])
                             
                    
                    elif k[0] == 'aylapes:':
                        print(booleans[str(False)])
                        
                                              
            except:
                pass


                    






