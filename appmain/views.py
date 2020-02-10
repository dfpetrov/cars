from django.views.generic import ListView

from .models import Car

class CarList(ListView):
    model = Car

    def get_queryset(self, **kwargs):
        
        from django.db.models import Q
        
        self_request = self.request
        
        qs = []

        if self_request.method == 'GET':
            manufacturer = self_request.GET.get('manufacturer')
            model = self_request.GET.get('model')
            year = self_request.GET.get('year')
            transmission = self_request.GET.get('transmission')

            if manufacturer and model and year and transmission:
                
                from django.db.models import Q

                return Car.objects.filter(Q(manufacturer=manufacturer) & Q(model=model) & Q(year__gte=int(year)) & Q(transmission=transmission))
            
            else:
                return Car.objects.all()