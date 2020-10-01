from django.shortcuts import render
from django.db.models import Prefetch

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ghostpostApp.serializers import GhostpostSerializer
from ghostpostApp.models import ghostpost

class GhostpostViewSet(viewsets.ModelViewSet):
    queryset = ghostpost.objects.all()
    serializer_class = GhostpostSerializer

    @action(detail=False)
    def Boasts(self, request):
        sort_boasts = ghostpost.objects.all().filter(ghostpost_choice='B')

        # page = self.paginate_queryset(sort_boasts)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(sort_boasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def Roasts(self, request):
        sort_roasts = ghostpost.objects.all().filter(ghostpost_choice='R')

        serializer = self.get_serializer(sort_roasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def Rating(self, request):
        sort_popular = sorted(
            ghostpost.objects.all(),
            key=lambda gp: gp.vote_score,
            reverse=True
            )

        serializer = self.get_serializer(sort_popular, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def Upvote(self, request, pk=None):
        serializer = GhostpostSerializer(data=request.data)
        x = ghostpost.objects.get(pk=pk)
        
        if serializer.is_valid():
            x.upvotes += 1
            x.save()

            return Response({'status': 200})

        return Response({'status': 400})

    @action(detail=True, methods=['post'])
    def Downvote(self, request, pk=None):
        serializer = GhostpostSerializer(data=request.data)
        x = ghostpost.objects.get(pk=pk)
        
        if serializer.is_valid():
            x.downvotes += 1
            x.save()

            return Response({'status': 200})

        return Response({'status': 400})