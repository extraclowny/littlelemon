from django.shortcuts import render
from django.http import JsonResponse
from .forms import CommentForm
from .models import UserComment, Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


def form_view(request):
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uc = UserComment(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd['comment'],
            )
            uc.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'blog.html', {'form': form})
 
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
