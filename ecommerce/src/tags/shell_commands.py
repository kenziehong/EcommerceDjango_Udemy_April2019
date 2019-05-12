Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Users\Administrator> cd Dev
PS C:\Users\Administrator\Dev> cd ecommerce
PS C:\Users\Administrator\Dev\ecommerce> cd src
PS C:\Users\Administrator\Dev\ecommerce\src> ls


    Directory: C:\Users\Administrator\Dev\ecommerce\src


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----         4/15/2019  10:21 PM            ecommerce
d----         4/20/2019   3:43 PM            products
d----          5/4/2019   6:55 PM            search
d----         4/16/2019   9:43 AM            static_my_proj
d----         5/12/2019   5:37 PM            tags
d----         4/23/2019  12:26 PM            templates
-a---         5/12/2019   5:41 PM     172032 db.sqlite3
-a---         4/15/2019   9:39 AM        829 manage.py


PS C:\Users\Administrator\Dev\ecommerce\src> python manage.py shell
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from tags.models import Tag
>>> Tag.object.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Tag' has no attribute 'object'
>>> Tag.objects.all()
<QuerySet [<Tag: T shirt>, <Tag: TShirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Black>]>
>>> Tag.object.last()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Tag' has no attribute 'object'
>>> Tag.objects.last()
<Tag: Black>
>>> black=Tag.objects.last()
>>> black.title
'Black'
>>> black.slug
'black'
>>> black.active
True
>>> black.products
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0
x0000000003F83EB8>
>>> black.products.all()
<ProductQuerySet [<Product: Hat>, <Product: SuperComputer>, <Product: T-shirt>]>
>>> black.products.all().first()
<Product: Hat>
>>> exit()
PS C:\Users\Administrator\Dev\ecommerce\src> python manage.py shell
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> qs=Product.objects.all()
>>> qs
<ProductQuerySet [<Product: Lorem Ipsum>, <Product: Hat>, <Product: SuperComputer>, <Product: T-shirt>]>
>>> tshirt=qs.last()
>>> tshirt
<Product: T-shirt>
>>> tshirt.title
'T-shirt'
>>> tshirt.tag
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Product' object has no attribute 'tag'
>>> tshirt.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0
x0000000003F69CC0>
>>> tshirt.tag_set.all()
<QuerySet [<Tag: T shirt>, <Tag: TShirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Black>]>
>>> tshirt.tag_set.filter(title__iexact='Black')
<QuerySet [<Tag: Black>]>
>>>
