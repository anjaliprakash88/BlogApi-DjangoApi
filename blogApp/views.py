from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def index(request):

    return Response({"Success":"The setup was successful"})


@api_view(['GET'])
def getallposts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def createpost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success':"Post successfullt created"}, status=201)
    else:
        return Response(serializer.errors, status=400)
    
@api_view(['DELETE'])
def deletepost(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({'success': 'The post was successfull'}, status=200)  
    except Post.DoesNotExist:
        return Response({'Error':'The post does not exist'}, status=400) 
    

@api_view(['GET'])
def getpost(request):  
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({'Error':'The post does not exist'}, status=400)
    

@api_view(['PUT'])
def updatepost(request):  
    post_id = request.data.get('post_id')
    get_new_title = request.data.get('new_title')
    get_new_content = request.data.get('new_content')
    try:
        post = Post.objects.get(id=post_id)
        if get_new_title:
            post.title = get_new_title
        if get_new_content:
            post.content = get_new_content
        post.save()
        return Response({'success': 'The post was successfull'}, status=200)   
    except Post.DoesNotExist:
        return Response({'Error':'The post does not exist'}, status=400)   