import requests
import json
import io
import random
import flask
from flask import Flask,render_template,request,Response,send_from_directory
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import time
from pandas.plotting import register_matplotlib_converters
from flask_caching import Cache
import matplotlib.pyplot as plt
register_matplotlib_converters()
#%matplotlib inline
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

plt.rcParams['figure.figsize'] = [15, 5]
from IPython import display
from ipywidgets import interact, widgets

app = Flask(__name__)
# Check Configuring Flask-Caching section for more details
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
import pickle

file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

import numpy as np 
import pandas as pd 
import plotly as py

from jinja2 import Template
from IPython.display import HTML
import json
import re

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

df=pd.DataFrame()
df_countries=pd.DataFrame()
df_countrydate=pd.DataFrame()

@app.route('/')
@app.route('/home')
@cache.cached(timeout=50)
def home():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"
    headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "d1f7e44bbamsh541e009b32d0df9p18e59cjsnc222439ff00f"
    }
    response = requests.get(url, headers=headers)
    params={
        'api_key':'0e230a7838364ca4baf2b954dc827c11',
    }
    r2 = requests.get(
      'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0e230a7838364ca4baf2b954dc827c11',
      params=params)
    return render_template('index.html',articles=json.loads(r2.text)['articles'],world=json.loads(response.text))






        





@app.route('/googlef5f481dd6625c9da.html')
def analytics():
    return render_template('googlef5f481dd6625c9da.html')

    
    
    
    

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
    
@app.route('/.well-known/brave-rewards-verification.txt')
def static_brave():
    return send_from_directory(app.static_folder, request.path[1:])

#@app.route('/wmap.html',methods=['GET', 'POST'])


# def show_map():

#     global df
#     global df_countries
#     global df_countrydate
#     url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv'
#     df = pd.read_csv(url)
#     df = df.rename(columns={'Country/Region':'Country'})
#     df_countries = df.groupby(['Country', 'Date']).sum().reset_index().sort_values('Date', ascending=False)
#     df_countries = df_countries.drop_duplicates(subset = ['Country'])
#     df_countries = df_countries[df_countries['Confirmed']>0]
#     df_countrydate = df[df['Confirmed']>0]
#     df_countrydate = df_countrydate.groupby(['Date','Country']).sum().reset_index()
    
#     fig = go.Figure(data=go.Choropleth(
#         locations = df_countries['Country'],
#         locationmode = 'country names',
#         z = df_countries['Confirmed'],
#         colorscale = 'Reds',
#         marker_line_color = 'black',
#         marker_line_width = 0.5,
#     ))
#     fig.update_layout(
#         title_text = 'Confirmed Cases as of March 28, 2020',
#         title_x = 0.5,
#         geo=dict(
#             showframe = False,
#             showcoastlines = False,
#             projection_type = 'equirectangular'
#         )
#     )
#     Manipulating the original dataframe
    
#     Creating the visualization
#     fig = px.choropleth(df_countrydate, 
#                         locations="Country", 
#                         locationmode = "country names",
#                         color="Confirmed", 
#                         hover_name="Country", 
#                         animation_frame="Date"
#                     )
#     fig.update_layout(
#         title_text = 'Global Spread of Coronavirus',
#         title_x = 0.5,
#         geo=dict(
#             showframe = False,
#             showcoastlines = False,
#         ))
#     py.offline.plot(fig, filename='templates/wmap.html',auto_open=False)
#     return render_template('wmap.html') 


@app.route('/indiastat')
@cache.cached(timeout=50)
def indiastat():
    url = "https://api.rootnet.in/covid19-in/stats/latest"
    response = requests.get(url) 
    url = "https://api.rootnet.in/covid19-in/contacts"
    k = requests.get(url)
    url = "https://api.rootnet.in/covid19-in/stats/hospitals"
    r = requests.get(url)
    ur= "http://newsapi.org/v2/top-headlines?country=in&apiKey=0e230a7838364ca4baf2b954dc827c11"
    r2= requests.get(ur)
    urls = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"
    headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "d1f7e44bbamsh541e009b32d0df9p18e59cjsnc222439ff00f"
    }
    r3 = requests.get(urls, headers=headers)
    world=json.loads(r3.text)['countries_stat']
    for i in world:
        if(i['country_name']=='India'):
            ca=i['cases']
            tr=i['total_recovered']
            de=i['deaths']
            break
    return render_template('examples/tables.html',ca=ca,tr=tr,de=de,regional=json.loads(response.text)['data']['regional'],rg=json.loads(k.text)['data']['contacts']['regional'], hs=json.loads(r.text)['data']['regional'],news=json.loads(r2.text)['articles'],overall=json.loads(response.text)['data']['summary'])



@app.route('/tracker')
@cache.cached(timeout=50)
def tracker():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"
    headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "d1f7e44bbamsh541e009b32d0df9p18e59cjsnc222439ff00f"
    }                                                                                                                                                           
    r1 = requests.get(url, headers=headers)
    params={
        'api_key':'0e230a7838364ca4baf2b954dc827c11',
    }
    r2 = requests.get(
      'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0e230a7838364ca4baf2b954dc827c11',
      params=params)
    urls = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"
    r3 = requests.get(urls, headers=headers)
    r4 = requests.get('http://newsapi.org/v2/top-headlines?sources=google-news&apiKey=0e230a7838364ca4baf2b954dc827c11',params=params)
    return render_template('examples/dashboard.html',articles=json.loads(r2.text)['articles'],world=json.loads(r1.text),countries_stat=json.loads(r3.text)['countries_stat'],wnews=json.loads(r4.text)['articles'])

# @app.route('/profile')
# def profile():
#     return render_template('examples/profile.html')



@app.route('/tst', methods=["GET", "POST"])
def tst():
    if request.method == "POST":
        myDict = request.form
        fever = float(myDict['fever'])
        age = int(myDict['age'])
        pain = int(myDict['pain'])
        runnyNose = int(myDict['dryCough'])
        diffBreath = int(myDict['diffBreath'])
        # Code for Inference
        inputFeatures = [fever, pain, age, runnyNose, diffBreath]
        infProb = clf.predict([inputFeatures])
        if infProb == 1:
            res="You may Have Positive Symptoms"
        else:
            res="You are Probably Safe"
        print(infProb)
        return render_template('examples/show.html', inf=res)
    return render_template('examples/profile.html')
    # return 'Hello, World!' + str(infProb)


@app.route('/indiastate', methods=['GET','POST'])
def indiastate():
    url = "https://api.rootnet.in/covid19-in/stats/latest"
    response = requests.get(url)
    regional=json.loads(response.text)['data']['regional']
    url = "https://api.rootnet.in/covid19-in/contacts"
    k = requests.get(url)
    url = "https://api.rootnet.in/covid19-in/stats/hospitals"
    r = requests.get(url)
    ur= "http://newsapi.org/v2/top-headlines?country=in&apiKey=0e230a7838364ca4baf2b954dc827c11"
    r2= requests.get(ur)
    res="Rajasthan-AshkokGehlot.jpg"
    res2="rajasthan.png"
    res3="Chief Minister Mr. Ashok Gehlot"
    for region in regional:
        if (region['loc'] == "Rajasthan"):
            a=region['confirmedCasesIndian']
            b=region['discharged']
            c=region['deaths']
            d=33
    res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2",
    "https://education.rajasthan.gov.in/content/dam/doitassets/education/medicaleducation/sms-medical-college-jaipur/pdf/News/Govt.%20Instructions%20for%20COVID%2019.pdf",
    "https://cmrelief.rajasthan.gov.in/ContributionCovid-19.aspx"]
    res5=["During the lockdown period in the state, supply of essential commodities will be done from house to house, supply of ration items, dairy products, vegetables and medicines will be done.",
            "Important decisions of Chief Minister for relief from Corona crisis.Big relief to farmers, industries and general public Electricity and water bills will be postponed for two months.",
            "In view of the effect of Corona virus by the state government, it has been decided to provide whole grains in the form of pulses, wheat to about 35 lakh beneficiaries through Anganwadi centers. Under this, 35 lakh families will be given 1 kg of pulses and 2 to 3 kg of wheat in a month under Integrated Child Development Services Scheme. This system will remain in force for the duration of the corona virus.",
            "Immediate financial assistance of Rs.1000 / - deposited in the account of 15.78 lakh construction workers.",
            "Apart from this, 36 lakh 51 thousand BPL,Beneficiaries of State BPL and Antyodaya Yojana,25 lakh construction workers and registered street vendors who are not covered under Social Security Pension Scheme, will be given one thousand rupees as a fixed ex-gratia amount so that they will get cash in their hands and they can meet their daily needs. Will be able to do it.",
            "Shri Gehlot has instructed to give 2 months pension simultaneously to the beneficiaries of the state's 78 lakh social security pension.",
            "Due to the lock down by the state government, liquor license shops, hotel bars, restaurant bars have been given relief by deciding certain fee waivers and postponement.",
            "Chief Minister has given permission to extend the term of interest waiver scheme-2019 of Agricultural Marketing Department and extension of waiver of outstanding mandi duty on imported agricultural commodities and sugar for agricultural processing from outside the state till June 30.",
            "A monthly honorarium of Rs 5000 has been sanctioned to such senior journalists above 60 years of age who have served in the field of journalism in life.",
            "The state government has exempted agricultural version units from applying to the Agricultural Produce Market Committees for a license for direct purchase from farmers. He said that at present, there was a provision for obtaining direct purchase license from the agricultural processing units of the state by applying to the respective agricultural produce market committees for direct purchase from the farmers.",
            "Flour mills will be made available to the wheat mills by cutting a maximum of 100 grams per kg, that is, cutting 10 percent of the size, in lieu of the quantity of wheat to be given.",
            "The State Government has directed to put Rs. 824 crore under the material head into the account of the workers with immediate effect so that the labor item as well as the material item is not paid due to any inconvenience to the workers in such a critical time.",
            "The state government has extended the period of 5 percent interest subsidy scheme from tenure of March 31, 2020 to June 30, 2020, to tenants taking long-term agricultural loans, giving big relief to the farmers. Now tenants who repay the loan on time will get agricultural loan at 6.65 percent interest rate.",
            "Chief Minister Mr. Ashok Gehlot has instructed all school operators in the state not to take three months advance fee from the students till the lockdown applicable to prevent corona infection continues.",
            " Chief Minister Mr. Ashok Gehlot has announced to provide assistance of Rs. 50 lakhs to the dependent / family in case of untimely death due to corona infection while all the employees of the state government are on duty related to corona campaign.",
            "According to Chief Minister Mr. Ashok Gehlot, 5 lakh minikits of certified seeds of maize and 5 lakh minikits of certified seeds of millet of 1.5 kg are available free of cost to 5 lakh farmers in the Scheduled Tribes area of ​​the state during the Kharif season will be made.",
            "With the receipt of two months pension together, the amount of Rs 1500 and above will reach the hands of the beneficiaries of social security pension. This amount will be directly deposited in the bank accounts of the beneficiaries.The state government has already announced to give one rupee and two rupees per kg of wheat to the families covered under NFSA till May. A package of about 2 thousand crores has been prepared for all these."]
    Res={'picture':res,'state':res2,'name':res3,'pdf':res4,'news':res5}
    if request.method == "POST":
        url = "https://api.rootnet.in/covid19-in/stats/latest"
        response = requests.get(url) 
        regional=json.loads(response.text)['data']['regional']
        url = "https://api.rootnet.in/covid19-in/contacts"
        k = requests.get(url)
        url = "https://api.rootnet.in/covid19-in/stats/hospitals"
        r = requests.get(url)
        ur= "http://newsapi.org/v2/top-headlines?country=in&apiKey=0e230a7838364ca4baf2b954dc827c11"
        r2= requests.get(ur)
        myDict = request.form
        state = str(myDict['browsers'])
        # print(state)
        if state=="Rajasthan":
            for region in regional:
                if (region['loc'] == "Rajasthan"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=33
            res="Rajasthan-AshkokGehlot.jpg"
            res2="rajasthan.png"
            res3="Chief Minister Mr. Ashok Gehlot"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2",
    "https://education.rajasthan.gov.in/content/dam/doitassets/education/medicaleducation/sms-medical-college-jaipur/pdf/News/Govt.%20Instructions%20for%20COVID%2019.pdf",
    "https://cmrelief.rajasthan.gov.in/ContributionCovid-19.aspx"]
            res5=["During the lockdown period in the state, supply of essential commodities will be done from house to house, supply of ration items, dairy products, vegetables and medicines will be done.",
            "Important decisions of Chief Minister for relief from Corona crisis.Big relief to farmers, industries and general public Electricity and water bills will be postponed for two months.",
            "In view of the effect of Corona virus by the state government, it has been decided to provide whole grains in the form of pulses, wheat to about 35 lakh beneficiaries through Anganwadi centers. Under this, 35 lakh families will be given 1 kg of pulses and 2 to 3 kg of wheat in a month under Integrated Child Development Services Scheme. This system will remain in force for the duration of the corona virus.",
            "Immediate financial assistance of Rs.1000 / - deposited in the account of 15.78 lakh construction workers.",
            "Apart from this, 36 lakh 51 thousand BPL,Beneficiaries of State BPL and Antyodaya Yojana,25 lakh construction workers and registered street vendors who are not covered under Social Security Pension Scheme, will be given one thousand rupees as a fixed ex-gratia amount so that they will get cash in their hands and they can meet their daily needs. Will be able to do it.",
            "Shri Gehlot has instructed to give 2 months pension simultaneously to the beneficiaries of the state's 78 lakh social security pension.",
            "Due to the lock down by the state government, liquor license shops, hotel bars, restaurant bars have been given relief by deciding certain fee waivers and postponement.",
            "Chief Minister has given permission to extend the term of interest waiver scheme-2019 of Agricultural Marketing Department and extension of waiver of outstanding mandi duty on imported agricultural commodities and sugar for agricultural processing from outside the state till June 30.",
            "A monthly honorarium of Rs 5000 has been sanctioned to such senior journalists above 60 years of age who have served in the field of journalism in life.",
            "The state government has exempted agricultural version units from applying to the Agricultural Produce Market Committees for a license for direct purchase from farmers. He said that at present, there was a provision for obtaining direct purchase license from the agricultural processing units of the state by applying to the respective agricultural produce market committees for direct purchase from the farmers.",
            "Flour mills will be made available to the wheat mills by cutting a maximum of 100 grams per kg, that is, cutting 10 percent of the size, in lieu of the quantity of wheat to be given.",
            "The State Government has directed to put Rs. 824 crore under the material head into the account of the workers with immediate effect so that the labor item as well as the material item is not paid due to any inconvenience to the workers in such a critical time.",
            "The state government has extended the period of 5 percent interest subsidy scheme from tenure of March 31, 2020 to June 30, 2020, to tenants taking long-term agricultural loans, giving big relief to the farmers. Now tenants who repay the loan on time will get agricultural loan at 6.65 percent interest rate.",
            "Chief Minister Mr. Ashok Gehlot has instructed all school operators in the state not to take three months advance fee from the students till the lockdown applicable to prevent corona infection continues.",
            " Chief Minister Mr. Ashok Gehlot has announced to provide assistance of Rs. 50 lakhs to the dependent / family in case of untimely death due to corona infection while all the employees of the state government are on duty related to corona campaign.",
            "According to Chief Minister Mr. Ashok Gehlot, 5 lakh minikits of certified seeds of maize and 5 lakh minikits of certified seeds of millet of 1.5 kg are available free of cost to 5 lakh farmers in the Scheduled Tribes area of ​​the state during the Kharif season will be made.",
            "With the receipt of two months pension together, the amount of Rs 1500 and above will reach the hands of the beneficiaries of social security pension. This amount will be directly deposited in the bank accounts of the beneficiaries.The state government has already announced to give one rupee and two rupees per kg of wheat to the families covered under NFSA till May. A package of about 2 thousand crores has been prepared for all these."]
        elif state=="WestBengal":
            for region in regional:
                if (region['loc'] == "West Bengal"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=23
            res="WB-MamataBanerjee.jpg"
            res2="west bengal.jpg"
            res3="Chief Minister Mrs. Mamata Banerjee"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2",
    "https://www.wbhealth.gov.in/other_files/118.pdf",
    "https://www.wbhealth.gov.in/uploaded_files/corona/Serf.pdf",
    "https://wb.gov.in/upload/MCLNEWS-200322111116287.pdf"]
            res5=["West Bengal Chief Minister Mamata Banerjee announced setting up of dedicated nodal hospitals for COVID-19 cases in each of the 22 districts.",
            "West Bengal Chief Minister  also announced an increased insurance payout to all the government doctors, nurses, health workers, pharmacists, cleaning staffs, ASHA workers and anyone who has been aiding the government to curtail the pandemic from Rs 5 lakh to 10 lakh. The payout also includes sanitation workers and police personnel.",
            "Mamata Banerjee announces West Bengal WBBSE Class 12 exams will be held in June.The students of class 11 and colleges would be promoted to the next class and semesters",
            "Chief Minister Mamata Banerjee has promised some money for Bengal migrants stranded outside the state for petty expenses.",
            "The West Bengal government has decided to deploy armed police in parts of the state which have been identified as 'red zones'- the areas where Covid-19 is severe."]
        elif state=="TamilNadu":
            for region in regional:
                if (region['loc'] == "Tamil Nadu"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=32
            res="TN-EdappadiKPalaniswami.gif"
            res2="tamil nadu.png"
            res3="Chief Minister Mr. Edappadi K Palaniswami"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2",
    "https://www.manupatrafast.com/covid_19/Tamil%20Nadu/Govt/Corona%20Virus%20Disease%20COVID19%20Infection%20Prevention%20and%20Control%20The%20Epidemic%20Diseases%20Act%201897.pdf",
    "http://www.hcmadras.tn.nic.in/COVID%2019_Administrative_directives_for_high_court.pdf",
    "https://ereceipt.tn.gov.in/cmprf/cmprf.html"]
            res5=["The Tamil Nadu government has ordered private banks, small finance banks and micro lenders to refrain from collecting loan repayments till further notice, raising the spectre of other states following suit that could create chaos and defaults.",
            "Tamil Nadu Chief Minister K Palaniswami on Tuesday announced sops to farmers, which include waiver of cold storage user fee and facilitation in marketing and logistics. Besides, loans upto Rs 10 lakh would be offered to farmer producer firms aimed at benefiting both ryots and consumers.",
            "The Tamil Nadu government made an announcement restricting volunteers and NGOs from distributing relief materials to people affected by the COVID-19 pandemic.",
            "Tamil Nadu CM writes to PM Modi, seeks funds to combat COVID-19.",
            "Tamil Nadu government announces one month of special pay to doctors, nurses and sanitation workers.",
            "The Chief Minister said all the ration card-holders would get ₹1000 and free rice, dal, cooking oil and sugar.",
            "Construction workers and autorickshaw drivers who are members of the welfare board would get ₹1000, 15 kg of rice, 1 kg of dal and 1 kg of cooking oil.",
            "For the elderly who depend on Anganwardis, the food will be distributed directly to them in their homes. For platform vendors who have registered with the government, an additional ₹1000 will be given.",
            "Those who are working under Mahatma Gandhi Rural Employment Scheme will get a two-day special salary.",
            "The government will provide a job to one person from such victims' families on compassionate grounds and based on their qualification, he said.",
            "The CM said that the  work of medical professionals in both public and private sectors and others will be recognised and such persons will be provided with awards, he said."]
        elif state=="MadhyaPradesh":
            for region in regional:
                if (region['loc'] == "Madhya Pradesh"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=52
            res="MP-ShivrajSinghChouhan.jpg"
            res2="madhya pradesh.png"
            res3="Chief Minister Mr. Shivraj Singh Chouhan"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["The state's control and command centre has been established where arrangements have been made for providing telemedicine facilities to people. Doctors are deployed and are answering people's calls, prescribing medicines and planning for providing them.",
            "The Chief Minister has also decided to provide ration free of cost to the poor, irrespective of whether they have ration cards or not, for the next three months.",
            "The Madhya Pradesh government has decided to promote students of all classes, except standards 10th and 12th of the state schools without exams in view of the coronavirus outbreak.",
            "Around 1,500 beds have been arranged at Bhopal and Indore for treatment of corona-affected patients.",
            "MP govt makes wearing masks mandatory while stepping out",
            " ₹1,000 would be provided to labourers as support through the State Building and Other Construction Workers Welfare Board.",
            " Mr. Chouhan announced ₹2,000 for two months to each Saharia, Baiga and Bharia family.",
            "Old age and social security pensioners would receive an advance amount of ₹1,200 for two months."]
        elif state=="Jharkhand":
            for region in regional:
                if (region['loc'] == "Jharkhand"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=24
            res="Jharkhand-HemantSoren.jpg"
            res2="jharkhand.png"
            res3="Chief Minister Mr. Hemant Soren"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2",
    "https://cdn.s3waas.gov.in/s32b8a61594b1f4c4db0902a8a395ced93/uploads/2020/03/2020032080.pdf"]
            res5=["As a significant portion of Jharkhand’s population is employed as migrant workers in other states, the Chief Minister, Hemant Soren has been working with his counterparts to bring back any person of the state who is stranded elsewhere in the country",
            "Rs. 200 crores have been earmarked towards expenditure in connection with the tests and setting up of other apparatus to deal with any emerging situation.",
            "The Jharkhand government has set up a 557-bed isolation ward for COVID-19 patients in different hospitals of the state. The state has also set up 1,469 quarantine centres at different places.",
            "Jharkhand Chief Minister Hemant Soren said his government has decided to provide two months ration in advance to the beneficiaries of the Public Distribution System, as the country entered the second day of the lockdown to contain the coronavirus outbreak.",
            "The state government of Jharkhand needs urgent help from the Centre, said CM Hemant Soren, as Jharkhand is a small, poor and backward state and at the early stage the coronavirus can be contained under control.",
            "17 districts are to be declared as green zones by the Jharkhand state government as no COVID-19 patients came from these states.",
            "The Jharkhand government for the first time has come up with an innovative idea to open up 600 dal bhat kendra in police stations to feed the poor. The poor will have access to meals at a throw-away price of Rs 5 in police stations.",
            "Jharkhand Chief Minister Hemant Soren said his government has decided to provide two months ration in advance to the beneficiaries of the public distribution system, as the country entered the lockdown to contain the COVID-19 outbreak.",
            "More than 350 khichidi centres will start functioning so that the needy can have meals, Chief Minister Hemant Soren announced amidst the pandemic.",
            "Jharkhand Chief Minister Hemant Soren on Sunday dismissed the government’s statements that an event organised by the Tablighi Jamaat in Delhi’s Nizamuddin area has led to a big jump in coronavirus infections in India.",
            "The Jharkhand state government issued a rate-chart of essential items at the public distribution outlets, following reports that a few ration shops were charging higher prices for commodities and some others selling them in the black market, taking advantage of the lockdown.",
            "Ranchi Deputy Commissioner Rai Mahimapat Ray said that the administration has launched an app - VeggiGo - for people to place online orders for essential commodities."]
        elif state=="Maharashtra":
            for region in regional:
                if (region['loc'] == "Maharashtra"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=36
            res="Maharashtra-UddhavThackeray.jpg"
            res2="maharashtra.png"
            res3="Chief Minister Mr. Uddhav Thackeray"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2",
    "https://www.maharashtra.gov.in/Site/Upload/Acts%20Rules/Marathi/Korona%20Notification%2014%20March%202020....pdf"]
            res5=["Uddhav Thackeray, Maharashtra CM promised the migrants of all possible help- food, shelter and necessary medication. Thackeray also urged the migrants to stay in their current locations and assured them of necessary arrangements once the situation improves.",
            "Relief camps have been set up all over the Maharashtra sheltering more than 5 lakh labourers.",
            "Maharashtra government  instructed all the landlords and house owners in the state to postpone rent collection by at least three months to help those whose income has been affected due to coronavirus lockdown.",
            "More than 1 crore people have been benefited through the PDS distribution of rice.",
            "2 task force has been deployed to work on the economic front.",
            "Wearing mask/cloth in public is made mandatory.",
            "There are no restrictions on agricultural activities, agricultural commodities like seeds, fertilizers or farming tools.",
            "The authorities are instructed to distribute essentials to tribal people who reside in remote and hilly terrains before beginning of monsoon."]
        elif state=="AndhraPradesh":
            for region in regional:
                if (region['loc'] == "Andhra Pradesh"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=13
            res="AP-YSJaganmohanReddy.jpeg"
            res2="ap.png"
            res3="Chief Minister Mr. Y S Jaganmohan Reddy"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["The State government  decided to supply ration to every poor family as food security.",
            "The social security pensions to beneficiaries and `1,000 aid to the poor people will be door delivered through village/ward volunteers.",
            "Andhra Pradesh was the first state to undertake a state-wide rollout of both laboratory and radiology services using a hybrid model.",
            "The Andhra Pradesh government has decided to take over facilities and manpower at private hospitals by invoking powers under the Disaster Management Act to tackle the Covid-19 pandemic.",
            "Reviewing the agriculture and horticulture situation in the State with higher officials , the Chief Minister said the government is gearing up for setting up YSR Janata Bazaars to help both farmers and consumers.CM says 22,000 Janata Bazaars with cold storage units and small and midsize trucks for transportation of farm produce, will create a robust marketing network to boost the income of farmers and others dependent on agriculture and allied sectors.",
            " Andhra Pradesh CM YS Jaganmohan Reddy has announced that the government will provide financial assistance of Rs 2,000 to every poor person who has completed quarantine in government facilities. If the coronavirus test is negative after completing quarantine, then after quarantine, every poor person will be given Rs 2000 so that he can buy nutritious food.",
            "Andhra Pradesh announces one-time aid of Rs 2,000 to 6,000 fishermen struck in Gujarat due to lockdown",
            "The Andhra Pradesh government  announced deferment of payment of full salaries to the chief minister, officers and employees, saying its revenue streams have totally dried up in view of the ongoing lockdown to combat coronavirus.",
            "The  government have made wearing face mask compulsory.",
            "Chief Minister Y.S. Jagan Mohan Reddy on Monday made a two-stage strategy to check the spread of COVID-19 with particular emphasis on urban areas in the State."]
        elif state=="Chattisgarh":
            for region in regional:
                if (region['loc'] == "Chhattisgarh"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=27
            res="Chhattisgarh-BhupeshBaghel.jpg"
            res2="chhattisgarh.png"
            res3="Chief Minister Mr. Bhupesh Baghel"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["The Chhattisgarh government will provide 100 beds each to all of 28 districts of the state to deal with coronavirus cases",
            "Raipur Institute of Medical Sciences College is being developed as a COVID-19 hospital where 500 beds are being arranged.",
            "In a bid to provide relief to the poor amid an ongoing coronavirus pandemic, the Chhattisgarh government issued a notification stating that rice and dal will be distributed to ration card holders, students and others.",
            "School children will also be allocated their quota of grains as per the mid-day meal scheme during the holiday period. Under this scheme, 40 days dry dal and rice will be supplied to the children of the school. Each student of primary school will be given 4 kg of rice and 800 grams of dal and 6 kg of rice and 1,200 grams of dal will be distributed to each student of higher secondary schools.",
            "As a goodwill gesture, the Chhattisgarh government has decided to give special allowance to the staff of the Health Department engaged in the treatment of the coronavirus.",
            "The government has licensed two distilleries for industrial manufacture of alcohol-based hand sanitisers as part of measures to prevent coronavirus",
            "The time limit for renewal of a licence or permit has also been increased by a month in all urban bodies of the state. The last date for depositing property tax in urban bodies of the state has been extended from March 31 to April 30",
            "The state government is also initiating a drive to use drones for spraying of disinfectants in areas which could be prone to coronavirus spread such as the vicinity of hospitals, marketplaces with concentration of food, medical and essential commodity stores etc. "]
        elif state=="Delhi":
            for region in regional:
                if (region['loc'] == "Delhi"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=11
            res="Delhi-ArvindKejriwal.jpg"
            res2="delhi.png"
            res3="Chief Minister Mr. Arvind Kejriwal"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2",
    "http://health.delhigovt.nic.in/wps/wcm/connect/146af7004d87f91c96a2f7982ee7a5c7/Epedimic+Act.pdf?MOD=AJPERES&lmod=-762064770&CACHEID=146af7004d87f91c96a2f7982ee7a5c7",
    "https://main.sci.gov.in/pdf/cir/covid19_14032020.pdf",
    "https://www.icmr.nic.in/sites/default/files/Circulars_front/Dopt_order1.pdf"]
            res5=["Delhi Chief Minister Arvind Kejriwal announced a 5T plan to stop the spread of the novel coronavirus. The 5T plan includes testing, tracing, treatment, teamwork and tracking.",
            "Delhi government is  also distributing food in over 500 schools and 238 night shelters.” The  568 schools have been converted into community kitchens to prepare food for the needy.",
            "Delhi CM Arvind Kejriwal  also announced  that families of healthcare personnel will get Rs 1 crore in case they die while dealing with coronavirus cases.",
            "Delhi government have made wearing face mask compulsory.",
            "The Delhi government will takeover 12,000 hotel rooms in the wake of spike in number of coronavirus cases, Kejriwal said.",
            "Delhi Chief Minister Arvind Kejriwal on Thursday announced an comprehensive plan named 'SHIELD' to control the spread of coronavirus in the national capital.S stands for sealing of localities, wherein, people from a locality will not go to other areas and vice-versa.   H means home quarantine i.e. people will remain in their homes only.  I stands for isolation and tracing under which COVID-19 patients will be isolated and people whom they have met will be traced, identified and will be isolated too.  E means essential supplies under which we will ensure door to door delivery of essential services.  L refers to local sanitisation under which areas will be disinfected on a regular basis.  While D stands for door-to-door checking under which we will ask every family whether there is any person having symptoms of coronavirus. If any such person is found, their samples will be taken and further procedure will be followed.",
            "The Delhi government will give 2,000 food coupons each to every MLA and MP in the city for distribution among the needy in their constituencies amid the coronavirus-induced lockdown.",
            "Government has also decided to provide free-ration to around 30 lakh people who do not have ration cards, asserting that there are currently 71 lakh beneficiaries of public distribution system and they are being provided free-ration by the government.",
            "Government will also distribute kits of daily-use items such as soap, oil, sugar, turmeric and salt along with ration for the month of May.",
            "The Delhi government will procure 60 new ambulances and an order has been issued for the same"
            ]
        elif state=="Bihar":
            for region in regional:
                if (region['loc'] == "Bihar"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=38
            res="1587169330081_Bihar-NitishKumar.jpg"
            res2="bihar.png"
            res3="Chief Minister Mr. Nitish Kumar"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2",
    "http://egazette.bih.nic.in/GazettePublished/212_2_2020.pdf",
    "http://www.cmrf.bih.nic.in/users/home.aspx"]
            res5=["Bihar State Disaster Management Department said a total of 14.56 lakh migrants have been provided relief so far in camps set up for the purpose in Delhi and Mumbai, and states like Tamil Nadu, Karnataka and West Bengal.",
            "The process of sending show-cause notices to another 122 doctors too has been started and will be issued against them soon”, said a senior Health Department Official.",
            "The State government on Monday announced that financial assistance of ₹1,000 was credited to the bank accounts of 1.03 lakh migrant workers of Bihar working in other States, through DBT (Direct Benefit Transfer) system.",
            " Chief Minister Nitish Kumar (CM Nitish Kumar) has announced to give one month's basic salary as a separate incentive amount to the doctors and other medical workers and also as a package of assistance to the pensioners from ration card holders to large Relieved.",
            "The Bihar government has also announced one month ration free to all ration card holders families.",
            "Chief Minister Nitish Kumar on Monday launched a scheme to provide special assistance of Rs 1,000 each to the natives of Bihar stranded in other states due to the nationwide lockdown prompted by coronavirus",
            "Apart from the ration cardholders, the Bihar chief minister has also asked the state Disaster Management officials to reach out to every state resident stranded outside Bihar because of the ongoing lockdown.",
            "The Bihar chief minister said Rs 100 crore has been released from the Chief Minister's Relief Fund for setting up shelters for rickshaw pullers and daily-wage earners.",
            "Also, three months pension will be given immediately in advance to all under old age pension, disabled pension, widow pension and old age pension. If this amount will be directly deposited in their account, then one thousand rupees per family will be given to all the ration card holder families in the panchayat of lockdown area and block headquarters. The amount will be sent to their account.",
            "Along with this, Chief Minister Nitish Kumar has also made a big announcement for the students and said that all students from 1st to 12th will be given scholarships.",
            "Chief Minister Nitish Kumar on Monday launched a scheme to provide special assistance of Rs 1,000 each to the natives of Bihar stranded in other states due to the nationwide lockdown prompted by coronavirus.",
            "Apart from the ration cardholders, the Bihar chief minister has also asked the state Disaster Management officials to reach out to every state resident stranded outside Bihar because of the ongoing lockdown.",
            "The Bihar chief minister said Rs 100 crore has been released from the Chief Minister's Relief Fund for setting up shelters for rickshaw pullers and daily-wage earners."]
        elif state=="UttarPradesh":
            for region in regional:
                if (region['loc'] == "Uttar Pradesh"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=75
            res="UP-YogiAdityanath.jpg"
            res2="uttar pradesh.png"
            res3="Chief Minister Mr. Yogi Adityanath"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["The Uttar Pradesh government transferred Rs 1,000 each to the bank accounts of daily wagers, including street vendors and rickshaw pullers, as maintenance allowance for the COVID-19 lockdown period.",
            "The Yogi Adityanath government in Uttar Pradesh has decided to completely seal  15 districts that have emerged as coronavirus hotspots. The districts to be sealed are Lucknow, Noida, Ghaziabad, Sitapur, Kanpur, Agra, Ferozabad, Bareilly, Meerut, Shamli, Saharanpur, Bulandshahr, Varanasi, Maharajganj and Basti.",
            "The Uttar Pradesh government allows migrant workers to go home after completing the quarantine period.",
            "Uttar Pradesh government bans gutkha to avoid COVID-19 spread.",
            "Uttar Pradesh has obtained clearance from the Indian Council for Medical Research (ICMR) to start pool testing becoming the first in the country to attempt this method which aims at expediting the testing process for Covid-19.",
            "The Uttar Pradesh Government has roped in professional counsellors to counsel people who are in quarantine centres, shelter homes and even people at home. "]

        elif state=="Goa":
            for region in regional:
                if (region['loc'] == "Goa"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=2
            res="cmgoa.jpg"
            res2="goa.jpg"
            res3="Chief Minister Mr Pramod Sawant"
            res4=["https://www.goa.gov.in/wp-content/uploads/2020/05/MHA-Order-Dt.-17.5.2020-on-extension-of-lockdown-till-31.5.2020-with-guidelines-on-lockdown-measures.pdf",
    "https://www.goa.gov.in/wp-content/uploads/2020/05/Media-BULLETIN.pdf",
    "https://www.goa.gov.in/wp-content/uploads/2020/03/Notifications-in-respect-of-Coronavirus.pdf",
    "https://www.goa.gov.in/wp-content/uploads/2020/04/Order-In-Order-To-Prevent-Spread-Of-COVID-19-In-The-State-Of-Goa-Public-Health-Department.pdf",
    "https://www.goa.gov.in/wp-content/uploads/2020/05/Order-Section-144-Restriction-or-Ban-imposed-in-North-Goa.pdf",
    "https://www.goa.gov.in/wp-content/uploads/2020/05/Order-Rules-Regarding-Quarantine-Facilities.pdf"]
            res5=["After the Central government formally declared both districts of Goa as Coronavirus-free green zones, Chief Minister Pramod Sawant said on Friday that war against COVID-19 is far from over as he praised “Corona Warriors” and people of his state.",
            "The pandemic management through technology tools and online platforms has helped Goa becoming the COVID-19 free, says Department of Information Technology, Government of Goa.",
            "The Chief Minister said that in the coming days, the government would scrutinize reports of its three-day door-to-door citizens survey done last week and decide on testing people for COVID-19 wherever felt necessary.",
            "The Goa government is in talks with the Railway Ministry regarding the matter and has informed that the Covid-19 situation in Goa can deteriorate due to the rise in coronavirus cases in Maharashtra, Therefore CM is likely to have a separate Standard Operating Procedure (SOP) for travellers coming from Maharashtra.",
            "Goa's Governor states Tourism is not a problem as Goa is Corona free so domestic tourists will come here. It will take some time for foreign tourists to return but they too will come. This is not a long-term loss to the industry.",
            "Residents of Goa, who are currently stranded in different parts of the country due to the lockdown, will be quarantined for free by the government once they return to the state, Chief Minister Pramod Sawant has announced.",
            "The Goa government has decided that people not wearing masks will not be given fuel at petrol pumps or ration at fair price shops in the state.",
            "The Chief Minister's Office tweeted that the state government had started running food buses/vehicles with cooked food for the needy. The Goa government website also has a list of about 150 establishments, shops, and volunteers who have been authorized for home delivery in the south district.",
            "The New Delhi-Goa special train will be stopped from the next week onwards, Goa Chief Minister Pramod Sawant said after the state saw a spike in the number of Covid-19 cases largely fueled by train passengers."]

        elif state=="Gujarat":
            for region in regional:
                if (region['loc'] == "Gujarat"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=33
            res="gujcm.jpg"
            res2="guj.png"
            res3="Chief Minister Mr. Vijay Rupani"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Gujarat Chief Minister Vijay Rupani on Thursday announced Rs 650 crore package for 65 lakh families of the poor, labourers, unorganised workers, construction workers of the state.",
            "The state government also announced Rs 30-35 crore financial aid for Gaushalas and cattle ponds. Under this Rs 25 per animal for the month of April will be provided to all Gaushalas and cattle ponds",
            "The fixed charges on electricity bill have also been waived off for the month of April for small industries, factories and MSMEs in the state.",
            "Rs 221 crore have been deposited in such person's bank accounts. This will benefit more than 13 lakh in the state",
            "The Gujarat government announced a relief package of Rs 14,000 crore to help revive the economy battered by the lockdown imposed to curb the spread of coronavirus, a measure that includes tax rebates to consumers and loan subsidy for business and shop owners.",
            "We have decided to give relief to people in payment of property tax, electricity bills and vehicle tax, Mr Rupani said.",
            "free ration to poor families during the period of lockdown and direct transfer of Rs 1,000 in their accounts.",
            "The government also decided to allocate Rs 100 crore to the health department and another Rs 100 crore to four municipal corporations - Ahmedabad, Surat, Vadodara and Rajkot - from the Chief Ministers Relief Fund to fight the novel coronavirus."]

        elif state=="Haryana":
            for region in regional:
                if (region['loc'] == "Haryana"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=22
            res="harcm.jpg"
            res2="har.png"
            res3="Chief Minister Mr. Manohar Lal Khattar"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["The state government  announced a special financial aides to help the poor Below Poverty Line and in low income groups like daily wagers, labourers, street vendors and construction workers.",
            "Haryana Chief Minister Manohar Lal Khattar on Thursday announced that the state government will provide insurance cover of Rs 10 lakh each to all journalists in Haryana who are reporting during the coronavirus pandemic.",
            "Haryana Chief Minister Manohar Lal Khattar on Thursday announced that his government will double the salary of the medical personnel deployed on the front lines of the COVID-19 battle.",
            "The state government has further decided to provide Rs 30 lakh cover, in case of death, to the police personnel directly engaged in the fight against the spread of COVID-19.",
            "Haryana To Promote All Students Of Classes 1 To 8 Without Final Exams.",
            "The Haryana government on Wednesday announced various financial benefits, especially to students who have taken education loans and poor people who want to take loans to start their business.",
            "Approximately, 36,000 students will benefit and Rs 40 crore worth benefit shall be extended to them by the state government.The chief minister added that the state government will also ensure a better relationship between banks and people.",
            "Haryana Chief Minister Manohar Lal Khattar today said that the industrial units that would follow the social distancing norms and would carry out their operations with less than 50 percent labour strength, can extend their working hours from 8 to12 hours, provided they shall pay double the salary for overtime to their workers as per Section 59 in The Factories Act, 1948."]
        
        elif state=="Karnataka":
            for region in regional:
                if (region['loc'] == "Karnataka"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=30
            res="karcm.jpg"
            res2="kar.png"
            res3="Chief Minister Mr.Bookanakere Siddalingappa Yediyurappa"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Karnataka CM announces Rs 3,000 each to registered construction workers.",
            "To support large industries to overcome lockdown difficulties we have decided that payment of fixed charges in electricity bills of large industries will be deferred without penalty and interest for two months,CM said",
            "A further Rs 162 crore financial package mainly aimed at vegetable and fruit growers apart from handloom workers in the state.",
            "The Karnataka government on Tuesday, June 2, announced Rs 5 lakh compensation for the kin of Umesh Hadagali, an ambulance driver who died due to a heart attack on duty on May 27 in Konnur in Gadag district.",
            "Under the Rs 1610 crore relief package, farmers cultivating flowers, who incurred crop losses due to lack of demand during the lockdown period, will be paid compensation of Rs 25,000 per hectare with a cap of one hectare. A separate relief package will be announced for farmers who grew fruits and vegetables and faced crop loss due to shortage in demand and inability to transport produce.",
            "While around 10 lakh maize farmers will get Rs 5,000 each, the Accredited Social Health Activists (ASHA) workers would get an incentive of Rs 3,000 each through cooperative institutions, Chief Minister B S Yediyurappa said.",
            "Karnataka CM  on Monday said that the state has restricted the entry of persons from four states till May 31.Visitors from Gujarat, Maharashtra, Kerala, and Tamil Nadu will not be allowed in Karnataka during the period."]

        elif state=="Punjab":
            for region in regional:
                if (region['loc'] == "Punjab"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=22
            res="puncm.jpg"
            res2="pun.jpg"
            res3="Chief Minister Mr.Amarinder Singh"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Punjab sanctions Rs 20 crore for free food, medicines to poor from CM Relief Fund.",
            "The state government had announced a relief of Rs 3,000 each for all registered construction workers in the state. A total of Rs 96 crore was earmarked for this purpose.",
            "Punjab CM announces the constitution of SIT to probe illicit liquor sale during Covid-19 lockdown.",
            "Punjab cm announces relaxation in fixed electricity charges,along with deferment of the deadline to pay bills.",
            "Wearing mask/cloth in public is made mandatory.",]

        elif state=="Telangana":
            for region in regional:
                if (region['loc'] == "Telangana"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=31
            res="telacm.jpg"
            res2="tela.png"
            res3="Chief Minister Mr.K. Chandrashekar Rao"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Telangana Chief Minister K Chandrashekhar Rao on Sunday said that the migrants in Telangana will get financial assistance of Rs 500 and 12-kilogram rice or wheat flour amid nationwide lockdown",
            "All migrants from other states will be treated as our own natives. They must be treated like our children. They are 'Telangana State's Development Partners'. The majority of migrants are in Rangareddy, Medchal, and Hyderabad. All the migrants in the state will be given Rs 500, 12-kilogram rice or wheat flour/per head. Orders are already given to collector, Rao said.",
            "Telangana government would credit around 7.4 million bank accounts with Rs 1,500 as support for the needy during the coronavirus-induced lockdown.",
            "Telangana CM K Chandrashekhar Rao says no need to worry but be cautious about coronavirus.",
            "Rao declared that in case of an increase in the positive cases, the medical and health departments were ready to offer medical services to the needy.",
            "The government is ready to provide treatment to any number of cases in the State. The required PPE Kits, test Kits, Masks, beds, ventilators, hospitals are all ready,” Rao said.",
            "The state has enough stock of essentials and medicines.",
            "Telangana govt makes wearing masks mandatory while stepping out."]

        elif state=="Kerala":
            for region in regional:
                if (region['loc'] == "Telangana"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=14
            res="kercm.jpg"
            res2="kerela.png"
            res3="Chief Minister Mr.Pinarayi Vijayan"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Kerala government announces Rs 20,000-crore package to tackle health crisis.",
            "The package includes Rs 500 crore for health initiatives, and Rs 2,000 crore for loans and free ration.",
            "Without differentiating families based on Below Poverty Line and Above Poverty Line cards, everyone will be given free rice, the chief minister added. APL [ABove Poverty Line] families will be given a total of 10 kg cereals. For this Rs 100 crore has been allotted.",
            "Loans worth Rs 2,000 crore would be disbursed to families in need through the all-women network of “Kudumbashree” in April and May, he said. Social security pensions that were scheduled to be given in April will be disbursed to 50 lakh people this month itself, he said, adding that this would amount to Rs 1,320 crore. Families that do not receive any social security pension will get Rs 1,000 each, he said, adding that this would cost Rs 1,00 crore.",
            "Vijayan also announced that consumers would get an extra month to clear their water and electricity bills, and that movie theatres would get a waiver of the entertainment tax.",
            "“Fitness fee for autorickshaws will be relaxed,” Vijayan added. “Stage carriage and contract carriage in buses will be tax-deductible. Stage carriers will be given a one-month exemption for three months tax.”",
            "The chief minister added that a string of 1,000 low-cost food outlets will be opened in April. They will serve meals for Rs 20 instead of Rs 25. “We had to start these food outlets by September, but under the new circumstances, 1,000 food outlets will be started by April itself,” said Vijayan."]


        elif state=="Odisha":
            for region in regional:
                if (region['loc'] == "Odisha"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=30
            res="odicm.jpg"
            res2="odisha.png"
            res3="Chief Minister Mr.Naveen Patnaik"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Odisha announces Rs 2200 crore package for poor to sail through lockdown.",
            "Patnaik said that the package will benefit about 1.64 crore people of the state out of the total population of 4.5 crore.",
            "The Chief Minister said all the 94 lakh poor families covered under the food security scheme will get financial assistance of Rs 1,000 each for which Rs 932 crore will be spent.",
            "The state government has also started providing foodgrains for three months to all the beneficiaries, he added.",
            "The state government is also providing advance social security pension for four months to 48 lakh beneficiaries. The state will bear an expenditure of around Rs 932 crore towards this measure, cm said.",
            "22 lakh construction workers will get Rs 1,500 each for the losses incurred due to the lockdown, cm said and added that Rs 932 crore will be spent for this.",
            "Odisha announces Rs 100 crore employment programme for 4.5 lakh urban poor families."]
        elif state=="Assam":
            for region in regional:
                if (region['loc'] == "Assam"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=33
            res="asscm.jpg"
            res2="ass.png"
            res3="Chief Minister Mr.Sarbananda Sonowal"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Assam announces COVID-19 package, tea gardens, agri-farms exempted from lockdown.",
            "Under the package, one-time assistance of Rs 1,000 will be provided to construction workers and those not covered under the National Food Security Act. From April 1, 58 lakh families under the NFSA will receive free rice, an official release said.",
            "From April 1, the Assam government allowed repairing and construction of embankments in view of the coming monsoon season, the release said.",
            "Under the package, 100 families in villages of 5,000 people, 150 families in areas of 5,000-10,000 people and 200 families in a place with a population of over 10,000 will also get Rs 1,000",
            "The government decided to give the cash assistance to 250 families of each ward of the Guwahati Municipal Corporation and 100 families of each ward of other municipal bodies in the state, the release stated.",
            "The Assam government on Monday decided to provide financial assistance to those people from the state stranded in other areas due to the nationwide lockdown, Finance and Health minister Himanta Biswa Sarma said.",
            "The state government had earlier announced financial assistance to cancer, kidney, heart and liver transplant patients from Assam who went for treatment outside the state and got stranded."]

        elif state=="Uttarakhand":
            for region in regional:
                if (region['loc'] == "Uttarakhand"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=13
            res="uttrcm.jpg"
            res2="uttr.png"
            res3="Chief Minister Mr.Trivendra Singh Rawat"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Chief Minister Trivendra Singh announced the lockdown till March end but assured the people that essential services would be available.",
            "Uttarakhand government to provide Rs 500 for poor to buy sanitisers, masks.Over 3 lakh daily wagers and labourers will get Rs 500 each to buy sanitisers and masks in Uttarakhand",
            "“All registered labourers in our state will be given Rs1000 in their accounts so that they do not have any problem in procuring food grains. I want to assure them that no one will go hungry in the state and the government will make all arrangements,” said CM Rawat.",
            "Amid the COVID-19 pandemic, Uttarakhand Chief Minister Trivendra Singh Rawat ,announced Rs 1 lakh assistance for kin of people who lost their lives due to the deadly virus in the state.",
            "Uttarakhand CM Trivendra Singh Rawat, on Wednesday, announced that all COVID-19 doctors and medical professionals will be provided life insurance by govt.",
            "Chief Minister Trivendra Singh Rawat has announced that Anganwadi and Asha Karkatri workers would, each, be given an honorarium of Rs 1000.",
            "He also said that category four employees were cooperating but the government decided not to deduct their salaries on humanitarian grounds."]
        
        elif state=="Manipur":
            for region in regional:
                if (region['loc'] == "Manipur"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=16
            res="mancm.jpg"
            res2="man.png"
            res3="Chief Minister Mr.N Biren Singh"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Manipur chief minister has asked his counterparts in other states to take care of the 30,000 Manipuri people who are stranded outside the state because of the lockdown.",
            "Manipur Chief Minister Nongthombam Biren Singh tweeted, “We are helping our people who are stranded and stuck outside the state due to the Covid-19 pandemic. Upto now, 3,771 stranded people outside the state have been provided Rs 2000 each. We will provide the same to the remaining 10,000-12,000 persons within 2-3 days.",
            "The chief minister had requested Prime Minister Narendra Modi to take action against racial slurs and harassment that people of the Northeastern region are facing in different parts of the country, amid the coronavirus crisis. He also appealed to other chief ministers to take care of the 30,000 Manipuri people who are stranded outside the state because of the lockdown.",
            "Meanwhile, Principal Secretary and current resident commissioner in New Delhi, PK Singh, distributed dry ration to students and other Manipuris stranded in the national capital. A total of about 700 students and other stranded Manipuris in Delhi-NCR have received packets containing pulses, potatoes, cooking oil, masks and sanitisers. Singh said that all items were being sourced through voluntary contributions.",
            "Although the coronavirus crisis has posed varied challenges for different communities, Manipur certainly offers significant takeaways that could be useful in the achievement of long term development goals."]

        elif state=="ArunachalPradesh":
            for region in regional:
                if (region['loc'] == "Arunachal Pradesh"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=22
            res="aruncm.jpg"
            res2="arun.png"
            res3="Chief Minister Mr.Pema Khandu"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Chief Minister Pema Khandu has welcomed the center’s announcement of Rs 1.7 lakh crore relief package aimed at providing a safety net to those hit the hardest by the Covid-19 lockdown.",
            "44660 beneficiaries under Ujjawala yojana will be getting free cooking gas (LPG) cylinders in next three months in the state.",
            "65000 farmers from the state shall receive Rs. 1000 as the first instalment of our top up amount announced in the budget in addition to the incentive of the centre for Rs. 2000.",
            "Health workers to get medical insurance cover of Rs. 50 lakh.",
            "2771 Self Help Groups of the state would reap the benefit of Collateral-free loan which has been doubled to Rs. 20 lakh.",
            "48912 beneficiaries consisting of Senior Citizens, Poor Widows and Poor disabled of the state would get the benefit of ex-gratia of Rs. 1000 per month for three months.",
            "Meanwhile, in a major decision, the state government shall provide Rs. 1000/- each to all the BPL families as one time assistance to cope up during this trying times. It shall cover 1,77,213 families and cost the state exchequer at Rs. 177213000 Cr.",
            "Another important announcement was to provide assistance to the families whose livelihood has been seriously affected due to the lockdown. DCs have been directed to identify these vulnerable population and provide assistance in form of either Ration or Cash."]

        elif state=="Nagaland":
            for region in regional:
                if (region['loc'] == "Nagaland"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=12
            res="nagacm.jpg"
            res2="naga.png"
            res3="Chief Minister Mr.Neiphiu Rio"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Nagaland government to give Rs 10,000 to stranded persons opting not to return at present.",
            "The state government has decided to prioritise the return of stranded elderly persons and patients who had gone outside the state for treatment.",
            "Additional Chief Secretary Sentiynager Imchen, convener of Empowered Group on COVID-19, said it has been decided that those returning from red zones will be screened at Dimapur or Kohima and placed under 14 days institutional quarantine.",
            "Meghalaya and Nagaland announced on Sunday that the existing restrictions would continue for the next round of lockdown beginning from Monday in the fight against Covid-19.",
            "The Nagaland government will provide immediate cash assistance to the citizens stranded outside the state owing to Covid-19.",
            "Chief minister Neiphiu Rio said a patient will be given cash assistance of Rs 20,000, a professional or working person will get Rs 4,000 while a student will receive Rs 3,000.",
            "The Chief Minister’s Relief Fund (CMRF) received a little over 2.95 crore as donations till date, according to the chief minister’s website.",
            "Out of this, Rs 2.32 crore has been disbursed as financial assistance to various entities."]

        elif state=="Meghalaya":
            for region in regional:
                if (region['loc'] == "Meghalaya"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths']
                    d=11
            res="meghcm.jpg"
            res2="megh.png"
            res3="Chief Minister Mr.Conrad Sangma"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Meghalaya CM Conrad Sangma observing home quarantine on return from Manipur.",
            "Thma U Rangli Juki and Workers’ Power of Meghalaya have urged the Meghalaya chief minister Conrad K Sangma to financially support the working classes of the state so that they can adopt ‘social distancing’.",
            "To ensure that everyone, including the poor, can adopt ‘social distancing’ as called by the government to prevent the spread of coronavirus, the two organizations in a letter to the Meghalaya chief minister have made several other suggestions.",
            "The organizations said, “Livelihoods lost through lockdowns should be compensated both for the urban unorganized sector and rural farming sector through cash transfers based on official minimum wage or a minimum income support.”",
            "“For the period of lockdown and for any respiratory tract infections or suspected novel coronavirus symptoms, the hospitalization or OPD charges and testing should be free,” the letter stated.",
            "“As a movement and organization of working classes in Meghalaya, we would like to offer our active support in fighting this pandemic by sharing scientifically accurate information and helping with structures which are put in place to encourage social distancing as well as proper personal hygiene practices,” the letter further said.",
            "“Anyone found discriminating against infected patients should be punished. Any organization encouraging meetings and assemblies should be actively discouraged,” the two organizations said."]

        elif state=="Tripura":
            for region in regional:
                if (region['loc'] == "Tripura"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths'] 
                    d=8
            res="tripura.jpg"
            res2="tripura.png"
            res3="Chief Minister Mr.Biplab Kumar Deb"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Tripura government will provide Rs 1,000 as financial assistance to 50,000 families.",
            "Mowever, Tripura government will also provide Rs 10 Lakh in case of death of any frontline worker during fight against COVID-19.",
            "In view of the increasing COVID-19 cases, the State Government came up with several welfare plans.",
            "Deb announced that 50,000 poor APL families, who got free ration, would now receive one-time assistance of Rs 1000 each.",
            "Tripura government on Wednesday announced that 6.19 lakh poor families in the state would get free ration for one month in view of the COVID-19 situation and the 21-day lockdown. Law Minister Ratan Lal Nath on Wednesday said that the decision to provide provide free ration for one month was taken in a meeting of the state council of ministers.",
            "Students in primary and elementary sections would be given take-home food under the mid day meal scheme, pregnant and lactating mothers would also be given take home food on daily basis. The minister said Rs 75 crore would be used for giving social security pension to all beneficiaries in advance.",
            "The scheme also covers 40,000 construction workers of the state who would get Rs 1,000 for next three months. The money would be credited in their account in DBT mode at a time. Urban homeless and destitute, who were provided cooked meal since last few days, would now be given rice, soyabean, eggs, spices, mustard oil, potatoes, onions as per requirements.",
            "This ration would be given for next seven days to 1,500 beneficiaries across the state. The state government will also provide ration to tea garden workers under the scheme.",
            "Nath said that Tripura has got 57 days buffer stock of rice, 78 days stock for wheat, 29 days sugar stock, 23 days salt stock, 9 days"]
        elif state=="Sikkim":
            for region in regional:
                if (region['loc'] == "Sikkim"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths'] 
                    d=8
            res="sikkim-cm.jpg"
            res2="sikkim.png"
            res3="Chief Minister Mr.Prem Singh Tamang"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["The CM said,The state government has laid highest priority on the overall improvement of healthcare system in the state. The government will make sure that the healthcare workers are not deprived of any necessary equipment or manpower. All gaps would be fulfilled immediately. We have allocated an enhanced budget of Rs 40 crore for the health sector, with an additional Rs 16 crore as buffer fund to meet any exigencies",
            "Sikkim govt. decided to allow construction and farming activities from April 21 to sustain the livelihood of the poor in the state, Chief Minister Prem Singh Tamang said.",
            "Farmers will be required to follow the guidelines on maintaining social distance in their fields, while contractors can resume construction activities by engaging only local labour force, he told reporters.",
            "Inter-state movement of vehicles was restricted to vehicles transporting essential goods.  These vehicles need to have a permanent pass for such movement.  On April 5, intra-state movement of vehicles was restricted to government officials, transportation of essential commodities, banks and PSUs, and media and cable networks.   Their passes are valid only from 8am to 5pm.",
            "On March 25, the state prohibited the sale of hand sanitisers without drug manufacturing licence label.  It also prohibited sale of N95 masks to general public without valid prescription. ",
            " On March 27, an economic relief package was announced by the state government.   This included free ration in specific quantities (other than the PDS entitlement) to needy families in rural and urban areas, daily wagers, migrant labourers, casual workers, and stranded people.  Further, the government announced an additional incentive wage of Rs 300/day for tea workers at Temi-tea estate.",
            "On April 16, the government announced that Asha workers will be given Rs 5,000 as honorarium for work done during COVID-19.  Further, it ordered the food and civil supply department to compile a list of all the left out beneficiaries for distribution of food relief packages.",
            "On April 16, the government announced that a financial relief of Rs 30,000 will be provided to each patient undergoing treatment and stranded outside Sikkim from the Chief Minister's relief fund."]
        elif state=="Jammu&Kashmir":
            for region in regional:
                if (region['loc'] == "Jammu&Kashmir"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths'] 
                    d=8
            res="j&k.jpg"
            res2="j&k.png"
            res3="Chief Minister Ms. Mehbooba Mufti"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["The Jammu and Kashmir government on Tuesday announced that close 94,000 stranded Jammu and Kashmir residents have been evacuated from other parts of the country to date.",
            "J-K Govt has evacuated more than 94000 stranded Jk residents to date, 67172 brought back via Lakhanpur; 26797 through 33 COVID specials. Rajdhani & Shramik special trains, 652 passengers brought back under Vande Bharat Mission through 4 special. flights,said the Department of Information and Public Relations, Jammu and Kashmir in a tweet.",
            "As per union Ministry of Health and Family Welfare, Jammu and Kashmir have a total of 1,668 COVID-19 cases of which 809 patients have recovered from the disease in the Union Territory while 23 have been reported due to the highly contagious virus.",
            "Since the past two and a half weeks, Jammu and Kashmir has been witnessing a steady rise in COVID-19 deaths, with more fatalities being reported in this period than the first three months of the pandemic.",
            "On March 25, the state prohibited the sale of hand sanitisers without drug manufacturing licence label.  It also prohibited sale of N95 masks to general public without valid prescription. ",
            " Till June 17, in the first three months of the virus outbreak, only 64 people had died in J&K with or of COVID-19, according to official records. But then, 67 Covid-19 patients have died in the two weeks since June 18,  taking the death toll in J&K to 127.",
            "Health authorities insist that the majority of the people who died in the first three months of the virus outbreak, had multiple underlying co-morbidities before contracting getting infected. However, among the dead, there were 13 patients between the age group of 18 to 45 years and a 15-day-old baby.",
            ]
        elif state=="Puducherry":
            for region in regional:
                if (region['loc'] == "Puducherry"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths'] 
                    d=8
            res="pudu-cm.jpg"
            res2="pudu.jpg"
            res3="Chief Minister Mr.  V Narayanasamy"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["Puducherry Chief Minister V Narayanasamy announced on Friday he would contribute every month 30 per cent of the pension amount he was receiving for having served as an MP.",
            "Puducherry Chief Minister V Narayanasamy on Wednesday alleged that despite several requests to the Centre for funds to tackle the current situation arising out of the COVID-19 pandemic, the union territory has received no aid.",
            "Talking to reporters here, he claimed that the NDA government has allocated money to a number of states to meet the exigencies but the Puducherry government's pleas have gone unheeded.",
            "He said Puducherry was at the crossroads with the Centre not extending a helping hand and the union territory also not able to mobilise funds from its own sources.",
            "Puducherry Chief Minister V Narayanasamy on Saturday urged the Union government to provide relief to the poor for a second time to enable them tide over the difficulties arising out of the COVID-19 lockdown.",
            "The Chief Minister’s relief fund received over Rs 7 crore which is being utilized by the health department to strengthen infrastructure to fight the spread of COVID-19, said Narayanasamy. He also urged the people to donate liberally to the fund.",
            ]
        elif state=="Ladakh":
            for region in regional:
                if (region['loc'] == "Ladakh"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths'] 
                    d=8
            res="ladakh-cm.jpg"
            res2="ladakh.jpg"
            res3="Chief Minister Jamyang Tsering Namgyal "
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["In view of the rapid rise in coronavirus positive cases in the Union Territory of Ladakh over the past two days, the UT administration has decided to enhance the testing capacity of the recently established COVID-19 testing laboratory—bio-safety level 2 (BSL-2) and ramped up the testing of suspected patients.",
            "Ladakh MP Jamyang Tsering Namgyal has sought the Centre's help for sufficient and fair distribution of groceries and financial assistance to the poor in the Union territory during the nationwide lockdown imposed amid the coronavirus pandemic.",
            "Appreciating the collective performance of the administration of Ladakh and district administrations of Leh and Kargil in containing the spread of COVID-19 in the Union territory without any loss of life.",
            "On 21 June, when people rolled out their mats to mark International Yoga Day, Ladakh’s capital Leh woke up to an eerie silence — the result of its first Sunday curfew, imposed due to the rising cases of the novel coronavirus. ",
            "Shops remained shut and all passenger and commercial vehicular movement were barred throughout the day. The only disruptions were the Indian Air Force’s sorties, tearing across Leh’s skies every few minutes. ",
            "On the road, Indian Army’s trucks and buses moved men and equipment around the town as check posts at every 20 metres ensured no civilian vehicular movement.",
            ]
        elif state=="Lakshadweep":
            for region in regional:
                if (region['loc'] == "Lakshadweep"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths'] 
                    d=8
            res="Lakshadweep-cm.jpg"
            res2="Lakshadweep.png"
            res3="Shri. Dineshwar Sharma"
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["The Union Territory imposed a partial lockdown on March 22 and a complete lockdown on March 25.",
            "We have a very few policemen and few officers of the Indian Reserve Battalion. They are struggling to keep a check on the spread of the disease as many people are not strictly following the lockdown rules,said Dr Muneer.",
            "Lakshdweep is the only island which has remained free of the disease which has affected over 1.3 lakh people in India and more than five million globally.",
            "The beautiful archipelago consisting of 36 islands has a population of about 64,000 people. The union territory is located off the coast of Kerala and depends on the southern state for much of its needs.",
            "As India overtook Russia and became the nation with the third most number of COVID-19 cases, Lakshadweep, the archipelago of 36 islands, seems to have cracked the code to tackle the virus, at least for now. The islands, the country’s smallest Union Territory with a population of about 64,000 and lying about 380 km off Kochi, has the rare distinction of becoming the only region under the Indian jurisdiction where not even a single case of COVID-19 has been reported till now. ",
            "On the road, Indian Army’s trucks and buses moved men and equipment around the town as check posts at every 20 metres ensured no civilian vehicular movement.",
            ]
        elif state=="Ladakh":
            for region in regional:
                if (region['loc'] == "Ladakh"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths'] 
                    d=8
            res="ladakh-cm.jpg"
            res2="ladakh.jpg"
            res3="Chief Minister Jamyang Tsering Namgyal "
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["In view of the rapid rise in coronavirus positive cases in the Union Territory of Ladakh over the past two days, the UT administration has decided to enhance the testing capacity of the recently established COVID-19 testing laboratory—bio-safety level 2 (BSL-2) and ramped up the testing of suspected patients.",
            "Ladakh MP Jamyang Tsering Namgyal has sought the Centre's help for sufficient and fair distribution of groceries and financial assistance to the poor in the Union territory during the nationwide lockdown imposed amid the coronavirus pandemic.",
            "Appreciating the collective performance of the administration of Ladakh and district administrations of Leh and Kargil in containing the spread of COVID-19 in the Union territory without any loss of life.",
            "On 21 June, when people rolled out their mats to mark International Yoga Day, Ladakh’s capital Leh woke up to an eerie silence — the result of its first Sunday curfew, imposed due to the rising cases of the novel coronavirus. ",
            "Shops remained shut and all passenger and commercial vehicular movement were barred throughout the day. The only disruptions were the Indian Air Force’s sorties, tearing across Leh’s skies every few minutes. ",
            "On the road, Indian Army’s trucks and buses moved men and equipment around the town as check posts at every 20 metres ensured no civilian vehicular movement.",
            ]
        elif state=="Andaman&Nicobar":
            for region in regional:
                if (region['loc'] == "Andaman&Nicobar"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths'] 
                    d=8
            res="Andaman&Nicobar-cm.jpg"
            res2="Andaman&Nicobar.png"
            res3="Manohar Parrikar "
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["The Andaman & Nicobar administration has shut all travel and tourism related activities in the union territory starting Monday till March 26.",
            "The Andaman and Nicobar Islands Administration informed that out of new cases, two are contacts of earlier positive cases and one is a traveller from another state.",
            "A total of 119 COVID-19 cases have been reported in the UT so far, including 65 active cases and 54 recoveries.",
            "Out of the total number of people quarantined, 1,500 went to the Andamans for a visit in the last few weeks. ",
            "Nearly 1,800 people in Andaman and Nicobar Islands were quarantined, including 75 passengers of two flights that had carried nine people who tested positive for the coronavirus, NDTV reported on Tuesday. The nine patients had been a part of the religious gathering in Delhi’s Nizamuddin area where several Covid-19 cases may have originated. ",
            "On the road, Indian Army’s trucks and buses moved men and equipment around the town as check posts at every 20 metres ensured no civilian vehicular movement.",
            ]
        elif state=="Daman&Diu":
            for region in regional:
                if (region['loc'] == "Daman&Diu"):
                    a=region['confirmedCasesIndian']
                    b=region['discharged']
                    c=region['deaths'] 
                    d=8
            res="Daman&Diu-cm.jpg"
            res2="Daman&Diu.jpg"
            res3="Manohar Parrikar "
            res4=["https://www.mohfw.gov.in/pdf/GuidelinesfornotifyingCOVID-19affectedpersonsbyPrivateInstitutions.pdf",
    "https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf",
    "https://www.who.int/docs/default-source/wrindia/situation-report/india-situation-report-8.pdf?sfvrsn=cd671813_2"]
            res5=["The Daman and Diu districts of the Union Territory of Dadra and Nagar Haveli have not reported any COVID-19 case so far, and the administration has attributed this to strict implementation of the lockdown orders and commitment of 'corona warriors'.",
            "There are nearly 2.5 lakh industrial workers in Daman and Diu, which are also quite popular among tourists, the Union Territory's administrator Praful Patel said on Sunday.",
            "Despite bordering Gujarat and being close to Maharashtra, two of the worst affected states, Daman and Diu have remained free of the viral disease so far because public followed the lockdown.",
            "While Dadra and Nagar Haveli has reported 19 COVID-19 cases, there has been no case so far in Daman and Diu.",
            "We have managed to achieve this success because our 'corona warriors' worked with full commitment. We succeeded in making people adhere to the lockdown for 75 days. We managed to have zero cases in Daman and Diu because people followed the lockdown with full commitment",
            "However, authorities remain alert as the Union Territory lies close to Gujarat and Maharashtra.",
            ]





        Res={'picture':res,'state':res2,'name':res3,'pdf':res4,'news':res5}
        
        return render_template('examples/map.html',a=a,b=b,c=c,d=d, inf=Res, regional=json.loads(response.text)['data']['regional'],rg=json.loads(k.text)['data']['contacts']['regional'], hs=json.loads(r.text)['data']['regional'],news=json.loads(r2.text)['articles'],overall=json.loads(response.text)['data']['summary'])
    return render_template('examples/map.html',a=a,b=b,c=c,d=d,inf=Res,regional=json.loads(response.text)['data']['regional'],rg=json.loads(k.text)['data']['contacts']['regional'], hs=json.loads(r.text)['data']['regional'],news=json.loads(r2.text)['articles'],overall=json.loads(response.text)['data']['summary'])



@app.route('/abc.html',methods=['GET', 'POST'])
@cache.cached(timeout=120)
def create_figure():
    ConfirmedCases_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    Deaths_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    Recoveries_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    def cleandata(df_raw):
        df_cleaned=df_raw.melt(id_vars=['Province/State','Country/Region','Lat','Long'],value_name='Cases',var_name='Date')
        df_cleaned=df_cleaned.set_index(['Country/Region','Province/State','Date'])
        return df_cleaned 
# Clean all datasets
    ConfirmedCases=cleandata(ConfirmedCases_raw)
    Deaths=cleandata(Deaths_raw)
    Recoveries=cleandata(Recoveries_raw)

    ### Get Countrywise Data
    def countrydata(df_cleaned,oldname,newname):
        df_country=df_cleaned.groupby(['Country/Region','Date'])['Cases'].sum().reset_index()
        df_country=df_country.set_index(['Country/Region','Date'])
        df_country.index=df_country.index.set_levels([df_country.index.levels[0], pd.to_datetime(df_country.index.levels[1])])
        df_country=df_country.sort_values(['Country/Region','Date'],ascending=True)
        df_country=df_country.rename(columns={oldname:newname})
        return df_country
  
    ConfirmedCasesCountry=countrydata(ConfirmedCases,'Cases','Total Confirmed Cases')
    DeathsCountry=countrydata(Deaths,'Cases','Total Deaths')
    RecoveriesCountry=countrydata(Recoveries,'Cases','Total Recoveries')

### Get DailyData from Cumulative sum
    def dailydata(dfcountry,oldname,newname):
        dfcountrydaily=dfcountry.groupby(level=0).diff().fillna(0)
        dfcountrydaily=dfcountrydaily.rename(columns={oldname:newname})
        return dfcountrydaily

    NewCasesCountry=dailydata(ConfirmedCasesCountry,'Total Confirmed Cases','Daily New Cases')
    NewDeathsCountry=dailydata(DeathsCountry,'Total Deaths','Daily New Deaths')
    NewRecoveriesCountry=dailydata(RecoveriesCountry,'Total Recoveries','Daily New Recoveries')


    CountryConsolidated=pd.merge(ConfirmedCasesCountry,NewCasesCountry,how='left',left_index=True,right_index=True)
    CountryConsolidated=pd.merge(CountryConsolidated,NewDeathsCountry,how='left',left_index=True,right_index=True)
    CountryConsolidated=pd.merge(CountryConsolidated,DeathsCountry,how='left',left_index=True,right_index=True)
    CountryConsolidated=pd.merge(CountryConsolidated,RecoveriesCountry,how='left',left_index=True,right_index=True)
    CountryConsolidated=pd.merge(CountryConsolidated,NewRecoveriesCountry,how='left',left_index=True,right_index=True)
    CountryConsolidated['Active Cases']=CountryConsolidated['Total Confirmed Cases']-CountryConsolidated['Total Deaths']-CountryConsolidated['Total Recoveries']
    CountryConsolidated['Share of Recoveries - Closed Cases']=np.round(CountryConsolidated['Total Recoveries']/(CountryConsolidated['Total Recoveries']+CountryConsolidated['Total Deaths']),2)
    CountryConsolidated['Death to Cases Ratio']=np.round(CountryConsolidated['Total Deaths']/CountryConsolidated['Total Confirmed Cases'],3)
    TotalCasesCountry=CountryConsolidated.max(level=0)['Total Confirmed Cases'].reset_index().set_index('Country/Region')
    TotalCasesCountry=TotalCasesCountry.sort_values(by='Total Confirmed Cases',ascending=False)
    TotalCasesCountryexclChina=TotalCasesCountry[~TotalCasesCountry.index.isin(['Mainland China','Others'])]
    Top10countriesbycasesexclChina=TotalCasesCountryexclChina.head(10)
    TotalCasesCountrytop10=TotalCasesCountry.head(10)
    fig = go.Figure(go.Bar(x=Top10countriesbycasesexclChina.index, y=Top10countriesbycasesexclChina['Total Confirmed Cases'],
                        text=Top10countriesbycasesexclChina['Total Confirmed Cases'],
                textposition='outside'))
    fig.update_layout(title_text='Top 10 Countries by Total Confirmed Cases')
    fig.update_yaxes(showticklabels=False)
    
    py.offline.plot(fig, filename='templates/abc.html',auto_open=False)
    return render_template('abc.html')
     
# @app.route('/map.html')
# def mp():



@app.route('/plot2.html',methods=['GET', 'POST'])
@cache.cached(timeout=120)
def create_figure2():
    ConfirmedCases_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    Deaths_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    Recoveries_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

    def cleandata(df_raw):
        df_cleaned=df_raw.melt(id_vars=['Province/State','Country/Region','Lat','Long'],value_name='Cases',var_name='Date')
        df_cleaned=df_cleaned.set_index(['Country/Region','Province/State','Date'])
        return df_cleaned 

    # Clean all datasets
    ConfirmedCases=cleandata(ConfirmedCases_raw)
    Deaths=cleandata(Deaths_raw)
    Recoveries=cleandata(Recoveries_raw)


    ### Get Countrywise Data
    def countrydata(df_cleaned,oldname,newname):
        df_country=df_cleaned.groupby(['Country/Region','Date'])['Cases'].sum().reset_index()
        df_country=df_country.set_index(['Country/Region','Date'])
        df_country.index=df_country.index.set_levels([df_country.index.levels[0], pd.to_datetime(df_country.index.levels[1])])
        df_country=df_country.sort_values(['Country/Region','Date'],ascending=True)
        df_country=df_country.rename(columns={oldname:newname})
        return df_country
    
    ConfirmedCasesCountry=countrydata(ConfirmedCases,'Cases','Total Confirmed Cases')
    DeathsCountry=countrydata(Deaths,'Cases','Total Deaths')
    RecoveriesCountry=countrydata(Recoveries,'Cases','Total Recoveries')

    ### Get DailyData from Cumulative sum
    def dailydata(dfcountry,oldname,newname):
        dfcountrydaily=dfcountry.groupby(level=0).diff().fillna(0)
        dfcountrydaily=dfcountrydaily.rename(columns={oldname:newname})
        return dfcountrydaily

    NewCasesCountry=dailydata(ConfirmedCasesCountry,'Total Confirmed Cases','Daily New Cases')
    NewDeathsCountry=dailydata(DeathsCountry,'Total Deaths','Daily New Deaths')
    NewRecoveriesCountry=dailydata(RecoveriesCountry,'Total Recoveries','Daily New Recoveries')

    CountryConsolidated=pd.merge(ConfirmedCasesCountry,NewCasesCountry,how='left',left_index=True,right_index=True)
    CountryConsolidated=pd.merge(CountryConsolidated,NewDeathsCountry,how='left',left_index=True,right_index=True)
    CountryConsolidated=pd.merge(CountryConsolidated,DeathsCountry,how='left',left_index=True,right_index=True)
    CountryConsolidated=pd.merge(CountryConsolidated,RecoveriesCountry,how='left',left_index=True,right_index=True)
    CountryConsolidated=pd.merge(CountryConsolidated,NewRecoveriesCountry,how='left',left_index=True,right_index=True)
    CountryConsolidated['Active Cases']=CountryConsolidated['Total Confirmed Cases']-CountryConsolidated['Total Deaths']-CountryConsolidated['Total Recoveries']
    CountryConsolidated['Share of Recoveries - Closed Cases']=np.round(CountryConsolidated['Total Recoveries']/(CountryConsolidated['Total Recoveries']+CountryConsolidated['Total Deaths']),2)
    CountryConsolidated['Death to Cases Ratio']=np.round(CountryConsolidated['Total Deaths']/CountryConsolidated['Total Confirmed Cases'],3)


    ## Get totals for all metrics
    GlobalTotals=CountryConsolidated.reset_index().groupby('Date').sum()
    GlobalTotals['Share of Recoveries - Closed Cases']=np.round(GlobalTotals['Total Recoveries']/(GlobalTotals['Total Recoveries']+GlobalTotals['Total Deaths']),2)
    GlobalTotals['Death to Cases Ratio']=np.round(GlobalTotals['Total Deaths']/GlobalTotals['Total Confirmed Cases'],3)
    GlobalTotals.tail(2)

    # Create Plots that show Key Metrics For the Covid-19
    chartcol='red'
    fig = make_subplots(rows=3, cols=2,shared_xaxes=True,
                        specs=[[{}, {}],[{},{}],
                        [{"colspan": 2}, None]],
                        subplot_titles=('Confirmed Cases','Active Cases','Deaths','Recoveries','Death to Cases Ratio'))
    fig.add_trace(go.Scatter(x=GlobalTotals.index,y=GlobalTotals['Total Confirmed Cases'],
                            mode='lines+markers',
                            name='Confirmed Cases',
                            line=dict(color=chartcol,width=2)),
                            row=1,col=1)
    fig.add_trace(go.Scatter(x=GlobalTotals.index,y=GlobalTotals['Active Cases'],
                            mode='lines+markers',
                            name='Active Cases',
                            line=dict(color=chartcol,width=2)),
                            row=1,col=2)
    fig.add_trace(go.Scatter(x=GlobalTotals.index,y=GlobalTotals['Total Deaths'],
                            mode='lines+markers',
                            name='Deaths',
                            line=dict(color=chartcol,width=2)),
                            row=2,col=1)
    fig.add_trace(go.Scatter(x=GlobalTotals.index,y=GlobalTotals['Total Recoveries'],
                            mode='lines+markers',
                            name='Recoveries',
                            line=dict(color=chartcol,width=2)),
                            row=2,col=2)
    fig.add_trace(go.Scatter(x=GlobalTotals.index,y=GlobalTotals['Death to Cases Ratio'],
                            mode='lines+markers',
                            line=dict(color=chartcol,width=2)),
                            row=3,col=1)
    fig.update_layout(showlegend=False)
    fig.update_layout(title_text='Global Statistics')

    py.offline.plot(fig, filename='templates/plot2.html',auto_open=False)
    return render_template('plot2.html')

@app.route('/team')
@cache.cached(timeout=50)
def team():
    return render_template('team/team.html')

@app.route('/faq')
@cache.cached(timeout=50)
def faq():
    return render_template('examples/upgrade.html')


@app.route('/facts')
@cache.cached(timeout=50)
def facts():
    return render_template('examples/facts.html')


    
if __name__ == '__main__':
    
    app.jinja_env.auto_reload = True
    app.run(debug=False,threaded =True)
