# serializer yazmaq ucundur (siralanma)
# cedvel formatindan kecirik JSON formatina. Niye gore? Cunki JSON formati beynelaxlaq standart formatidir ve butun proqramlasdirma dilleri terefinden taninir. Bu da bize imkan verir, biz muxtelif proqramlasdirma dillerinde yazilmis proyetleri bir-birine inteqrasiya ede bilek. Python ile yazdiqim API-yi basqa bir proyekt yazilib JavaScript ile yazilib onlari bir -birine inteqrasiya ede bilek.URL-lere request gonserilerek elde olunan melumatlar istenilen yerde istifade edile bilir.
from rest_framework.serializers import ModelSerializer
from a_app.models import Account, Resource, Exam, Forum, Comment, Question, Answer, UserAnswerCard, Result

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        
        # saheleri eyni olduqu ucun creat-ni yaratmaqa ehtiyac yoxdur
# class AccountCreateSerializer(ModelSerializer):
#     class Meta:
#         model= Account
#         fields = "__all__"



        
class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"

class ResourceCreateSerializer(ModelSerializer):
    class Meta:
        model = Resource
        exclude = ("date",) 

class ExamSerializer(ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"
        
class ForumSerializer(ModelSerializer):
    class Meta:
        model = Forum
        fields = "__all__"
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        
class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question  
        fields = "__all__"
        
class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
        
class UserAnswerCardSerializer(ModelSerializer):
    class Meta:
        model = UserAnswerCard
        fields = "__all__"
        
class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"
        
class ExamSerializer(ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"
        

        

        

        
        
        
    
    
