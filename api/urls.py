
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('user-questions/<int:user>', views.QuestionDetailClass.as_view(),name='questions'),
    path('questions/', views.QuestionDetailClass.as_view(),name='questions'),
    path('solutions/', views.SolutionDetailClass.as_view(),name='solutions'),
    path('solutions/<int:questionId>', views.SolutionDetailClass.as_view(),name='solutions'),
    path('solutions/update/<int:solutionId>', views.getSolutionById,name='solutions'),
   
    path('posts/', views.PostView.as_view(),name='posts'),
    path('posts/<int:postId>', views.getPostById,name='posts'),


    
]

urlpatterns = format_suffix_patterns(urlpatterns)
