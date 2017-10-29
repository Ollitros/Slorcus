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

    products_in_basket = OrderInBasket.objects.filter(session_key=session_key)

    # book = Book.objects.filter(id=book_id)

    return_dict = dict()
    # return_dict["products"] = list()
    for item in products_in_basket:
        print(item.id)
        print(item.session_key)
        print(item.book_id)

    for item in products_in_basket:
        return_dict["book_id"] = item.book_id
        return_dict["session_key"] = item.session_key

    return JsonResponse(return_dict)

