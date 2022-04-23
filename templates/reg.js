$('#submit').click(function(event) {
    var name = document.getElementById("name");
    var uname0 = document.getElementById("uname0");
    var pswd0 = document.getElementById("pswd0");
    var form_data = new FormData($('#uploadform')[0]);
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:5000/uploadajax',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        success: function(data) {
            console.log('Success!');
        },
    });
})