/*3. Solicitar que se ingrese el nombre y la clave de un usuario. Mostrar una ventana de
alerta si en la clave se ingresan menos de 7 caracteres o más de 20 (capturar el evento
onBlur) */

function validar(){
    let clave=document.getElementById('contraseña').value.length;
    if(clave<7 || clave>20){
        alert('Largo de clave incorrecta, ingresar entre 7 y 20 caracteres');
    }
    else{
        alert('Datos ingresados correctamente')
    }
}