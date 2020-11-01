from django.contrib import admin
from .models import (Hostel,Room,Student,Parents,Visitors,Mess,Fees,Staff)

# Register your models here.
admin.site.register(Hostel)
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Parents)
admin.site.register(Visitors)
admin.site.register(Mess)
admin.site.register(Fees)
admin.site.register(Staff)
