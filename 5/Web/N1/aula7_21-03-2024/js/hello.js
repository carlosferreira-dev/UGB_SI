/*
comentar mais de uma linha
*/

// comentar uma linha
var mensagem = "Olá mundo";
mensagem = document.querySelector("h1");
console.log(mensagem);
var novo = document.querySelector('.novo');
console.log('Novo: ', novo);
//console.log('Novo: ', novo.textContent);
//console.log('Novo: ', novo.innerHTML);
//novo.textContent = 'Novo valor';
var texto = document.querySelector('#texto');
console.log('Texto: ', texto);
console.log('Texto: ', texto.textContent);
var mes = document.querySelectorAll('.mes');
console.log('mes', mes[0].textContent);
console.log('mes', mes[1].innerHTML);
console.log('mes', mes[2].textContent);
console.log('mes', mes[3].innerText);


function mostraAlerta() {
    alert("Funciona!");
}

// obtendo um elemento através de um seletor de ID
var botao = document.querySelector("#botaoEnviar");
botao.onclick = mostraAlerta;