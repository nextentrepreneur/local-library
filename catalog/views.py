from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
# Create your views here.
def index(request):
	"""
	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	num_books=Book.objects.all().count()
	num_instances=BookInstance.objects.all().count()
	#Available books(status='a')
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()
	num_authors=Author.objects.count()	# The 'all()' is implied by default
	# Number of visits to this view, as counted in the session variable.
	num_visits=request.session.get('num_visits',0)
	request.session['num_visits']=num_visits+1
    
    #request.session['num_visits'] = num_visits+1
	# Render the HTML template index.html with the data in the text variable
	return render(
		request,
		'index.html',
		context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_visits':num_visits}, #num_visits appended
		)

# Class based views
from django.views import generic

class BookListView(generic.ListView):
	model = Book
	context_object_name = 'my_book_list' #  your own name for the list as a template variable
	queryset = Book.objects.filter(title__icontains='war')[:1] # Get 1 book that contains 'war' in its title
	template_name = 'books/book_list.html'	# specify your own template name/location
