from django.contrib.auth import get_user_model
from rest_framework import serializers 
from djoser.serializers import UserCreateSerializer

from .models    import Question,Solution,Post


User = get_user_model()



class CreateUserSerializer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'
        depth=2
        

class QuestionSerializer(serializers.ModelSerializer):
    

  
    class Meta:
        model = Question
        fields =[ 'id','question_title','question_link','question_created','question_updated','question_author','question_description','question_type','question_status','question_topics']
        
        
        
        




 
class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields =[ 'id','solution_approach','solution_time_complexity','solution_space_complexity','solution_type','solution_question','code_snippets','created_at','updated_at']




POST_TYPES = [
        ('Interview Experience', 'Interview Experience'),
        ('Technical Discussion', 'Technical Discussion'),
        ('Project Showcase', 'Project Showcase'),
        ('General Advice', 'General Advice'),
        ('Event Announcement', 'Event Announcement'),
       
    ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','post_author','post_title','post_content','post_images','post_type','created_at','updated_at']
       