from django.shortcuts import render
from django.views.generic import ListView
from goods.models import Good

# Create your views here.


class GoodListView(ListView):
    model = Good
    template_name = 'goods/goods_list.html'

