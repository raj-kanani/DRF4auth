from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from .customtoken import CustomToken
# JWT authentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('StudentModel', views.StudentModel, basename='mystudent')
router.register('StudentModel1', views.StudentModel1, basename='mystudent1')
router.register('StudentModel2', views.StudentModel2, basename='mystudent2')
router.register('mysession', views.StudentSession, basename='mysession')
router.register('mycustom', views.StudentCustom, basename='mycustom')
router.register('mytoken1', views.StudentToken1, basename='mytoken1')
# authentication
router.register('myauth', views.StudentAuth, basename='myauth')


# throttle
router.register('StudentThrottle', views.StudentThrottle, basename='StudentThrottle')

urlpatterns = [

    # class based with viewset and router
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),

    # default token generate by commandline in terminal
    # path('gettoken/', obtain_auth_token),

    # custom token generate
    path('gettoken/', CustomToken.as_view()),

    # generate token with jwt
    # http POST http://127.0.0.1:8000/getjwt/ username="admin" password="admin"
    path('getjwt/', TokenObtainPairView.as_view()),

    # refresh token with jwt
    # http POST http://127.0.0.1:8000/refreshjwt/ refresh=(refresh token enter)
    path('refreshjwt/', TokenRefreshView.as_view()),
    # verify token with jwt 5 min validity

    # check / verify token with JWT
    # http POST http://127.0.0.1:8000/verifyjwt/ token=(accesss token enter)
    path('verifyjwt/', TokenVerifyView.as_view()),

    # filter with users
    path('studentfilter/', views.StudentFilter.as_view()),

    # django filter backend / custom filter with city & name
    path('studentfilter1/', views.StudentFilter1.as_view()),

    # username wise filter data
    path('studentfilter2/', views.StudentFilter2.as_view()),

    # pagination
    path('StudentPagination/', views.StudentPagination.as_view()),
    path('StudentPagination1/', views.StudentPagination1.as_view()),
    path('StudentPagination2/', views.StudentPagination2.as_view()),







]
