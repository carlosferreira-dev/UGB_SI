/*/
 * Exercício 1
/*/

using ConceitosBasicos;

int n1 = 20;
int n2 = 11, result;
Somador soma;
soma = new Somador();
result = soma.Soma(n1, n2);
Console.WriteLine($"A soma dos números {n1} + {n2} é {result}");

/*/
 * Exercício 2
/*/

double metros = 10.45;
Console.WriteLine($"A medida de {metros} corresponde a {Conversor.MetrosMilimetros(metros)} milimetros");

/*/
 * Exercício 14 static
/*/

double valor_atual = 500.50;
int percentual = 10;
Console.WriteLine($"Valor atual:{valor_atual} - Percentual de desconto: {percentual} - Valor do desconto: {(CalculaDesconto.Desconto(valor_atual, percentual))} - Valor final da mercadoria: {valor_atual - (CalculaDesconto.Desconto(valor_atual, percentual))}");
