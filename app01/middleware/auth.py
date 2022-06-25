from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class M1(MiddlewareMixin):
    '''登录拦截'''
    def process_request(self,request):
        if request.path_info in ["/login/","/image/code/","/register/"]:
            return
        else:
            admin_object=request.session.get("info")
            if admin_object:
                return
            return redirect("/login/")