# Python - Udemy
- 13/05/2026

## Seção 3 - Iniciando na programação com Python (Lógica de programação básica)

### Interpretador Python + cmentários de código

> #### **Comentários**
>
> - Importante para explicar uma linha de código.
> - É importante explicar o código om comentário pois alem de nos nem sempre lembrarmos o que estávamos pensando quando escrevemos ele, outras pessoas podem ter que trabalhar com o código que criamos, e ninguem é obrigado a saber o que se passava pela nosso cabaça quando escrevemos, né.
> Além disso, o interpretador ignora o que está escrito no comentário. Podem ser escritos acima, abaixo ou na frente da linha de código.
>
> - Existem dois tipos de comentário em Python
    >   - (#) - O comentário só funciona na mesma linha em que a cerquilha .
    >   - (""" """) - Não é extatamante um comentario já que o interpretador lê o que esta escrito, mas é utilizado em alguns casos caso queira ser feito um comentário multilinha. É chamado de DOCSTRING. Pode ser usado aspas duplas ou simples.

> - print(1 + 1) - Imprimir na tela

___
___

- 14/05/2026

> #### **Tipos de dados**
>
> - Python - Linguagem de programação
> - Tipo de tipagem - Dinâmica / Forte
>   - Tipagem dinâmica
>       - " É uma caracteristica de linguagens de programação onde o tipo de um dado de uma variável (número , texto, booleano)é verificado e definido em tempo de execução (runtime), e não durante a compilação. Isso permite que variáveis udem de tipo ao lngo o código sem declaração prévia " - Alura<br /><br /> Ou seja, o Python já sabe o tipo da informação que estams passando para ele.<br /><br />
>   - Tipagem Forte
>       - " É um conceito em linguagens de programação onde o tipo de dado de uma variavel é estritamente respeitado, proibindo operações entre tipos incompatíveis (como somar número e texto) sem conversão explícita. Ela garante maior seguranç e estabilidade, reduzindo bugs, pois impede coversões automáticas indesejadas " - IBM<br /><br />
>
>#### **Tipo STRING**
> - str -> string -> texto
> - Strings são textos que estão dentro de aspas
>   - Essas aspas podem ser
>       - Aspas simples ('')
>           - print('abc')
>       - Aspas duplas ("")
>           - print("abc")

>
><br><br/>
><br><br/>
> Não é possivel usar aspas dentro de uma string (print("Heloisa " Duarte")). Para isso é usado um caractere **escape**.
> - " **Uma sequência de escape** é uma combinação de caracteres, iniciada por uma barra invertida ( \ ), sada em programação para representar caracteres especiais, não impriíveis ou de controle dentro de uma string (texto). Ela altera o significado do caractere seguinte para que o compilador o interprete de forma especial. " - IBM
>   - print("Heloisa \ "Duarte")
><br><br/>
> - Caso, por algum motivo, você queira que a " \ " apareça, exite o prefixo **r**.
>   - " O refixo **r** ou **R** antes de uma string em Python define uma **raw string** (strin bruta). Ele diz ao Pythn para tratar arras invertidas ( \ ) como caracteres literais, ignorando **sequências de escape**( como \n para nova linha ou \t para tabulação). É amplamente usado para caminhos de arquivose expressões regulares."
>       - print(r"Heloisa \ " Duarte \ " ")
>
> Mas, para evitar uma confusão no código, basta usar um truque e por aspas simples junto com as aspas duplas ( até porque, asim fica muito menos desorganizado e bagunçado ).
>   - print('Heloisa "Duarte" ')
><br><br/>
>#### **Tipo INT e FLOAT**
> - int -> Números inteiros
> - O ipo **int** representa qualquer número positivo ou negativo. **int** sem inal é considerado positivo.
>   - print(11) - int
>   - print(-11) - int
><br><br/>
> - float - Número de ponto flutuante
> - O tipo **float** representa qualquer números positivo ou negativo com ponto flutuante. **float** sem sinal é considerado positivo.
>   - print(1.1) - float
>   - print(10.11) - float
>
> **OBS: Função TYPE**
> -  A **função type** mostra o tipo que o Python inferiu ao valor
>   - O **type**, na verdade, é uma **classe**, mas como se inicia com lera minúscula ( que não é padrao das classes, pois elas iniciam com maiúscula), é chamada de **função** por costume ( já que as funções são iniciadas por letras minúsculas ).
>       - print(type("Heloisa"))