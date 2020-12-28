$('.like_form').submit(function(event){
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/blog/like',
        data: {
            post_id: $(this).children('input[name=post_id]').val(),
            csrfmiddlewaretoken: $(this).children('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (json) {
            console.log(json);
            console.log('#' + 'button_' + json['post_id']);
            $('#' + 'button_' + json['post_id']).attr('data-like', json['like']);
        }
    })
});