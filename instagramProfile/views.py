from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from instagramProfile.logic import InstagramScraperLogic
from instagramProfile.custom_exceptions import BadRequest, UserNotAuthorize, DataBaseException

class InstagramScraperViewSet(viewsets.ModelViewSet):
    
    @api_view(['POST'])
    def add_user_profile(request):

        try:
            user_login = request.data.get('user_login')
            password_login = request.data.get('password_login')
            user_names = request.data.get('user_names')
            result = InstagramScraperLogic.add_user_profile(user_login, password_login, user_names)

            return Response(status=status.HTTP_200_OK, data=result)
            
        except BadRequest as error:
            return Response(status=status.HTTP_401_UNAUTHORIZED , data=str(error))
        except DataBaseException as error:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR , data=str(error))
        except Exception as error:
            return Response(status=status.HTTP_400_BAD_REQUEST , data=str(error))