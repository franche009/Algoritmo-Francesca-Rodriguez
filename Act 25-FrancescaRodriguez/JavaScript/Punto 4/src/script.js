/*
4-
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
 Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
sea menor o igual a 10 unidades para emitir un aviso de compra urgente.
*/

function cargar() {
    let inventario = [];
    for (let i=0; i<5; i++) {
        let nombre=String(prompt("Ingrese el nombre del artículo:"));
        let precio=parseFloat(prompt("Ingrese el precio:"));
        let stock=parseInt(prompt("Ingrese el stock:"));
        let articulo = [nombre, precio, stock];
        inventario.push(articulo);
    }
    return inventario;
}


function imprimir(inventario) {
    console.log("-- INVENTARIO --")
    for (let [nombre, precio, stock] of inventario) {
        console.log("Artículo:", nombre);
        console.log("Precio:", precio);
        console.log("Stock:", stock);
    }
}


function valor(inventario) {
    let total=0;
    for (let [nombre, precio, stock] of inventario) {
        total=total+precio*stock;
    }

    console.log("El valor total del inventario es:", total);
}


function alerta(inventario) {
    for (let [nombre, precio, stock] of inventario) {
        if (stock <= 10) {
            console.log("Es necesario reponer", nombre);
        }
    }
}


let inventario = cargar();
imprimir(inventario);
valor(inventario);
alerta(inventario);