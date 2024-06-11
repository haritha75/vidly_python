from django.urls import path
from . import views #relative path

app_name = "movies"
# url configuration
urlpatterns = [
  path('',views.index,name='index'), # here i am using reference not function calling when use make request django take resposibility
  path("<int:movie_id>",views.detail,name='detail')
]
# here mepty string nothing but root of this app like ''