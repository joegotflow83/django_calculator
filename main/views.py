from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import MathForm


# Helper Functions
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y
def div(x, y):
    return x / y



class IndexView(View):


    def post(self, request):
        """Calculate the digits entered by user"""
        left_side = int(request.POST['left_side'])
        right_side = int(request.POST['right_side'])
        if request.POST['operator'] == "+":
            total = add(left_side, right_side)
        elif request.POST['operator'] == '-':
            total = sub(left_side, right_side)
        elif request.POST['operator'] == '*':
            total = mul(left_side, right_side)
        elif request.POST['operator'] == '/':
            total = div(left_side, right_side)
        print(total)
        return render(request, 'main/index.html', {'total': total})

    def get(self, request):
        """Display the calculater form"""
        form = MathForm
        return render(request, 'main/index.html', {'form': form})
