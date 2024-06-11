from django.urls import path
from .views import bank, created

urlpatterns = [
    path('', bank, name='bank'),        # URL pattern for the bank view
    path('created/<int:accno>/', created, name='created'),   # URL pattern for the created view
]
