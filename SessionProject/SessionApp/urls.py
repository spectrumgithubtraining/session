
from django.urls import path
from.import views
# Example urls.py

# from django.urls import path
# from .views import index_view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index/', index_view, name='index'),  # Make sure this line is present
# ]



urlpatterns = [
    path('',views.index,name='index'),
    path('reg/',views.reg,name='reg'),
]

