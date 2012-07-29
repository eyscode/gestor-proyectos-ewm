var clientes = [];
var groups = [];
function handleDragStart(e) {
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
    var iduser = $(dragSrcEl).attr('iduser');
    var idgroup = $(this).attr('idgroup');
    var grupo = $(this);
    $.ajax({
        url:'/add-client/?iduser=' + iduser + '&idgroup=' + idgroup,
        type:'GET',
        success:function (data) {
            if (data == '1') {
                grupo.find('.plus1').fadeIn();
                grupo.find('.plus1').transition({ x:-100 }, function () {
                    $(this).transition({ opacity:0 }, function () {
                        grupo.find('.plus1').hide();
                        grupo.find('.plus1').css('opacity', 100);
                        grupo.find('.plus1').transition({x:0}, 0);
                    }, 2000);
                });
            } else if (data == '2') {
                grupo.find('.mensaje').fadeIn();
                grupo.find('.mensaje').fadeOut();
            }
        }
    });
    // See the section on the DataTransfer object.

    return false;
}

function handleDragEnd(e) {
    // this/e.target is the source node.
    if (clientes.classList) {
        [].forEach.call(clientes, function (col) {
            clientes.classList.remove('over');
        });
    }
}

$(document).ready(function () {

    var posini = {'home':0, 'projects':98, 'account':196, 'groups':294, 'explore':392};
    $('#dock .triangulo').transition({
        y:posini[actual] + 'px'
    });

    $('#sub-dock .option').mouseenter(function () {
        if ($(this).attr('id') == "more") {
            $('#extra-option').show();
        }
        $(this).find('.sub').css('background-color', '#5D9AB9');
        var clase = $(this).find('.icono').attr('class').split(" ")[0];
        $(this).find('.icono').css('background', 'no-repeat url("../static/img/dock/' + clase + '_go.png")');
    });

    $('#extra-option .option').mouseenter(function () {
        var clase = $(this).find('.icono').attr('class').split(" ")[0];
        $(this).find('.sub').css('background-color', 'white');
        $(this).find('.icono').css('background', 'no-repeat url("../static/img/dock/' + clase + '_go.png")');
    });

    $('#extra-option .option').mouseleave(function () {
        var clase = $(this).find('.icono').attr('class').split(" ")[0];
        $(this).find('.sub').css('background-color', 'whitesmoke');
        $(this).find('.icono').css('background', 'no-repeat url("../static/img/dock/' + clase + '.png")');
    });

    $('#extra-option').mouseenter(function () {
        $('#extra-option').show();
    });

    $('#extra-option').mouseleave(function () {
        $('#extra-option').hide();
    });

    $('#sub-dock .option').mouseleave(function () {
        if ($(this).attr('id') == "more") {
            $('#extra-option').hide();
        }
        $(this).find('.sub').css('background-color', '#2D6987');
        var clase = $(this).find('.icono').attr('class').split(" ")[0];
        $(this).find('.icono').css('background', 'no-repeat url("../static/img/dock/' + clase + '.png")');
    });
    $('#sub-dock .option a').click(function () {
        var url = $(this).attr('href');
        var clase = $(this).find('.icono').attr('class').split(" ")[0];
        var clickeado = $(this).parent().parent();
        var valor = 0;
        var menos = 0;
        var posis = {'home':0, 'projets':1, 'account':2, 'groups':3, 'explore':4};
        $('#sub-dock .option').each(function (index) {
            if (index < 5) {
                if (index < posis[clase]) {
                    if ($(this).css('display') == 'none') {
                        menos += 1;
                    }
                }
                if ($(this).attr('id') == clickeado.attr('id')) {
                    valor = index;
                    return;
                }
            }
        });
        $.ajax({
            url:$(this).attr('href'),
            type:"GET",
            success:function (data) {
                //var dim = final - parseInt($('#dock .triangulo').css('top'));
                var dim = (valor - menos) * 98;
                $('#dock .triangulo').transition({
                    y:dim + 'px'
                });
                //$('#dock .triangulo').css('top', option.offset().top - 70);
                $('#contenido').html(data);
                $(window).scrollTop(0);
                window.history.pushState(data, clase, url);
                actual = clase;
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
            }
        });
        return false;
    });
    $('#extra-option .option a').click(function () {
        var url = $(this).attr('href');
        var clase = $(this).find('.icono').attr('class').split(" ")[0];
        var cual;
        var dim = -1;
        $('#sub-dock .option').each(function (index) {
            if (index < 5) {
                if ($(this).css('display') != "none") {
                    cual = $(this);
                    dim += 1;
                }
            }
        });
        var este = $(this).parent().parent();
        $.ajax({
            url:$(this).attr('href'),
            type:"GET",
            success:function (data) {
                $('#dock .triangulo').transition({
                    y:dim * 98 + 'px'
                });
                cual.hide();
                $('#extra-' + cual.attr('id')).show();
                este.hide();
                $('#' + clase).show();
                $('#contenido').html(data);
                actual = clase;
                $(window).scrollTop(0);
                window.history.pushState(data, clase, url);
            }
        });

        return false;
    });
    setInterval(function () {
        if ($(window).height() <= 600 || $(window).width() <= 990) {
            $('#header').css('position', 'relative');
            $('#contentPane .sombra').css('position', 'static');
            $('#contentPane .marco-arriba').css('position', 'static');
            $('#dock').css('top', '0');
            $('#header-alt').css('height', '0');
            if ($(window).scrollTop() <= 103) {
                $('#dock').css('position', 'absolute');
            } else {
                $('#dock').css('position', 'fixed');
            }
        } else if ($(window).height() <= 600 && $(window).width() > 990) {
            $('#dock').css('position', 'fixed');
            $('#dock').css('top', 'auto');
        } else {
            $('#header').css('position', 'fixed');
            $('#contentPane .sombra').css('position', 'fixed');
            $('#contentPane .marco-arriba').css('position', 'fixed');
            $('#dock').css('top', 'auto');
            $('#header-alt').css('height', '102px');
            $('#dock').css('position', 'fixed');
        }
        if ($(window).width() <= 990) {
            if ($(window).scrollTop() <= 103) {
                $('#dock').css('left', '-' + $(window).scrollLeft() / 100 + 'px');
            } else {
                $('#dock').css('left', '-' + $(window).scrollLeft() + 'px');
            }
        }
    }, 100);
    $(window).resize(function () {
        if ($(window).height() > 640) {
            $('#more').hide();
            $('#explore').show();
            $('#groups').show();
            $('#account').show();
            $('#projects').show();
            $('#home').show();
        } else if ($(window).height() <= 640 && $(window).height() > 540) {
            $('#more').show();
            if (actual != "explore") {
                $('#explore').hide();
                $('#groups').show();
                $('#extra-explore').show();
                $('#extra-groups').hide();
            } else {
                $('#explore').show();
                $('#groups').hide();
                /*$('#dock .triangulo').transition({
                 y:294 + 'px'
                 });*/
                $('#extra-explore').hide();
                $('#extra-groups').show();
            }
            $('#account').show();
            $('#projects').show();
            $('#home').show();
            $('#extra-option').css('top', '386px');
            $('#extra-account').hide();
            $('#extra-projects').hide();
            $('#extra-home').hide();
        } else if ($(window).height() <= 540 && $(window).height() > 440) {
            $('#more').show();
            if (actual != "explore" && actual != "groups") {
                $('#explore').hide();
                $('#groups').hide();
                $('#account').show();
                $('#extra-explore').show();
                $('#extra-groups').show();
                $('#extra-account').hide();
            } else {
                var alt = [$('#explore'), $('#groups')];
                for (var i in alt) {
                    alt[i].hide();
                    $('#extra-' + alt[i].attr('id')).show();
                }
                $('#' + actual).show();
                $('#extra-' + actual).hide();
                $('#account').hide();
                $('#extra-account').show();
                /*$('#dock .triangulo').transition({
                 y:196 + 'px'
                 });*/
            }
            $('#projects').show();
            $('#home').show();
            $('#extra-option').css('top', '286px');
            $('#extra-projects').hide();
            $('#extra-home').hide();
        } else if ($(window).height() <= 440 && $(window).height() > 340) {
            $('#more').show();
            if (actual != "explore" && actual != "groups" && actual != "account") {
                $('#explore').hide();
                $('#groups').hide();
                $('#account').hide();
                $('#projects').show();
                $('#extra-explore').show();
                $('#extra-groups').show();
                $('#extra-account').show();
                $('#extra-projects').hide();
            } else {
                var alt = [$('#explore'), $('#groups'), $('#account')];
                for (var i in alt) {
                    alt[i].hide();
                    $('#extra-' + alt[i].attr('id')).show();
                }
                $('#' + actual).show();
                $('#extra-' + actual).hide();
                $('#projects').hide();
                $('#extra-projects').show();
                /*$('#dock .triangulo').transition({
                 y:98 + 'px'
                 });*/
            }
            $('#home').show();
            $('#extra-option').css('top', '190px');
            $('#extra-home').hide();
        } else if ($(window).height() <= 340) {
            $('#more').show();
            if (actual != "explore" && actual != "groups" && actual != "account" && actual != "projects") {
                $('#explore').hide();
                $('#groups').hide();
                $('#account').hide();
                $('#projects').hide();
                $('#extra-explore').show();
                $('#extra-groups').show();
                $('#extra-account').show();
                $('#extra-projects').show();
                $('#home').show();
                $('#extra-home').hide();
            } else {
                var alt = [$('#explore'), $('#groups'), $('#account'), $('#projects')];
                for (var i in alt) {
                    alt[i].hide();
                    $('#extra-' + alt[i].attr('id')).show();
                }
                $('#' + actual).show();
                $('#extra-' + actual).hide();
                $('#home').hide();
                $('#extra-home').show();
                $('#dock .triangulo').transition({
                    y:0 + 'px'
                });
            }
            $('#extra-option').css('top', '92px');
        }
        var posini = {'home':0, 'projects':98, 'account':196, 'groups':294, 'explore':392};
        var posis = {'home':0, 'projets':1, 'account':2, 'groups':3, 'explore':4};
        var valor = posini[actual];
        var menos = 0;
        $('#sub-dock .option').each(function (index) {
            if (index < 5) {
                if (index < posis[actual]) {
                    if ($(this).css('display') == 'none') {
                        menos += 1;
                    }
                }
                if ($(this).attr('id') == actual) {
                    return;
                }
            }
        });
        /*$('#dock .triangulo').transform({
         y:(valor - (menos * 98)) + 'px'
         });*/
        $('#dock .triangulo').transition({ y:(valor - (menos * 98)) + 'px' }, 'slow');
    });
    $(window).load(function () {
        if ($(window).height() > 640) {
            $('#more').hide();
            $('#explore').show();
            $('#groups').show();
            $('#account').show();
            $('#projects').show();
            $('#home').show();
        } else if ($(window).height() <= 640 && $(window).height() > 540) {
            $('#more').show();
            if (actual != "explore") {
                $('#explore').hide();
                $('#groups').show();
                $('#extra-explore').show();
                $('#extra-groups').hide();
            } else {
                $('#explore').show();
                $('#groups').hide();
                $('#dock .triangulo').transition({
                    y:294 + 'px'
                });
                $('#extra-explore').hide();
                $('#extra-groups').show();
            }
            $('#account').show();
            $('#projects').show();
            $('#home').show();
            $('#extra-option').css('top', '386px');
            $('#extra-account').hide();
            $('#extra-projects').hide();
            $('#extra-home').hide();
        } else if ($(window).height() <= 540 && $(window).height() > 440) {
            $('#more').show();
            if (actual != "explore" && actual != "groups") {
                $('#explore').hide();
                $('#groups').hide();
                $('#account').show();
                $('#extra-explore').show();
                $('#extra-groups').show();
                $('#extra-account').hide();
            } else {
                var alt = [$('#explore'), $('#groups')];
                for (var i in alt) {
                    alt[i].hide();
                    $('#extra-' + alt[i].attr('id')).show();
                }
                $('#' + actual).show();
                $('#extra-' + actual).hide();
                $('#account').hide();
                $('#extra-account').show();
                $('#dock .triangulo').transition({
                    y:196 + 'px'
                });
            }
            $('#projects').show();
            $('#home').show();
            $('#extra-option').css('top', '286px');
            $('#extra-projects').hide();
            $('#extra-home').hide();
        } else if ($(window).height() <= 440 && $(window).height() > 340) {
            $('#more').show();
            if (actual != "explore" && actual != "groups" && actual != "account") {
                $('#explore').hide();
                $('#groups').hide();
                $('#account').hide();
                $('#projects').show();
                $('#extra-explore').show();
                $('#extra-groups').show();
                $('#extra-account').show();
                $('#extra-projects').hide();
            } else {
                var alt = [$('#explore'), $('#groups'), $('#account')];
                for (var i in alt) {
                    alt[i].hide();
                    $('#extra-' + alt[i].attr('id')).show();
                }
                $('#' + actual).show();
                $('#extra-' + actual).hide();
                $('#projects').hide();
                $('#extra-projects').show();
                $('#dock .triangulo').transition({
                    y:98 + 'px'
                });
            }
            $('#home').show();
            $('#extra-option').css('top', '190px');
            $('#extra-home').hide();
        } else if ($(window).height() <= 340) {
            $('#more').show();
            if (actual != "explore" && actual != "groups" && actual != "account" && actual != "projects") {
                $('#explore').hide();
                $('#groups').hide();
                $('#account').hide();
                $('#projects').hide();
                $('#extra-explore').show();
                $('#extra-groups').show();
                $('#extra-account').show();
                $('#extra-projects').show();
                $('#home').show();
                $('#extra-home').hide();
            } else {
                var alt = [$('#explore'), $('#groups'), $('#account'), $('#projects')];
                for (var i in alt) {
                    alt[i].hide();
                    $('#extra-' + alt[i].attr('id')).show();
                }
                $('#' + actual).show();
                $('#extra-' + actual).hide();
                $('#home').hide();
                $('#extra-home').show();
                $('#dock .triangulo').transition({
                    y:0 + 'px'
                });
            }
            $('#extra-option').css('top', '92px');
        }
    });
});