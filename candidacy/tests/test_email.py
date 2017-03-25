from django.test import TestCase
from django.core import mail

from candidacy.forms import CandidacyForm


class CandidacyEmailTest(TestCase):
    def make_form(self, **kwargs):
        data = dict(
            name='Felipe Ramos',
            email='felipe@ramos.com',
        )
        data.update(kwargs)
        form = CandidacyForm(data)
        form.is_valid()
        return form

    def test_send_email(self):
        'One generic email should be sent'
        self.make_form().send_email()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Obrigado por se candidatar')

    def test_generic_email(self):
        'One generic email should be sent with all knowledge lower than 7'
        form = self.make_form(
            html_knowledge=6,
            css_knowledge=4,
            js_knowledge=2,
            python_knowledge=5,
            django_knowledge=6,
            ios_knowledge=4,
            android_knowledge=3,
        )
        form.send_email()

        self.assertEqual(len(mail.outbox), 1)
        self.assertListEqual(form._get_profiles(), [''])
        for index, profile in enumerate(['']):
            self.assertIn(profile, mail.outbox[index].alternatives[0][0])

    def test_frontend_email(self):
        'One frontend email should be sent'
        form = self.make_form(
            html_knowledge=8,
            css_knowledge=8,
            js_knowledge=8,
        )
        form.send_email()

        self.assertEqual(len(mail.outbox), 1)
        self.assertListEqual(form._get_profiles(), ['Front-End'])
        for index, profile in enumerate(['Front-End']):
            self.assertIn(profile, mail.outbox[index].alternatives[0][0])

    def test_backend_email(self):
        'One backend email should be sent'
        form = self.make_form(
            python_knowledge=8,
            django_knowledge=8,
        )
        form.send_email()

        self.assertEqual(len(mail.outbox), 1)
        self.assertListEqual(form._get_profiles(), ['Back-End'])
        for index, profile in enumerate(['Back-End']):
            self.assertIn(profile, mail.outbox[index].alternatives[0][0])

    def test_mobile_email(self):
        'One mobile email should be sent'
        form = self.make_form(
            ios_knowledge=8,
        )
        form.send_email()

        self.assertEqual(len(mail.outbox), 1)
        self.assertListEqual(form._get_profiles(), ['Mobile'])
        for index, profile in enumerate(['Mobile']):
            self.assertIn(profile, mail.outbox[index].alternatives[0][0])

    def test_frontend_backend_email(self):
        'Two emails should be sent'
        form = self.make_form(
            html_knowledge=8,
            css_knowledge=8,
            js_knowledge=8,
            python_knowledge=8,
            django_knowledge=8,
        )
        form.send_email()

        self.assertEqual(len(mail.outbox), 2)
        self.assertListEqual(form._get_profiles(), ['Front-End', 'Back-End'])
        for index, profile in enumerate(['Front-End', 'Back-End']):
            self.assertIn(profile, mail.outbox[index].alternatives[0][0])

    def test_frontend_backend_mobile_email(self):
        'Tree emails should be sent'
        form = self.make_form(
            html_knowledge=8,
            css_knowledge=8,
            js_knowledge=8,
            python_knowledge=8,
            django_knowledge=8,
            android_knowledge=8,
        )
        form.send_email()

        self.assertEqual(len(mail.outbox), 3)
        self.assertListEqual(form._get_profiles(), ['Front-End', 'Back-End', 'Mobile'])
        for index, profile in enumerate(['Front-End', 'Back-End', 'Mobile']):
            self.assertIn(profile, mail.outbox[index].alternatives[0][0])
