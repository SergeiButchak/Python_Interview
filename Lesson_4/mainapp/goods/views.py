from django.shortcuts import render
from django.views.generic import ListView
from goods.models import Good

# Create your views here.


class GoodListView(ListView):
    model = Good
    template_name = 'goods/goods_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        filter_cat = self.kwargs.get('category_id', None)
        if filter_cat:
            self.set_category_filter(filter_cat)
        context = super(GoodListView, self).get_context_data()
        context['title'] = 'GeekShop - Каталог'
        # context['categories'] = GoodCategory.objects.all()
        context['filter'] = filter_cat
        return context

    def set_category_filter(self, filter_cat):
        # self.object_list = GoodCategory.objects.filter(category=filter_cat)
        pass