Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> queryset = Product.objects.all()
>>> queryset
<QuerySet [<Product: T-shirt>, <Product: Hat>]>
>>> qs = Product.objects.filter(title__contains="shirt")
>>> qs
<QuerySet [<Product: T-shirt>]>
>>> qs = Product.objects.filter(title__contains="hat")
>>> qs
<QuerySet [<Product: Hat>]>
>>> qs = Product.objects.filter(description__contains="hat")
>>> qs
<QuerySet [<Product: Hat>]>
>>> qs = Product.objects.filter(description__icontains="hat")
>>> qs
<QuerySet [<Product: Hat>]>
>>>
>>> qs = Product.objects.filter(description__icontains="product")
>>> qs
<QuerySet []>