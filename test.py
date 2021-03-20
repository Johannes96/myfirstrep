import webbrowser

print('Weleche Seite möchtest du öffnen?')
print('1: GRIPS')
print('2: LSF')
inp = input()

if inp == '1':
      webbrowser.open('https://elearning.uni-regensburg.de/')
elif inp == '2':
    webbrowser.open('https://lsf.uni-regensburg.de/qisserver/rds?state=user&type=0')
else:
    print('ungültige Anfrage')
