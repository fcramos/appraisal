# coding utf-8
from django.test import TestCase

from candidacy.forms import CandidacyForm


class CandidacyFormTest(TestCase):

    def test_form_fields(self):
        'Form should 9 fields'
        form = CandidacyForm()
        self.assertCountEqual([
            'name',
            'email',
            'html_knowledge',
            'css_knowledge',
            'js_knowledge',
            'python_knowledge',
            'django_knowledge',
            'ios_knowledge',
            'android_knowledge'
        ], form.fields)

    def test_knowledge_fields_optional(self):
        'Knowledge fields is optional'
        form = self.make_validated_form(
            html_knowledge=None,
            css_knowledge=None,
            js_knowledge=None,
            python_knowledge=None,
            django_knowledge=None,
            ios_knowledge=None,
            android_knowledge=None
        )
        self.assertFalse(form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(
            name='Felipe Ramos',
            email='felipe@ramos.com',
            html_knowledge=8,
            css_knowledge=8,
            js_knowledge=8,
            python_knowledge=9,
            django_knowledge=10,
            ios_knowledge=0,
            android_knowledge=3
        )
        data.update(kwargs)
        form = CandidacyForm(data)
        form.is_valid()
        return form
