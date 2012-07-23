//LOGIN
var project=0;
$( '#btn_enter' ).live( 'vclick',function(event){
	email=$('#email').val();
	password=$('#password').val();
	alert(email);
  	$.ajax({
		type:"GET",
		//type:"POST",
		url: "http://localhost:8082/subastas/subastas/getArticulos/1",
		dataType: 'json',
		//data: {'email':email,'password':password},
		success: function(data){
			  	
				/*if(data.id==-1){
					alert('incorrecto')
				}else{
					localStorage.setItem('idUser', data.id);
					$.mobile.changePage("menu.html", "slide", false, true);
				}*/
				$.mobile.changePage("menu.html", "slide", false, true);
		}
	});
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

