var tasks = [];
var columns = [];
function handleDragStart(e) {
    dragSrcEl = this;
    console.log($(dragSrcEl));
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/html', this.innerHTML);
}

function handleDragOver(e) {
    if (e.preventDefault) {
        e.preventDefault(); // Necessary. Allows us to drop.
    }

    e.dataTransfer.dropEffect = 'move';  // See the section on the DataTransfer object.

    return false;
}

function handleDragEnter(e) {
    // this / e.target is the current hover target.
    this.classList.add('over');
}

function handleDragLeave(e) {
    this.classList.remove('over');  // this / e.target is previous target element.
}

function handleDrop(e) {
    this.classList.remove('over');
    // this / e.target is current target element.

    if (e.stopPropagation) {
        e.stopPropagation(); // stops the browser from redirecting.
    }

    var idtask = $(dragSrcEl).attr('idtask');
    var idcolumn = $(this).attr('idcolumn');
    var column = $(this);
    $.ajax({
        url:'/projects/move-task/?idcolumn=' + idcolumn + '&idtask=' + idtask + '&pila=' + $(dragSrcEl).attr('pila'),
        type:'GET',
        success:function (data) {
            if (data.estado == 1) {
                if ($(dragSrcEl).attr('pila') == "true") {
                    var newNode = dragSrcEl.cloneNode(true);
                    newNode.addEventListener('dragstart', handleDragStart, false);
                    newNode.addEventListener('dragover', handleDragOver, false);
                    newNode.addEventListener('dragend', handleDragEnd, false);
                    newNode = $(newNode).attr('pila', 'false');
                    column.append(newNode);
                } else {
                    $(dragSrcEl).attr('pila', 'false');
                    column.append($(dragSrcEl));
                }
            }
        }
    });
    // See the section on the DataTransfer object.
    return false;
}

function handleDragEnd(e) {
    // this/e.target is the source node.
    if (tasks.classList) {
        [].forEach.call(tasks, function (col) {
            tasks.classList.remove('over');
        });
    }
}
$('#Kboard').ready(function () {
    var columns = document.querySelectorAll('#Ktablero .Ktask');
    [].forEach.call(columns, function (col) {
        col.addEventListener('dragenter', handleDragEnter, false);
        col.addEventListener('dragleave', handleDragLeave, false);
        col.addEventListener('drop', handleDrop, false);
        col.addEventListener('dragend', handleDragEnd, false);
        col.addEventListener('dragover', handleDragOver, false);
    });
    var tasks = document.querySelectorAll('#Kboard .one-task');
    [].forEach.call(tasks, function (col) {
        col.addEventListener('dragstart', handleDragStart, false);
        col.addEventListener('dragover', handleDragOver, false);
        col.addEventListener('dragend', handleDragEnd, false);
    });
});

$('#Kactions .crear-columna').click(function (e) {
    $('#crear-columna-content').modal();
    $('#crear-columna-content form').submit(function () {
        $.ajax({
            url:'/projects/create-column/',
            type:'POST',
            data:$(this).serialize(),
            success:function (data) {
                console.log("ya fue");
                var idboard = $('#board-id').val();
                $.ajax({
                    url:"/projects/get-board/?idboard=" + idboard,
                    type:'GET',
                    success:function (data) {
                        $('#contenido').html(data);
                        $(window).scrollTop(0);
                    }
                })
            }
        });
        return false;
    });
    return false;
});

$('#Kactions .eliminar-columna').click(function (e) {
    $('#eliminar-columna-content').modal();
    $('#eliminar-columna-content form').submit(function () {
        $.ajax({
            url:'/projects/delete-column/',
            data:$(this).serialize(),
            success:function (data) {
                var idboard = $('#board-id').val();
                $.ajax({
                    url:"/projects/get-board/?idboard=" + idboard,
                    type:'GET',
                    success:function (data) {
                        $('#contenido').html(data);
                        $(window).scrollTop(0);
                    }
                })
            }
        });
        return false;
    });
    return false;
});

$('#Kactions .crear-paquete').click(function (e) {
    $('#crear-paquete-content').modal();
    $('#crear-paquete-content form').submit(function () {
        $.ajax({
            url:'/projects/create-package/',
            type:'POST',
            data:$(this).serialize(),
            success:function (data) {
                var idboard = $('#board-id').val();
                $.ajax({
                    url:"/projects/get-board/?idboard=" + idboard,
                    type:'GET',
                    success:function (data) {
                        $('#contenido').html(data);
                        $(window).scrollTop(0);
                    }
                })
            }
        });
        return false;
    });
    return false;
});
$('#Kactions .eliminar-paquete').click(function (e) {
    $('#eliminar-paquete-content').modal();
    $('#eliminar-paquete-content form').submit(function () {
        $.ajax({
            url:'/projects/delete-package/',
            data:$(this).serialize(),
            success:function (data) {
                var idboard = $('#board-id').val();
                $.ajax({
                    url:"/projects/get-board/?idboard=" + idboard,
                    type:'GET',
                    success:function (data) {
                        $('#contenido').html(data);
                        $(window).scrollTop(0);
                    }
                })
            }
        });
        return false;
    });
    return false;
});
$('#Kactions .crear-tarea').click(function (e) {
    $('#crear-tarea-content').modal();
    $('#crear-tarea-content form').submit(function () {
        $.ajax({
            url:'/projects/create-task/',
            type:'POST',
            data:$(this).serialize(),
            success:function (data) {
                var idboard = $('#board-id').val();
                $.ajax({
                    url:"/projects/get-board/?idboard=" + idboard,
                    type:'GET',
                    success:function (data) {
                        $('#contenido').html(data);
                        $(window).scrollTop(0);
                    }
                })
            }
        });
        return false;
    });
    return false;
});
$('#Kactions .eliminar-tarea').click(function (e) {
    $('#eliminar-tarea-content').modal();
    $('#eliminar-tarea-content form').submit(function () {
        $.ajax({
            url:'/projects/delete-task/',
            data:$(this).serialize(),
            success:function (data) {
                var idboard = $('#board-id').val();
                $.ajax({
                    url:"/projects/get-board/?idboard=" + idboard,
                    type:'GET',
                    success:function (data) {
                        $('#contenido').html(data);
                        $(window).scrollTop(0);
                    }
                })
            }
        });
        return false;
    });
    return false;
});