from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        # HTML Tag와 동일
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'title',
                'placeholder':'제목을 입력해 주세요...!',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        # widget : Input Type 지정 -> Textarea / 알맞은 속성값 부여
        widget=forms.Textarea(
            attrs={
                'class':'content',
                'placeholder':'내용을 입력해 주세요오오오옹',
                'rows':5,
                'cols':30,
            }
        )
    )
    