$(document).ready(function () {

    var dragSrcEl = null;

    function handleDragStart(e) {
        this.style.opacity = '0.4';  // this / e.target is the source node.
        dragSrcEl = this;
        e.dataTransfer.effectAllowed = 'move';
        var dragIcon = document.createElement('img');
        dragIcon.src = '../static/img/user_drag.png';
        dragIcon.width = 100;
        e.dataTransfer.setDragImage(dragIcon, 0, 5);
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
        console.log($(dragSrcEl).attr('iduser'));
        var iduser = $(dragSrcEl).attr('iduser');
        var idgroup = $(this).find('.grupo_id');
        $.ajax({
            url:'/add-client/?iduser=' + iduser,
            type:'GET',
            success:function (data) {
                alert("+1");
            }
        });
        // See the section on the DataTransfer object.

        return false;
    }

    function handleDragEnd(e) {
        // this/e.target is the source node.

        [].forEach.call(clientes, function (col) {
            clientes.classList.remove('over');
        });
    }

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
                $('#contenido-grupo .alt').html('');
                for (i in data) {
                    $('#contenido-grupo .alt').append('<li draggable="true" iduser=' + data[i].pk + '><span class="icon medium lupa" data-icon="u"></span>' + data[i].fields.first_name + ' ' + data[i].fields.last_name + '</li>');
                }
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
            }
        });
    });

});