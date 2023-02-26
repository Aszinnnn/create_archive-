import time
import os
print("""
\033[33;0;0 m
   ▄████████    ▄████████ 
  ███    ███   ███    ███ 
  ███    ███   ███    █▀  
  ███    ███   ███        
▀███████████ ▀███████████ 
  ███    ███          ███ 
  ███    ███    ▄█    ███ 
  ███    █▀   ▄████████▀  


Developer JavaScript and Python
Github: @Aszinnnn

""")
time.sleep(4)
print('\033[35;0;0 mIniciando projetos...')
time.sleep(5)

s = (input('Digite a senha:'))

print('Senha {} autorizada'.format(s))
time.sleep(6)

print('''

[1] Sim
[2] Não
         
         ''')
fzr = input('Gostaria de criar arquivos?')

if fzr == '1':
    file_name = input('Qual nome voce gostaria?')
file = open(f'{file_name}', 'a')
print(f'O {file_name} foi criado com sucesso')


print("Processo encerrado.")
time.sleep(2)
exit()