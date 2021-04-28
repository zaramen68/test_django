from rest_framework import serializers
from .models import Article, Poll, Question, Choice, Answer, Respondent


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author_id')


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'timeOfBegin', 'title', 'description', 'body', 'questions') 

        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'typeQ', 'title', 'description', 'polls') 

class ChoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('question_id', 'text', 'votes') 


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('respondent', 'question', 'answerIs')        


class RespondentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respondent
        fields = ('name', )         

        
    # title = serializers.CharField(max_length=120)
    # description = serializers.CharField()
    # body = serializers.CharField()
    # author_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Article.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.body = validated_data.get('body', instance.body)
    #     instance.author_id = validated_data.get('author_id', instance.author_id)
    #     instance.save()
    #     return instance