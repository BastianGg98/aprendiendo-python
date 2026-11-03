const API_URL = "http://127.0.0.1:8000";

let carrito = JSON.parse(localStorage.getItem("chuzo_carrito")) || [];

document.addEventListener("DOMContentLoaded", () => {
    console.log("¡El chuzo de Bastian esta listo para vender!");
});


function seleccionarProducto(nombre, precio){
    document.getElementById("producto").value = nombre;
    document.getElementById("precio").value = precio;
    calcularTotal();
}

function calcularTotal(){
    const precio = Number(document.getElementById("precio").value) || 0;
    const cantidad = Number(document.getElementById("cantidad").value) || 1;
    const total = precio * cantidad;
    document.getElementById("total-cuenta").textContent = `Total: $${total.toLocaleString()}`;
}

