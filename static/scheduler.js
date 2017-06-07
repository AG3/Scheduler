function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function(){
    
    var csrftoken = $("input[name='csrfmiddlewaretoken']").val()
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $("#btn").click(function(){
        $.ajax({
            type:"POST",
            url:"/app/search/",
            data:{
                "subject": "subjectdata",
                "course": "coursedata"
            }
        }).done(function(msg){
            console.log(msg)
        })
    });
}); 