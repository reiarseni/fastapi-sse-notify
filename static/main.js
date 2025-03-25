document.addEventListener("DOMContentLoaded", function() {
    const notificationsList = document.getElementById("notifications");
    // Conexión al endpoint SSE utilizando el parámetro userId
    const evtSource = new EventSource(`/notifications?user_id=${userId}`);

    evtSource.onmessage = function(event) {
        const data = JSON.parse(event.data);
        const li = document.createElement("li");
        li.className = "list-group-item";
        li.textContent = `${data.timestamp}: ${data.message}`;
        // Agregar la nueva notificación al inicio de la lista
        notificationsList.prepend(li);
    };

    evtSource.onerror = function(err) {
        console.error("Error en EventSource:", err);
        // La reconexión automática es gestionada por el navegador
    };
});

