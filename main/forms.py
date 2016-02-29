from django import forms


class MathForm(forms.Form):


    operator = forms.ChoiceField(choices=[('', '+'), ('', '-'), ('', '*'), ('', '/')])

