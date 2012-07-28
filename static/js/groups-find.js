$('#contenido-grupo').ready(function () {

    var grupos = document.querySelectorAll('#grupos .un-grupo');
    [].forEach.call(grupos, function (col) {
        col.addEventListener('dragenter', handleDragEnter, false)
        col.addEventListener('dragleave', handleDragLeave, false);
        col.addEventListener('drop', handleDrop, false);
        col.addEventListener('dragend', handleDragEnd, false);
        col.addEventListener('dragover', handleDragOver, false);
    });

    var clientes = document.querySelectorAll('#contenido-grupo .listado li');
    [].forEach.call(clientes, function (col) {
        col.addEventListener('dragstart', handleDragStart, false);
        col.addEventListener('dragover', handleDragOver, false);
        col.addEventListener('dragend', handleDragEnd, false);
    });


    $('#nombre').keyup(function () {
        var valor = $(this).val();
        $.ajax({
            url:'/get-client/?name=' + valor,
            type:'GET',
            dataType:'json',
            success:function (data) {
                console.log(data);
                $('#contenido-grupo .alt').html('');
                for (i in data) {
                    $('#contenido-grupo .alt').append('<li draggable="true" iduser=' + data[i].pk + '>' + data[i].fields.first_name + ' ' + data[i].fields.last_name + '</li>');
                }
            }
        });
    });
});