$(document).ready(function(){

    $('#ask_grandpy').click(function(e){
        e.preventDefault(); 

        var question = encodeURIComponent( $('#question').val() );

        $.ajax({
            url : "/ask_grandpy",
            type : "POST",
            data :  question,
            dataType: "text",
            
            success: function(response, textStatus, jqXHR) {
                var obj = JSON.parse(response);
                alert(response);
                $('#commentaires').append("<p>Moi " + question + "</p>");
                $('#commentaires').append("<p>GrandPy: Hey oui mon kiki j'ai la réponse! Elle se trouve juste ici!<a target='_blank' href=" + obj.url +">"+ obj.url +"</a></p>");
            },
            error: function (data) {
                $('#commentaires').append("<p>Moi " + question + "</p>");
                $('#commentaires').append("<p>GrandPy: Je suis désolé mon kiki, Papy y sait pas tout tu sais :(</p>");
            },
        });

        
        
    });
});