from django.contrib import admin
from .models import ongoing_task , coffee_recipei , machine_info , machine_log , coffee_logs , machine_tasks
# Register your models here.

admin.site.register(ongoing_task)
admin.site.register(coffee_recipei)
admin.site.register(machine_info)
admin.site.register(machine_log)
admin.site.register(coffee_logs)
admin.site.register(machine_tasks)
