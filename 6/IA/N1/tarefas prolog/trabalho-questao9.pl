exerc9 :-
    write("Primeiro valor: "), read(N1), nl,
    write("Segundo valor: "), read(N2), nl,
    write("Terceiro valor: "), read(N3), nl,
    maior(N1, N2, N3).

maior(N1, N2, N3) :-
    (N1 >= N2, N1 >= N3 ->
        write("O maior numero e: "), write(N1)
    ; N2 >= N1, N2 >= N3 ->
        write("O maior numero e: "), write(N2)
    ; write("O maior numero e: "), write(N3)
    ).