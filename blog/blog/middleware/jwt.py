from django.http import HttpResponse, HttpResponseRedirect
from users.models import User
import datetime
import jwt

from users.forms import LoginForm

class JwtMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        token = request.COOKIES.get('access_token')
        
        
        #Login -----------------------------------------------------------
        #Chequea que el usuario y la contraseña sean correctos. Si es así, pide a User el token JWT y lo setea en la cookie access_token.
        
        if request.path == "/api/login/":
            form = LoginForm(request.POST)
            
            if form.is_valid():
                username = form.cleaned_data.get("username")
                try:
                    user = User.objects.get(username=username)
                except Exception as e:
                    print("error: ", e)
                    return HttpResponseRedirect("/login/?error=invalid_credentials")
            
                if user.check_password(form.cleaned_data['password']):
                    
                    token = user.get_jwt()
                    response.set_cookie(
                        key="access_token",
                        value=token,
                        expires=datetime.datetime.now() + datetime.timedelta(days=1),
                        secure=False, 
                        httponly=True,
                        samesite="Lax"
                    )               
                    #return HttpResponseRedirect("/")
            
                else:
                    return HttpResponseRedirect("/login/?error=invalid_credentials")
            else: 
                print("Invalid form")
                return HttpResponseRedirect("/login/?error=invalid_credentials")
        
        
        #Validación token -------------------------------------------------------
        if not token and request.path != "/login/" and request.path != "/api/login/" and request.path != "/api/signup/" and request.path != "/signup/" :
            return HttpResponseRedirect("/login/")
        
        if token:
            try:
                payload = jwt.decode(token, "secret", algorithms=["HS256"])
                
                #Chequea si el token expiró y borra la cookie
                #TODO: implementar refresh token
                if payload["jwt_exp"] < str(datetime.datetime.now()):
                    response.delete_cookie("access_token")
                    #return HttpResponseRedirect("/login/?error=token_expired")
                
            except:
                response.delete_cookie("access_token")
                return HttpResponseRedirect("/login/?error=invalid_token")
            
            

        return response