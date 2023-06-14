from django.shortcuts import render


def def_url_elements(request):
    url_elements_list = request.path.split("/")
    print("url_elements_list: ", url_elements_list)
    print("last_url_element: ", url_elements_list[-2])
    return {"last_url_element": url_elements_list[-2]}


def index(request):
    last_url_element = def_url_elements(request)
    return render(request, "website/base.html", last_url_element)


def home(request):
    last_url_element = {"last_url_element": "home"}
    return render(request, "website/home.html", last_url_element)


def info(request):
    last_url_element = def_url_elements(request)
    return render(request, "website/info.html", last_url_element)


def courts(request):
    last_url_element = def_url_elements(request)
    return render(request, "website/courts.html", last_url_element)


def sproduct1(request):
    last_url_element = def_url_elements(request)
    return render(request, "website/sproduct1.html", last_url_element)


def sproduct2(request):
    last_url_element = def_url_elements(request)
    return render(request, "website/sproduct2.html", last_url_element)


def sproduct3(request):
    last_url_element = def_url_elements(request)
    return render(request, "website/sproduct3.html", last_url_element)


def sproduct4(request):
    last_url_element = def_url_elements(request)
    return render(request, "website/sproduct4.html", last_url_element)


def sproduct5(request):
    last_url_element = def_url_elements(request)
    return render(request, "website/sproduct5.html", last_url_element)


def store(request):
    last_url_element = def_url_elements(request)
    objects_array = [
        {
            "id": "1",
            "title": "adidas 1",
            "vendor_code": "adidas shoes 1",
            "description": "Adizero Cubersonic Tennis Shoes",
            "price": 98,
            "img": "/images/adidas_shoes.jpg",
            "onclick": "window.location.href='http://127.0.0.1:8000/websiteApp/store/sproduct1/';",
        },
        {
            "id": "2",
            "title": "adidas 2",
            "vendor_code": "adidas shoes 2",
            "description": "Adizero Ubersonic 4 Tennis Shoes",
            "price": 92,
            "img": "/images/adidas_shoes2.jpg",
            "onclick": "window.location.href='http://127.0.0.1:8000/website/store/sproduct2/';",
        },
        {
            "id": "3",
            "title": "nike 1",
            "vendor_code": "nike shoes 1",
            "description": "NikeCourt Air Zoom Vapor Pro 2",
            "price": 120,
            "img": "images/nike_shoes.jpg",
            "onclick": "window.location.href='http://127.0.0.1:8000/website/store/sproduct3/';",
        },
        {
            "id": "4",
            "title": "nike 2",
            "vendor_code": "nike shoes 2",
            "description": "NikeCourt Air Zoom Vapor Pro 9.5 Tour",
            "price": 128,
            "img": "images/nike_shoes2.jpg",
            "onclick": "window.location.href='http://127.0.0.1:8000/website/store/sproduct4/';",
        },
    ]
    dict_of_array = {"objects_array": objects_array}
    context = {"urls": last_url_element, "dict_of_array": dict_of_array}
    print(context)
    return render(request, "website/store.html", context)


def store_result(request):  # http://127.0.0.1:8000/renderApp/greet/Ивaнoв
    print(request.__dir__())
    req = dict(request.GET)
    print(req)
    vendor_code = req.get("vendor_code")
    amount = req.get("amount")
    print(vendor_code, amount)
    i = 0
    d = {}
    for _ in vendor_code:
        print(vendor_code[i], amount[i])
        d[vendor_code[i]] = amount[i]
        i += 1
    print(d)
    return render(request, "website/store_result.html", {"d": d})
