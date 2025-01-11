exerc2:-
    write("Digite o valor do lado quadrado: "), read(Lado),
    Perimetro is (Lado * 4),
    Area is (Lado ** 2),
    Diag is sqrt(2 * Lado ** 2),
    write("Perimetro: "), write(Perimetro), nl,
    write("Area.....: "), write(Area), nl,
    write("Diagonal.: "), write(Diag).