from django.urls import path
from a_app.api import views  


urlpatterns = [
    path('accounts/',views.AccountListAPIView.as_view(),name="accounts"),
    path('account-create/',views.AccountCreateAPIView.as_view(),name="account_create"),
    path('account-retrieve/<int:id>/',views.AccountRetrieveAPIView.as_view(),name="account_retrieve"),
    path('account-update/<int:pk>/',views.AccountUpdateAPIView.as_view(),name="account_update"),
    path('account-delete/<int:pk>/',views.AccountDeleteAPIView.as_view(),name="account_delete"),
    path('forums/',views.ForumListAPIView.as_view(),name='forums'),
    path('exams/',views.ExamListAPIView.as_view(), name='exams'),
    path('resources/',views.ResourceListAPIView.as_view(),name='resources'),
    path('resource-create/',views.ResourceCreateAPIView.as_view(),name='resources-create'),
    path('questions/',views.QuestionListAPIView.as_view(),name='questions'),
    path('answers/',views.AnswerListAPIView.as_view(),name='answers'),
    path('useranswercards/',views.UserAnswerCardListAPIView.as_view(),name='useranswercards'),
    path('results/',views.ResultListAPIView.as_view(),name='results'),
    path('comments/',views.CommentListAPIView.as_view(),name='comments')
]