from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm) :
  class Meta:
    model=Post
    fields=['title', 'content']

class Commentform(forms.ModelForm):
  class Meta:
    model=Comment
    fields=['username', 'comment_text'] #필드 중 사용자에게 입력받을 필드만 여기에 적어주면 됨