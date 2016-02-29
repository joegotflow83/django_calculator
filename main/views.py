from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

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

def exp(x, y):
    return x ** y


class IndexView(View):


    def post(self, request):
        """Calculate the digits entered by user"""
        try:
            left_side = float(request.POST['left_side'])
            right_side = float(request.POST['right_side'])
        except ValueError:
            return render(request, 'main/error.html')
        if request.POST['operator'] == "+":
            total = add(left_side, right_side)
        elif request.POST['operator'] == '-':
            total = sub(left_side, right_side)
        elif request.POST['operator'] == '*':
            total = mul(left_side, right_side)
        elif request.POST['operator'] == '/':
            try:
                total = div(left_side, right_side)
            except ZeroDivisionError:
                return render(request, 'main/fail.html')
        elif request.POST['operator'] == '^':
            total = exp(left_side, right_side)
        return render(request, 'main/index.html', {'total': total})

    def get(self, request):
        """Display the calculater form"""
        form = MathForm
        return render(request, 'main/index.html', {'form': form})
