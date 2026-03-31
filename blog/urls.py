from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
  path('', home, name='home'),
  path('post/<int:post_id>', detail, name='detail'),
  path('new/', new, name="new"),
  path('create/', create, name="create"),
  path('delete/<int:post_id>', delete, name="delete"),
  path('update_page/<int:post_id>', update_page, name="update_page"),
  path('update_post/<int:post_id>', update_post, name="update_post"),
  path('<int:post_id>/comment', add_comment, name='add_comment'), 
  #자료랑 다른 부분(위에서 이미 경로 설정해주었기 때문에, 여기서는 view 함수명만 적어주면됨) (자료와의 차이점 이해해보기)
]