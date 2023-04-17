# duration-da zamanin formatini deyismek ucun
# template-in icinde yazilan melumatlar uzerinde isleyen funksiyalar filtr funksiyalardir
# custom filters yaziriq (proqramcinin ozunun yazdiqi) 
from django import template 

register = template.Library()

@register.filter  # dekoration yazmaqda meqsed bunu sən artıq funksiya kimi istifadə edəbilərsən
def duration(d):
    seconds=int(d.total_seconds())
    hours=seconds//3600   # 3600 saniye
    minutes=(seconds%3600)//60
    sec=(seconds%3600)%60
    result=''
    if hours:
        result+=str(hours) + ' saat' 
    if minutes:
        result+=str(minutes) + ' dəqiqə'
    if sec:
        result+=str(sec) + ' saniyə'
    return result


        
    
    
    