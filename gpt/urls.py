from django.urls import path,include
from .views import CodeFixerView

urlpatterns = [
    path('code_fixer/', CodeFixerView.as_view(), name='code_fixer'),
]
