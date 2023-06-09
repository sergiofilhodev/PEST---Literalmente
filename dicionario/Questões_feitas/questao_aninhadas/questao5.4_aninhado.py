# Escreva um programa que crie um dicionário de nomes de alunos e suas notas em disciplinas. Cada aluno
# deve estar associado a duas disciplinas (Português e Matemática) e cada disciplina deve ter uma ou mais
# notas. O programa deve permitir ao usuário adicionar novos alunos e notas, atualizar notas existentes e
# excluir alunos do dicionário. O programa também deve calcular a média de notas do aluno por disciplina.
import json
boletin = {}
def menu():
    print('''
    ------------------ Menu ------------------
    [1] - Adicionar Aluno com nota(s). ➕.
    [2] - Atualizar notas.
    [3] - Excluir Aluno ❗.
    [4] - Calcular media.
    [5] - Salvar notas.
    [6] - Carregar notas.
    [7] - Mostrar notas do aluno.
    [0] - Sair ❌.
    ------------------------------------------
    ''')
    return int(input('Digite a opção: '))


def add_aluno_nota(nome_aluno, lista_nota_aluno_matematica, lista_nota_aluno_portugues):
    if nome_aluno in boletin:
        print("="*15)
        print("Nome já existendi.")
        print("="*15)
    else:
        boletin[nome_aluno] = {'matematica': lista_nota_aluno_matematica,'portugues': lista_nota_aluno_portugues}
        print('=-'*7)
        print(boletin)
        print()
        print('alunos matriculado.')
        print('=-'*7)
    

def atualizar_notas(nome_aluno, lista_nota_aluno_matematica, lista_nota_aluno_portugues):
    if nome_aluno in boletin:
        boletin[nome_aluno]['matematica'] = lista_nota_aluno_matematica
        boletin[nome_aluno]['portugues'] = lista_nota_aluno_portugues
        print('=-'*7)
        print(boletin)
        print()
        print('Notas atualizadas.')
        print('=-'*7)
    else:
        print("="*15)
        print(f"Nenhum aluno cadastrado com esse nome: {nome_aluno}.")
        print("="*15)


def excluir_aluno(nome_aluno):
    if nome_aluno in boletin:
        del boletin[nome_aluno]
        print('=-'*7)
        print(boletin)
        print()
        print('aluno deletado.')
        print('=-'*7)
    else:
        print("="*15)
        print(f"Nenhum aluno cadastrado com esse nome: {nome_aluno}.")
        print("="*15)


def calc_media(nome_aluno):
    if nome_aluno in boletin:
        media = sum(boletin[nome_aluno]['matematica'])/len(boletin[nome_aluno]['matematica'])
        print('=-'*7)
        print(boletin[nome_aluno]['matematica'])
        print()
        print(f'Sua media em matematica é: {media}.')
        print('=-'*7)

        media = sum(boletin[nome_aluno]['portugues'])/len(boletin[nome_aluno]['portugues'])
        print('=-'*7)
        print(boletin[nome_aluno]['portugues'])
        print()
        print(f'Sua media em portugues é: {media}.')
        print('=-'*7)
    else:
        print("="*15)
        print(f"Nenhum aluno cadastrado com esse nome: {nome_aluno}.")
        print("="*15)


def save_notas():
    with open('notas_alunos.json', 'w') as f:
        json.dump(boletin, f)
    
    return print("Arquivo salvo com sucesso.")

def load_notas(boletin):
    with open('notas_alunos.json', 'r') as f:
        boletin = json.load(f)
    print(boletin)
    return boletin


while True:
    op = menu()
    if op == 1:
        lista_notas_matematica = []
        lista_notas_portugues = []
        nome_aluno = input("Digite o nome do aluno: ")
        while True:
            nota_aluno = input("Digite a nota de matematica ou -1 para sair: ")
            if nota_aluno == "-1":
                break
            else:
                if nota_aluno.isdecimal() == True:
                    nota_aluno = float(nota_aluno)
                    if nota_aluno >= 0 and nota_aluno <= 10:
                        
                        lista_notas_matematica.append(nota_aluno)
                        continue
                    else:
                        print("Nota errada.")
                        break
                elif nota_aluno.isdecimal() == False:
                    print("Só pode numero.")
                    break
        
        while True:
            nota_aluno = input("Digite a nota de portugues ou -1 para sair: ")
            if nota_aluno == '-1':
                break
            else:
                if nota_aluno.isdecimal() == True:
                    nota_aluno = float(nota_aluno)
                    if nota_aluno >= 0 and nota_aluno <= 10:
                        lista_notas_portugues.append(nota_aluno)
                        continue
                    else:
                        print("Nota errada.")
                        break
                elif nota_aluno.isdecimal() == False:
                    print("Só pode numero.")
                    break
        add_aluno_nota(nome_aluno, lista_notas_matematica, lista_notas_portugues)

    elif op == 2:
        nome_aluno = input("Digite o nome do aluno: ")
        if nome_aluno in nome_aluno:
            print(boletin[nome_aluno]['matematica'])
            print(boletin[nome_aluno]['portugues'])
            pergunta_matematica = input('Digite a nota que você queira editar de matematica ou -1 para sair, ex: 1, 2...: ')
            pergunta_portugues = input('Digite a nota que você queira editar de portugues ou -1 para sair, ex: 1, 2...: ')
            if pergunta_matematica.isdecimal() == True and pergunta_portugues.isdecimal() == True:
                pergunta_matematica = int(pergunta_matematica)-1
                pergunta_portugues = int(pergunta_portugues)-1
                if pergunta_matematica == -2 or pergunta_portugues == -2:
                    continue
                else:
                    nota_matematica = boletin[nome_aluno]['matematica']
                    nota_portugues = boletin[nome_aluno]['portugues']
                    nota_matematica[(pergunta_matematica)-1] = (float(input("Digite a nova nota de matematica: ")))
                    nota_portugues[(pergunta_portugues)-1] = (float(input("Digite a nova nota de portugues: ")))
                atualizar_notas(nome_aluno,nota_matematica, nota_portugues)
            else:        
                print("Notas invalidas.")
                continue
        else:
            print("Aluno não existe.")
            break
    
    elif op == 3:
        nome_aluno = input("Digite o nome do aluno que queira excluir: ")
        excluir_aluno(nome_aluno)
    
    elif op == 4:
        nome_aluno = input('Digite o nome do aluno que queira calcular a sua media final: ')
        calc_media(nome_aluno)

    elif op == 5:
        save_notas()

    elif op == 6:
        
        boletin = load_notas(boletin)

    elif op == 7:
        nome_aluno = input("Digite o nome do aluno que você queira vem as notas: ")
        if nome_aluno in boletin:
            boletin = boletin[nome_aluno]
            print(boletin)
        else:
            print(f"{nome_aluno} não existe.")

    elif op == 0:
        break

# nome = input('Digite a nota: ')
# nome.replace('.','').replace(',','').replace(' ','')
# verificador = nome.isalpha()
# if verificador == True:
#     print("a senha tem que ter pelo menos um numero")
# elif nome.isdecimal() == True:
#     print("Tem que ter pelo menos uma letra.")
# else:
#     print("Pronto")