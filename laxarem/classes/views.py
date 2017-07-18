from django.shortcuts import render
from django.http import HttpResponse
from classes.models import students
import json
from django.http import JsonResponse
import time
from django.views.decorators.csrf import csrf_exempt
# data = students(studentId=2269)

# Create your views here.
@csrf_exempt
def student(request):
	print('>>>>>>>',request)
	try:
		
		# data = json.loads(d)
		# a = classes.objects.get(id=id)
		if request.method == 'GET':
			return HttpResponse('Nothing to see here!')

		if request.method == 'POST':
			# q=QueryDict(request.POST)
			payload = request.body
			payload_unicode = request.body.decode('utf-8')
			payload_json = json.loads(payload_unicode)
			print('PAYLOAD>>>>',payload_json,'student_ID',payload_json['id'])
			student_id = int(payload_json['id']);
			d = students.objects.get(studentId=student_id).data
			all_students = students.objects.all()
			print(all_students)
			# data= {}
			# for student in all_students:
			# 	data[student.data['className']]=student
			# 	# print(student.data['className'])
			# print(data)

			# print('retrieved:',d,student_id)
			# content = body['content']
			
			return JsonResponse(d)
	except:

		return HttpResponse('Exception!!!')

@csrf_exempt
def allPosts(request):
	print('>>>>>>>',request)
	try:
		
		# data = json.loads(d)
		# a = classes.objects.get(id=id)
		if request.method == 'GET':
			return HttpResponse('Nothing to see here!')

		if request.method == 'POST':
			# q=QueryDict(request.POST)
			d={"0":{"title":'farzan'}}
			print('All posts:');
			return JsonResponse(d)
	except:
		return HttpResponse('Exception!!!')