from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.utils import timezone

from core.models import Prescription, MedicalRecord, Approval, User


@login_required(login_url="login/")
def home(request):
    context = {}
    if request.user.user_type == "PA":
        context["pending_approvals"] = Approval.objects.filter(status="PE", prescription__user=request.user)
    else:
        context["approved_prescriptions"] = Prescription.objects.filter(approval__user=request.user,
                                                                        approval__status="AP")
        context["pending_prescriptions"] = Prescription.objects.filter(approval__user=request.user,
                                                                       approval__status="PE")
        context["rejected_prescriptions"] = Prescription.objects.filter(approval__user=request.user,
                                                                        approval__status="RE")
        context["available_prescriptions"] = Prescription.objects.filter(
            Q(approval__isnull=True)) | Prescription.objects.filter(~Q(approval__user=request.user))
    return render(request, context=context, template_name="index.html")


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


@login_required(login_url="login/")
def approval_create(request):
    user_id = request.POST['user']
    user = User.objects.get(pk=user_id)
    prescription_id = request.POST['prescription']
    prescription = Prescription.objects.get(pk=prescription_id)
    Approval.objects.create(user=user, prescription=prescription)
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url="login/")
def patient_approve(request, pk):
    approval = Approval.objects.get(pk=pk)
    approval.status = 'AP'
    approval.save()
    return HttpResponseRedirect(reverse('home'))