# coding utf-8
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
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

    def _get_profiles(self):
        profiles = []
        if sum([int(self.data.get('{}_knowledge'.format(x)) or 0) in range(7, 11) for x in ['html', 'css', 'js']]) == 3:
            # Perfil Front-End
            profiles.append('Front-End')

        if sum([int(self.data.get('{}_knowledge'.format(x)) or 0) in range(7, 11) for x in ['python', 'django']]) == 2:
            # Perfil Back-End
            profiles.append('Back-End')

        if sum([int(self.data.get('{}_knowledge'.format(x)) or 0) in range(7, 11) for x in ['ios', 'android']]) == 1:
            # Perfil Mobile
            profiles.append('Mobile')

        if sum([int(self.data.get('{}_knowledge'.format(x)) or 0) > 6 for x in ['html', 'css', 'js', 'python', 'django', 'ios', 'android']]) == 0:
            # Perfil Genérico
            profiles = ['']

        return profiles

    def send_email(self):
        for profile in self._get_profiles():
            msg = EmailMultiAlternatives(
                'Obrigado por se candidatar',
                'This is an important message.',
                settings.SERVER_EMAIL,
                [self.data['email']],
            )

            message = '\n'.join([
                'Obrigado por se candidatar, assim que tivermos uma vaga disponível',
                'para programador {0} entraremos em contato.'.format(profile)
            ])

            html = render_to_string('candidacy/email.html', {'message': message})
            msg.attach_alternative(html, 'text/html')

            msg.send()
