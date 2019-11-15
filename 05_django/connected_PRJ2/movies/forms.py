from django import forms
from .models import Movie,Rating

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='영화 제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class':'title',
                'placeholder':'영화제목을 입력해주세요....',
            }
        )
    )

    description = forms.CharField(
        label='영화 개요',
        widget=forms.Textarea(
            attrs={
                'class':'content',
                'placeholder':'영화개요를 입력해주세요....',
                'rows':5,
                'cols':30,
            }
        )
    )

   
    class Meta:
        model = Movie
        fields = ('title', 'description', 'poster') # 지정해서 가져오기
        #fields = '__all__' # 전체가져오기


# class CommentForm(forms.ModelForm):
#     content = forms.CharField(
#         label = '댓글',
#         max_length=100,
#         widget=forms.Textarea(
#             attrs={
#                 'class':'content',
#                 'placeholder':'댓글을 입력해주세요!!',
#                 'rows':5,
#                 'cols':30,
#             }
#         )
#     )

#     class Meta:
#         model = Comment
#         fields = ('content',)