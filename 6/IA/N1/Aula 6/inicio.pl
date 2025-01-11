animal(zebra).
animal(leao).
animal(elefante).
vegetal(capim).
vegetal(folha).
come(zebra, capim).
come(leao, zebra).
come(elefante, folha).
herbivoro(X):-come(X, Y), vegetal(Y).
carnivoro(X):-come(X, Y), animal(Y).

ex1:-write("Hello World").

ex2:-write("Digite o seu nome: "),
    read(Nome), write(Nome),
    write(" e um nome bonito.").

ex3:-write("Digite o primeiro valor: "), read(A),
    write("Digite o segundo valor: "), read(B),
    S is A + B, write("Soma.....: "), write(S), nl,
    D is A - B, write("Diferenca: "), write(D), nl,
    P is A * B, write("Produto:.: "), write(P), nl,
    quociente(A, B).
    quociente(_, 0):-write("Nao existe divisao por 0").
    quociente(A, B):-Q is A / B, write("Quociente: "), write(Q).