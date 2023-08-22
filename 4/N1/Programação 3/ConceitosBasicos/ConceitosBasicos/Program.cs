using ConceitosBasicos;

int n1 = 20;
int n2 = 11, result;
Somador soma;
soma = new Somador();
result = soma.Soma(n1, n2);
Console.WriteLine($"A soma dos números {n1} + {n2} é {result}");

/*/
 * 
/*/

double metros = 10.45;
Console.WriteLine($"A medida de {metros} corresponde a {Conversor.MetrosMilimetros(metros)}");

/*/
 * 
/*/

