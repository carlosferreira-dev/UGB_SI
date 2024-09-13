exerc4:-
    write("Digite o primeiro valor: "), read(A),
    write("Digite o segundo valor.: "), read(B),
    write("Digite o terceiro valor: "), read(C),
    eTriangulo(A, B, C), tipo(A, B, C).

    eTriangulo(A, B, C):-
        A < B + C, B < C + A, C < A + B.
    eTriangulo(_, _, _):-
        write("Nao pode formar triangulo!"), !, fail.
    
    tipo(A, A, A):-
        write("E Equilatero!").
    tipo(A, A, _):-
        write("E Isosceles!").
    tipo(A, _, A):-
        write("E Isosceles!").
    tipo(_, A, A):-
        write("E Isosceles!").
    tipo(_, _, _):-
        write("E Escaleno!").