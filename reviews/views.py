from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Review
from .forms import ReviewForm


def reviews(request):
    if request.method == 'POST':
        review = ReviewForm(request.POST)
        if review.is_valid():
            review.save()
            messages.info(request, 'Your review has been submitted.')
            reviews = Review.objects.all()
            return render(request, 'reviews/reviews.html', {'reviews': reviews})
    else:
        reviews = Review.objects.all()
        context = {
            'reviews': reviews,
        }
    return render(request, 'reviews/reviews.html', context)


def add_review(request):
    """ A view to display form for adding new reviews """
    if request.method == 'POST':
        review = ReviewForm(request.POST)
        if review.is_valid():
            review.save()
            messages.info(request, 'Your review has been submitted.')
            reviews = Review.objects.all()
            return render(request, 'reviews/reviews.html', {'reviews': reviews})
    else:
        reviews = Review.objects.all()
        context = {
            'reviews': reviews,
        }
    return render(request, 'reviews/add_review.html', context)
