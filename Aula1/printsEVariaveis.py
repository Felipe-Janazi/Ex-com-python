#  A funcao HELP e utilizada para entendermos o como funciona cada comando:
# help()
# E apos abrir o terminal do HELP voce informa qual comenaod voce deseja verificar



# Com a funcao print podemos fazer com que seja printado na tela alguma informacao
print("Brasil ganhou 5 títulos mundiais")
# Brasil ganhou 5 títulos mundiais


# mas dentro deste print podemos usar funcoes a mais, como o sep="" que ira colocar algo entra os valores do print
print("Brasil", "ganhou", 5, "títulos mundiais", sep="_")
# Brasil_ganhou_5_títulos mundiais!


# com o end="/n" ele quebra a linha igual a um br, fazendo com que vá para a linha abaixo no terminal ou qualquer outra informacao que vai aparecer no final
print("Brasil ganhou 5 títulos mundiais", end="___\n") 
# Brasil ganhou 5 títulos mundiais___"


# \n serve para quebrar linha quando está dentro de uma frase no print


# Para deixar o nome do país e a quantidade de títulos dinâmicos:
pais = "Alemanha"
print(type(pais))
quantidade = 4
print(type(quantidade))

print(pais, "ganhou", quantidade, "títulos mundiais")


# no mundo python vc não precisa definir o tempo explicitamente alem de poder mudar dinamicamente o seu tipo
pais = "Brasil"
print(type(pais))
pais = 15
print(type(pais))

# Além de que o python utiliza por padrão a linguagem Snake_Case, colocando "_" entre as palavras dos nomes de variaveis