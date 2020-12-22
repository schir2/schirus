$('#like-form').submit(function(event){
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/blog/like',
        data: {
            post_id: $('input[name=post_id]').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        dataType: 'json',
        success: function (json) {
            console.log(json);
        }
    })
});