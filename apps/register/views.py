from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from models import User,Movie,Screen,Movie_screenTime

def index(request):
    return render(request, 'register/index.html')

def register(request):
    
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    #enforcing the uniqueness of user name and email.
    if User.objects.filter(user_name = request.POST['user_name']) or User.objects.filter(email = request.POST['email']) :
        return redirect('/')
    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],user_name=request.POST['user_name'] ,
    password=hashed_password, email=request.POST['email'], birthdate = request.POST['birth_date'], user_type = request.POST['user_type'])
    user.save()
    request.session['id'] = user.user_name
    return redirect('/success')

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            request.session['id'] = user.user_name
            if user.user_type == "customer":
                return redirect('/customer')
            else:
                return redirect('/admin')
    return redirect('/error')

def error(request):
    return render(request,'register/error.html')

def success(request):
    user = User.objects.get(user_name=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'register/success.html', context)

def admin(request):
    return render(request,'register/admin.html')

def customer(request):
    return render(request,'register/customer.html')

def screen_success(request):
    screen = Screen.objects.get(screen_number=request.session['id'])
    context = {
        "screen":screen
    }
    return render(request,'register/success_screen.html', context)

def screen_failure(request):
    return render(request,'register/failure_screen.html')

def movie_success(request):
    movie = Movie.objects.get(movie_id=request.session['id'])
    context = {
        "movie":movie
    }
    return render(request,'register/success_movie.html', context)

def movie_failure(request):
    return render(request,'register/failure_movie.html')

def screen_time_success(request):
    movie_st = Movie_screenTime.objects.get(screen_time_id=request.session['id'])
    context = {
        "movie_st":movie_st
    }
    return render(request,'register/success_movie_st.html', context)

def screen_time_failure(request):
    return render(request,'register/failure_movie_st.html')

def add_screen(request):
    errors = screen_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/admin')

    #enforcing the uniqueness of user name and email.
    if Screen.objects.filter(screen_number = request.POST['screen_number']):
        return redirect('/screen_failure') # should redirect here to some failure page.
    screen = Screen.objects.create(screen_number=request.POST['screen_number'], rows=request.POST['rows'],columns=request.POST['columns'])
    request.session['id'] = screen.screen_number
    return redirect('/screen_success')
    return 0

def screen_validator(postData):
    errors = {}
    if (postData['screen_number'].isdigit()):
        sn = int(postData['screen_number'])
        if(sn > 50 or sn <= 0):
            errors['screen_number'] = "should be a Number between 1 and 50"
    else:
        errors['screen_number'] = "Should be a Numeric Value!"

        
    if (postData['rows'].isdigit()):
        sn = int(postData['rows'])
        if(sn > 50 or sn <= 0):
            errors['rows'] = "should be a Number between 1 and 50"
    else:
            errors['rows'] = "Should be a Numeric Value!"

        
    if (postData['columns'].isdigit()):
        sn = int(postData['columns'])
        if(sn > 50 or sn <= 0):
            errors['columns'] = "should be a Number between 1 and 50"
    else:
        errors['columns'] = "Should be a Numeric Value!"
    return errors

def movie_validator(postData):
    errors = {}
    if (postData['movie_name'].isalpha()) == False:
        if len(postData['movie_name']) < 2:
            errors['movie_name'] = "movie name can not be shorter than 2 characters"

    if (postData['genre'].isalpha()) == False:
        if len(postData['genre']) < 2:
            errors['genre'] = "genre can not be shorter than 2 characters"

    if not (postData['movie_id'].isdigit()):
        errors['movie_id'] = "Not A Numeric Value"
    else:
        mi = int(postData['movie_id'])
        if(mi < 0):
            errors['movie_id'] = "A movie can't have a negative id"
        
    if not (postData['duration'].isdigit()):
        errors['duration'] = "Not A Numeric Value"
    else:
        dr = int(postData['duration'])
        if (dr < 30) :
            errors['duration'] = "Not a valid duration. Movie duration should be 30 minutes at least." 

    if not (postData['screen_number'].isdigit()):
        errors['screen_number'] = "Not A Numeric Value"
    return errors
    
def add_movie(request):
    errors = movie_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/admin')

    #enforcing the uniqueness of user name and email.
    if Movie.objects.filter(movie_id = request.POST['movie_id']):
        return redirect('/movie_failure') # should redirect here to some failure page.
    if not Screen.objects.filter(screen_number = request.POST['screen_number']):
        return redirect('/movie_failure') # should redirect here to some failure page.
    
    movie = Movie.objects.create(movie_id=request.POST['movie_id'], genre=request.POST['genre'],movie_name=request.POST['movie_name'], duration= request.POST['duration'],screen_number = request.POST['screen_number'])
    request.session['id'] = movie.movie_id
    return redirect('/movie_success')
    return 0

def screen_time_validator(postData):
    errors = {}
    
    if not (postData['moviee_id'].isdigit()):
        errors['moviee_id'] = "Not A Numeric Value"
        
    if not (postData['screen_time_id'].isdigit()):
        errors['screen_time_id'] = "Not A Numeric Value"
    else:
        dr = int(postData['screen_time_id'])
        if (dr < 0) :
            errors['screen_time_id'] = "Not a valid screen time id." 

    return errors
    
#Assumptions : each screen has only one movie.
def add_screen_time(request):
    errors = screen_time_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/admin')

    #enforcing the uniqueness of user name and email.
    if Movie_screenTime.objects.filter(screen_time_id = request.POST['screen_time_id']):
        return redirect('/screen_time_failure') # should redirect here to some failure page.
    if not Movie.objects.filter(movie_id = request.POST['moviee_id']):
        return redirect('/screen_time_failure') # should redirect here to some failure page.
    
    movie_screen_time = Movie_screenTime.objects.create(moviee_id=request.POST['moviee_id'],screen_time_id = request.POST['screen_time_id'],time=request.POST['screening_time']) 
    request.session['id'] = movie_screen_time.screen_time_id
    return redirect('/screen_time_success')
    return 0

def get_movie(request):
    movies = Movie.objects.filter()
    context ={
        "movies" :movies
    }
    return render(request,"register/view_movies.html",context)

def reserve_seat(request):
    
    mov_st = Movie_screenTime.objects.filter()
    context ={
        "mov_st" :mov_st
    }
    return render(request,"register/reserve_seat.html",context)
def reserve(request):
    screen = Movie_screenTime.objects.filter()
    context ={
        "rows" : screen.rows,
        "columns" : screen.columns
    }
    return render(request,"register/reserve.html",context)

