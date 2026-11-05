const API_URL = "http://127.0.0.1:8000";

let carrito = JSON.parse(localStorage.getItem("chuzo_carrito")) || [];

document.addEventListener("DOMContentLoaded", () => {
    console.log("¡El chuzo de Bastian esta listo para vender!");

    // Recalcular en vivo cada vez que el usuario suba o baje la cantidad
    document.getElementById("cantidad").addEventListener("input", calcularTotal);
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
    return total;
}

document.getElementById("form-pedido").addEventListener("submit", async (e) => {
    e.preventDefault();

    const precio = parseFloat(document.getElementById("precio").value) || 0;
    const cantidad = parseInt(document.getElementById("cantidad").value) || 1;
    const total = precio * cantidad;

    const nuevoPedido = {
        cliente: document.getElementById("cliente").value,
        producto: document.getElementById("producto").value,
        precio: precio,
        cantidad: cantidad,
        total: total
    };

    try {
        const respuesta = await fetch(`${API_URL}/pedido`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(nuevoPedido)
        }); 

        const data = await respuesta.json();
        if (respuesta.ok) {
            alert(`✅ ¡Pedido marchado a la cocina con éxito! Total: $${total.toLocaleString()}`);
            carrito.push(data);
            localStorage.setItem("chuzo_carrito", JSON.stringify(carrito));
            document.getElementById("form-pedido").reset();
            document.getElementById("total-cuenta").textContent = "Total: $0";
        } else {
            alert(`Error al realizar el pedido: ${data.detail || "Error desconocido"}`);
        }
    } catch (error) {
        console.error("Error al realizar el pedido:", error);
        alert("❌ No se pudo conectar con el servidor.");
    }
});
