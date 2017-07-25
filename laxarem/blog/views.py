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
#For user agents:
from ua_parser import user_agent_parser
import pprint
import telegram
try:
	bot = telegram.Bot(token='408944874:AAGCpMHYscl_5QNh8STPzSeS57R51xH7vMY')
	print('BOT:::::',bot.get_me())
except:
	print('Bot not running!')
# Create your views here.
pp = pprint.PrettyPrinter(indent=4)

def hit(request):
	ua_string=request.META.get('HTTP_USER_AGENT',None)
	parsed_ua = user_agent_parser.Parse(ua_string)	
	# print("user>>>>>",parsed_ua['user_agent'])
	# print("string>>>>>",parsed_ua['string'])
	source=request.META.get('REMOTE_ADDR',None)
	
	# parsed_ua[0]['source'].append(source);
	print(source)
	parsed_ua['source']=source
	try:
		bot.send_message(chat_id='-1001103347409', 
			text=pp.pformat(parsed_ua)
			)

	except:
		print('too many messages')
	# print(chat_id)
	# 

@csrf_exempt	
def allTitles(request):
	hit(request);
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
					# print(post.body)

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
@csrf_exempt
def rootHit(request):
	print(">>>>>>>",request.META.get('HTTP_USER_AGENT',None))
	return JsonResponse("{}",safe=False)