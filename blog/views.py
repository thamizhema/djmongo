import os
import re
import django
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
from .models import AddPost, IMG
import base64
from django.contrib import messages

from django.core.mail import send_mail

from django.core.files.storage import FileSystemStorage
import imgbbpy
sendImage = imgbbpy.SyncClient('0b5946cb8e6e9f69f10b1783630c5818')
client = MongoClient('mongodb+srv://root:root@practice.ri5be.mongodb.net/blog_app')
db = client['blog_app']
collection = db['blog_addpost']
# Create your views here.
def home(req):
    username =  req.session.get('username')
    if(req.method == 'POST'):  
        req.session['username'] = req.POST['username']
        username = req.session.get('username')
    return render(req, 'home.html',{'username': username})

def logout(req):
    del req.session['username']
    return redirect('home')

def addPost(req):  
    if(req.method == 'POST'):  
        title = req.POST['title']
        content = req.POST['content']
        uploaded_file = req.FILES['profile']
        print('***********')
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file )
        pic =  sendImage.upload(file=os.getcwd()+fs.base_url+uploaded_file.name)
        print(pic.url)
        os.remove(os.getcwd()+fs.base_url+uploaded_file.name)
        addData = collection.insert_one({'title':title,'content':content,'profile':pic.url}) 
        # add_post = AddPost()
        # add_post.title = title
        # add_post.content = content
        # add_post.save()
        allData = collection.find().sort('date',pymongo.DESCENDING)
        docs = []
        for doc in allData:   
            doc.update({'docId':str(doc['_id'])})
            docs.append(doc)
        return redirect('get_post')
    else:
        return render(req, 'add_post.html' )

def getPost(req):  
    if(req.method == 'POST'):  
        title = req.POST['title']
        content = req.POST['content']
        uploaded_file = req.FILES['profile']
        print('***********')
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file )
        pic =  sendImage.upload(file=os.getcwd()+fs.base_url+uploaded_file.name)
        print(pic.url)
        os.remove(os.getcwd()+fs.base_url+uploaded_file.name)
        addData = collection.insert_one({'title':title,'content':content,'profile':pic.url}) 
        # add_post = AddPost()
        # add_post.title = title
        # add_post.content = content
        # add_post.save()
    allData = collection.find().sort('date',pymongo.DESCENDING)
    docs = []
    for doc in allData:   
        doc.update({'docId':str(doc['_id'])})
        docs.append(doc)  
    return render(req, 'get_post.html',{'posts':docs} )

def delete(req,id):
    collection.delete_one({'_id':ObjectId(oid=id)})
    return redirect('get_post')

def updateForm(req,id):
   
    data = collection.find_one({'_id':ObjectId(id)})
    return render(req, 'update.html',{'data':data,'id':id})

def update(req,id):
    title = req.POST['title']
    content = req.POST['content']
    collection.update_one({'_id':ObjectId(oid=id)},{"$set":{'title':title,'content':content}})
    return redirect('get_post')

def fileUpload(req):  
    return render(req,'file.html')
    
def fileView(req): 
    if req.method == "POST":
        uploaded_file = req.FILES['document']
        print('***********')
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file )
        pic =  sendImage.upload(file=os.getcwd()+fs.base_url+uploaded_file.name)
        print(pic.url)
        os.remove(os.getcwd()+fs.base_url+uploaded_file.name)  
    return redirect('get_post')

def sendEmail(req):
    if(req.method == 'POST'):
        request = req.POST
        fromAdress = request['from']
        to = request['to']
        subject = request['subject']
        message = request['message']   
        send_mail(subject, message,'thamizharasan2373@gmail.com', [to], fail_silently=False)
        messages.success(req, f'{fromAdress} => {to} => {subject} => {message}')
        return redirect('home')
    return render(req, 'send_mail.html')
    