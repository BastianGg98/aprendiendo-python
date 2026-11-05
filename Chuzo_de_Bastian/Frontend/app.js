const API_URL = "http://127.0.0.1:8000";

let carrito = JSON.parse(localStorage.getItem("chuzo_carrito")) || [];

document.addEventListener("DOMContentLoaded", () => {
    console.log("¡El chuzo de Bastian esta listo para vender!");

    // Recalcular en vivo cada vez que el usuario suba o baje la cantidad
    document.getElementById("cantidad").addEventListener("input", calcularTotal);
    cargarPedidosCocina();
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

async function cargarPedidosCocina() {
    try {
        const respuesta = await fetch(`${API_URL}/pedidos`);
        const data = await respuesta.json();
        const contenedor = document.getElementById("lista-comandas");
        contenedor.innerHTML = ""; // Limpiar antes de agregar

        if (data.pedidos.length === 0) {
            contenedor.innerHTML = `<p class="sin-comandas">No hay pedidos pendientes en la cocina 😴</p>`;
            return;
        }
        data.pedidos.forEach((pedido, index) => {
            const tarjeta = document.createElement("div");
            tarjeta.className = "tarjeta-comanda";
            tarjeta.innerHTML = `
                <div class="comanda-header">
                    <span class="comanda-cliente">👤 ${pedido.cliente}</span>
                    <span class="comanda-badge">Mesa #${index + 1}</span>
                </div>
                <div class="comanda-producto">🍔 <strong>${pedido.producto}</strong></div>
                <div class="comanda-detalle">
                    <span>Cant: ${pedido.cantidad} x $${pedido.precio.toLocaleString()}</span>
                    <span class="comanda-total">$${pedido.total.toLocaleString()}</span>
                </div>
                    <button class="btn-despachar" onclick="despacharPedido(${index})">
                    ✅ ¡Despachar Pedido!
                    </button>
            `;
            contenedor.appendChild(tarjeta);
        });
    } catch (error) {
        console.error("Error cargando pedidos:", error);
    }
}

async function despacharPedido(index) {
    try {
        const respuesta = await fetch(`${API_URL}/pedido/${index}`, {
            method: "DELETE"
        });
        const data = await respuesta.json();
        if (respuesta.ok) {
            alert(`✅ ${data.mensaje}: ${data.pedidoEntregado.producto}`);
            cargarPedidosCocina(); // 👈 Esto borra la tarjeta de la pantalla en vivo
        } else {
            alert(`❌ Error: ${data.detail}`);
        }
    } catch (error) {
        console.error("Error al despachar pedido:", error);
        alert("❌ No se pudo conectar con el servidor.");
    }
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
            cargarPedidosCocina();
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


