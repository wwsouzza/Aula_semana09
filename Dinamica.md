# Dinamica 1 

# Cenário A: Deixaria em branco o valor da idade. Não retirar o dado da lista, pois pode ser útil os demais dados. 
# Cenario B: Removeria as linhas correspondentes ao periodo. Como o sensor falhou não temos informações uteis a serem utilizadas.
# Cenario C: Preencheria com a média dos valores não ausentes. Colocaria a média para que possamos utilizar os demais dados dos clientes. 

# Dinamica 2

1- Com significado - fazer um grupo especifico com tais clientes 

2- Aleatória - retirar as linhas

3- Explicada - considerar colocar a media

4- Explicada - Fazer um grupo a parte para analise


Exercicio diagnostico_ausentes.py- O que foi encontrado:

1 - Faltam valores conforme a seguir:
area_m2               28
idade_anos            63
condicao              47
distancia_praia_km    20
Obs.: Pode se verificar a falta de valores mais acentuadamente para idade_anos e Condição


2- Existem ausentes disfarçados conforme a seguir:

condicao
NaN     47
Ruim    36
N/D      5
?        4

Idade_anos minima
-1.0

area_m2
s/i    5


3- Verificando novamente os ausentes utilizando o na_values e replace temos o seguinte:

area_m2               33
idade_anos            69
condicao              56
distancia_praia_km    20

Obs.: podemos observar um aumento de ausentes em todos os rotulos com exceção da distancia_praia_km.


4- Agrupando os ausentes de idde_anos por tipo em porcentagem, temos: 

Apartamento     8.1
Casa           20.2
Cobertura       2.8
Studio          4.8

Obs.: verificamos no tipo casa um valor bem maior de ausências.



# prever a saida 

Primeira pergunta - [1.0,2.0,3.0,2.0]

Segunda pergunta - 2.0 , 2, 2


