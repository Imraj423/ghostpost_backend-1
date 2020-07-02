from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import GhostPostSerializer
from api.models import GhostPost

# Create your views here.
class GhostPostViewSet(ModelViewSet):
    serializer_class = GhostPostSerializer
    basename = 'post'
    queryset = GhostPost.objects.all().order_by()

    @action(detail=False)
    def boast(self, request):
        boast = GhostPost.objects.filter(boast=True).order_by('-date')
        page = self.paginate_queryset(boast)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.boast)
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        roast = GhostPost.objects.filter(roast=True).order_by('-date')
        page = self.paginate_queryset(roast)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.roast)
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def up_vote(self, request, id=None):
        post = GhostPost.objects.get(id=id)
        post.up_vote += 1
        post.sum_of_votes += 1
        post.save()
        return Response({
            'id': post.id,
            'up_vote': post.up_vote
        })

    @action(detail=True, methods=['post'])
    def down_vote(self, request, id=None):
        post = GhostPost.objects.get(id=id)
        post.down_vote += 1
        post.sum_of_votes -= 1
        post.save()
        return Response({
            'id': post.id,
            'down_vote': post.down_vote
        })