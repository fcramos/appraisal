# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

from candidacy.forms import CandidacyForm


class CandidacyTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('candidacy:form'))

    def test_get(self):
        """
        GET / should return status 200
        """
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'candidacy/index.html')

    def test_html(self):
        'Should contain html elements'
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 82)
        self.assertContains(self.response, 'type="text"')
        self.assertContains(self.response, 'type="reset"')
        self.assertContains(self.response, 'type="radio"', 77)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        'Hmtl must contain csrf token'
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the candidacy form'
        form = self.response.context['form']
        self.assertIsInstance(form, CandidacyForm)


class CandidacyPostTest(TestCase):
    def setUp(self):
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
        self.response = self.client.post(r('candidacy:form'), data)

    def test_post(self):
        'Valid POST should redirect to /'
        self.assertEqual(self.response.status_code, 302)


class CandidacyInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Felipe Ramos',
        )
        self.response = self.client.post(r('candidacy:form'), data)

    def test_post(self):
        'Invalid POST should redirect'
        self.assertEqual(self.response.status_code, 200)

    def test_form_errors(self):
        'Form must contain errors'
        self.assertTrue(self.response.context['form'].errors)
