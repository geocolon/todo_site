from django import forms # type: ignore
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"