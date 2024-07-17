# vehiculos/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import VehiculoForm
from .models import Vehiculo, Foto

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculos/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        files = request.FILES.getlist('imagenes')

        if form.is_valid() and files:
            return self.form_valid(form, files)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, files):
        vehiculo = form.save()
        for f in files:
            Foto.objects.create(vehiculo=vehiculo, imagen=f)
        return redirect(self.success_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'vehiculos/vehiculo_list.html'
    context_object_name = 'vehiculos'