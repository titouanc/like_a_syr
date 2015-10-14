from django.views.generic.edit import CreateView
from datetimewidget.widgets import DateWidget
from .models import Home


class HomeCreate(CreateView):
    def get_form(self, form_class):
        form = super(HomeCreate, self).get_form(form_class)
        form.fields['dispo_from'].widget = DateWidget(
            attrs=form.fields['dispo_from'].widget.attrs,
            usel10n=True, bootstrap_version=3)
        form.fields['dispo_to'].widget = DateWidget(
            attrs=form.fields['dispo_to'].widget.attrs,
            usel10n=True, bootstrap_version=3)
        return form

    model = Home
    success = "/thx.html"
    fields = (
        'name', 'dispo_from', 'dispo_to',
        'places', 'address', 'phone', 'email',
        'user_prefs')
