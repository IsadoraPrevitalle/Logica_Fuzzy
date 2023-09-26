# Logica Fuzzy

A lógica fuzzy, também conhecida como lógica difusa ou nebulosa é a forma de lógica multivalorada que tenta modelar o senso de palavras ou senso comum para tomada de decisões. Ela trabalha com uma grande variedade de informações vagas e incertas, permitindo tratar estados imprecisos e aspectos incertos da informação.
A lógica fuzzy contraria a lógica boolena, enquanto uma admite apenas valores de verdadeiro ou falso (0 ou 1), a fuzzy trata de valores que variam nesse intervalo (0 a 1).

# Funcionamento
A lógica fuzzy visa encontrar o "meio termo" de uma função com base em variáveis linguisticas e regras condicionais.
As variáveis linguisticas são expressões que modela o senso de palavras, por exemplo, ao pensar em um copo de suco e, ao dizer q ele está cheio pode-se inferir, pela lógica boolena, que ele representa 1, já vazio representa 0. Na lógica difusa as possibilidades para o nível de suco no copo pode ser expressa como meio cheio, meio vazio, quase cheio ou quase vazio. Essas demais expressões são nomeadas como as variáveis linguisticas.
Além desse conceito, também é levado em consideração as regras condicionais que vão influenciar as variaveis linguisticas. 
Por exemplo, ao dizer que "o copo só está cheio se maria está com sede" pode-se compreender que essa frase é uma regra para induzir o nível de liquido no copo.

# Exemplo prático
Tomemos como exemplo um estudo de caso para descobrir o valor de uma gorjeta com base na avaliação do cliente em um restaurante, tendo como variaveis linguisticas o agrado com a comida e com o serviçlo prestado no estabelecimento.
O primeiro passo é determinar quais serão as varivéis linguísticas de entrada (antecedente):
- Serviço: que nota você daria para o serviço, em uma escala de 0 a 10? (ruim, aceitavel, ótimo)
- Qualidade da Comida: quão boa estava a comida, em uma escala de 0 a 10? (ruim, boa, saborosa)

Em seguida é necessário determinar quais serão as variáveis de saída (consequentes):
- Gorjetas: quanta gorjeta você daria, entre 0% e 20%? (media, baixa, alta)

Por fim é preciso estabelecer as regras condicionais, dizemos então que:
- Se a qualidade da commida for RUIM e o serviço for RUIM então gorjeta será BAIXA
- Se o serviço for ACEITAVEL então a gorjeta será MEDIA
- Se o serviço for OTIMO e a qualidade da comida for SABOROSA então a gorjeta será ALTA
