from django.shortcuts import render,redirect
from .models import ServiceQuestion,ServiceComment
from .forms import QuestionCreateForm, ServiceCommentCreateForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from card.models import Card, CompareCard, Benefit
from django.http import JsonResponse
import json
# Create your views here.

def index(request):
    # ======== nav바에 카드비교 카테고리 ========= 
    if request.user.is_authenticated:
        compare_cards = CompareCard.objects.filter(user=request.user)
    else:
        compare_cards = '로그인을 해야 카드 비교 기능을 사용하실 수 있습니다'

    questions = ServiceQuestion.objects.all()
    
    if request.method == 'GET':
        text = request.GET.get('search')
        if text :
            questions = ServiceQuestion.objects.filter(title__contains=text)

    page = int(request.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(questions, '5') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    context = {
        "compare_cards": compare_cards,
        'question_list' : page_obj,
    }
    return render(request, 'servicecenter/index.html', context)

@login_required(login_url='/login/')
def create(request):
    # ======== nav바에 카드비교 카테고리 ========= 
    if request.user.is_authenticated:
        compare_cards = CompareCard.objects.filter(user=request.user)
    else:
        compare_cards = '로그인을 해야 카드 비교 기능을 사용하실 수 있습니다'

    if request.method == 'POST':
        form = QuestionCreateForm(request.POST)
        if form.is_valid():
            serv_form = form.save(commit=False)
            serv_form.user = request.user
            serv_form.save()
            return redirect('service:index')
    else:
        form = QuestionCreateForm()
    context = {
        "compare_cards": compare_cards,
        'form' : form,
    }
    return render(request, 'servicecenter/create.html',context)

def detail(request,pk):
    # ======== nav바에 카드비교 카테고리 ========= 
    if request.user.is_authenticated:
        compare_cards = CompareCard.objects.filter(user=request.user)
    else:
        compare_cards = '로그인을 해야 카드 비교 기능을 사용하실 수 있습니다'
    
    question = ServiceQuestion.objects.get(pk=pk)
    comment = ServiceComment.objects.filter(quest_id = pk).order_by("-created_at")
    
    comment_form = ServiceCommentCreateForm()

    context = {
        "compare_cards" : compare_cards,
        'question' : question,
        'comment_form' : comment_form,
        'comments':comment,
    }
    return render(request, 'servicecenter/detail.html', context)
from django.contrib import messages
def comment(request, pk):
    service = ServiceQuestion.objects.get(id = pk)
    user = request.user.pk

    if request.method == 'POST':
        if request.user.is_staff == True:

            comment_form = ServiceCommentCreateForm(request.POST)
            if comment_form.is_valid():
                form = comment_form.save(commit=False)
                form.quest_id = pk
                form.user = request.user
                form.save()
        else:
            messages.warning(request,'not staff')
    comments = ServiceComment.objects.filter(quest_id = service.id).order_by("-created_at")
    comment_data = []

    for comment in comments:
        create = comment.created_at
        create = create.strftime("%Y-%m-%d %H:%M")

        comment_data.append({
            "commentId": comment.id,
            "user_id" : comment.user.id,
            "content": comment.content,
            "created_at": create,
            "commentUser": comment.user.username,
            "commentUserImg" : comment.user.profile.url,
        })

    data = {
        "commentData": comment_data,
        "user" : user,
        "serviceId": service.id,
    }

    return JsonResponse(data)


def comment_delete(request, service_pk, comment_pk):
    service = ServiceQuestion.objects.get(id = service_pk)
    comment = ServiceComment.objects.get(id = comment_pk)
    user = request.user.pk

    if request.user == comment.user:
        comment.delete()

    comments = ServiceComment.objects.filter(quest_id = service.id).order_by("-created_at")
    comment_data = []

    for comment in comments:
        create = comment.created_at
        create = create.strftime("%Y-%m-%d %H:%M")

        comment_data.append({
            "commentId": comment.id,
            "user_id" : comment.user.id,
            "content": comment.content,
            "created_at": create,
            "commentUser": comment.user.username,
            "commentUserImg" : comment.user.profile.url,
        })

    data = {
        "commentData": comment_data,
        "user" : user,
        "serviceId": service.id,
    }

    return JsonResponse(data)

def comment_update(request, service_pk, comment_pk):
    service = ServiceQuestion.objects.get(id = service_pk)
    comment = ServiceComment.objects.get(id = comment_pk)
    user = request.user.pk

    jsonObject = json.loads(request.body)

    if request.user == comment.user:

        if request.method == "POST":
            comment.content = jsonObject.get("content")
            comment.save()


    comments = ServiceComment.objects.filter(quest_id = service.id).order_by("-created_at")
    comment_data = []

    for comment in comments:
        create = comment.created_at
        create = create.strftime("%Y-%m-%d %H:%M")

        comment_data.append({
            "commentId": comment.id,
            "user_id" : comment.user.id,
            "content": comment.content,
            "created_at": create,
            "commentUser": comment.user.username,
            "commentUserImg" : comment.user.profile.url,
        })

    data = {
        "commentData": comment_data,
        "user" : user,
        "serviceId": service.id,
    }

    return JsonResponse(data)