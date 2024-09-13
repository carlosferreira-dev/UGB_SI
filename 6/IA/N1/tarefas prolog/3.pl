exerc3:-
    write("Digite o raio da circunferencia : "), read(Raio),
    Diametro is (Raio * 2),
    Perimetro is (pi * Raio * 2),
    Area is (pi * Raio ** 2),
    write("Diametro..: "), write(Diametro), nl,
    write("Perimetro.: "), write(Perimetro), nl,
    write("Area......: "), format('~2f', [Area]).