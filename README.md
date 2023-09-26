# Lógica Fuzzy

A lógica fuzzy, também conhecida como lógica difusa ou nebulosa, é uma forma de lógica multivalorada que tenta modelar o senso de palavras ou senso comum para tomada de decisões. Ela trabalha com uma grande variedade de informações vagas e incertas, permitindo tratar estados imprecisos e aspectos incertos da informação.
A lógica fuzzy contrasta com a lógica booleana, enquanto esta admite apenas valores de verdadeiro ou falso (0 ou 1), a fuzzy trata de valores que variam nesse intervalo (0 a 1).

# Funcionamento
A lógica fuzzy visa encontrar o "meio termo" de uma função com base em variáveis linguísticas e regras condicionais.
As variáveis linguísticas são expressões que modelam o senso de palavras, por exemplo, ao pensar em um copo de suco e ao dizer que ele está cheio, pode-se inferir, pela lógica booleana, que ele representa 1, já vazio representa 0. Na lógica difusa, as possibilidades para o nível de suco no copo podem ser expressas como meio cheio, meio vazio, quase cheio ou quase vazio. Essas demais expressões são nomeadas como as variáveis linguísticas.
Além desse conceito, também é levada em consideração as regras condicionais que vão influenciar as variáveis linguísticas. 
Por exemplo, ao dizer que "o copo só está cheio se Maria está com sede", pode-se compreender que essa frase é uma regra para induzir o nível de líquido no copo.

# Exemplo prático
Tomemos como exemplo um estudo de caso para descobrir o valor de uma gorjeta com base na avaliação do cliente em um restaurante, tendo como variáveis linguísticas o agrado com a comida e com o serviço prestado no estabelecimento.
O primeiro passo é determinar quais serão as variáveis linguísticas de entrada (antecedentes):
- Serviço: que nota você daria para o serviço, em uma escala de 0 a 10? (ruim, aceitável, ótimo)
- Qualidade da Comida: quão boa estava a comida, em uma escala de 0 a 10? (ruim, boa, saborosa)

Em seguida, é necessário determinar quais serão as variáveis de saída (consequentes):
- Gorjetas: quanto de gorjeta você daria, entre 0% e 20%? (média, baixa, alta)

Por fim, é preciso estabelecer as regras condicionais, dizemos então que:
- Se a qualidade da comida for RUIM e o serviço for RUIM, então a gorjeta será BAIXA.
- Se o serviço for ACEITÁVEL, então a gorjeta será MÉDIA.
- Se o serviço for ÓTIMO e a qualidade da comida for SABOROSA, então a gorjeta será ALTA.

Para gerar o resultado ou previsão, é executado o processo de defuzzificação. Uma das maneiras de realizar esse processo é por meio da defuzzificação por centroide, que funciona da seguinte maneira:

Dada a figura:

![image](https://github.com/IsadoraPrevitalle/Logica_Fuzzy/assets/104457205/84b5aec2-eef8-4d31-a0e5-5fd4af8c85cb)

Para realizar o processo de defuzzificação, é necessário calcular o eixo central das áreas, pelo centroide definido como a mediana de 0 a 7 e a mediana de 5 e 12.

Em seguida, é realizado o cálculo do trapézio, analisando a base menor e maior do eixo X, levando em consideração o grau de pertinência do eixo Y.

Dando continuidade, é feito o cálculo da área para a variável linguística "muito frio" e "frio" através da fórmula: *grau de pertinência * (base menor + base maior)/2*.

Com o resultado do cálculo das áreas, basta calcular a média ponderada do centroide, através da fórmula: *(Eixo X "Muito frio" * cálculo área muito frio + Eixo X "Frio" * cálculo da área frio) / (cálculo da área muito frio + cálculo da área frio)*.























