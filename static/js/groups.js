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
                    console.log("se intenta crear");
                    $.ajax({
                        url:$('#form-crear-grupo form').attr('action'),
                        data:$('#form-crear-grupo form').serialize(),
                        type:'POST',
                        success:function (data) {
                            $('#form-crear-grupo form .descripcion-errors').html('');
                            $('#form-crear-grupo form .nombre-errors').html('');
                            if (data.estado == 0) {
                                if (data.error.nombre.length > 0) {
                                    for (i in data.error.nombre) {
                                        $('#form-crear-grupo form .nombre-errors').append('<div class="notice error">' +
                                                '<span class="icon medium" data-icon="X" style="display: inline-block; "><span aria-hidden="true">X</span></span>' + data.error.nombre[i] + '</div>');
                                    }
                                }
                                if (data.error.descripcion.length > 0) {
                                    for (i in data.error.descripcion) {
                                        $('#form-crear-grupo form .descripcion-errors').append('<div class="notice error">' +
                                                '<span class="icon medium" data-icon="X" style="display: inline-block; "><span aria-hidden="true">X</span></span>' + data.error.descripcion[i] + '</div>');
                                    }
                                }
                            } else {
                                //se agrego el grupo entonces cargar con ajax la busqueda y mostrar mensaje
                                $.ajax({
                                    url:'/groups/',
                                    type:'GET',
                                    success:function (data) {
                                        $('#contenido').html('');
                                        $('#contenido').html(data);
                                        $(window).scrollTop(0);
                                        grupos = document.querySelectorAll('#grupos .un-grupo');
                                        [].forEach.call(grupos, function (col) {
                                            col.addEventListener('dragenter', handleDragEnter, false);
                                            col.addEventListener('dragleave', handleDragLeave, false);
                                            col.addEventListener('drop', handleDrop, false);
                                            col.addEventListener('dragend', handleDragEnd, false);
                                            col.addEventListener('dragover', handleDragOver, false);
                                        });

                                        clientes = document.querySelectorAll('#contenido-grupo .listado li');
                                        [].forEach.call(clientes, function (col) {
                                            col.addEventListener('dragstart', handleDragStart, false);
                                            col.addEventListener('dragover', handleDragOver, false);
                                            col.addEventListener('dragend', handleDragEnd, false);
                                        });
                                        $('#contenido-grupo .agregado-bien').show();
                                    }
                                });
                            }
                        }
                    });
                    return false;
                });
            }
        });
    });

    $('#grupos .un-grupo').click(function () {
        var idgroup = $(this).attr('idgroup');
        $.ajax({
            url:'/get-group/?idgroup=' + idgroup,
            success:function (data) {
                $('#contenido-grupo').html('');
                $('#contenido-grupo').html(data);
                $('.listado a').click(function () {
                    $(this).parent().remove();
                });
                $('#form-crear-grupo .guardar').click(function () {
                    console.log("se intenta editar");

                    var users = "";
                    $(this).parent().parent().find('li').each(function (index) {
                        if (index > 0) {
                            users = users + "," + $(this).attr('iduser');
                        } else {
                            users = users + $(this).attr('iduser');
                        }
                    });
                    if (users.length > 0) {
                        users = 'users=' + users;
                    }

                    var data = users + '&' + $(this).parent().parent().serialize();

                    $.ajax({
                        url:'/get-group/',
                        type:'POST',
                        data:data,
                        success:function (data) {
                            $('#form-crear-grupo form .descripcion-errors').html('');
                            $('#form-crear-grupo form .nombre-errors').html('');
                            if (data.estado == 0) {
                                if (data.error.nombre.length > 0) {
                                    console.log("hay errores en nombre");
                                    for (i in data.error.nombre) {
                                        $('#form-crear-grupo form .nombre-errors').append('<div class="notice error">' +
                                                '<span class="icon medium" data-icon="X" style="display: inline-block; "><span aria-hidden="true">X</span></span>' + data.error.nombre[i] + '</div>');
                                        console.log(data.error.nombre[i]);
                                    }
                                }
                                if (data.error.descripcion.length > 0) {
                                    console.log("hay errores en descripcion");
                                    for (i in data.error.descripcion) {
                                        $('#form-crear-grupo form .descripcion-errors').append('<div class="notice error">' +
                                                '<span class="icon medium" data-icon="X" style="display: inline-block; "><span aria-hidden="true">X</span></span>' + data.error.descripcion[i] + '</div>');
                                        console.log(data.error.descripcion[i]);
                                    }
                                }
                            } else {
                                //editar
                                $.ajax({
                                    url:'/groups/',
                                    type:'GET',
                                    success:function (data) {
                                        $('#contenido').html('');
                                        $('#contenido').html(data);
                                        $(window).scrollTop(0);
                                        grupos = document.querySelectorAll('#grupos .un-grupo');
                                        [].forEach.call(grupos, function (col) {
                                            col.addEventListener('dragenter', handleDragEnter, false);
                                            col.addEventListener('dragleave', handleDragLeave, false);
                                            col.addEventListener('drop', handleDrop, false);
                                            col.addEventListener('dragend', handleDragEnd, false);
                                            col.addEventListener('dragover', handleDragOver, false);
                                        });

                                        clientes = document.querySelectorAll('#contenido-grupo .listado li');
                                        [].forEach.call(clientes, function (col) {
                                            col.addEventListener('dragstart', handleDragStart, false);
                                            col.addEventListener('dragover', handleDragOver, false);
                                            col.addEventListener('dragend', handleDragEnd, false);
                                        });
                                        $('#contenido-grupo .editado-bien').show();
                                    }
                                });
                            }
                        }
                    });

                    return false;
                });
                $('#form-crear-grupo .eliminar').click(function () {
                    console.log("se quiere borrar");
                    $.ajax({
                        url:'/delete-group/?groupid=' + $(this).parent().parent().find('.group-id').val(),
                        success:function (data) {
                            if (data.estado == 1) {
                                //eliminar
                                $.ajax({
                                    url:'/groups/',
                                    type:'GET',
                                    success:function (data) {
                                        $('#contenido').html('');
                                        $('#contenido').html(data);
                                        $(window).scrollTop(0);
                                        grupos = document.querySelectorAll('#grupos .un-grupo');
                                        [].forEach.call(grupos, function (col) {
                                            col.addEventListener('dragenter', handleDragEnter, false);
                                            col.addEventListener('dragleave', handleDragLeave, false);
                                            col.addEventListener('drop', handleDrop, false);
                                            col.addEventListener('dragend', handleDragEnd, false);
                                            col.addEventListener('dragover', handleDragOver, false);
                                        });

                                        clientes = document.querySelectorAll('#contenido-grupo .listado li');
                                        [].forEach.call(clientes, function (col) {
                                            col.addEventListener('dragstart', handleDragStart, false);
                                            col.addEventListener('dragover', handleDragOver, false);
                                            col.addEventListener('dragend', handleDragEnd, false);
                                        });
                                        $('#contenido-grupo .eliminado-bien').show();
                                    }
                                });
                            } else {
                                //falla eliminar
                            }
                        }
                    });

                    return false;
                });

                var grupos = document.querySelectorAll('#grupos .un-grupo');
                [].forEach.call(grupos, function (col) {
                    col.addEventListener('dragenter', handleDragEnter, false);
                    col.addEventListener('dragleave', handleDragLeave, false);
                    col.addEventListener('drop', handleDrop, false);
                    col.addEventListener('dragend', handleDragEnd, false);
                    col.addEventListener('dragover', handleDragOver, false);
                });

                var clientes = document.querySelectorAll('#form-crear-grupo .listado li');
                [].forEach.call(clientes, function (col) {
                    col.addEventListener('dragstart', handleDragStart, false);
                    col.addEventListener('dragover', handleDragOver, false);
                    col.addEventListener('dragend', handleDragEnd, false);
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
                [].forEach.call(grupos, function (col) {
                    col.addEventListener('dragenter', handleDragEnter, false);
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
                            $('#contenido-grupo .alt').html('');
                            for (i in data) {
                                $('#contenido-grupo .alt').append('<li draggable="true" iduser=' + data[i].pk + '>' +
                                        '<span class="icon darkgray" data-icon="u" style="display: inline-block; "><span aria-hidden="true">u</span></span>' + data[i].fields.first_name + ' ' + data[i].fields.last_name + '</li>');
                            }
                            var grupos = document.querySelectorAll('#grupos .un-grupo');
                            [].forEach.call(grupos, function (col) {
                                col.addEventListener('dragenter', handleDragEnter, false);
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
                        }
                    });
                });
            }
        });

    });
    $('#nombre').keyup(function () {
        var valor = $(this).val();
        $.ajax({
            url:'/get-client/?name=' + valor,
            type:'GET',
            dataType:'json',
            success:function (data) {
                $('#contenido-grupo .alt').html('');
                for (i in data) {
                    $('#contenido-grupo .alt').append('<li draggable="true" iduser=' + data[i].pk + '>' +
                            '<span class="icon darkgray" data-icon="u" style="display: inline-block; "><span aria-hidden="true">u</span></span>' + data[i].fields.first_name + ' ' + data[i].fields.last_name + '</li>');
                }
                var grupos = document.querySelectorAll('#grupos .un-grupo');
                [].forEach.call(grupos, function (col) {
                    col.addEventListener('dragenter', handleDragEnter, false);
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
            }
        });
    });
});