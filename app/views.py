from django.contrib.auth import views
from django.shortcuts import render
from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins, viewsets, views

# Create your views here.

class Home(View):
    def get(self,request):
        return render(request, 'app/home.html')

import io
from io import BytesIO
import pandas as pd
from google.cloud import storage

class send_files(views.APIView):

    def post(self, request):
        state = request.POST.get("state")
        ac = request.POST.get("ac")
        myfile = request.FILES.getlist("uploadfiles")

        storage_client = storage.Client.from_service_account_json('/home/this/Downloads/bjp-saral-039039e1a469.json')
        bucket = storage_client.get_bucket('public-saral')

        for f in myfile:
            filename = "%s/%s/%s" % (state, ac, f)
            blob = bucket.blob(filename)
            blob.upload_from_file(f)

        print('Uploaded Successfully')



        return redirect("http://127.0.0.1:8000/")

