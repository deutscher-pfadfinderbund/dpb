from django.views import generic


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = ''

    def get_queryset(self):
        return None

class BundesordnungView(generic.ListView):
    template_name = 'bundesordnung.html'
    context_object_name = ''

    def get_queryset(self):
        return None


class DPBView(generic.ListView):
    template_name = 'dpb.html'
    context_object_name = ''

    def get_queryset(self):
        return None
