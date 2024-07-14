from django.urls import path
from . import views
urlpatterns = [
    # login
    path("", views.login_page, name="login_page"),
    path("signup/", views.register_user, name="register_user"),
    path("add_user/", views.add_user, name="add_user"),
    path("authenticate/", views.user_login, name="authenticate"),

    # forms
    path("basic/", views.basic, name="basic"),
    path("education/", views.education, name="education"),
    path("workexprience/", views.workexprience, name="workexprience"),
    path("technology/", views.technology, name="technology"),
    path("languages/", views.languages, name="languages"),
    path("reference/", views.reference, name="reference"),
    path("preference/", views.preference, name="preference"),
    
    # form data post function
    path("basicsubmit/", views.basic_submit, name="basicsubmit"),
    path("educationsubmit/", views.education_submit, name="educationsubmit"),
    path("workexpriencesubmit/", views.workexprience_submit, name="workexpriencesubmit"),
    path("techonologysubmit/", views.techonology_submit, name="techonologysubmit"),
    path("languagesubmit/", views.languages_submit, name="languagesubmit"),
    path("referencesubmit/", views.reference_submit, name="referencesubmit"),
    path("preferencesubmit/", views.preference_submit, name="preferencesubmit"),
    
    path('get_states/', views.state_view, name='get_states'),
    path('get_cities/', views.get_cities, name='get_cities'),
    
    # updating the form
    path("basicupdate/<int:userid>/<int:id>", views.basic_update, name="basicupdate"),
    path("educationupdate/<int:id>", views.education_update, name="educationupdate"),
    path("exprienceupdate/<int:id>", views.exprience_update, name="exprienceupdate"),
    path("langaugeupdate/<int:id>", views.langauge_update, name="langaugeupdate"),
    path("technologyupdate/<int:id>", views.technology_update, name="technologyupdate"),
    path("referenceupdate/<int:id>", views.reference_update, name="referenceupdate"),
    path("preferenceupdate/<int:id>", views.preference_update, name="preferenceupdate"),
    
    
 
    # update data funct
    path("basicupdatedata/<int:id>", views.basic_update_data, name="basic_update_data"),
    path("educationupdatedata/<int:id>", views.education_update_data, name="education_update_data"),
    path("exprienceupdatedata/<int:id>", views.exprience_update_data, name="exprienceupdatedata"),
    path("langaugeupdatedata/<int:id>", views.langauge_update_data, name="langaugeupdatedata"),
    path("technologyupdatedata/<int:id>", views.technology_update_data, name="technologyupdatedata"),
    path("referenceupdatedata/<int:id>", views.reference_update_data, name="referenceupdatedata"),
    path("preferenceupdatedata/<int:id>", views.preference_update_data, name="preferenceupdatedata"),
    

    # delete the data
    path("delete/<int:userid>/<int:id>", views.delete, name="delete"),



    # on click of back button
    path("basicback/", views.basic_back, name="basicback"),
    path("educationback/", views.education_back, name="educationback"),
    path("exprienceback/", views.exprience_back, name="exprienceback"),
    path("langaugeback/", views.langauge_back, name="langaugeback"),
    path("technologyback/", views.technology_back, name="technologyback"),
    path("referenceback/", views.reference_back, name="referenceback"),
    # path("preferenceback/", views.preference_back, name="preferenceback"),
 
    # home and navigation
    path("home/", views.home, name="home"),
    path("detailed/<id>", views.detailedview, name="detailed"),
]   
