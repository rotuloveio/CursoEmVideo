# Dentro do pacote utilidadesCeV criado no DESAFIO 111, temos o módulo chamado dado.
# Crie uma função chamada leiadinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de
# dados para aceitar valores que sejam monetários.
from utilidadesCeV import moeda, dado

moeda.resumo(dado.leiadinheiro('Digite o preço: R$'), 35, 22)
