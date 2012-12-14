//LOGIN
//var url_menu="http://localhost:9000/view_login_movil";
//var url="http://localhost:8082/subastas/subastas/getJson"
//var url="http://ofisis.herokuapp.com/app/login";
var url={login:"http://localhost:8000/app/login",
		get_project:"http://localhost:8000/app/proyectos",
		get_tablet:"http://localhost:8000/app/tableros" ,
		get_columnas:"http://localhost:8000/app/columnas",
		get_columna_tareas:"http://localhost:8000/app/tareas_columna", };
var project=0;
var tablero;
var proyect_user;
var error;
var url_alert;
$( '#btn_enter' ).live( 'vclick',function(event){
	email=$('#email').val();
	password=$('#password').val();
	$.ajax({
		url: url.login,
		dataType: 'jsonp',
		data: {'email':email,'password':password},
		success: function(data){
			if(data.id!=-1){
				//id_user=data.id;
				localStorage.setItem('idUser', data.id);
				$.mobile.changePage("menu.html", "slide", false, true);
			}else{
				//$('#errorText').html("Usuario Incorrecto");
				error="usuario o password inexistentes";
				$.mobile.changePage('alert.html', 'slide', false, false);
				url_alert="mobile.html";
				//alert("error al loguearse");
			}
		}
	});

});
//ERROR
$('#alert_dialog').live('pageinit', function (event) {
        //$("#alert_title").text(error);
    $("#alert_body").text(error);
});
$("#btn_acept_alert").live( 'vclick',function(event){
	 $('#alert_dialog').dialog('close');
});
//MENU
$('#option_projects').live( 'vclick',function(event){
	$.mobile.changePage("projectos.html", "slide", false, true);
});
$( '#option_friends' ).live( 'vclick',function(event){
	//alert(event.target.name);
});
$( '#btn_count' ).live( 'vclick',function(event){
	
});
$( '#btn_readme' ).live( 'vclick',function(event){
	
});


//PROYECTOS
$( '#projectos_list li' ).live( 'vclick',function(event){
	//alert("name:" +project + event.target.name);
	project=event.target.name;
	$.mobile.changePage("projecto_menu.html", "slide", false, true);
});


//PROYECTO


$( '#projecto_menu' ).live( 'pagecreate',function(event){
  	//alert(project);
  	//$('#menu_principal_options').append('<li><a href="#"><img src="icons/projectos.png" alt=""><h3>Amigos</h3></a></li>');
});


$( '#projectos' ).live( 'pagecreate',function(event){
  	id_user=localStorage.getItem('idUser');
  	//alert(id_user);
  	$.ajax({
		url: url.get_project,
		dataType: 'jsonp',
		data: {'id_user':id_user},
		success: function(data){
			proyect_user=data;
			$.each(data, function(i,item){
                var name = item.fields.name;
                //alert(name);
                $('#projectos_list').append(listaSimple(item.pk,name));
            });
		}
	});
});

//TABLEROS
$( '#tableros' ).live( 'pagecreate',function(event){
  	//id_user=localStorage.getItem('idUser');
  	alert(project);
  	$.ajax({
		url: url.get_tablet,
		dataType: 'jsonp',
		data: {'id_proyecto':project},
		success: function(data){
			alert('dataaa'+data);
			//proyect_user=data;
			$.each(data, function(i,item){
                var name = item.fields.name;
                //alert(name);
                $('#list_tableros').append(listaSimple(item.pk,name));
            });
		}
	});
});

$( '#list_tableros li' ).live( 'vclick',function(event){
	//alert("name:" +project + event.target.name);
	tablero=event.target.name;
	$.mobile.changePage("tablero.html", "slide", false, true);
});
//COLUMNAS
$( '#columnas' ).live( 'pagecreate',function(event){
  	//id_user=localStorage.getItem('idUser');
  	alert(tablero);
  	$.ajax({
		url: url.get_columnas,
		dataType: 'jsonp',
		data: {'id_tablero':tablero},
		success: function(data){
			alert('dataaa'+data);
			//proyect_user=data;
			$.each(data, function(i,item){
                var name = item.fields.name;
                //alert(name);
                $('#list_columnas').append(listaSimple(item.pk,name));
            });
		}
	});
});
$( '#list_columnas li' ).live( 'vclick',function(event){
	//alert("name:" +project + event.target.name);
	columna=event.target.name;
	$.mobile.changePage("columna.html", "slide", false, true);
});
//Tareas
$( '#columna' ).live( 'pagecreate',function(event){
  	//id_user=localStorage.getItem('idUser');
  	alert(columna);
  	$.ajax({
		url: url.get_columna_tareas,
		dataType: 'jsonp',
		data: {'id_columna':columna},
		success: function(data){
			//alert('dataaa'+data);
			//proyect_user=data;
			$.each(data, function(i,item){
                var name = item.fields.title;
                //alert(name);
                $('#list_tareas').append(listaConparrafo(item.pk,name,item.fields.description));
            });
		}
	});
});

//UTILS
function listaSimple(id,name){
	return "<li data-theme='c' class='ui-btn ui-btn-icon-right ui-li-has-arrow ui-li ui-btn-up-c'><div class='ui-btn-inner ui-li'><div class='ui-btn-text'><a href='' name="+id+" class='ui-link-inherit'>"+name+"</a></div><span class='ui-icon ui-icon-arrow-r ui-icon-shadow'/></div></li>";
} 

function listaConparrafo(id,name,parrafo){
	return "<li data-theme='c' class='ui-btn ui-btn-icon-right ui-li-has-arrow ui-li ui-btn-up-c'><div class='ui-btn-inner ui-li'><div class='ui-btn-text'><a href='' name="+id+" class='ui-link-inherit'>"+"<h3 class='ui-li-heading'>"+name+"</h3><p class='ui-li-desc'>"+parrafo+"</p></a></div><span class='ui-icon ui-icon-arrow-r ui-icon-shadow'/></div></li>";
}