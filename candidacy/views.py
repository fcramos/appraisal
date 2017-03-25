from django.views.generic.edit import FormView
from django.contrib import messages

from .forms import CandidacyForm


class CandidacyView(FormView):
    template_name = 'candidacy/index.html'
    form_class = CandidacyForm
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Candidatura enviado com sucesso')
        return super(CandidacyView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Falha ao enviar a candidatura')
        return super(CandidacyView, self).form_invalid(form)
