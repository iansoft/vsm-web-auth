# _*_ coding:utf-8 _*_
from django import shortcuts
from django.conf import settings
from django.utils import functional
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache  # noqa
from django.views.decorators.csrf import csrf_exempt  # noqa
from django.views.decorators.csrf import csrf_protect  # noqa
from django.views.decorators.debug import sensitive_post_parameters  # noqa

from openstack_auth import utils
from openstack_auth import exceptions

def login(request):
    if request.method == "POST":
        region = request.POST.get("region","")
        domain = request.POST.get("domain","")
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        print region
        print domain
        print username
        print password
        try:
            print "+++To Authenticate+++++++"
            user = authenticate(
                request=request,
                auth_url="http://139.196.208.113:5000/v3",
                user_domain_name="default",
                username="admin",
                password="123456"
            )
            print user
        except exceptions.KeystoneAuthException as exc:
            msg = "Login failed for user"
            print exc

    return shortcuts.render(request,'login/login.html')


# @sensitive_post_parameters()
# @csrf_protect
# @never_cache
# def login(request):
#     # If the user enabled websso and selects default protocol
#     # from the dropdown, We need to redirect user to the websso url
#     # 我们重POST回来的数据中查找到WEBSSO
#     if request.method == 'POST':
#         auth_type = request.POST.get('auth_type', 'credentials')
#         if utils.is_websso_enabled() and auth_type != 'credentials':
#             auth_url = request.POST.get('region')
#             url = utils.get_websso_url(request, auth_url, auth_type)
#             return shortcuts.redirect(url)
            
#     if not request.is_ajax():
#         # print "====it's not a ajax request===="
#         # If the user is already authenticated, redirect them to the
#         # dashboard straight away, unless the 'next' parameter is set as it
#         # usually indicates requesting access to a page that requires different
#         # permissions.
#         # 如果用户已经验证通过了，且没有next page的参数，那么就直接到dashboard页面
#         if (request.user.is_authenticated() and
#                 auth.REDIRECT_FIELD_NAME not in request.GET and
#                 auth.REDIRECT_FIELD_NAME not in request.POST):
#             return shortcuts.redirect(settings.LOGIN_REDIRECT_URL)
           
#         # Get our initial region for the form.
#         # 访问region，如果访问的region在region list中，且不是当前的region，那么就更新当前的region为Current Region
#         initial = {}
#         current_region = request.session.get('region_endpoint', None)
#         requested_region = request.GET.get('region', None)
#         regions = dict(getattr(settings, "AVAILABLE_REGIONS", []))
#         if requested_region in regions and requested_region != current_region:
#             initial.update({'region': requested_region})
#         # the regions
#         print current_region
#         print requested_region
#         print regions
#         print initial
        
#         curry_test(1,2,3)
#         test = functional.curry(curry_test,x=22)
            
#     return shortcuts.render(request,'login/login.html')
    
   
# def curry_test(x,y,z):
#     print x,y,z