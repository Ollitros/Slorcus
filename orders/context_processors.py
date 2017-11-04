from .models import OrderInBasket
from Library.models import *


def getting_basket_info(request):

    session_key = request.session.session_key
    if not session_key:
        #workaround for newer Django versions
        request.session["session_key"] = 123
        #re-apply value
        request.session.cycle_key()

    products_in_basket = OrderInBasket.objects.filter(session_key=session_key)

    # book_id_in_session = list()
    # for item in products_in_basket:
    #     book_id_in_session.append(item.book_id)
    #
    # book_objects = dict()
    # for item in book_id_in_session:
    #     c = 0
    #     book_objects[item] = Book.objects.filter(id=book_id_in_session[c])
    #     c = c + 1
    #     print(book_objects[item])

    return locals()