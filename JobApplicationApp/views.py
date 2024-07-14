from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
import json
from django.http import JsonResponse
from . import forms
from .models import User, BasicDetails, LanguagesKnown, TechnologiesKnown, EducationDetails, WorkExperienceDetails, References, Preferences, City, State
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def register_user(request):
    context = {
        "form": forms.RegistrationForm
    }
    return render(request, "registration.html", context)


def add_user(request):
    form = forms.RegistrationForm(request.POST)
    if form.is_valid():
        register = User(username=form.cleaned_data['username'], first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'], phone_number=form.cleaned_data["phone_number"], email=form.cleaned_data["email"])
        register.set_password(form.cleaned_data["password"])
        register.save()
        messages.add_message(request, messages.SUCCESS,
                             "Signed In Successfully!")
        return redirect("login_page")
    else:
        return render(request, "registration.html", {'form': form})


def login_page(request):
    context = {
        'form': forms.LoginForm
    }
    return render(request, "login.html", context)


def user_login(request):
    print(request.POST)
    if request.method == 'POST':
        details = forms.RegistrationForm(request.POST)
        user = authenticate(
            request, username=request.POST['username'], password=request.POST["password"])
        request.session['username'] = str(user)
        if user is not None:
            return redirect("home")
    return redirect("login_page")

    # return redirect("register_user")


def get_data_user(request, user):
    basicformset = BasicDetails.objects.filter(user_id=user.id)
    datasets = []
    dbtbl = (EducationDetails, WorkExperienceDetails, LanguagesKnown,
             TechnologiesKnown, References, Preferences)
    nameset = ("education", "workExperience", "languages",
               "technologies", "references", "preferences")
    for basic in basicformset:
        temp = {}
        cnt = 0
        temp["basic"] = basic
        for tbl in dbtbl:
            objset = tbl.objects.filter(form_id=basic.id).values()
            temp[nameset[cnt]] = objset
            cnt += 1

        datasets.append(temp)
    return datasets


def detailedview(request, id):
    suser = request.session["username"]
    # user = User.objects.filter(username = suser).first()
    basicobj = BasicDetails.objects.filter(id=id).values()
    dbtbl = (EducationDetails, WorkExperienceDetails, LanguagesKnown,
             TechnologiesKnown, References, Preferences)
    nameset = ("education", "Work Experience", "languages",
               "technologies", "references", "preferences")
    dataset = {"basic": basicobj}
    cnt = 0

    for tbl in dbtbl:
        objset = tbl.objects.filter(form_id=id)
        dataset[nameset[cnt]] = objset.values()
        cnt += 1

    print(dataset["basic"][0]["first_name"])
    context = {
        "user": suser,
        "data": dataset
    }
    # print(dataset)
    return render(request, "detailedview.html", context)


def home(request):
    suser = request.session["username"]
    user = User.objects.filter(username=suser).first()
    basicdata = BasicDetails.objects.filter(user_id=user.id)
    p = Paginator(basicdata, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(10)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {
        "username": suser,
        # "formrow": basicdata,
        "pageobj": page_obj
    }
    return render(request, "home.html", context)


def super_rendering_function(req, conkey, convalue, rfilename):
    context = {
        conkey: convalue
    }
    return render(req, rfilename, context)


def basic(request):
    return super_rendering_function(request, "basic", forms.BasicModelFrom, "basic.html")


def education(request):
    # eduset = forms.EducationSet(queryset=EducationDetails.objects.none(), prefix="eduset")
    return super_rendering_function(request, "education", forms.EducationForm, "education.html")


def workexprience(request):
    workset = forms.WorkExperienceFrom
    return super_rendering_function(request, "exprience", workset, "exprience.html")


def languages(request):
    langaugeset = forms.languageFormSet(
        queryset=LanguagesKnown.objects.none(), prefix="language")
    return super_rendering_function(request, "language", langaugeset, "language.html")


def technology(request):
    technologyset = forms.technologyFormSet(
        queryset=TechnologiesKnown.objects.none(), prefix="techonologies")
    return super_rendering_function(request, "technology", technologyset, "technology.html")


def reference(request):
    referenceset = forms.referenceformSet(
        queryset=References.objects.none(), prefix="references")
    return super_rendering_function(request, "reference", referenceset, "reference.html")


def preference(request):
    return super_rendering_function(request, "preference", forms.PrefrencesForm, "preference.html")


# submitting the form data into the models


# super parent functions 
def basic_super(req, post_form):
    if post_form.is_valid():
        data_seriel = {}

        for data in post_form.cleaned_data:
            if data == "birth_date":
                birth_date = str(post_form.cleaned_data[data])
                data_seriel[data] = birth_date
            else:
                data_seriel[data] = post_form.cleaned_data[data]

        req.session["basic_details"] = data_seriel
        print(req.session["basic_details"], "basic super")
        # print("basic ", dict(postForm.data))
        return True

    else:
        return False


# educational updates
def education_super(request, post_form):
    if post_form.is_valid():
        print(post_form.data)
        sessionedulist = []
        newdatadict = dict(post_form.data)
        for i in range(len(newdatadict["education_authority"])):
            ndict = {}
            for k, v in newdatadict.items():
                if "csrfmiddlewaretoken" == k or "next" == k:
                    continue
                else:
                    ndict[k] = v[i]

            sessionedulist.append(ndict)

        request.session["education"] = sessionedulist
        print(request.session["education"], "education super")
        return True
    else:
        return False


# workexperience updates
def workexperience_super(request, post_form):
    if post_form.is_valid():
        print("Sp")
        sessionexplist = []
        newdatadict = dict(post_form.data)
        for i in range(len(newdatadict["company"])):
            ndict = {}
            for k, v in newdatadict.items():
                if "csrfmiddlewaretoken" == k or "next" == k:
                    continue
                else:
                    ndict[k] = v[i]

            sessionexplist.append(ndict)
        request.session["workexprience"] = sessionexplist
        print(request.session["workexprience"], "work super")
        return True
    else:
        return False


# for reference 
def references_super(request, post_form):
    if post_form.is_valid():
        data_seriel = []
        for data in post_form.cleaned_data:
            data_seriel.append(data)

        request.session["references"] = data_seriel
        print(request.session["references"], "references")
        return True
    else:
        return False


# basic details 
def basic_submit(request):
    form = forms.BasicModelFrom(request.POST)
    if basic_super(request, form):
        if "education" in request.session and len(request.session["education"]): 
            data = request.session["education"]
            context = {"education": data, "backid": True}
            return render(request, "education.html", context)
        else:
            return redirect("education")
    else:
        return render(request, "basic.html", {'basic': form})


def education_submit(request):
    form = forms.EducationForm(request.POST)
    if education_super(request, form):
        if "workexprience" in request.session and len(request.session["workexprience"]): 
            data = request.session["workexprience"]
            context = {"exprience": data, "backid": True}
            return render(request, "exprience.html", context)
        else:
            return redirect("workexprience")
    else:
        return render(request, "education.html", {'education': form})
    

def workexprience_submit(request):
    form = forms.WorkExperienceFrom(request.POST)
    if workexperience_super(request, form):
        if "language" in request.session and len(request.session["language"]): 
            data = request.session["language"]
            context = {"language": data, "backid": True}
            return render(request, "language.html", context)
        else:
            return redirect("languages")
    else:
        return render(request, "education.html", {'education': form})
    

def languages_submit(request):
    form = forms.languageFormSet(request.POST, prefix="language")
    if form.is_valid():
        request.session["language"] = form.cleaned_data
        print(request.session["language"], "language")

    if "technology" in request.session and len(request.session["technology"]): 
        # request.session["language"] = form.data
        data = request.session["technology"]
        context = {"technology": data, "backid": True}
        return render(request, "technology.html", context)
    
    return redirect("technology")


def techonology_submit(request):
    form = forms.technologyFormSet(request.POST, prefix="techonologies")
    if form.is_valid():
        request.session["technology"] = form.cleaned_data
        print(request.session["technology"], "technology")
        
    if "references" in request.session and len(request.session["references"]):     
        data = request.session["references"]
        context = {"reference": data, "backid":True}
        return render(request, "reference.html", context)
        # return super_rendering_function(request, "references", forms.RefrenceForm(initial=data), "reference.html")
    return redirect("reference")


def reference_submit(request):
    form = forms.referenceformSet(request.POST, prefix="references")
    if "references" in request.session and len(request.session["references"]): 
        sessionexplist = [] 
        newdatadict = dict(form.data)
        for i in range(len(newdatadict["rname"])):
            ndict = {}
            for k, v in newdatadict.items():
                if "csrfmiddlewaretoken" == k or "next" == k:
                    continue
                else:
                    ndict[k] = v[i]

            sessionexplist.append(ndict)
        request.session["references"] = sessionexplist
        return redirect("preference")
    
    if references_super(request, form):
        return redirect("preference")
    else:
        return render(request, "reference.html", {"reference": form})


def preference_submit(request):
    form = forms.PrefrencesForm(request.POST)
    # print("preference ", form.data, form.is_valid())
    try:
        if form.is_valid():
            request.session["preference"] = form.cleaned_data

            # printing the session data
            print("basic details", request.session["basic_details"])
            print("education", request.session["education"])
            print("workexprience", request.session["workexprience"])
            print("language", request.session["language"])
            print("technology", request.session["technology"])
            print("references", request.session["references"])
            print("preference ss", request.session["preference"])

            # add the data into the database
            basic = request.session["basic_details"]
            edusetli = request.session["education"]
            workli = request.session["workexprience"]
            langli = request.session["language"]
            techli = request.session["technology"]
            refli = request.session["references"]
            pref = request.session["preference"]

            # getting the username from session to filter the id
            susername = request.session["username"]
            userobj = User.objects.filter(username=susername).first()

            # making entry of data one by one   
            basicdb = BasicDetails(user_id=userobj, first_name=basic["first_name"], last_name=basic["last_name"], designation=basic["designation"], email=basic["email"], gender=basic["gender"],
                                   birth_date=basic["birth_date"], relationship=basic["relationship"], city=basic["city"],  address1=basic["address1"], address2=basic["address2"], zipcode=basic["zipcode"], state=basic["state"])
            basicdb.save()

            # for eduset in edusetli:
            for eduset in edusetli:
                educadb = EducationDetails(form_id=basicdb,  education_authority=eduset["education_authority"], course=eduset[
                                           "course"], passing_year=eduset["passing_year"], percentage=eduset["percentage"])
                educadb.save()

            for work in workli:
                workedb = WorkExperienceDetails(
                    form_id=basicdb, company=work["company"], desingnation=work["desingnation"], from_year=work["from_year"], to_year=work["to_year"])
                workedb.save()

            for lang in langli:
                langudb = LanguagesKnown(
                    form_id=basicdb, langauage=lang["langauage"], isread=lang["isread"], isspeak=lang["isspeak"], iswrite=lang["iswrite"])
                langudb.save()

            for tech in techli:
                techndb = TechnologiesKnown(
                    form_id=basicdb, technology=tech["technology"], status=tech["status"])
                techndb.save()

            for ref in refli:
                referdb = References(
                    form_id=basicdb, rname=ref["rname"], rphone_number=ref["rphone_number"], relation=ref["relation"])
                referdb.save()

            prefedb = Preferences(form_id=basicdb, pref_location=pref["pref_location"], notice_period=pref["notice_period"],
                                  department=pref["department"], expected_ctc=pref["expected_ctc"], actual_ctc=pref["actual_ctc"])
            prefedb.save()

            sessionvar = ("basic_details", "education", "workexprience",
                          "language", "technology", "references", "preference")
            for sess in sessionvar:
                del request.session[sess]

            return redirect("home")

        else:
            return render(request, "preference.html", {"preference": form})
    except Exception as e:

        print(f"Something wrong while submiting the form\n Exeption: {e}")
        return render(request, "preference.html", {"preference": form})


# updating the form

# updating the basic details
def basic_update(request, userid, id):
    user = User.objects.filter(id=userid)
    basic = BasicDetails.objects.get(id=id)
    context = { "basic": forms.BasicModelFrom(instance = basic), "updateid": basic.id}
    return render(request, "basic.html", context)

def basic_update_data(request, id):
    form = forms.BasicModelFrom(request.POST)
    if basic_super(request, form):
        return redirect(f"/educationupdate/{id}")
    else:
        return render(request, "basic.html", {'basic': form})


# updating the educatiion details
def education_update(request, id):
    edu = EducationDetails.objects.filter(form_id=id)
    # context2 = { "education": forms.EducationForm(instance = edu), "updateid": id}
    context = {"education": edu, "updateid": id}
    return render(request, "education.html", context)

def education_update_data(request, id):
    form = forms.EducationForm(request.POST)
    if education_super(request, form):
        return redirect(f"/exprienceupdate/{id}")
    else:
        return render(request, "education.html", {'education': form})

def exprience_update(request, id):
    exp = WorkExperienceDetails.objects.filter(form_id = id)
    # context = { "exprience": forms.WorkExperienceFrom(instance = exp), "updateid": id}
    context = { "exprience": exp, "updateid": id}
    return render(request, "exprience.html", context)

def exprience_update_data(request, id):
    form = forms.WorkExperienceFrom(request.POST)
    if workexperience_super(request, form):
        return redirect(f"/langaugeupdate/{id}")
    else:
        return render(request, "education.html", {'education': form})

def langauge_update(request, id):
    lang = LanguagesKnown.objects.filter(form_id = id)
    context = { "language": lang, "updateid": id}
    return render(request, "language.html", context)

def langauge_update_data(request, id):
    form = forms.languageFormSet(request.POST, prefix="language")
    request.session["language"] = dict(form.data)

    print(request.session["language"], "From Sesson Lang")
    #'id': ['1', '2', '3'], 'language': ['gujarati', 'english', 'hindi'], 'isread': ['on', 'on', 'on'], 'isspeak': ['on', 'on', 'on'], 'iswrite': ['on', 'on', 'on']

    return redirect(f"/technologyupdate/{id}")

def technology_update(request, id):
    tech = TechnologiesKnown.objects.filter(form_id = id)
    # context = { "technology": forms.TechnologyForm(instance = tech), "updateid": id}

    context = { "technology": tech, "updateid": id}
    return render(request, "technology.html", context)


def technology_update_data(request, id):
    form = forms.technologyFormSet(request.POST, prefix="techonologies")
    request.session["technology"] = dict(form.data)
    print(request.session["technology"], "From Sesson tech")
    return redirect(f"/referenceupdate/{id}")

def reference_update(request, id):
    ref = References.objects.filter(form_id = id)
    # context = { "reference": forms.RefrenceForm(instance = ref), "updateid": id}
    context = { "reference": ref, "updateid": id}
    return render(request, "reference.html", context)

def reference_update_data(request, id):
    form = forms.RefrenceForm(request.POST)

    if form.is_valid():
        sessionexplist = []
        newdatadict = dict(form.data)
        for i in range(len(newdatadict["rname"])):
            ndict = {}
            for k, v in newdatadict.items():
                if "csrfmiddlewaretoken" == k or "next" == k:
                    continue
                else:
                    ndict[k] = v[i]

            sessionexplist.append(ndict)
        request.session["references"] = sessionexplist

        print(request.session["references"], "reference data from session")
        return redirect(f"/preferenceupdate/{id}")
    else:
        return render(request, "reference.html", {"reference": form})


def preference_update(request, id):
    pref = Preferences.objects.filter(form_id = id).first()
    context = { "preference": forms.PrefrencesForm(instance = pref), "updateid": id}
    return render(request, "preference.html", context)


def preference_update_data(request, id):
    form = forms.PrefrencesForm(request.POST)
    refli = request.session["references"]
    # print("cleand data prfe", form.data, form.is_valid())
    if form.is_valid():
        print("cleand data prfe", form.cleaned_data)
        request.session["preference"] = form.cleaned_data

        basic = request.session["basic_details"]
        edusetli = request.session["education"]
        workli = request.session["workexprience"]
        langli = request.session["language"]
        techli = request.session["technology"]
        pref = request.session["preference"]

        print("Data from the session prefeces final stage")
        print("basic ", basic)
        print("edu ", edusetli)
        print("work ", workli)
        print("lang ", langli)
        print("tech ", techli)
        print("ref ", refli)
        print("pref ", pref)

        BasicDetails.objects.filter(id=id).update(first_name=basic["first_name"], last_name=basic["last_name"], designation=basic["designation"], email=basic["email"], gender=basic["gender"], birth_date=basic["birth_date"], relationship=basic["relationship"], city=basic["city"],  address1=basic["address1"], address2=basic["address2"], zipcode=basic["zipcode"], state=basic["state"])

        idlistedu = []
        for e in edusetli:
            idlistedu.append(e["id"])

        for eduset in edusetli:
            if eduset["id"] == "newedu":
                newbasic = BasicDetails.objects.filter(id=id).first()
                EducationDetails.objects.create(form_id=newbasic, education_authority=eduset["education_authority"], course=eduset["course"], passing_year=eduset["passing_year"], percentage=eduset["percentage"])
            else:
                dbedu = EducationDetails.objects.filter(form_id = id)
                
                for dbid in dbedu:
                    if str(dbid.id) not in idlistedu:
                        EducationDetails.objects.filter(id=dbid.id).delete()
                        
                EducationDetails.objects.filter(form_id=id, id=eduset["id"]).update(education_authority=eduset["education_authority"], course=eduset["course"], passing_year=eduset["passing_year"], percentage=eduset["percentage"])
            
        idlistwork = []
        for e in workli:
            idlistwork.append(e["id"])

        for work in workli:
            if work["id"] == "newwork":
                newbasic = BasicDetails.objects.filter(id=id).first()
                WorkExperienceDetails.objects.create(form_id=newbasic, company=work["company"], desingnation=work["desingnation"], from_year=work["from_year"], to_year=work["to_year"])
            else:
                dbedu = WorkExperienceDetails.objects.filter(form_id = id)
                for dbid in dbedu:
                    if str(dbid.id) not in idlistwork:
                        WorkExperienceDetails.objects.filter(id=dbid.id).delete()                        
                WorkExperienceDetails.objects.filter(form_id=id, id=work["id"]).update(form_id=id, company=work["company"], desingnation=work["desingnation"], from_year=work["from_year"], to_year=work["to_year"])
        
        for ref in refli:            
            References.objects.filter(form_id=id, id=ref["id"]).update(rname=ref["rname"], rphone_number=ref["rphone_number"], relation=ref["relation"])

        for ti, tech in zip(techli["id"], techli["technology"]):
            TechnologiesKnown.objects.filter(form_id=id, id=ti).update(technology = tech, status = techli[tech][0])
        

        def update_db(lan, alang, ability, lid):
            if lan == alang and ability == "isread":
                LanguagesKnown.objects.filter(form_id=id, id=lid, langauage=lan).update(isread=True)
            if lan == alang and ability == "iswrite":
                LanguagesKnown.objects.filter(form_id=id, id=lid, langauage=lan).update(iswrite=True)
            if lan == alang and ability == "isspeak":
                LanguagesKnown.objects.filter(form_id=id, id=lid, langauage=lan).update(isspeak=True)
        
        for lid in langli["id"]:
            LanguagesKnown.objects.filter(form_id=id, id=lid).update(isspeak=False, iswrite=False, isread=False)
            for key in langli:
                if "_" in key:
                    [ability, lan] = key.split("_")
                    if lan.lower() == "gujarati":
                        update_db(lan, "gujarati", ability, lid)

                    if lan == "english":
                        update_db(lan, "english", ability, lid)

                    if lan == "hindi":
                        update_db(lan, "hindi", ability, lid)
    
        Preferences.objects.filter(form_id=id).update(pref_location=pref["pref_location"], notice_period=pref["notice_period"], department=pref["department"], expected_ctc=pref["expected_ctc"], actual_ctc=pref["actual_ctc"])

        sessionvar = ("basic_details", "education", "workexprience",
                        "language", "technology", "references", "preference")
        for sess in sessionvar:
            del request.session[sess]

    return redirect("home")






# handling the delete operations
def delete(request, userid, id):
    try:
        user = User.objects.filter(id=userid)
        basic = BasicDetails.objects.filter(id=id).first()
        education = EducationDetails.objects.filter(form_id=id).first()
        workexperience = WorkExperienceDetails.objects.filter(form_id=id).first()
        languages = LanguagesKnown.objects.filter(form_id=id).first()
        technologies = TechnologiesKnown.objects.filter(form_id=id).first()
        references = References.objects.filter(form_id=id).first()
        preferences = Preferences.objects.filter(form_id=id).first()
        
        print(basic, education, workexperience, languages, technologies, references, preferences)

        if preferences:
            preferences.delete()

        if references:
            references.delete()

        if education:
            education.delete()

        if workexperience:
            workexperience.delete()

        if technologies: 
            technologies.delete()
        
        if languages:
            languages.delete()

        if basic:
            basic.delete()
        
        print("data deleted successfully!")
        return redirect("home")
    except Exception as e:
        print("error occured while delete: ", e)
        return redirect("home")


def basic_back(request):
    data = request.session["basic_details"]
    return super_rendering_function(request, "basic", forms.BasicModelFrom(initial=data), "basic.html")
    

def education_back(request):
    data = request.session["education"]
    context = {"education": data, "backid": 1}
    return render(request, "education.html", context)
    

def exprience_back(request):
    data = request.session["workexprience"]
    context = { "exprience": data, "backid":1 }
    return render(request, "exprience.html", context)
    

def langauge_back(request):
    data = request.session["language"]
    context = { "language": data, "backid":1 }
    return render(request, "language.html", context)
    # return super_rendering_function(request, "language", forms.LanguagesForm(initial=data), "language.html")
    

def technology_back(request):
    data = request.session["technology"]
    context = { "technology": data, "backid":1 }
    return render(request, "technology.html", context)
    # return super_rendering_function(request, "technology", forms.TechnologyForm(initial=data), "technology.html")

def reference_back(request):
    data = request.session["references"]
    context = {"reference": data, "backid":True}
    return render(request, "reference.html", context)
    # return super_rendering_function(request, "references", forms.RefrenceForm(initial=data), "reference.html")
    return redirect("reference")


def state_view(request):
    states = State.objects.all()
    state_choices = [(state.id ,state.name) for state in states]
    return JsonResponse({'state_choices': state_choices})

def get_cities(request):
    state_id = request.GET.get('state_id') 
    cities = City.objects.filter(state_id=state_id)
    city_choices = [(city.id, city.name) for city in cities]
    return JsonResponse({'city_choices': city_choices})
