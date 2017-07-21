from django.shortcuts import render
from django.http import HttpResponse
from blog.models import blog
from blog.models import category
import json
from django.http import JsonResponse
import time
import datetime 
from django.views.decorators.csrf import csrf_exempt
# data = students(studentId=2269)

# Create your views here.
@csrf_exempt
def allTitles(request):
	data={}
	# data = json.loads(d)
	# a = classes.objects.get(id=id)
	if request.method == 'GET':
		return HttpResponse('no blogs to see here!')
	if request.method == 'POST':
		payload = request.body
		payload_unicode = request.body.decode('utf-8')
		payload_json = json.loads(payload_unicode)
		if (payload_json['field'] == 'titles'):

			titles = blog.objects.values_list('id','title','modifiedDate','blogId','category','description')
			categories = category.objects.values_list('id','title','color')
			

			for idx,title in enumerate(titles):
				if title[5]=='':
					post = blog.objects.get(id=title[0])
					print(post.body)

				cat='undefined'
				color = '#000000'
				for _category in enumerate(categories):
					if _category[1][0]==title[4]:
						cat=_category[1][1]
						color=_category[1][2]
						# print(_category)

				data[idx]={"title":title[1],
							"modifiedDate":str(title[2]),
							"id":title[0],
							"category":cat,
							"description":title[5],
							"show":True,
							"color":color
				}
				# print(modifiedDate[idx][1])

			
			jsnData = data
			
		elif (payload_json['field'] == 'post'):

			obj = blog.objects.get(id=payload_json['idx'])
			data={"body":obj.body,
				  "title":obj.title,
				  "background":str(obj.background)}
			print(obj.background)
			jsnData = data
		elif (payload_json['field'] == 'categories'):
			categories = category.objects.values_list('id','title')
			for idx,_category in enumerate(categories):
				data[_category[0]] =_category[1]
			jsnData=json.dumps(data)
		else:
			jsnData = "{}"
		return JsonResponse(jsnData,safe=False)
	print('DONE')

def convertDatetimeToString(o):
	DATE_FORMAT = "%Y-%m-%d" 
	TIME_FORMAT = "%H:%M:%S"

	if isinstance(o, datetime.date):
	    return o.strftime(DATE_FORMAT)
	elif isinstance(o, datetime.time):
	    return o.strftime(TIME_FORMAT)
	elif isinstance(o, datetime.datetime):
	    return o.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))
# Create your views here.
