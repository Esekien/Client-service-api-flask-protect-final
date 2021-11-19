function init() {
    var delete2 = document.getElementById("delete2");

    delete2.onclick = function (e) {
        var valorBoton = $('#delete2').val();
        console.log(valorBoton)
        var data1 = {"v1":A, "v2":B, "operacion":operacion}
        $.ajax({
            url: '/',
            data : JSON.stringify(data1),
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            success: function(post){
                console.log('bien');
                resetear();
                resultado.textContent=post;//Devuelve el resultado guardado en rest
            },
            error: function(error){
                console.log(error);
            }
        })
    }
}