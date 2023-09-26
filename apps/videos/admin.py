from django.contrib import admin
from apps.videos.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('id','categoria')

class especialidadAdmin(admin.ModelAdmin):
    list_display = ('id','especialidad')

class subEspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id','subEspecialidad')

class idiomaAdmin(admin.ModelAdmin):
    list_display = ('id','language')

class tipoVideoAdmin(admin.ModelAdmin):
    list_display = ('id','tipe_video')

admin.site.register(Categoria,categoriaAdmin)
admin.site.register(Idioma,idiomaAdmin)
admin.site.register(tipoVideo,tipoVideoAdmin)
admin.site.register(Video)
admin.site.register(Especialidad,especialidadAdmin)
admin.site.register(subEspecialidad,subEspecialidadAdmin)

