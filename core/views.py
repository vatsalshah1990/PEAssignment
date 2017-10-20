from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.utils import timezone

from core.models import Prescription, MedicalRecord


@login_required(login_url="login/")
def home(request):
    return render(request, "index.html")


class PrescriptionDetailView(DetailView):

    model = Prescription
    template_name = 'prescription_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PrescriptionDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class MedicalRecordDetailView(DetailView):

    model = MedicalRecord
    template_name = 'medicalrecord_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MedicalRecordDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
