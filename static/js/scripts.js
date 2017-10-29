$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);

    function basketUpdating(book_id){
        var data = {};
        data.book_id = book_id;
         var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
         data["csrfmiddlewaretoken"] = csrf_token;

         var url = form.attr("action");

         $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function(data){
                 console.log(data["book_id"] + data["session_key"]);
                        // $('#basket').append("<p>" +data["book_id"] + data["session_key"] + "</p>");
            }
         });

    }


    form.on('submit', function(e){
        e.preventDefault();

        var submit_btn = $('#add_to_cart_button');
        var book_id = submit_btn.data("book_id");

        basketUpdating(book_id)
    });

    $("#tap").on('click', function (e) {
        alert("Hello");
    })

    // $(document).on('click', '.delete-item', function(e){
    //      e.preventDefault();
    //      product_id = $(this).data("product_id");
    //
    //      basketUpdating(product_id)
    //  });
});