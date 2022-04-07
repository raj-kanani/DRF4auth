from django_filters.rest_framework import DjangoFilterBackend
from .customthrottle import SetThrottle
from rest_framework import viewsets, filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from .custompermission import MyPermission
from .models import Student, Student1
from .serializers import StudentSerializer, Student1Serializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, \
    IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, \
    DjangoModelPermissions, DjangoObjectPermissions
from .custompermission import MyPermission
from .customauth import CustomAuth
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


# used default permission and authentication classes

class StudentModel(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # by default allow any user permission
    permission_classes = [IsAuthenticated]


class StudentModel1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # any user access data
    permission_classes = [AllowAny]


class StudentModel2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Enter  username & pwd check permission
    authentication_classes = [BasicAuthentication]
    # only superuser access the data
    permission_classes = [IsAdminUser]


# Session with authentication

class StudentSession(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # only superuser access the data
    # permission_classes = [IsAdminUser]

    # permission_classes = [IsAuthenticatedOrReadOnly]

    # perform to set update,delete,add permission in admin panel
    # permission_classes = [DjangoModelPermissions]  # only read permission

    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # not login user read permission

    permission_classes = [DjangoObjectPermissions]  # per object set permission


# set custom permission
class StudentCustom(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]


# generate token authentication
class StudentToken(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]


# httpie using auto generate token
'''
    terminal in  http http://127.0.0.1:8000/mytoken1/ 
    'Authorization:Token (user token enter)' 
     then  user access api data
'''

# post method :
''' 
    http -f POST http://127.0.0.1:8000/mytoken1/ 
    name=jay roll=105 city=mumbai 
    'Authorization:Token (user token enter)'
'''


class StudentToken1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]


# custom authentication use base-authentication
# browser : http://127.0.0.1:8000/myauth/?username=admin
class StudentAuth(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [CustomAuth]

    # http http://127.0.0.1:8000/myauth/ 'Authorization:Bearer (access code enter)

    #  add data : http -f POST
    #  http://127.0.0.1:8000/myauth/ name=akash roll=105 city=ahd 'Authorization:Bearer (access code enter)
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


# using filter in users
class StudentFilter(ListAPIView):
    queryset = Student1.objects.all()
    serializer_class = Student1Serializer

    def get_queryset(self):
        user = self.request.user
        return Student1.objects.filter(passby=user)


# city & name wise filter & customize filter
# pip install django-filter
class StudentFilter1(ListAPIView):
    queryset = Student1.objects.all()
    serializer_class = Student1Serializer

    # browser in 127.0.0.1: 8000 / studentfilter1 /?city=rajkot&name=raj
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city', 'name']

    # http://127.0.0.1:8000/studentfilter1/?search=AVADH
    # filter_backends = [filters.SearchFilter]

    # http: // 127.0.0.1: 8000 / studentfilter1 /?ordering =-name
    filter_backends = [filters.OrderingFilter]
    search_fields = ['name']


# username wise filter data
class StudentFilter2(ListAPIView):
    serializer_class = Student1Serializer

    def get_queryset(self):
        queryset = Student1.objects.all()

        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(passby=username)
        return queryset


# # paginaton area


# subclass of pagenumberpagination
class Mypage(PageNumberPagination):
    page_size = 3
    # replace the page to pg
    page_query_param = 'pg'  # url in pg=last to move on last page
    # client require specific page in no. of data
    page_size_query_param = 'record'
    # user can max page size no. of usage
    max_page_size = 5


class StudentPagination(ListAPIView):
    queryset = Student1.objects.all()
    serializer_class = Student1Serializer
    pagination_class = Mypage


#  Use of LimitOffsetPagination
# http://127.0.0.1:8000/StudentPagination1/?limit=4&offset=4
# - offset=4 means data start will be next on 4 number.
class Mypage1(LimitOffsetPagination):
    pass


class StudentPagination1(ListAPIView):
    queryset = Student1.objects.all()
    serializer_class = StudentSerializer
    pagination_class = Mypage1


# use of cursor pagination
class Mypage2(CursorPagination):
    page_size = 3
    ordering = 'roll'


class StudentPagination2(ListAPIView):
    queryset = Student1.objects.all()
    serializer_class = Student1Serializer
    pagination_class = Mypage2


# versioning in rest-framework
#
# class StudentVVersioning(ListAPIView):
#     def get(self, request):
#         queryset = Student1.objects.all()
#         serializer = Student1Serializer(queryset, many=True, context={'request': request})
#         return Response({'student1': serializer.data})


#  throttle area
class StudentThrottle(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # throttle_classes = [AnonRateThrottle, SetThrottle]
    throttle_classes = [ScopedRateThrottle]  # global generate throttle

