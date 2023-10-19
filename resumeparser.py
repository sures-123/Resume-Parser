import spacy
from spacy.tokens import DocBin
from  tqdm import tqdm
import json
from typing import Union
from fastapi import FastAPI
nlp=spacy.load("resume parsermy_desired_filename/model-best")
text="""RESUME
		PATEL VIVEK NARSINHBHAI ADDRESS: Akhil Anjana Samaj,
		Nikunj Niwas,
		Madalpur Gam
		Ellise Bridge
		Ahmedabad
		PIN NO: 380006
		PH.NO: (M) 09624234734
		EMAIL ID : viveknp010@gmail.com
		CAREER OBJECTIVE
		To obtain a challenging environment where I can impart my , skills and competencies
		for the growth of an organization.
		SKILL SETS
		Technical Skill: MS Office, Internet.
		Interpersonal Skill: Proactive, Positive attitude, Problem solving, Confident.
		EDUCATIONAL BACKGROUND
		QUALIFICATION SCHOOL/COLLEGE UNI/BOARD YEAR PERCENTAGE
		M.B.A(International
		Business)
		Center For
		Management Studies,
		Ahmedabad
		Ganpat
		University
		2013 5.94 %
		(CGPA)
		M.A(English) H.K.M Arts & P.N
		Patel Commerce
		Collage,Idar(S K)
		North Gujarat
		University,
		Patan
		2011 48.49%
		B. A (English) H.K.M Arts & P.N
		Patel Commerce
		Collage,Idar(S K)
		North Gujarat
		University,
		Patan
		2008 43.66%
		H.S.C Sheth N.L Highshool,
		Laxmipura.
		GSEB 2003 52.67%
		S.S.C Sheth N.L Highshool, GSEB 2001 78.43%
		TRAINING/PROJECT
		(A.
		ORGANIZATION City Tiles Ltd.
		DURATION 57 days.
		PROJECT TITLE Summer Internship Project on“A Case Study: Measuring Customers
		Satisfaction At City Tiles Ltd.”
		TRAINING
		OBJECTIVE
		The objective of this training was to measure customer satisfaction
		toward City Tiles. Problems reorganization and Solution Which were
		Company facing.
		(B.
		ORGANIZATION Duke Plasto International.
		DURATION 30 days.
		PROJECT TITLE “A Project on: Duke Plasto facing problems in international market”
		TRAINING
		OBJECTIVE
		Company was facing problems in international market & how those
		could be solved.
		WORK EXPERIENCE
		 I have been appointed as Sales Executive in Ocean Healthcare, from 23rd August 2013 to
		10th July 2018.
		 I have been appointed as Sales Executive in Reliance Home Finance LTD, from 23rd July
		2018 to till date.
		EXTRACURRICULAM ACTIVITIES
		 I have done industrial visit to “COCA COLA COMPANY”, “KING FISHER LIQUORE
		COMPANY” at BADDI in (HP) in 2012.
		 I have attended the 7nt National-Level Symposium on “Entrepreneurship and Business
		Innovation” held on March 16, 2012.
		PERSONAL DETAILS
		NAME: Vivek Narsinhbhai Patel
		DATE OF BIRTH: 26th August, 1985
		GENDER: Male
		NATIONALITY: Indian.
		LANGUAGES KNOWN: English, Hindi, Guajarati
		I hereby declare that all the information provided by me in this application is factual and correct
		to the best of my  and belief.
		_________________
		[Vivek Patel]
		 I have done industrial visit to “COCA COLA COMPANY”, “KING FISHER LIQUORE COMPANY” at BADDI in (HP) in 2012.
		 I have attended the 7nt National-Level Symposium on “Entrepreneurship and Business Innovation” held on March 16, 2012.
		PERSONAL DETAILS"""
#Print Text Data
doc=nlp(text)
for ent in doc.ents:
  print(ent.label_,":",ent.text)
  #Appending Labels One-By-One:
#res=[]
#for ent in doc.ents: res.append({ent.label_:ent.text}) print(res)
    # Visualize the parse tree
#displacy.render(doc, style='dep', jupyter=True, options={'distance': 90})
# Visualize named entities
#ent_options = {'bg': '#f2f2f2', 'color': '#008000'}  # Using green for named entities
#displacy.render(doc, style='ent', jupyter=True, options=ent_options)
app = FastAPI()
@app.get('/')
def home():
    return {'name':'prasad','city':'newyork'}
