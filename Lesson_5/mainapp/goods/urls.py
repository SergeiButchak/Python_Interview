from django.urls import path

from goods.views import GoodListView

app_name = 'products'

urlpatterns = [
    path('', GoodListView.as_view(), name='index'),
    # path('category/<int:category_id>/', PGoodListView.as_view(), name='categories'),
]