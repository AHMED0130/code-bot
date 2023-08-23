from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import CodeSerializer
from .models import Code
import openai

# Create your views here.


class CodeFixerView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        queryset=Code.objects.filter(user_id=request.user.id)
        serializer=CodeSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        problem = serializer.validated_data['problem']
        language = serializer.validated_data['language']
        serializer.validated_data.update({"user_id":request.user.id})
        #enter your own key...  
        openai.api_key = '***********************'
        
        try:
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f"respond only with code problem is {problem} programming language is {language}",
                temperature=0,
                max_tokens=1000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            
            solution = response.choices[0].text.strip()
            
            # Save the data to the database
            code_instance = Code(problem=problem, language=language, solution=solution)
            code_instance.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



