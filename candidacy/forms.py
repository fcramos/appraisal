# coding utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _


class CandidacyForm(forms.Form):
    CHOICES = [(x, x) for x in range(11)]
    name = forms.CharField(
        label=_('Nome'),
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})

    )
    html_knowledge = forms.ChoiceField(
        label=_('HTML'),
        required=False,
        choices=CHOICES,
        widget=forms.RadioSelect()
    )
    css_knowledge = forms.ChoiceField(
        label=_('CSS'),
        required=False,
        choices=CHOICES,
        widget=forms.RadioSelect()
    )
    js_knowledge = forms.ChoiceField(
        label=_('JavaScript'),
        required=False,
        choices=CHOICES,
        widget=forms.RadioSelect()
    )
    python_knowledge = forms.ChoiceField(
        label=_('Python'),
        required=False,
        choices=CHOICES,
        widget=forms.RadioSelect()
    )
    django_knowledge = forms.ChoiceField(
        label=_('Django'),
        required=False,
        choices=CHOICES,
        widget=forms.RadioSelect()
    )
    ios_knowledge = forms.ChoiceField(
        label=_('Desenvolvimento iOS'),
        required=False,
        choices=CHOICES,
        widget=forms.RadioSelect()
    )
    android_knowledge = forms.ChoiceField(
        label=_('Desenvolvimento Android'),
        required=False,
        choices=CHOICES,
        widget=forms.RadioSelect()
    )
