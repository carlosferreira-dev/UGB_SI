exerc5:-
    write("Digite o primeiro valor: "), read(A),
    write("Digite o segundo valor.: "), read(B),
    write("Digite o terceiro valor: "), read(C),
    eEqSegundoGrau(A), 
    Delta is (B ** 2 - 4 * A * C),
    raizes(A, B, C, Delta).

    eEqSegundoGrau(0):-
        write("Nao e equacao do segundo grau!"), !, fail.
    eEqSegundoGrau(_).
    raizes(_, _, _, Delta):-
        Delta < 0, write("Nao existe raiz").
    raizes(A, B, C, Delta):-
        R1 is (-B + sqrt(Delta)) / 2 * A, write("Raiz 1: "), format('~2f', [R1]), nl,
            raizes2(A, B, C, Delta).
    raizes2(_, _, _, 0).
    raizes2(A, B, C, Delta):-
        R2 is (-B - sqrt(Delta)) / 2 * A, write("Raiz 2: "), format('~2f', [R2]).