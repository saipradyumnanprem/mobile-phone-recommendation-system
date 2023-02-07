from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#import requests as r
#from bs4 import BeautifulSoup as bs

# Create your views here.
finalPhones={}

def recommendphones(request):
    return render(request, 'recommend_phones.html')

def results(request):

    selectedPhones = {}
    selectList = []

    if request.method == 'POST': 
        ram = request.POST['ram']
        rom = request.POST['rom']
        size = request.POST['size']
        rating = request.POST['rating']
        camera = request.POST['camera']
        battery = request.POST['battery']
        budget = request.POST['budget']
        #selectedPhones = {ram, rom, size, front_camera, rear_camera, battery, budget}
        selectedPhones = {'ram' : ram, 'rom' : rom, 'size' : size, 
                        'camera' : camera, 
                        'battery' : battery, 'budget' : budget  }

    print(selectedPhones)

    data = {
        "Name":['User Req name'],
        "Rating":rating,
        "Price Rs": '',
        "RAM Gb": ram,
        "ROM Gb": rom,
        "Expandable GB": '',
        "Size Cm": '',
        "Size Inch": size,
        "R1 Cam MP":camera,
        "R2 Cam MP":'',
        "R3 Cam MP":'',
        "R4 Cam MP":'',
        "Battery Mah":budget,
        "Processor":'',
        "Image":' '
    }

    userDf = pd.DataFrame(data)
    df = pd.read_csv("A:/Projects/DataScience/recommender/mainDataset.csv")  

    df = userDf.append(df, ignore_index = True)

    def combineFeatures(row):
        return str(row['Price Rs'])+" "+str(row['RAM Gb'])+" "+ str(row['ROM Gb'] )+" "+str (row['Size Inch'])+" "+ str(row['R1 Cam MP'])+" "+str(row['Battery Mah'])
        

    df["combinedFeatures"]=df.apply(combineFeatures,axis=1)

    cv=CountVectorizer()
    countMatrix=cv.fit_transform(df['combinedFeatures'])

    similar=cosine_similarity(countMatrix)
    similarPhones=list(enumerate(similar[0]))

    sortedSimilarPhones=sorted(similarPhones,key=lambda x:x[1], reverse=True)

    x=0
  
    for phone in sortedSimilarPhones:
        if (df[df.index==phone[0]]['Name'].values[0]=='User Req name'):
            pass
        else:
            finalPhones[df[df.index==phone[0]]['Name'].values[0]]={
                'size':str(df[df.index==phone[0]]['Size Inch'].values[0]),
                'ram':str(df[df.index==phone[0]]['RAM Gb'].values[0]),
                'rom':str(df[df.index==phone[0]]['ROM Gb'].values[0]),
                'camera':df[df.index==phone[0]]['R1 Cam MP'].values[0],
                'budget':df[df.index==phone[0]]['Price Rs'].values[0],
                'processor':df[df.index==phone[0]]['Processor'].values[0],
                'rating':df[df.index==phone[0]]['Rating'].values[0],
                'image':df[df.index==phone[0]]['Image'].values[0],
                'battery':str(df[df.index==phone[0]]['Battery Mah'].values[0]),    
                }
                    
        x=x+1
        if(x==10):
            break   

    template = loader.get_template("results.html")  
    data1 = {
        "products" : finalPhones 
    }
    res = template.render(data1, request)
    return HttpResponse(res)
