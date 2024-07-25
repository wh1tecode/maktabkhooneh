from django.contrib import messages

def save_errors(request, form):
    try:
        error: dict = form.errors.as_data()
        errors = []
        for ex in error:
            lsd = list(error[ex][0])
            errors += lsd
        error_str = "<br>".join(errors)
        messages.add_message(
                request=request, level=messages.ERROR, message=error_str
            )
    except Exception as ex:
        print(ex)