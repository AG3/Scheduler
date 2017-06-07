var maybeAppendSlash = function (url) {
    if (url[url.length-1] !== "/") {
        url += '/';
    }
    return url;
};

var ensureTrailingSlash = function (url) {
    var parser = document.createElement('a');
    parser.href = url;
    parser.pathname = maybeAppendSlash(parser.pathname);
    return parser.href;
};

$(document).ready(function(){
	$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        settings.url = ensureTrailingSlash(url);
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