from rest_framework import viewsets
from .models import AccessLog
from .serializers import AccessLogSerializer

class AccessLogViewSet(viewsets.ModelViewSet):
    
    serializer_class = AccessLogSerializer

    def get_queryset(self):
        logs = AccessLog.objects.all().order_by('-timestamp')
        
        card_filter = self.request.query_params.get('card_id')
        if card_filter:
            logs = logs.filter(card_id=card_filter)
        
        return logs
