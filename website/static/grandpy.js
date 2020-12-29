function initMap(coords) {
    let map = new google.maps.Map(document.getElementById("map"), {
        center: coords,
        zoom: 10,
    });
}

            
$(document).ready(function(){

    $('#ask_grandpy').click(function(e){
        e.preventDefault(); 

        var question = encodeURIComponent( $('#question').val() );
        $('#sentence').append("<p>Moi " + question + "</p>");
        $('#sentence').append("<p>Laisse moi réfléchir............</p>");

        $.ajax({
            url : "/ask_grandpy",
            type : "POST",
            data :  question,
            dataType: "text",
            
            success: function(response, textStatus, jqXHR) {
                var obj = JSON.parse(response);
                alert(response);
                $('#sentence').append("<p>GrandPy: Hey oui mon kiki j'ai la réponse! Elle se trouve juste ici!<a target='_blank' href=" + obj.url +">"+ obj.url +"</a></p>");
                initMap(obj.location);
                
            },
            error: function (data) {
                $('#sentence').append("<p>GrandPy: Je suis désolé mon kiki, Papy y sait pas tout tu sais :(</p>");
            },
        });
    });
});