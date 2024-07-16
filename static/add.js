$(document).ready(function () {
    $('.add_wishlist').on('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission

        $.ajax({
            type: 'POST',
            url: '/wishlist', // The URL to the Django view
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                id: $('.id').val()
            }, // Serialize form data
            success: function (response) {
                console.log($('.id').val())
                console.log(response)
                $('.message').html(`
                        <div class="alert alert-success alert-dismissible fade show" role="alert">
    <strong>${response}</strong>
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>`); // Display response message
            },
            error: function (xhr, status, error) {
                console.error('AJAX error:', status, error);
            }
        });
    });
});