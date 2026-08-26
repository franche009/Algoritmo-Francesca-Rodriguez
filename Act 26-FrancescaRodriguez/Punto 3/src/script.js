/*Ejercicio 03: Simulador de Votación en Línea
Plantear una página con 3 botones, cada uno representando un candidato distinto.
Al hacer clic en uno de los botones, se deberá aumentar el contador de votos de ese
candidato y mostrar el total actualizado en pantalla.
Además:
 El sistema debe mostrar en consola quién va ganando cada vez que se registra
un voto.
 Si hay un empate, debe mostrar el mensaje “Hay un empate”. */


let numerogato=0;
let numeroerizo=0;
let numeroperro=0;
let aux=1;


let botongato = document.getElementById("botongato")
botongato.addEventListener("click", function(){
    numerogato=numerogato+aux;
    console.log("Votos totales del candidato gato: ", numerogato);
    compararVotos();
});



let botonerizo = document.getElementById("botonerizo")
botonerizo.addEventListener("click", function(){
    numeroerizo=numeroerizo+aux;
    console.log("Votos totales del candidato erizo: ", numeroerizo)
    compararVotos();
});



let botonperro = document.getElementById("botonperro")
botonperro.addEventListener("click", function(){
    numeroperro=numeroperro+aux;
    console.log("Votos totales del candidato perro: ", numeroperro)
    compararVotos();
});

function compararVotos(){
    if(numerogato>numeroerizo && numerogato>numeroperro){
    console.log("Va ganando el candidato gato");
}
    else if(numeroerizo>numerogato && numeroerizo>numeroperro){
        console.log("Va ganando el candidato erizo");
    }
    else if(numeroperro>numerogato && numeroperro>numeroerizo){
        console.log("Va ganando el candidato perro");
    }
    else if(numerogato==numeroerizo || numeroerizo==numeroperro || numeroperro==numerogato){
        console.log("Hay un empate")
    }
}