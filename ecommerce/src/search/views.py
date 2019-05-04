from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.
class SearchProductView(ListView):
	#queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		print(request.GET)
		method_dict = request.GET
		query = method_dict.get('q', None) #method_dict['q']
		if query is not None:
			return Product.objects.filter(title__icontains=query)
		return Product.objects.featured()	
		'''
		__icontains = field contains this
		__iexact = fields is exactly this

		'''