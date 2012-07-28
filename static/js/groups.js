$(document).ready(function () {

    $('#grupos .crear-grupo').click(function () {
        $('#contenido-grupo').html('');
        $.ajax({
            url:'/create-group',
            data:'GET',
            success:function (data) {
                $('#contenido-grupo').html('');
                $('#contenido-grupo').html(data);
                $('#form-crear-grupo form').submit(function () {
                    $.ajax({
                        url:$('#form-crear-grupo form').attr('action'),
                        data:$('#form-crear-grupo form').serialize(),
                        type:'POST',
                        success:function (data) {
                            console.log(data);
                        }
                    });
                    return false;
                });
            }
        });
    });

    $('#grupos .buscar-client').click(function () {
        $.ajax({
            url:'/groups/find-client',
            data:'GET',
            success:function (data) {
                $('#contenido-grupo').html('');
                $('#contenido-grupo').html(data);
                var grupos = document.querySelectorAll('#grupos .un-grupo');
                console.log(grupos);
                [].forEach.call(grupos, function (col) {
                    console.log("VOLO 1");
                    col.addEventListener('dragenter', handleDragEnter, false);
                    console.log("VOLO 2");
                    col.addEventListener('dragleave', handleDragLeave, false);
                    col.addEventListener('drop', handleDrop, false);
                    col.addEventListener('dragend', handleDragEnd, false);
                    col.addEventListener('dragover', handleDragOver, false);
                    console.log("VOLO");
                });
                console.log("se buscaron clientes");

                var clientes = document.querySelectorAll('#contenido-grupo .listado li');
                console.log(clientes);
                [].forEach.call(clientes, function (col) {
                    console.log("esta entrado=");
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
            }
        });

    });
    $('#nombre').keyup(function () {
        var valor = $(this).val();
        console.log(valor);
        $.ajax({
            url:'/get-client/?name=' + valor,
            type:'GET',
            dataType:'json',
            success:function (data) {
                $('#contenido-grupo .alt').html('');
                for (i in data) {
                    $('#contenido-grupo .alt').append('<li draggable="true" iduser=' + data[i].pk + '>' + data[i].fields.first_name + ' ' + data[i].fields.last_name + '</li>');
                }
            }
        });
    });
});

(function ($) {
    $(window).load(function () {
        $("#grupos").mCustomScrollbar({
            scrollButtons:{
                enable:true
            }
        });
    });
})(jQuery);