from accounts.serializers import CurrentUserTaskSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from .permissions import ReadOnly, AuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema


class CustomPaginator(PageNumberPagination):
    page_size = 5
    page_query_param = "page"
    page_size_query_param = "page_size"


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def homepage(request: Request):

    if request.method == "POST":
        data = request.data

        response = {"message": "Welcome to Todo List App", "data": data}

        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Welcome to Todo List App"}
    return Response(data=response, status=status.HTTP_200_OK)


class TaskListCreateView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):

    """
    a view for creating and listing tasks
    """

    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    queryset = Todo.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)

    @swagger_auto_schema(
        operation_summary="Shows all tasks",
        operation_description="This endpoint return all tasks posted by registered users."
    )
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a task",
        operation_description="This endpoint creates a task."
    )
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskRetrieveUpdateDeleteView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [AuthorOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Get a task by its specific id",
        operation_description="This endpoint retrieves a task by an id."
    )
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a task by its specific id",
        operation_description="This endpoint updates a task by its id."
    )
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete a task",
        operation_description="This endpoint deletes a task."
    )
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def get_posts_for_current_user(request: Request):
    user = request.user

    serializer = CurrentUserTaskSerializer(instance=user, context={"request": request})

    return Response(data=serializer.data, status=status.HTTP_200_OK)


class ListTasksForAuthor(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get("username") or None

        queryset = Todo.objects.all()

        if username is not None:
            return Todo.objects.filter(author__username=username)

        return queryset

    @swagger_auto_schema(
        operation_summary="List tasks for a specific user",
        operation_description="This endpoint return all tasks by a specific user."
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)