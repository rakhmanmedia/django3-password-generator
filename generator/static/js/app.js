// Function copy to clipboard
function copyPassword() {
    navigator.clipboard.writeText($('#pass-gen-res').val())
}

// Event generate password on submit
$(document).on('submit', '#pass-gen-form', function(e) {
    e.preventDefault();
    $.ajax({
        url: 'password',
        data: {
            length: $('#length').val(),
            uppercase: $('#uppercase:checked').val(),
            numbers: $('#numbers:checked').val(),
            special: $('#special:checked').val(),
            similar: $('#similar:checked').val(),
        },
        success: function(data){
            $('#pass-gen-res').val(data)
        }
    })
})