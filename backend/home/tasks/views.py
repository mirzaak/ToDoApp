from rest_framework import generics
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from users.serializers import UserSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Task.objects.none()
        return qs.filter(user=request.user)


task_list_create_view = TaskListCreateAPIView.as_view()

class TaskListUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

task_update_view = TaskListUpdateAPIView.as_view()

class TaskListDestroyAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

task_destroy_view = TaskListDestroyAPIView.as_view()
