$(function(){
	$('form').submit(function(event){
		console.log("Works")
		event.preventDefault()
		$.ajax({  //Sends click and form info to url: /predict for processing
			url: '/predict',
			data: $('form').serialize(), //processes all data in form serialwise
			type: 'POST',
			success: function(response){
				console.log(response);//shows the response
				$("#final-text").text(response).show(); //Outputs the value
			},
			error: function(error){
				console.log(error);
			},

		});
	});
});