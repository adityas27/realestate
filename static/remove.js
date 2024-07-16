$(document).ready(function () {
    $('.del_wishlist').on('submit', function (e) {
      e.preventDefault(); // Prevent the default form submission

      $.ajax({
        type: 'POST',
        url: '/del_wishlist', // The URL to the Django view
        data: {
          // csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          id: $('#id').val()
        }, // Serialize form data
        success: function (response) {
          $('#message').html(response.message);
          doc = ``;
          id = $('#id').val()
          $(`#${id}`).remove();
        },
        error: function (xhr, status, error) {
          console.error('AJAX error:', status, error);
        }
      });
    });
  });