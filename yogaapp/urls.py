from django.urls import path
from . import views
app_name="yogaapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('200HoursYogaTeachersTrainingCourse', views.twohundred, name='200HoursYogaTeachersTrainingCourse'),
    path('300HoursYogaTeachersTrainingCourse', views.threehundred, name='300HoursYogaTeachersTrainingCourse'),
    path('YogaPhilosophyTeachersTraining', views.philosophy, name='YogaPhilosophyTeachersTraining'),
    path('ChakraHealerCourse', views.chakra, name='ChakraHealerCourse'),
    path('AncientCosmicEnergyHealingProcess', views.cosmic, name='AncientCosmicEnergyHealingProcess'),
    path('PrenatalandPostnatalYogaTTC', views.natal, name='PrenatalandPostnatalYogaTTC'),
]

