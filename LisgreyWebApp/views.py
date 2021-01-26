from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from LisgreyWebApp.forms import ReservationForm, UserRegistrationForm
from LisgreyWebApp.models import FoodItem, Allergen
from django.contrib import messages

from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework import permissions
from LisgreyWebApp.serializers import UserSerializer, UserSerializerWithToken


# create reservation
def create_reservation_view(request):
    if request.method == 'POST' or None:
        reservation_form = ReservationForm(request.POST or None)

        if reservation_form.is_valid():
            reservation_form.save()
            reservation_form.customer = request.user
            return HttpResponseRedirect('/')

        else:
            return render(request, 'reservations/create_reservation.html', {'form': reservation_form})

    else:
        reservation_form = ReservationForm()
        return render(request, 'reservations/create_reservation.html', {'form': reservation_form})


# registration handling
def register(request):
    if request.method == 'POST':  # if the form has been submitted
        form = UserRegistrationForm(request.POST)  # form bound with post data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


# food menu items
def get_food_menu(request):
    menu_items = FoodItem.objects.get()

    data = {
        'name': menu_items.name,
        'allergens': menu_items.allergen,
        'description': menu_items.description
    }
    return render(request, 'menu.html', data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)