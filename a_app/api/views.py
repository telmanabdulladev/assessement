# API larin goruntelenmesiucundur
# listeleme
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from a_app.models import Account, Resource, Question, Forum, Answer, UserAnswerCard,Comment,Result, Exam
from a_app.api.serializers import AccountSerializer, ResourceSerializer, QuestionSerializer,ForumSerializer,AnswerSerializer,UserAnswerCardSerializer,CommentSerializer,ResultSerializer, ExamSerializer

class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
class AccountCreateAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
class AccountRetrieveAPIView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer 
    lookup_field = "id"
    
class AccountUpdateAPIView(UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = "pk" 
    
class AccountDeleteAPIView(DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = "pk"
    
class ResourceListAPIView(ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    
class ResourceCreateAPIView(CreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    
class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class=QuestionSerializer
    
class ForumListAPIView(ListAPIView):
    queryset = Forum.objects.all()
    serializer_class=ForumSerializer  
    
class AnswerListAPIView(ListAPIView):
    queryset = Answer.objects.all()
    serilaizer_class=AnswerSerializer
    
class UserAnswerCardListAPIView(ListAPIView):
    queryset=UserAnswerCard.objects.all()
    serializer_class=UserAnswerCardSerializer 
    
class CommentListAPIView(ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    
class ResultListAPIView(ListAPIView):
    queryset=Result.objects.all()
    serializer_class=ResultSerializer  

class ExamListAPIView(ListAPIView):
    queryset=Exam.objects.all()
    serializer_class =ExamSerializer
    
    
    
    
