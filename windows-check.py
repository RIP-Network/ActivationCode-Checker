import random
import string
import time

print(" ___________________")
print(" | _______________ |")
print(" | |XXXXXXXXXXXXX| |")
print(" | |XXXXXXXXXXXXX| |")
print(" | |XXXXXXXXXXXXX| |")
print(" | |XXXXXXXXXXXXX| |")
print(" | |XXXXXXXXXXXXX| |")
print(" |_________________|")
print("     _[_______]_")
print(" ___[___________]___")
print("|         [_____] []|__")
print("|         [_____] []|  \__")
print("L___________________J     \ \___\/")
print(" ___________________      /\ ")
print("/###################\    (__)")
      
print("Created by RIP-Network")
time.sleep(4)

def generar_codigo():
    codigo = ''
    for i in range(5):
        codigo += ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if i < 4:
            codigo += '-'
    return codigo


codigos = []
for i in range(25):
    codigos.append(generar_codigo())


with open('codigos.txt', 'w') as f:
    for codigo in codigos:
        f.write(codigo + '\n')

print("       _nnnn_ ")
print("        dGGGGMMb ")
print("       @p~qp~~qMb ")
print("       M|@||@) M| ")
print("       @,----.JM| ")
print("      JS^\__/  qKL ")
print("     dZP        qKRb ")
print("    dZP          qKKb ")
print("   fZP            SMMb ")
print("   HZM            MMMM ")
print("   FqM            MMMM ")
print(" __| /.        |\dSsqML ")
print(" |    `.       | `' \Zq ")
print("_)      \.___.,|     .' ")
print("\____   )MMMMMM|   .' ")
      
print("Probando los codigos de activacion por favor espere...")
time.sleep(3)

import subprocess

def check_activation_code(activation_code):

    cmd = 'slmgr.vbs /dli {}'   

    
    process = subprocess.Popen(cmd.format(activation_code), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    
    if 'License Status: Licensed' in output:
        return True
    else:
        return False


archivo = 'codigos.txt'


with open(archivo, 'r') as f:
    activation_codes = f.read().splitlines()


for activation_code in activation_codes:
    if check_activation_code(activation_code):
        print(f'El código de activación {activation_code} es válido.')
    else:
        print(f'El código de activación {activation_code} es inválido.')

