from todolist import views
from rest_framework.routers import DefaultRouter

# cria automaticamente todas as urls necessárias para os models presentes no aplicativo,
# além das para os métodos padrão de manipulação dos dados do aplicativo
router = DefaultRouter()
router.register(r'tarefa', views.TarefaViewSet)
urlpatterns = router.urls