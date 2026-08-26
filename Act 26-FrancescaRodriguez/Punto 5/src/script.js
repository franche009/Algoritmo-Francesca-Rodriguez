/*
  Ejercicio 05: Control de Temperatura
  -----------------------------------------------
  Conceptos del documento aplicados:
  - querySelector(): para seleccionar elementos usando selectores CSS,
    como alternativa a getElementById().
  - textContent: para mostrar el mensaje de resultado sin interpretar HTML.
  - Date(): para registrar la fecha y hora exacta de cada verificación.
*/

let inputTemp = document.getElementById("inputTemp");
let btnVerificarTemp = document.getElementById("btnVerificarTemp");
let resultadoTemp = document.getElementById("resultadoTemp");

btnVerificarTemp.addEventListener("click", function(){
  let temp = parseFloat(inputTemp.value);
  if (isNaN(temp)) {
    resultadoTemp.textContent = "Por favor ingresa un número válido";
    resultadoTemp.style.color = "orange";
    return;
  }

  let mensaje, color;
  if (temp < 10) {
    mensaje = "Hace frío";
    color = "blue";
  } else if (temp <= 25) {
    mensaje = "Clima agradable";
    color = "green";
  } else {
    mensaje = "Hace calor";
    color = "red";
  }

  resultadoTemp.textContent = mensaje;
  resultadoTemp.style.color = color;

  console.log(`Verificación de temperatura (${temp}°C): ${mensaje} - ${new Date()}`);
});