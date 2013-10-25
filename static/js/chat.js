$(document).ready(function() {
    var url = "ws://127.0.0.1:8080/websocket";
    var socket;  
    if (!window.WebSocket) {  
        window.WebSocket = window.MozWebSocket;  
    }  

    // Javascript Websocket Client  
    if (window.WebSocket) {  
        socket = new WebSocket(url);  
        socket.onmessage = function(event) {  
            var ta = document.getElementById('responseText');  
            ta.value = ta.value + '\n' + event.data  
        };  

        socket.onopen = function(event) {  
            var ta = document.getElementById('responseText');  
            ta.value = "Web Socket opened!";  
        };  

        socket.onclose = function(event) {  
            var ta = document.getElementById('responseText');  
            ta.value = ta.value + "Web Socket closed";  
        };  
    } else {  
        alert("Your browser does not support Web Socket.");  
    }  

    // Send Websocket data  

    function send(message) {  
        if (!window.WebSocket) {
            return;
        }  
        if (socket.readyState == WebSocket.OPEN) {  
            socket.send(message);  
        } else {  
            alert("The socket is not open.");  
        }  
    }  

    $("#sendmsg").click(function() {
        send($("#chat-input").val());
    });
});
