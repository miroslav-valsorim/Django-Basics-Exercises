from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic as views

from shopping_cart.product.models import Products, Category


class ListProductsView(views.ListView):
    model = Products
    paginate_by = 2
    template_name = 'products/products_list.html'
    # context_object_name = 'products / 'products' else its 'object_list' in the template

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = Products.get_all_products_by_categoryid(category_id)
        else:
            queryset = Products.get_all_products()

        queryset = queryset.exclude(category__name="Tickets")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.get_all_categories()

        # Exclude the category "tickets"
        categories = [category for category in categories if category.name != "Tickets"]

        context['categories'] = categories
        return context


class DetailProductView(views.DetailView):
    model = Products
    template_name = 'products/product_details.html'


class CategoryView(views.View):
    def get(self, request, *args, **kwargs):
        # cart = request.session.get('cart')
        # if not cart:
        #     request.session['cart'] = {}

        category_id = request.GET.get('category')
        categories = Category.get_all_categories()
        categories = [category for category in categories if category.name != "Tickets"]  # case sensitive
        products = Products.get_all_products_by_categoryid(category_id)

        data = {
            'products': products,
            'categories': categories,
            # 'user_email': request.session.get('email')
        }

        return render(request, 'products/categories.html', data)


class ListTicketsView(views.ListView):
    model = Products
    paginate_by = 2
    template_name = 'products/tickets_list.html'
    # context_object_name = 'products / 'products' else its 'object_list' in the template

    def get_queryset(self):
        category = Category.objects.get(name='Tickets')
        if category:
            queryset = Products.get_all_products_by_categoryid(category.id)
        else:
            queryset = Products.get_all_products()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.get_all_categories()

        # Exclude the category "tickets"
        categories = [category for category in categories if category.name == "Tickets"]

        context['categories'] = categories
        return context


# class Index(views.View):
#
#     def post(self, request):
#         # product = request.POST.get('product')
#         # remove = request.POST.get('remove')
#         # cart = request.session.get('cart')
#         # if cart:
#         #     quantity = cart.get(product)
#         #     if quantity:
#         #         if remove:
#         #             if quantity <= 1:
#         #                 cart.pop(product)
#         #             else:
#         #                 cart[product] = quantity - 1
#         #         else:
#         #             cart[product] = quantity + 1
#         #
#         #     else:
#         #         cart[product] = 1
#         # else:
#         #     cart = {}
#         #     cart[product] = 1
#         #
#         # request.session['cart'] = cart
#         # print('cart', request.session['cart'])
#         return redirect('home_page')
#
#     def get(self, request):
#         # print()
#         return HttpResponseRedirect(f'/products{request.get_full_path()[1:]}')


# def list_products(request):
#     cart = request.session.get('cart')
#     if not cart:
#         request.session['cart'] = {}
#
#     products = None
#     categories = Category.get_all_categories()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Products.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Products.get_all_products()
#
#     print(categoryID)
#
#     data = {
#         'products': products,
#         'categories': categories,
#         'user_email': request.session.get('email')  # Add user email to data
#     }
#
#     print('you are : ', request.session.get('email'))
#     return render(request, 'products/products_list.html', data)


# class ListProductsView(views.ListView):
#     model = Products
#     paginate_by = 2
#     template_name = 'products/products_list.html'
#
#     def get(self, request, *args, **kwargs):
#         # cart = request.session.get('cart')
#         # if not cart:
#         #     request.session['cart'] = {}
#
#         products = None
#         categories = Category.get_all_categories()
#         category_ID = request.GET.get('category')
#
#         if category_ID:
#             products = Products.get_all_products_by_categoryid(category_ID)
#         else:
#             products = Products.get_all_products()
#
#         data = {
#             'products': products,
#             'categories': categories,
#             # 'user_email': request.session.get('email')  # Add user email to data
#         }
#
#         # print('you are : ', request.session.get('email'))
#         return render(request, 'products/products_list.html', data)
