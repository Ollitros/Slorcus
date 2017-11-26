from django.shortcuts import render
from django.shortcuts import redirect
from Library.models import *
from orders.models import *
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from orders.forms import *


def basket_adding(request):

    session_key = request.session.session_key
    print(request.POST)

    data = request.POST
    book_id = data.get("book_id")

    if not OrderInBasket.objects.filter(book_id=book_id):
        print("False")
        b = OrderInBasket(book_id=book_id, session_key=session_key)
        b.save()

        c = OrderInBasket.objects.get(book_id=book_id)
        book_object = Book.objects.get(id=book_id)
        print(book_object)
        book_object.orderinbasket_set.add(c)

    products_in_basket = OrderInBasket.objects.filter(session_key=session_key)

    return_dict = dict()
    return_dict["products"] = list()

    for item in products_in_basket:
        print(item.id)
        print(item.session_key)
        print(item.book_id)

    # for item in book_info:
    #     return_dict["book_name"] = item.name

    for item in products_in_basket:
        product_dict = dict()
        product_dict["name"] = item.books.name
        product_dict["book_id"] = item.book_id
        product_dict["session_key"] = item.session_key
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def product_in_order(request):
    session_key = request.session.session_key
    print("PRODUCT IN ORDER:")
    # print(request.POST)

    data = request.POST
    book_id = data.get("book_id")
    book_quantity = data.get("quantity")

    print("book_id = ", book_id)
    print("quantity = ", book_quantity)

    preliminary_test_product = ProductInOrder.objects.filter(session_key_product_in_order=session_key, product__id=book_id)

    for item in preliminary_test_product:
        print("preliminary_test_product: ", item.quantity)
        print("preliminary_test_product: ", item.product.id)

    if not preliminary_test_product:
        print("PRODUCT IN ORDER IS FALSE(does not exist)")
        book = Book.objects.get(id=book_id)
        book_in_order = ProductInOrder(session_key_product_in_order=session_key, quantity=book_quantity)
        book_in_order.product = book
        book_in_order.price_per_item = book.price
        book_in_order.save()
    else:
        print("PRODUCT IN ORDER IS TRUE(EXISTS)")
        book_in_order = ProductInOrder.objects.get(session_key_product_in_order=session_key, product__id=book_id)
        book_in_order.quantity = book_quantity
        book_in_order.save()

    book_in_order = ProductInOrder.objects.get(session_key_product_in_order=session_key, product__id=book_id)

    product_in_order_id = book_in_order.product.id
    amount = book_in_order.quantity
    price_per_item = book_in_order.price_per_item
    total_price = book_in_order.total_price

    return_dict = dict()
    return_dict["id"] = product_in_order_id
    return_dict["amount"] = amount
    return_dict["price_per_item"] = price_per_item
    return_dict["total_price"] = total_price

    return JsonResponse(return_dict)


def ordering(request, book_id):
    print(book_id)
    session_key = request.session.session_key

    if not OrderInBasket.objects.filter(book_id=book_id):
        print("False")
        b = OrderInBasket(book_id=book_id, session_key=session_key)
        b.save()

        c = OrderInBasket.objects.get(book_id=book_id)
        book_object = Book.objects.get(id=book_id)
        print(book_object)
        book_object.orderinbasket_set.add(c)

    products = OrderInBasket.objects.filter(session_key=session_key)
    products_in_order = ProductInOrder.objects.filter(session_key_product_in_order=session_key)

    """FORMS FOR ORDERING"""

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST, request.FILES)
        form_p = ProductsForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            appendage = form.cleaned_data['appendage']
            mobile_number = form.cleaned_data['mobile_number']
            address = form.cleaned_data['address']
            image = form.cleaned_data['image']

            order = Order(address=address, email=email, mobile_number=mobile_number, appendage=appendage,
                          name=name, surname=surname, session_key_in_order=session_key, image=image)
            order.save()
            prod_in_order = ProductInOrder.objects.filter(session_key_product_in_order=session_key)
            order = Order.objects.get(session_key_in_order=session_key)

            for item in prod_in_order:
                item.order = order
                total_price_prod = item.total_price
                total_price_order = order.total_price
                total_price_order = total_price_order + total_price_prod
                order.total_price = total_price_order

                item.save()
                order.save()

            products_in_basket = OrderInBasket.objects.filter(session_key=session_key)
            products_in_basket.delete()
            products_in_basket.update()


            return redirect('/done_ordering/')

            # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()

    # if products_in_order:
    #     for prod in products:
    #         for prorder in products_in_order:
    #             if int(prod.book_id) == prorder.product.id:
    #                 return redirect('/check_on_exist/')


    return render(request, 'orders/ordering.html', locals())


def done_ordering(request):
    return render(request, 'orders/done_ordering.html', locals())

def check_on_exist(request):
    return render(request, 'orders/check_on_exist.html', locals())
