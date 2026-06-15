from django.contrib import admin
from .models import Darta, DartaDocument, Chalan, ChalanDocument, ActivityLog

admin.site.register(Darta)
admin.site.register(DartaDocument)
admin.site.register(Chalan)
admin.site.register(ChalanDocument)
admin.site.register(ActivityLog)