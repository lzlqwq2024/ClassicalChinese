from django import template
from django.utils.html import conditional_escape
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from riddle.models import Article

register = template.Library()

def replace_string(beforestring, stringlist, afterstring):
    dnum = stringlist.index(beforestring)
    stringlist.remove(beforestring)
    stringlist.insert(dnum, afterstring)

@register.filter(needs_autoescape=True, name='strong')
@stringfilter
def strong(value, autoescape=False):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    textlist = list(value)
    result = '<strong>%s</strong>%s'%(value[:textlist.index('：')], value[textlist.index('：'):textlist.index('；')+1])

    while True:
        try:
            replace_string('：', textlist, '_')
            semecolon = textlist.index('；')
            colon = textlist.index('：')
            replace_string('；', textlist, '_')
            semecolon_after = textlist.index('；')
            tstring = '<strong>%s</strong>%s'%(value[semecolon+1:colon], value[colon:semecolon_after+1])
            result = result + tstring
        except:
            return mark_safe(result)

@register.filter(name='turnnumber')
def turnnumber(value):
    return "A%s"%(str(int(value)+100))

@register.filter(name='fulldevide')
def fulldevide(value, dividenum):
    if int(value) >= dividenum:
        return int(value) // int(dividenum)
    else:
        return 1

@register.filter(name='remainder')
def remainder(value, remaindernum):
    return int(value) % int(remaindernum)

@register.filter(name='addstr')
def addstr(value, data):
    return str(value)+str(data)

@register.filter(needs_autoescape=True, name='insert')
@stringfilter
def insert(data, value, autoescape=True):
    datalist = data.split("^")
    
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    insert_template = "<input type='text' class='kind%s-input'>" %(datalist[-1])
    datalist.pop(-1)

    while "_" in datalist:
        dnum = datalist.index("_")
        datalist.pop(dnum)
        datalist.insert(dnum, '')
    
    valuelist = list(value)
    resultlist = list(value)
    insertlist = []
    result = ''

    for x in range(valuelist.count("）")):
        insert_position = valuelist.index("）")
        insertlist.append(insert_position)
        valuelist.pop(insert_position)
        valuelist.insert(insert_position, "_")

    for time in range(len(insertlist)):
        resultlist.insert(insertlist[time]+time, insert_template)

    for resultstr in resultlist:
        result = result+resultstr
    return mark_safe(result)

@register.filter(needs_autoescape=True, name='judgestr')
def judgestr(value, cutnum, autoescape=False):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    if value == 'error':
        return ''
    if cutnum:
        try:
            value = value[int(cutnum)-1]
        except:
            return ''
    else:
        value = value[0]

    result_str = ''
    for value_str in value:
        if value_str == '0':
            result_str = result_str+"<font style='color: crimson; display:inline; padding-left: 10px; font-size: 25px;'><b>×</b></font>"
        else:
            result_str = result_str+"<font style='color: darkcyan; display:inline; padding-left: 10px; font-size: 25px;'><b>√</b></font>"
    return mark_safe(result_str)
        
@register.filter(name="search_seen")
def search_seen(value, uid):
    if value:
        seen_uid_list = value.split(" ")
        if str(uid) in seen_uid_list:
            return True
        else:
            return False
    return False
        
        
        
    
    
    






















    
