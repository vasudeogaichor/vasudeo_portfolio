from django.shortcuts import render
import pickle

def password_strength_home(request):
	return render(request, 'password_strength/strength_checker.html')

def password_strength_result(request):
	chars = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 
	'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
	'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
	'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
	'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&',
	'(', ')', '*', '+', '-', '.', '/', ';', '<', '=', '>', '?', '@', '[',
	'\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']

	pw = request.GET.get('password')

	test_array = []

	if ' ' in pw:
		return render(request, 'password_strength/result.html',
		{'password':pw, 'strength':'N/A',
		'message':'Your password should not contain space(s)'})
	elif len(pw) == 0:
		return render(request, 'password_strength/result.html',
		{'password':pw, 'strength':'N/A',
		'message':'Please enter a password!'})
	else:
		for char in chars:
			test_array.append(pw.count(char))
			
		filename = 'password_strength/password_strength_checker.sav'
		model = pickle.load(open(filename, 'rb'))
		
		strength = model.predict([test_array])
		
		result_array = ['Weak','Strong','Very Strong']
		result_class = ['text-warning','text-primary','text-sucess']

		if strength[0] in [0,1]:
			message_ = 'You can do better!'	
		else:
			message_ = ''

		return render(request, 'password_strength/result.html',
			{'password':pw,'strength':result_array[strength[0]],'result_class':result_class,
			'message':message_})
