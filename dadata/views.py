from django.shortcuts import render
from django.http.response import HttpResponse
from .dafetcher import myportal_toolbox as toolbox
from .models import Course
from django.db import transaction
# Create your views here.
def to24Hr(x):
    if x[6] == 'p':
        hr = int(x[:2])
        if hr != 12:
            hr += 12
        x = str(hr) + x[2:5]
    return x

def getDAdata():
    classes = toolbox.GetClasses()
    for i in classes:
        subjects = toolbox.GetSubject(i[0])
        print("Subject:", i[1])
        data=[]
        for j in subjects:
            print("Section:", j[1])
            data = toolbox.GetCourse(i[0], j[2])

            for classes in data:
                #print(classes)
                t = Course()
                t.CRN = classes[0]
                t.Subj = classes[1]
                t.Crse = classes[2]
                t.Sec = classes[3]
                t.Cred = classes[4]
                t.Title = classes[5]
                t.Days = classes[6]
                temp_time = classes[7]
                tb = "TBA"
                te = "TBA"
                temp_time.replace(' ', '')
                if len(temp_time) > 3:
                    tt = temp_time.split('-')
                    tb = tt[0]
                    te = tt[1]
                    tb = to24Hr(tb)
                    te = to24Hr(te)
                t.Time_begin = tb
                t.Time_end = te
                t.Instructor = classes[8]
                t.Location = classes[9]
                t.Attribute = classes[10]
                t.save()
            toolbox.MyPortal.goto(toolbox.util.URL_SELECTSUBJECT)


def UpdateDatabase(request):
    with transaction.atomic():
        getDAdata()
    return HttpResponse("XD")
