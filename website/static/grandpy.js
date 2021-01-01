function create_map(coords) {
    var map_div = document.createElement("div");
    map_div.setAttribute('id', 'map');

    new google.maps.Map(map_div, {
        center: coords,
        zoom: 10,
    });

    return map_div;
}

function create_element(name, text) {
    var element = document.createElement(name);
    var element_text = document.createTextNode(text);
    element.appendChild(element_text);
    return element;
}

            
$(document).ready(function(){
    
    $('#ask_grandpy').click(function(e){
        e.preventDefault(); 
        var question = encodeURIComponent( $('#question').val() );
        
        // Sentence Div Creation
        var chat_box = document.getElementById('chat-box');
        var ask_box = document.createElement("div");
        ask_box.setAttribute('id', 'sentence');
        chat_box.appendChild(ask_box)


        question_element = create_element("p", "Moi " + question)
        grandpy_think_element = create_element("p", "Laisse moi réfléchir...")

        ask_box.appendChild(question_element);
        ask_box.appendChild(grandpy_think_element);

        $.ajax({
            url : "/ask_grandpy",
            type : "POST",
            data :  question,
            dataType: "text",
            
            success: function(response, textStatus, jqXHR) {
                var obj = JSON.parse(response);
                alert(response);

                grandpy_answer_element = create_element("p", "GrandPy: Hey oui mon kiki j'ai la réponse! Elle se trouve juste ici!");

                var url = document.createElement("a");
                var url_text = document.createTextNode(obj.url)
                url.setAttribute('href', obj.url);
                url.setAttribute('_target', 'blank');
                url.appendChild(url_text);

                grandpy_answer_element.appendChild(url);
                ask_box.appendChild(grandpy_answer_element);
                ask_box.appendChild(create_map(obj.location));
            },
            error: function (data) {
                grandpy_answer_element = create_element("p", "GrandPy: Je suis désolé mon kiki, Papy y sait pas tout tu sais :(");
                ask_box.appendChild(grandpy_answer_element);
            },
        });
    });
});