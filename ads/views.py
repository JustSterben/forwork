from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Ad, ExchangeProposal
from .forms import AdForm, ExchangeProposalForm


# Список всех объявлений
def ad_list(request):
    ads = Ad.objects.all().order_by('-created_at')

    query = request.GET.get('q')
    category = request.GET.get('category')
    condition = request.GET.get('condition')

    if query:
        ads = ads.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if category:
        ads = ads.filter(category__icontains=category)
    if condition:
        ads = ads.filter(condition=condition)

    # Пагинация — 5 объявлений на страницу
    paginator = Paginator(ads, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ads/ad_list.html', {
        'ads': page_obj,  # теперь ads — это не QuerySet, а Page
        'page_obj': page_obj
    })

# Просмотр одного объявления
def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'ads/ad_detail.html', {'ad': ad})

# Создание объявления
@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = AdForm()
    return render(request, 'ads/ad_form.html', {'form': form})

# Редактирование объявления
@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if ad.user != request.user:
        return HttpResponseForbidden("Вы не автор этого объявления.")

    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = AdForm(instance=ad)

    return render(request, 'ads/ad_form.html', {'form': form})

# Удаление объявления
@login_required
def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if ad.user != request.user:
        return HttpResponseForbidden("Вы не автор этого объявления.")

    if request.method == 'POST':
        ad.delete()
        return redirect('ad_list')

    return render(request, 'ads/ad_confirm_delete.html', {'ad': ad})

@login_required
def create_exchange_proposal(request, ad_id):
    ad_receiver = get_object_or_404(Ad, id=ad_id)

    if ad_receiver.user == request.user:
        return HttpResponseForbidden("Нельзя предложить обмен на своё же объявление.")

    if request.method == 'POST':
        form = ExchangeProposalForm(request.POST, user=request.user)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.ad_receiver = ad_receiver
            proposal.status = 'pending'
            proposal.save()
            return redirect('ad_detail', ad_id=ad_receiver.id)
    else:
        form = ExchangeProposalForm(user=request.user)

    return render(request, 'ads/exchange_form.html', {
        'form': form,
        'ad_receiver': ad_receiver
    })

@login_required
def exchange_proposals(request):
    proposals_sent = ExchangeProposal.objects.filter(ad_sender__user=request.user)
    proposals_received = ExchangeProposal.objects.filter(ad_receiver__user=request.user)

    return render(request, 'ads/exchange_list.html', {
        'proposals_sent': proposals_sent,
        'proposals_received': proposals_received,
    })

@login_required
def update_proposal_status(request, proposal_id):
    proposal = get_object_or_404(ExchangeProposal, id=proposal_id)

    if proposal.ad_receiver.user != request.user:
        return HttpResponseForbidden("Вы не получатель этого предложения.")

    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['accepted', 'rejected']:
            proposal.status = status
            proposal.save()
    return redirect('exchange_proposals')