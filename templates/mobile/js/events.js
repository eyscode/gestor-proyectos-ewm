//LOGIN
//var url_menu="http://localhost:8082/mobile/menu.html";
//var url="http://localhost:8082/subastas/subastas/getJson"
var url="http://ofisis.herokuapp.com/app/login";
var project=0;
$( '#btn_enter' ).live( 'vclick',function(event){
	//$.mobile.changePage(url_menu, "slide", false, true);
	email=$('#email').val();
	//email='ofisis';
	password=$('#password').val();
	id_user=-2;
	//alert(email+" "+password);
	$.jsonp({
        url: url,
        //method:'POST',
        callbackParameter: '',
        //data: {'email':"ofisis",'password':"ofisis"},
        success: function(data, status) {
        	alert("entra");
            //$('#your-tweets').append('<li>The feed loads fine');
            /*$.each(data, function(i,item){
                var tweet = item.text;
                $('#your-tweets').append('<li>'+tweet);
            });*/
        },
        error: function(){
        	alert("error");
            //$('#your-tweets').append('<li>There was an error loading the feed');

        }

    });

	/*$.getJSON("http://localhost:8082/subastas/subastas/getJson?callback=?",
  		function(data){
    		alert(data);// data es el json cargado por jsonp
  	});*/
	/*$.ajax({
		   type: 'GET',
		    url: url,
		    async: false,
			jsonpCallback: '?',
			contentType: "application/json",
			dataType: 'jsonp',
			success: function(data) {
			 	alert("llego");
				alert(data);
		 
		    },
		    error: function(e) {
		    	alert("error");
		       alert(e.message);
		    }
		});*/
  	/*$.ajax({
//type:"GET",
		//type:"POST",
		url: "http://localhost:8082/subastas/subastas/getArticulos/1",
		dataType: 'jsonp',
		//data: JSON.stringify(requestObject),
   		contentType: 'application/json; charset=utf-8',
		//data: {'email':"ofisis",'password':"ofisis"},
		success: function(data){
			alert(data);
			/*if(data.id==-1){
			alert(data);
			alert('incorrecto')
			}else{
				alert(data);
				localStorage.setItem('idUser', data.id);
				$.mobile.changePage("menu.html", "slide", false, true);
			}*/
	//		$.mobile.changePage("menu.html", "slide", false, true);
	//	}
	//});

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

