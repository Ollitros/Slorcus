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
                    $('#basket').append("<p>" + v.book_id + v.name + "</p>");
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
                console.log(data.amount);
                $('#price_per_item_label').html("");
                $('#total_price_label').html("");
                $("#price_per_item_label").append( "Price: $" , data.price_per_item);
                $("#total_price_label").append("Total price: $" , data.total_price);
            }
        });

    }

     $('#product_in_basket_form').on('change', function (e){
         e.preventDefault();
         // var product_in_ordering_form = $('product_in_basket_form');
         var input_quantity = $("#quantity");
         var quantity = input_quantity.val();
         var book_id = input_quantity.data("book_id");
         console.log(quantity);
         console.log(book_id);
         product_in_order(book_id, quantity);

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

});