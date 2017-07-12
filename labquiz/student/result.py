from teacher.models import Exam,Question

def function(count, request, exam):
	quess = Question.objects.filter(exam=exam)
	for i in range(count):
		ques_id = quess[i].id
		name = 'op_' + str(ques_id)
		print ques_id
		responses = request.POST.getlist(ques_id) #this is not returning the values of responses, returning null everytime.
		print responses
		print request.POST
