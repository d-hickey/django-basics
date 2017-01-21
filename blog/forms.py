from django.forms import ModelForm

from .models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title_text', 'body_text',)
