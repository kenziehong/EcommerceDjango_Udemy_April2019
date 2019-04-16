#from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

#get_context_data(abc, 123, afddgs, another=abc, abc=123)

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request,"products/list.html",context)


class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		#context['abc'] = 123
		return context

	
def product_detail_view(request, pk=None, *args, **kwargs ):
	#print(args)
	#print(kwargs)
	#queryset = Product.objects.all()
	#instance = Product.objects.get(pk=pk) #id, primary key
	#instance = get_object_or_404(Product, pk=pk)

	# try:
	# 	instance = Product.objects.get(id=pk)
	# except Product.DoesNotExist:
	# 	print('no product here')
	# 	raise Http404("Product doesnt exist")
	# except:
	# 	print("huh?")		

	qs = Product.objects.filter(id=pk)
	if qs.exists() and qs.count() ==1:
		instance = qs.first()
	else:
		raise Http404("Product doesnt exist")		
	
	context = {
		"object": instance,
		#"abc" : 123
	} 
	return render(request,"products/detail.html",context)
