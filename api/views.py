from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer,SolutionSerializer,PostSerializer
from .models import Question,Solution,Post
from rest_framework import status
from rest_framework.views import APIView


class QuestionDetailClass(APIView):

    def get(self,request,user,format=None):
    
        questions=Question.objects.filter(question_author=user)
    
        if questions:
            serializer=QuestionSerializer(questions,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            default_errors = serializer.errors
            new_error = {}
            for field_name, field_errors in default_errors.items():
                new_error[field_name] = field_errors[0]
            return Response(new_error, status=status.HTTP_400_BAD_REQUEST)
    


    

  


    def post(self,request,format=None):
        serializer=QuestionSerializer(data=request.data)
        print(request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            default_errors = serializer.errors
            new_error = {}
            for field_name, field_errors in default_errors.items():
                new_error[field_name] = field_errors[0]
            return Response(new_error, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request):
        data=request.data
        id=data['id']
        serializer=QuestionSerializer(data=data)
        if id:
            question=Question.objects.get(id=id)
            if id and question:
                serializer=QuestionSerializer(instance=question,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            default_errors = serializer.errors
            new_error = {}
            for field_name, field_errors in default_errors.items():
                new_error[field_name] = field_errors[0]
            return Response(new_error, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request):
        data=request.data
        id=data['id']
        question=Question.objects.filter(id=id)
        if id and question:
        
            question.delete()
            return Response('Question Deleted',status=status.HTTP_200_OK)
        else:
            return Response('Question Not Found',status=status.HTTP_404_NOT_FOUND)



class SolutionDetailClass(APIView):

    def post(self,request):
        data=request.data
        serializer=SolutionSerializer(data=data)
        
    
        solutionType=data['solution_type']
        print(solutionType)
        previousQuestionWithSameSolutionType=Solution.objects.filter(solution_type=solutionType,solution_question=data['solution_question'])
        if previousQuestionWithSameSolutionType:
            return Response('Solution with same type already exists for this question',status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            default_errors = serializer.errors
            new_error = {}
            for field_name, field_errors in default_errors.items():
                new_error[field_name] = field_errors[0]
            return Response(new_error, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,questionId):
        solutions=Solution.objects.filter(solution_question=questionId)
        if solutions:
            serializer=SolutionSerializer(solutions,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response('No Solutions Found',status=status.HTTP_404_NOT_FOUND)
        
    
        
    def patch(self,request):
        data = request.data
        solution_type=data['solution_type']
        id=data['id']
        solution=Solution.objects.filter(id=id)
        if id and solution:
            previousQuestionWithSameSolutionType=Solution.objects.filter(solution_type=solution_type,solution_question=data['solution_question']).exclude(id=id)
            if previousQuestionWithSameSolutionType:
                return Response('Solution with same type already exists for this question',status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer=SolutionSerializer(instance=solution[0],data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response('Invalid Data',status=status.HTTP_400_BAD_REQUEST)
                
        else:
            return Response('Solution Not Found',status=status.HTTP_404_NOT_FOUND)
        
    
       
           
       
        
    def delete(self,request):
        data=request.data
        id=data['id']
        solution=Solution.objects.filter(id=id)
        if id and solution:
            solution.delete()
            return Response('Solution Deleted',status=status.HTTP_200_OK)
        else:
            return Response('Solution Not Found',status=status.HTTP_404_NOT_FOUND)
        

        
    
        
class PostView(APIView):
    def get(self,request):
        posts=Post.objects.all()
        if posts:
            serializer=PostSerializer(posts,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response('No Posts Found',status=status.HTTP_404_NOT_FOUND)
    
        
        
    def post(self,request):
        data=request.data
        serializer=PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response('Invalid Data',status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request):
        data=request.data
        id=data['id']
        post=Post.objects.filter(id=id)
        if post:
            serializer=PostSerializer(instance=post[0],data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response('Invalid Data',status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Post Not Found',status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request):
        data=request.data
        id=data['id']
        post=Post.objects.filter(id=id)
        if post:
            post.delete()
            return Response('Post Deleted',status=status.HTTP_200_OK)
        else:
            return Response('Post Not Found',status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getPostById(request,postId):
    post=Post.objects.filter(id=postId)
    if post:
        serializer=PostSerializer(post[0])
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response('Post Not Found',status=status.HTTP_404_NOT_FOUND)
        

@api_view(['GET'])
def getSolutionById(request,solutionId):
    solution=Solution.objects.filter(id=solutionId)
    if solution:
        serializer=SolutionSerializer(solution[0])
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response('Solution Not Found',status=status.HTTP_404_NOT_FOUND)
        
            
            

