from django.views import generic


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = ''

    def get_queryset(self):
        return None
