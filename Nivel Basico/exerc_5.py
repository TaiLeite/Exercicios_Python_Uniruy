'''Média de Notas
Peça ao usuário para inserir três notas e calcule a média. Informe se o aluno foi aprovado (média
>= 7) ou reprovado.'''


nota1 = float(input("Digite a primeira nota:" ))
nota2 = float(input("Digite a segunda nota:" ))
nota3 = float(input("Digite a terceira nota:" ))

media = (nota1 + nota2 + nota3)/3

if media >= 7 :
    print(f"A media do aluno eh{media:.2f}, aluno aprovado")
elif media >5 and media <7:
    print(f" A media do aluno eh {media:.2f}, aluno esta na recupareacao")
else: print(f" A media do aluno eh {media:.2f}, aluno reprovado")

