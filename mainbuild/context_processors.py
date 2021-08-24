from .forms import RegisterForm


def add_my_register_form(request):
    return {
        'register_form': RegisterForm(),
    }