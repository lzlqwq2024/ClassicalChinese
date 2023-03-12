from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
from django.core.paginator import Paginator
from .models import Article, Comment
from login.models import User
from django.utils.html import conditional_escape
import os

# Create your views here.

def ArticleFilter(keyword, intext, atype, user):
    if not(intext):
        if keyword:
            if keyword.isnumeric():
                if int(keyword) > 100:
                    try:
                        if (not(atype) or atype == "1"):
                            all_article = Article.objects.filter(number__contains=int(keyword)-100)
                        elif atype == "2":
                            all_article = Article.objects.filter(number__contains=int(keyword)-100)
                            selected_article = []
                            for selectedArticle in all_article:
                                if selectedArticle.seen_user:
                                    user_id_list = selectedArticle.seen_user.split(" ")
                                    if user_id_list:
                                        if str(user.id) in user_id_list:
                                            selected_article.append(selectedArticle)
                            all_article = selected_article
                        else:
                            all_article = Article.objects.filter(number__contains=int(keyword)-100) 
                            selected_article = []
                            for selectedArticle in all_article:
                                try:
                                    user_id_list = selectedArticle.seen_user.split(" ")
                                    if not(str(user.id) in user_id_list):
                                        selected_article.append(selectedArticle)
                                except:
                                    selected_article.append(selectedArticle)
                            all_article = selected_article
                    except:
                        all_article = []
                else:
                    try:
                        if (not(atype) or atype == "1"):
                            all_article = Article.objects.filter(number__contains=int(keyword))
                        elif atype == "2":
                            all_article = Article.objects.filter(number__contains=int(keyword))
                            selected_article = []
                            for selectedArticle in all_article:
                                if selectedArticle.seen_user:
                                    user_id_list = selectedArticle.seen_user.split(" ")
                                    if user_id_list:
                                        if str(user.id) in user_id_list:
                                            selected_article.append(selectedArticle)
                            all_article = selected_article
                        else:
                            all_article = Article.objects.filter(number__contains=int(keyword))
                            selected_article = []
                            for selectedArticle in all_article:
                                try:
                                    user_id_list = selectedArticle.seen_user.split(" ")
                                    if not(str(user.id) in user_id_list):
                                        selected_article.append(selectedArticle)
                                except:
                                    selected_article.append(selectedArticle)
                            all_article = selected_article                            
                    except:
                        all_article = []
            elif (keyword[0] == "A" or keyword[0] == "a"):
                try:
                    if (not(atype) or atype == "1"):
                        all_article = Article.objects.filter(number__contains=int(keyword[1:])-100)
                    elif atype == "2":
                        all_article = Article.objects.filter(number__contains=int(keyword[1:])-100)
                        selected_article = []
                        for selectedArticle in all_article:
                            if selectedArticle.seen_user:
                                user_id_list = selectedArticle.seen_user.split(" ")
                                if user_id_list:
                                    if str(user.id) in user_id_list:
                                        selected_article.append(selectedArticle)
                        all_article = selected_article
                    else:
                        all_article = Article.objects.filter(number__contains=int(keyword[1:])-100)
                        selected_article = []
                        for selectedArticle in all_article:
                            try:
                                user_id_list = selectedArticle.seen_user.split(" ")
                                if not(str(user.id) in user_id_list):
                                    selected_article.append(selectedArticle)
                            except:
                                selected_article.append(selectedArticle)
                        all_article = selected_article   
                except:
                    all_article = []
            else:
                try:
                    if (not(atype) or atype == "1"):
                        all_article = Article.objects.filter(name__contains=keyword)
                        if not(len(all_article)):
                            for p in range(len(keyword)):
                                partkey = keyword[p]
                                all_article = Article.objects.filter(name__contains=partkey)
                                if len(all_article):
                                    break
                    elif atype == "2":
                        all_article = Article.objects.filter(name__contains=keyword)
                        selected_article = []
                        for selectedArticle in all_article:
                            if selectedArticle.seen_user:
                                user_id_list = selectedArticle.seen_user.split(" ")
                                if user_id_list:
                                    if str(user.id) in user_id_list:
                                        selected_article.append(selectedArticle)
                        all_article = selected_article
                        if not(len(all_article)):
                            for p in range(len(keyword)):
                                partkey = keyword[p]
                                all_article = Article.objects.filter(name__contains=partkey)
                                selected_article = []
                                for selectedArticle in all_article:
                                    if selectedArticle.seen_user:
                                        user_id_list = selectedArticle.seen_user.split(" ")
                                        if user_id_list:
                                            if str(user.id) in user_id_list:
                                                selected_article.append(selectedArticle)
                                all_article = selected_article
                                if len(all_article):
                                    break
                    else:
                        all_article = Article.objects.filter(name__contains=keyword)
                        selected_article = []
                        for selectedArticle in all_article:
                            try:
                                user_id_list = selectedArticle.seen_user.split(" ")
                                if not(str(user.id) in user_id_list):
                                    selected_article.append(selectedArticle)
                            except:
                                selected_article.append(selectedArticle)
                        all_article = selected_article 
                        if not(len(all_article)):
                            for p in range(len(keyword)):
                                partkey = keyword[p]
                                all_article = Article.objects.filter(name__contains=partkey)
                                selected_article = []
                                for selectedArticle in all_article:
                                    try:
                                        user_id_list = selectedArticle.seen_user.split(" ")
                                        if not(str(user.id) in user_id_list):
                                            selected_article.append(selectedArticle)
                                    except:
                                        selected_article.append(selectedArticle)
                                all_article = selected_article 
                                if len(all_article):
                                    break
                except:
                    all_article = []
        else:
            if (not(atype) or atype == "1"):
                all_article = Article.objects.all()
            elif atype == "2":
                all_article = Article.objects.all()
                selected_article = []
                for selectedArticle in all_article:
                    if selectedArticle.seen_user:
                        user_id_list = selectedArticle.seen_user.split(" ")
                        if user_id_list:
                            if str(user.id) in user_id_list:
                                selected_article.append(selectedArticle)
                all_article = selected_article
            else:
                all_article = Article.objects.all()
                selected_article = []
                for selectedArticle in all_article:
                    try:
                        user_id_list = selectedArticle.seen_user.split(" ")
                        if not(str(user.id) in user_id_list):
                            selected_article.append(selectedArticle)
                    except:
                        selected_article.append(selectedArticle)
                all_article = selected_article 
    else:
        if keyword.isnumeric():
            all_article = []
        else:
            try:
                if (not(atype) or atype == "1"):
                    all_article = Article.objects.filter(text__contains=keyword)
                    if not(len(all_article)):
                        for p in range(len(str(keyword))):
                            partkey = str(keyword)[:p]
                            all_article = Article.objects.filter(text__contains=partkey)
                            if len(all_article):
                                break
                elif atype == "2":
                    all_article = Article.objects.filter(text__contains=keyword)
                    selected_article = []
                    for selectedArticle in all_article:
                        if selectedArticle.seen_user:
                            user_id_list = selectedArticle.seen_user.split(" ")
                            if user_id_list:
                                if str(user.id) in user_id_list:
                                    selected_article.append(selectedArticle)
                    all_article = selected_article
                    if not(len(all_article)):
                        for p in range(len(str(keyword))):
                            partkey = str(keyword)[:p]
                            all_article = Article.objects.filter(text__contains=partkey)
                            selected_article = []
                            for selectedArticle in all_article:
                                if selectedArticle.seen_user:
                                    user_id_list = selectedArticle.seen_user.split(" ")
                                    if user_id_list:
                                        if str(user.id) in user_id_list:
                                            selected_article.append(selectedArticle)
                            all_article = selected_article
                            if len(all_article):
                                break
                else:
                    all_article = Article.objects.filter(text__contains=keyword)
                    selected_article = []
                    for selectedArticle in all_article:
                        try:
                            user_id_list = selectedArticle.seen_user.split(" ")
                            if not(str(user.id) in user_id_list):
                                selected_article.append(selectedArticle)
                        except:
                            selected_article.append(selectedArticle)
                    all_article = selected_article 
                    if not(len(all_article)):
                        for p in range(len(str(keyword))):
                            partkey = str(keyword)[:p]
                            all_article = Article.objects.filter(text__contains=partkey)
                            selected_article = []
                            for selectedArticle in all_article:
                                try:
                                    user_id_list = selectedArticle.seen_user.split(" ")
                                    if not(str(user.id) in user_id_list):
                                        selected_article.append(selectedArticle)
                                except:
                                    selected_article.append(selectedArticle)
                            all_article = selected_article 
                            if len(all_article):
                                break
            except:
                all_article = []
    return all_article

def article_index(request, pagenum):
    article_keyword = conditional_escape(request.GET.get('keywords', ''))
    article_intext = conditional_escape(request.GET.get('text', ''))
    article_type = conditional_escape(request.GET.get('type', ''))
    login = conditional_escape(request.session.get('is_login', ''))
    
    if login:
        try:
            name = conditional_escape(request.session.get('user_name'))
            user = User.objects.get(name=name)
        except:
            name = None
            user = None
    else:
        name = None
        user = None

    all_article = ArticleFilter(article_keyword, article_intext, article_type, user)
    paginator = Paginator(all_article, 10)
    
    page = paginator.get_page(pagenum)
    if len(page):
        first_article = page[0]
        article_list = page[1:]
    else:
        first_article = None
        article_list = None
    page_sum = paginator.num_pages
    if page_sum <= 7:
        pagelist = [i for i in range(1,page_sum+1)]
    elif pagenum in [i for i in range(1,5)]:
        pagelist = [i for i in range(1,8)]
    elif pagenum in [i for i in range(page_sum-3,page_sum+1)]:
        pagelist = [i for i in range(page_sum-6,page_sum+1)]
    else:
        pagelist = [i for i in range(pagenum-3, pagenum+4)]
    context = {'all_article':page, 'article_list': article_list, 'pagelist': pagelist, 'first_article': first_article, 'page_num': pagenum, 'page_sum': page_sum, 'keyword': article_keyword, 'intext': article_intext, 'type': article_type, 'login':login, 'username':name, 'user':user}
    return render(request, 'riddle/article_index.html', context)

def tologin(request):
    response = redirect('/login/login/')
    response.set_cookie(key="redirect_href", value="/Chinese/article/1/")
    return response

def get_root_comments(comments):
    roots = []
    for comment in comments:
        if not comment.parent_comment:
            roots.append(comment)
    return roots

def search_comments(root, result=[]):
    result.append(root)
    if root.child_comment:
        child_list = root.child_comment.split(" ")
        child_list = [Comment.objects.get(id=i) for i in child_list]
        for child in child_list:
            search_comments(child, result)
    return result

def get_comments(comments):
    roots = get_root_comments(comments)
    comment_list = []
    for root in roots:
        comment_list = comment_list + search_comments(root, [])
    return comment_list

def get_child_comments(comments):
    for comment in comments:
        comment.child_comment = ""
        comment.save()
    for comment in comments:
        if comment.parent_comment:
            parent = comment.parent_comment
            if parent.child_comment:
                parent.child_comment = parent.child_comment + " " + str(comment.id)
                parent.save()
            else:
                parent.child_comment = str(comment.id)
                parent.save()

def show_article(request, snum):
    try:
        num = int(str(snum)[1:])-100
    except:
        return HttpResponseNotFound()
    
    try:
        user = User.objects.get(name=request.session.get("user_name", ""))
    except:
        user = None

    article = get_object_or_404(Article, number=num)
    if user:
        if article.seen_user:
            if str(user.id) in article.seen_user.split(" "):
                pass
            else:
                article.seen_user = article.seen_user + " " + str(user.id)
        else:
            article.seen_user = str(user.id)
        article.save()
    else:
        article.save()

    if user:
        if user.not_read_comment_articleid:
            not_read_comment_articleid_list = user.not_read_comment_articleid.split(" ")
            if str(article.id) in not_read_comment_articleid_list:
                not_read_comment_articleid_list.remove(str(article.id))
                not_read_comment_articleid_str = ""
                for i in not_read_comment_articleid_list:
                    if not_read_comment_articleid_list.index(i) == 0:
                        not_read_comment_articleid_str = i
                    else:
                        not_read_comment_articleid_str = not_read_comment_articleid_str + " " + i
                user.not_read_comment_articleid = not_read_comment_articleid_str
                user.save()

    message = ""
    if request.method == "POST":
        addcomment = request.POST.get("addcomment", "")
        try:
            user = User.objects.get(name=conditional_escape(request.session.get("user_name", "")))
            if user.no_comment:
                message = "您已经被禁言，无法创建评论！"
            elif addcomment:
                Comment.objects.create(user=user, article=article, text=addcomment)
            else:
                message = "评论内容不能为空！"
        except:
            message = "未知错误！无法创建评论！"

    comments = Comment.objects.filter(article=article)
    get_child_comments(comments)
    comments = Comment.objects.filter(article=article)
    comment_list = get_comments(comments)
        
    context = {'article': article, 'last_number': Article.objects.last().number, 'comment_list':comment_list, 'comment_sum': len(comment_list), 'message':message, 'is_login':request.session.get('is_login','')}
    return render(request, 'riddle/show_article.html', context)

def comment_reply(request, snum, cid):
    try:
        num = int(str(snum)[1:])-100
    except:
        return HttpResponseNotFound()

    if not conditional_escape(request.session.get('is_login', None)):
        return redirect('/Chinese/article/%s/' %(snum))
    
    article = get_object_or_404(Article, number=num)
    comment = get_object_or_404(Comment, id=cid)

    message = ""
    if request.method == "POST":
        replycomment = request.POST.get("replycomment", "")
        try:
            user = User.objects.get(name=conditional_escape(request.session.get("user_name", "")))
            if user.no_comment:
                message = "您已经被禁言，无法创建评论！"
            if replycomment:
                Comment.objects.create(user=user, article=article, text=replycomment, parent_comment=comment)
                parent_user = comment.user
                comment_article_id = str(comment.article.id)
                if parent_user.not_read_comment_articleid:
                    if not(comment_article_id in parent_user.not_read_comment_articleid.split(" ")):
                        parent_user.not_read_comment_articleid = parent_user.not_read_comment_articleid + " " + comment_article_id
                        parent_user.save()
                else:
                    parent_user.not_read_comment_articleid = comment_article_id
                    parent_user.save()

                return redirect('/Chinese/article/%s/' %(snum))
            else:
                message = "评论内容不能为空！"
        except:
            message = "请先登录后再创建评论！"

    context = {'article': article, 'comment': comment, 'message':message}
    return render(request, 'riddle/reply_comment.html', context)

def article_reset_allstate(request, pagenum):
    if request.method == 'POST':
        article_keyword = conditional_escape(request.GET.get('keywords', ''))
        article_intext = conditional_escape(request.GET.get('text', ''))
        article_type = conditional_escape(request.GET.get('type', ''))
        try:
            user = User.objects.get(name=conditional_escape(request.session.get("user_name","")))
        except:
            user = None
        article_list = ArticleFilter(article_keyword, article_intext, article_type, user)
        if user:
            for article in article_list:
                if article.seen_user:
                    seen_user_list = article.seen_user.split(" ")
                    if str(user.id) in seen_user_list:
                        seen_user_list.remove(str(user.id))
                        seen_user_strflist = ""
                        for seen_user_id in seen_user_list:
                            if seen_user_strflist:
                                seen_user_strflist = seen_user_id
                            else:
                                seen_user_strflist = seen_user_strflist + " " + seen_user_id
                        article.seen_user = seen_user_strflist
                        article.save()
    if article_keyword:
        if article_intext:
            return redirect('/Chinese/article/%s/?keywords=%s&text=1'%(str(pagenum), article_keyword))
        else:
            return redirect('/Chinese/article/%s/?keywords=%s'%(str(pagenum), article_keyword))
    else:
        return redirect('/Chinese/article/%s/'%(str(pagenum)))

def article_reset_pagestate(request, pagenum):
    if request.method == 'POST':
        article_keyword = conditional_escape(request.GET.get('keywords', ''))
        article_intext = conditional_escape(request.GET.get('text', ''))
        article_type = conditional_escape(request.GET.get('type', ''))
        try:
            user = User.objects.get(name=conditional_escape(request.session.get("user_name","")))
        except:
            user = None
        article_list = ArticleFilter(article_keyword, article_intext, article_type, user)
        paginator = Paginator(article_list, 10)
        page = paginator.get_page(int(pagenum))
        if user:
            for article in page:
                if article.seen_user:
                    seen_user_list = article.seen_user.split(" ")
                    if str(user.id) in seen_user_list:
                        seen_user_list.remove(str(user.id))
                        seen_user_strflist = ""
                        for seen_user_id in seen_user_list:
                            if seen_user_strflist:
                                seen_user_strflist = seen_user_id
                            else:
                                seen_user_strflist = seen_user_strflist + " " + seen_user_id
                        article.seen_user = seen_user_strflist
                        article.save()
    if article_keyword:
        if article_intext:
            return redirect('/Chinese/article/%s/?keywords=%s&text=1'%(str(pagenum), article_keyword))
        else:
            return redirect('/Chinese/article/%s/?keywords=%s'%(str(pagenum), article_keyword))
    else:
        return redirect('/Chinese/article/%s/'%(str(pagenum)))

def turn_answer(answer,riddle):
    answerlist = answer.split("^")
    riddlelist = []

    while ("_" in answerlist):
        replace_position = answerlist.index("_")
        answerlist.pop(replace_position)
        answerlist.insert(replace_position, '')

    for single_riddle in riddle:
        riddle_answer = single_riddle.keyword
        if ("；" in riddle_answer):
            riddle_answer_list = riddle_answer.split("；")
        else:
            riddle_answer_list = [riddle_answer]
        for riddle_keywords in riddle_answer_list:
            if ("，" in riddle_keywords):
                riddle_keywords_list = riddle_keywords.split("，")
            else:
                riddle_keywords_list = [riddle_keywords]
            for riddle_smallkeywords in riddle_keywords_list:
                if (" " in riddle_smallkeywords):
                    inum = riddle_keywords_list.index(riddle_smallkeywords)
                    riddle_smallkeywords_list = riddle_smallkeywords.split(" ")
                    riddle_keywords_list.pop(inum)
                    riddle_keywords_list.insert(inum, riddle_smallkeywords_list)
                else:
                    inum = riddle_keywords_list.index(riddle_smallkeywords)
                    riddle_keywords_list.pop(inum)
                    riddle_keywords_list.insert(inum, [riddle_smallkeywords])
            inum = riddle_answer_list.index(riddle_keywords)
            riddle_answer_list.pop(inum)
            riddle_answer_list.insert(inum, riddle_keywords_list)
        riddlelist.append(riddle_answer_list)

    return (answerlist, riddlelist)

def PopStr(replace_str,dnum,insertkey="_"):
    replace_str_list = list(replace_str)
    replace_str_list.pop(dnum)
    replace_str_list.insert(dnum,insertkey) 
    show_str = ""
    for x in replace_str_list:
        show_str = show_str + x
    return show_str   

def contact(keyword, answer):
    keywordlist = list(str(keyword))
    positions = []
    flags = []
    for small_keyword in keywordlist:
        if (small_keyword in answer):
            dnum = answer.index(small_keyword)
            positions.append(dnum)
            answer = PopStr(answer,dnum)
        else:
            return False
    if len(positions) == 1:
        return True
    for dnum in range(1,len(positions)):
        if positions[len(positions)-dnum] < positions[len(positions)-dnum-1]:
            return False
    return True

def judge_answer(answer_list, keywords_list):
    single_keywords = []
    flags = []
    result_flag = ''
    for k1 in keywords_list:
        for k2 in k1:
            single_keywords.append(k2)
    if len(answer_list) != len(single_keywords):
        return "error"

    for dnum in range(len(answer_list)):
        answer = answer_list[dnum]
        keywords = single_keywords[dnum]
        small_flag = 0
        big_flag = []
        for small_keywords_list in keywords:
            for small_keywords in small_keywords_list:
                if contact(small_keywords, answer):
                    small_flag = 1
            big_flag.append(small_flag)
            small_flag = 0
        if (0 in big_flag):
            final_flag = 0
        else:
            final_flag = 1
        flags.append(final_flag)

    for rflag in flags:
        result_flag = result_flag+str(rflag)

    return result_flag

def cut_answer_flag(flag, riddle):
    riddle_sum_list = []
    result_flag_list = []
    dnum = 0
    for single_riddle in riddle:
        riddle_sum_list.append(single_riddle.riddlesum)
    if (flag == "error" or sum(riddle_sum_list) != len(flag)):
        return "error"

    for riddle_sum in riddle_sum_list:
        if riddle_sum_list.index(riddle_sum) == 0:
            cut_flag = flag[:riddle_sum]
            result_flag_list.append(cut_flag)
            dnum = riddle_sum
            rdnum = riddle_sum_list.index(riddle_sum)
            riddle_sum_list.pop(rdnum)
            riddle_sum_list.insert(rdnum, '_')
        elif riddle_sum_list.index(riddle_sum) == len(riddle_sum_list)-1:
            cut_flag = flag[dnum:]
            result_flag_list.append(cut_flag)
            dnum = dnum+riddle_sum
            rdnum = riddle_sum_list.index(riddle_sum)
            riddle_sum_list.pop(rdnum)
            riddle_sum_list.insert(rdnum, '_')
        else:
            cut_flag = flag[dnum:dnum+riddle_sum]
            result_flag_list.append(cut_flag)
            dnum = dnum+riddle_sum
            rdnum = riddle_sum_list.index(riddle_sum)
            riddle_sum_list.pop(rdnum)
            riddle_sum_list.insert(rdnum, '_')

    return result_flag_list

def show_article_riddle(request, snum):
    num = int(str(snum)[1:])-100
    article = get_object_or_404(Article, number=num)
    all_related_riddle = article.riddle_set
    kind1_riddle = all_related_riddle.filter(kind=1)
    kind2_riddle = all_related_riddle.filter(kind=2)
    kind3_riddle = all_related_riddle.filter(kind=3)
    kind4_riddle = all_related_riddle.filter(kind=4)

    all_riddle1_list = [i.riddlesum for i in kind1_riddle]
    all_riddle1_sum = sum(all_riddle1_list)
    null_answer1 = ""
    for num in range(all_riddle1_sum):
        if num != all_riddle1_sum-1:
            null_answer1 = null_answer1+"_^"
        else:
            null_answer1 = null_answer1+"_"

    if kind1_riddle:
        get_answer1 = conditional_escape(request.POST.get('answer1', ''))

        if get_answer1 == '':
            get_answer1 = null_answer1
            flag1 = []
        else:
            turn_answer_result = turn_answer(get_answer1, kind1_riddle)
            answer1 = turn_answer_result[0]
            keywords1 = turn_answer_result[1]
            result_flag1 = judge_answer(answer1, keywords1)
            flag1 = cut_answer_flag(result_flag1, kind1_riddle)
    else:
        get_answer1 = null_answer1
        flag1 = []

    all_riddle2_sum = len(kind2_riddle)
    null_answer2 = ""
    for num in range(all_riddle2_sum):
        if num != all_riddle2_sum-1:
            null_answer2 = null_answer2+"_^"
        else:
            null_answer2 = null_answer2+"_"

    if kind2_riddle:
        get_answer2 = conditional_escape(request.POST.get("answer2",''))
        if not(get_answer2):
            get_answer2 = null_answer2            
    else:
        get_answer2 = null_answer2


    all_riddle3_list = [i.riddlesum for i in kind3_riddle]
    all_riddle3_sum = sum(all_riddle3_list)
    null_answer3 = ""
    for num in range(all_riddle3_sum):
        if num != all_riddle3_sum-1:
            null_answer3 = null_answer3+"_^"
        else:
            null_answer3 = null_answer3+"_"

    if kind3_riddle:
        get_answer3 = conditional_escape(request.POST.get('answer3', ''))

        if get_answer3 == '':
            get_answer3 = null_answer3
            flag3 = []
        else:
            turn_answer_result = turn_answer(get_answer3, kind3_riddle)
            answer3 = turn_answer_result[0]
            keywords3 = turn_answer_result[1]
            result_flag3 = judge_answer(answer3, keywords3)
            flag3 = cut_answer_flag(result_flag3, kind3_riddle)
    else:
        get_answer3 = null_answer3
        flag3 = []


    all_riddle4_sum = len(kind4_riddle)
    null_answer4 = ""
    for num in range(all_riddle4_sum):
        if num != all_riddle4_sum-1:
            null_answer4 = null_answer4+"_^"
        else:
            null_answer4 = null_answer4+"_"

    if kind4_riddle:
        get_answer4 = conditional_escape(request.POST.get("answer4",''))
        if not(get_answer4):
            get_answer4 = null_answer4            
    else:
        get_answer4 = null_answer4

    context = {'article': article, 'riddle1': kind1_riddle, 'riddle2': kind2_riddle, 'riddle3': kind3_riddle, 'riddle4': kind4_riddle, 'flag1': flag1, 'answer1': get_answer1, 'answer2': get_answer2, 'flag3': flag3, 'answer3': get_answer3, 'answer4': get_answer4, 'last_number': Article.objects.last().number}
    return render(request, 'riddle/show_article_riddle.html', context)

def download_article(request, snum):
    num = int(str(snum)[1:])-100
    article = get_object_or_404(Article, number=num)
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    try:
        return FileResponse(open(path+'//static//riddle//docx//'+str(article.number)+article.name+".docx", "rb"), as_attachment=True)
    except:
        return HttpResponse('<h1 style="margin-left: 30px;margin-top: 30px;">抱歉，没有找到该文章相关 word 文档资源</h1>')
    

