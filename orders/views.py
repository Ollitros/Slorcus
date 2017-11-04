from django.shortcuts import render
from Library.models import *
from orders.models import *
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect


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

    return render(request, 'orders/ordering.html', locals())
