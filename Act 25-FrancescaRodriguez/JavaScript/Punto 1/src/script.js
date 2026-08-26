/*
1-
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo.
*/

function cargar(){
    let lista=[];

    for (let i=0; i<6; i++) {
        let val=parseFloat(prompt("Ingrese la temperatura:" ));
        lista.push(val);
    }

    return lista;
}

function extremos(temperaturas) {
    let max=temperaturas[0];
    let min=temperaturas[0];

    for (let i=0; i<6; i++) {
        if (temperaturas[i]>max) {
            max = temperaturas[i];
        }

        if (temperaturas[i]<min) {
            min=temperaturas[i];
        }
    }

    return [max, min];
}

let temperaturas = cargar();

let [max, min] = extremos(temperaturas);

console.log("La máxima temperatura de las ultimas 6 horas es:", max);
console.log("La mínima temperatura de las ultimas 6 horas es:", min);