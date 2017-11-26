$(document).ready(function() {
    var form = $('#form_buying_product');
    console.log(form);

    function basketUpdating(book_id) {
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
            success: function (data) {
                console.log(data["book_id"] + data["session_key"]);
                $('#basket').html("");
                $.each(data.products, function (k, v) {
                    $('#basket-li').append(" " + v.name);
                });
            }
        });

    }


    form.on('submit', function (e) {
        e.preventDefault();

        var submit_btn = $('#add_to_cart_button');
        var book_id = submit_btn.data("book_id");

        basketUpdating(book_id)
    });

    function product_in_order(book_id, quantity){
        var my_form = $('#product_in_basket_form');
        var data = {};
        data.book_id = book_id;
        data.quantity = quantity;
        var csrf_token = $('#product_in_basket_form [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = my_form.attr("action");

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                var book_id = data.id;
                $('#price_per_item_label'+ book_id).html("");
                $('#total_price_label'+ book_id).html("");
                $("#price_per_item_label"+book_id).append( "Price: $" , data.price_per_item);
                $("#total_price_label"+book_id).append("Total price: $" , data.total_price);
            }
        });

    }

     $('#product_in_basket_form').on('change', function (e){
         e.preventDefault();
         // var input_quantity = $(".input_quantity");
         // var quantity = input_quantity.val();
         // var book_id = input_quantity.data("book_id");

         var input_quantity = $(".input_quantity");

         var quantity = new Array();
         for (var p=0; p<input_quantity.length; p++) {

             quantity[p] = input_quantity.eq(p).val();
         }

         var book_id = new Array();
          for (var p=0; p<input_quantity.length; p++) {
             book_id[p] = input_quantity.eq(p).data("book_id");
         }

          for (var p=0; p<input_quantity.length; p++) {
              product_in_order(book_id[p], quantity[p]);
          }

     });


    // $(document).on('click', '.delete-item', function(e){
    //      e.preventDefault();
    //      product_id = $(this).data("product_id");
    //
    //      basketUpdating(product_id)
    //  });

    $('#Name').on('change', function (e) {
            e.preventDefault();
            var input = $('#Name');
            console.log("Ok");
            console.log(input.val());
            if (input.val())
            {
                $('#error1').addClass('hidden');
                $('#correct1').removeClass('hidden');
            }
            else
            {
                $('#error1').removeClass('hidden');
                $('#correct1').addClass('hidden');
            }

        });
    $('#Surname').on('change', function (e) {
            e.preventDefault();
            var input = $('#Surname');
            console.log("Ok");
            console.log(input.val());
            if (input.val())
            {
                $('#error2').addClass('hidden');
                $('#correct2').removeClass('hidden');
            }
            else
            {
                $('#error2').removeClass('hidden');
                $('#correct2').addClass('hidden');
            }

        });
    $('#Email').on('change', function (e) {
            e.preventDefault();
            var input = $('#Email');
            console.log("Ok");
            console.log(input.val());
            if (input.val())
            {
                $('#error3').addClass('hidden');
                $('#correct3').removeClass('hidden');
            }
            else
            {
                $('#error3').removeClass('hidden');
                $('#correct3').addClass('hidden');
            }

        });
    $('#Mobile_number').on('change', function (e) {
            e.preventDefault();
            var input = $('#Mobile_number');
            console.log("Ok");
            console.log(input.val());
            if (input.val())
            {
                $('#error4').addClass('hidden');
                $('#correct4').removeClass('hidden');
            }
            else
            {
                $('#error4').removeClass('hidden');
                $('#correct4').addClass('hidden');
            }

        });
    $('#Address').on('change', function (e) {
            e.preventDefault();
            var input = $('#Address');
            console.log("Ok");
            console.log(input.val());
            if (input.val())
            {
                $('#error_address').addClass('hidden');
                $('#correct_address').removeClass('hidden');
            }
            else
            {
                $('#error_address').removeClass('hidden');
                $('#correct_address').addClass('hidden');
            }

        });



});