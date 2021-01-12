var random_answer = ['Excellente question! Tu savais que ', 'C\'est marrant que tu me demandes ça, je vais te raconter : ', 'Hum... si je ne dis pas de bétise ' ]

function get_random_answer(){
	var random_number = Math.floor(Math.random() * (3 - 1)) + 0;
	var answer = random_answer[random_number];
	return answer;
}

function create_map(coords) {
    var map_card_div = document.createElement("div");
    map_card_div.setAttribute('class', 'card-body text-center');
    
    var map_div = document.createElement("div");
    map_div.setAttribute('class', 'map-container-5 z-depth-1-half');
    map_div.setAttribute('style', 'height: 300px');

    map = new google.maps.Map(map_div, {
        center: coords,
        zoom: 20,
    });

    const marker = new google.maps.Marker({
        position: coords,
        map: map,
      });
    

    map_card_div.appendChild(map_div)
    
    return map_card_div;
}

function create_element(name, text) {
    var element = document.createElement(name);
    var element_text = document.createTextNode(text);
    element.appendChild(element_text);
    return element;
}

function create_question_div(question) {

    var chat_entry = document.createElement("div")
    chat_entry.setAttribute('class', 'chat');

    var chat_avatar = document.createElement("div")
    chat_avatar.setAttribute('class', 'chat-avatar');
    var you = create_element("p", "Vous")

    chat_avatar.appendChild(you)
    chat_entry.appendChild(chat_avatar)

    var chat_body = document.createElement("div")
    chat_body.setAttribute('class', 'chat-body');

    var chat_content = document.createElement("div")
    chat_content.setAttribute('class', 'chat-content');
                    // Create p
    var grandpy = create_element("p", question)

    chat_content.appendChild(grandpy)
    chat_body.appendChild(chat_content)
    chat_entry.appendChild(chat_body)
    
    return chat_entry
}

function create_positive_answer_div(answer, wiki_summary, url_div, map_div) {
    // Create div class="chat"
    var chat_entry = document.createElement("div")
    chat_entry.setAttribute('class', 'chat  chat-left');

    var chat_avatar = document.createElement("div")
    chat_avatar.setAttribute('class', 'chat-avatar');
    var you = create_element("p", "Grandpy")

    chat_avatar.appendChild(you)
    chat_entry.appendChild(chat_avatar)

    var chat_body = document.createElement("div")
    chat_body.setAttribute('class', 'chat-body');

    var chat_content = document.createElement("div")
    chat_content.setAttribute('class', 'chat-content');

    var grandpy = create_element("p", answer)

    var summary = create_element("p", wiki_summary)
    summary.appendChild(url_div)
    grandpy.appendChild(summary)
 
    chat_content.appendChild(grandpy)
    chat_content.appendChild(map_div)

    chat_body.appendChild(chat_content)
    chat_entry.appendChild(chat_body)
    

    return chat_entry
}

function create_negative_answer_div(answer) {
    // Create div class="chat"
    var chat_entry = document.createElement("div")
    chat_entry.setAttribute('class', 'chat  chat-left');

    var chat_avatar = document.createElement("div")
    chat_avatar.setAttribute('class', 'chat-avatar');
    var you = create_element("p", "Grandpy")

    chat_avatar.appendChild(you)
    chat_entry.appendChild(chat_avatar)


    var chat_body = document.createElement("div")
    chat_body.setAttribute('class', 'chat-body');

    var chat_content = document.createElement("div")
    chat_content.setAttribute('class', 'chat-content');

    var grandpy = create_element("p", answer)

    chat_content.appendChild(grandpy)

    chat_body.appendChild(chat_content)
    chat_entry.appendChild(chat_body)
    

    return chat_entry
}

            
$(document).ready(function(){
    
    $('#ask_grandpy').click(function(e){
        e.preventDefault(); 
        var question = encodeURI( $('#question').val() );

        
        // Sentence Div Creation
        var chat_box = document.getElementById('chat-box');
        
        question_entry = create_question_div(decodeURI(question))
        chat_box.appendChild(question_entry)
        
        answer_entry = create_question_div("Laisse moi réfléchir...")
        chat_box.appendChild(question_entry)


        $.ajax({
            url : "/ask_grandpy",
            type : "POST",
            data :  question,
            dataType: "text",
            
            success: function(response, textStatus, jqXHR) {
                var obj = JSON.parse(response);

                var url = document.createElement("a");
                var url_text = document.createTextNode(" Si tu veux en savoir plus, c'est par ici!")
                url.setAttribute('href', obj.info.url);
                url.setAttribute('target', '_blank');
                url.appendChild(url_text);

                var map_google = create_map(obj.info.location)

                answer_entry = create_positive_answer_div(get_random_answer(), obj.info.summary, url, map_google)

                chat_box.appendChild(answer_entry)

            },
            error: function (data) {

                grandpy_answer_element = create_negative_answer_div("GrandPy: Je suis désolé mon kiki, Papy y sait pas tout tu sais :(");
                chat_box.appendChild(grandpy_answer_element);
            },
        });
    });
});