from django.shortcuts import render, redirect
from random import randint




# Create your views here.
def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'message' not in request.session:
		request.session['message'] = [("woke up", "green")]
	return render(request, "ninja_gold/index.html")

def process(request):
	activity = {
		"farm": [10,20],
		"cave": [5,10],
		"house": [2,5],
		"casino":[-50,50]
	}
	if request.method == 'POST':
		actParams = activity[request.POST['action']]
		goldEarned = randint(actParams[0],actParams[1])
		if goldEarned >= 0: 
			status = "green"
			report = "You earned {} gold at the {}".format(goldEarned, request.POST['action'])
		else:
			status = "red"
			report = "You lost {} gold at the {}".format(goldEarned, request.POST['action'])


		request.session['gold'] += goldEarned
		request.session['message'].insert(0,(report, status))
	return redirect('/')
