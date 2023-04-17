from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Allo, galocka!')

    class Meta:
        model = Post
        fields = ['author', 'title', 'rating', 'text', 'check_box']
