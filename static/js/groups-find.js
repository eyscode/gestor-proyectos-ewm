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
});