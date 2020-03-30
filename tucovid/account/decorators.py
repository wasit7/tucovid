def is_anonymous(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_anonymous:
            return function(request, *args, **kwargs)

        else:
            return redirect('relation:index')

    return wrap
