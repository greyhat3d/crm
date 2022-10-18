from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Beneficiary
# from typings impor
# Create your views here.
def index(request):
    return render(request, "../templates/index.html")


def add_client(request):
    if request.method == "POST":
        # get user inputs
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        srname = request.POST.get("srname")
        gender = request.POST.get("gender")
        disbility = request.POST.get("disability")
        education = request.POST.get("education")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        county = request.POST.get("county")
        location = request.POST.get("location")
        dob = request.POST.get("dob")
        dor = request.POST.get("dor")
        

        

        beneficiary = Beneficiary()
        beneficiary.firstname = firstname
        beneficiary.lastname = lastname
        beneficiary.srname = srname
        beneficiary.gender = gender
        beneficiary.disability = disbility
        beneficiary.education = education
        beneficiary.phone = phone
        beneficiary.email = email
        beneficiary.county = county
        beneficiary.location = location
        beneficiary.dob = dob
        beneficiary.dor = dor


        beneficiary.save()

        
    return render(request, "../templates/add.html")


def update(request, id):
    if request.method  == 'GET':

        beneficiary = Beneficiary.objects.get(pk=id)
        context = {
            "data":beneficiary
        }
        print(beneficiary)

        return render(request, "../templates/update.html", context)
    if request.method == 'POST':
        # get user inputs
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        srname = request.POST.get("srname")
        gender = request.POST.get("gender")
        disbility = request.POST.get("disability")
        education = request.POST.get("education")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        county = request.POST.get("county")
        location = request.POST.get("location")
        dob = request.POST.get("dob")
        dor = request.POST.get("dor")

        print(lastname)
