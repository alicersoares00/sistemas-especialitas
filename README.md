**Sistema Especialista de Identificação de Cogumelos**

**Sobre o projeto**
Este projeto implementa em Python um sistema especialista para identificação de cogumelos e análise de sua periculosidade à saúde.
A ideia é simular o raciocínio de um especialista humano, utilizando uma base de conhecimento e regras de inferência para chegar a conclusões.

**O que são sistemas especialistas?**
Um sistema especialista é um programa que busca reproduzir a capacidade de decisão de um especialista em um domínio específico.
Ele se baseia em dois componentes principais:

1. Base de conhecimento: conjunto de fatos e regras sobre o domínio (neste caso, cogumelos).
2. Mecanismo de inferência: lógica que aplica as regras aos fatos para gerar conclusões.
3. Exemplos reais de sistemas especialistas incluem diagnósticos médicos, manutenção industrial e suporte técnico.

**Funcionalidades implementadas**
O sistema possui um menu interativo com três opções:

1.Encontrar cogumelo pelas características: o usuário fornece características (ex.: "chapeu marrom, anel presente"). O sistema calcula o nível de compatibilidade e explica quais características coincidem ou faltam.

2.Pesquisar por cogumelo específico: busca por nome completo ou parcial (ex.: "cubensis" encontra "Psilocybe cubensis").

3.Estimar probabilidade de ser perigoso à saúde: sistema retorna os 3 cogumelos mais compatíveis e calcula a chance de serem perigosos.


**🖥️ Exemplo de uso**
Opção 1
Entrada:
chapeu marrom, anel presente

Saída:
Amanita pantherina - Venenoso (100.0%)
Coincidentes: ['chapeu marrom', 'anel presente']
Faltantes: []

Opção 2
Entrada:
cubensis

Saída:
Nome: Psilocybe cubensis
Toxicidade: Alucinogeno
Características: azula ao toque, cresce em esterco, chapeu dourado, anel persistente

Opção 3
Entrada:
chapeu marrom, anel presente

Saída:
Probabilidade estimada de ser perigoso à saúde: 33.3%


*Como executar*
Clone o repositório:

bash
git clone https://github.com/seuusuario/sistemas-especialistas.git

Entre na pasta:
bash
cd sistemas-especialistas

Execute o programa:
bash
python sistemas_int.py


📌 Conclusão
Este projeto demonstra como sistemas especialistas podem ser aplicados em domínios práticos, auxiliando na tomada de decisão.
Ele organiza informações complexas e fornece respostas claras ao usuário, simulando o raciocínio de um especialista humano.
