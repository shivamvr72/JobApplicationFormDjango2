import re
from django import forms
from . import models
from django.forms import modelformset_factory


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'last_name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
        }

    def clean(self):
        super(RegistrationForm, self).clean()
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            self._errors['username'] = self.error_class(
                ['Minimum 5 characters required'])

        email = self.cleaned_data.get('email')
        emailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(emailregex, email):
            self._errors['email'] = self.error_class(['Enter Valid Email'])


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            })
        }


def widget_maker(fieldsArr, widgets):
    # widgets = {}
    for field in fieldsArr:
        widgets[field] = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': f'{field}'
        })


def empty_check(self, field):
    if not field:
        self._errors['first_name'] = self.error_class(['*Required Fields!'])


class BasicModelFrom(forms.ModelForm):
    class Meta:
        rel_status = (
            ("single", "single"),
            ("married", "married"),
        )

        model = models.BasicDetails

        fields = ['first_name', 'last_name', 'designation', 'email', 'gender',
                  'birth_date', 'relationship', 'city', 'address1', 'address2', 'zipcode', 'state']

        widgets = {
            "gender": forms.RadioSelect,
            'birth_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            "relationship": forms.Select(choices=rel_status),
        }

        fieldsetArr = ['first_name', 'last_name', 'designation',
                       'email', 'city', 'address1', 'address2', 'zipcode', 'state']
        widget_maker(fieldsetArr, widgets)

    def clean(self):
        super(BasicModelFrom, self).clean()
        firstname = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        gender = self.cleaned_data.get('gender')
        birth_date = self.cleaned_data.get('birth_date')
        city = self.cleaned_data.get('city')
        address1 = self.cleaned_data.get('address1')
        zipcode = self.cleaned_data.get('zipcode')
        rfield = (firstname, last_name, email, gender,
                  birth_date, city, address1, zipcode)

        for field in rfield:
            empty_check(self, field)

        # zipcode validation india
        zipre = "^[1-9][0-9]{5}$"
        if not re.match(zipre, str(zipcode)):
            self._errors['zipcode'] = self.error_class(
                ['Please Enter Valid Indian Zipcode'])

        # email validation
        emailre = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.match(emailre, str(email)):
            self._errors["email"] = self.error_class(
                ["Please Enter Valid Email"])


class EducationForm(forms.ModelForm):
    class Meta:
        model = models.EducationDetails
        # fields = "__all__"
        fields = [
            "education_authority",
            "course",
            "passing_year",
            "percentage",
        ]

        widgets = {}
        widget_maker(fields, widgets)

    def clean(self):
        super(EducationForm, self).clean()
        education_authority = self.cleaned_data.get("education_authority")
        course = self.cleaned_data.get("course")
        passing_year = self.cleaned_data.get("passing_year")
        percentage = self.cleaned_data.get("percentage")

        fields = (education_authority, course, passing_year, percentage)
        for field in fields:
            empty_check(self, field)


# EducationSet = modelformset_factory(models.EducationDetails, form=EducationForm, extra=4)

class WorkExperienceFrom(forms.ModelForm):
    class Meta:
        model = models.WorkExperienceDetails
        fields = [
            "company",
            "desingnation",
            "from_year",
            "to_year"
        ]
        widgets = {}
        widget_maker(fields, widgets)

    def clean(self):
        super(WorkExperienceFrom, self).clean()
        company = self.cleaned_data.get("company")
        desingnation = self.cleaned_data.get("desingnation")
        to_year = self.cleaned_data.get("to_year")
        from_year = self.cleaned_data.get("from_year")
        fields = (company, desingnation, to_year)
        for field in fields:
            empty_check(self, field)

        # year validation
        yearre = "^[1-2][0-9]{3}$"
        if not re.match(yearre, to_year):
            self._errors['to_year'] = self.error_class(
                ['Enter valid start year'])

        if not re.match(yearre, from_year):
            self._errors['from_year'] = self.error_class(
                ['Enter valid end year'])

# WorkExperienceSet = modelformset_factory(models.WorkExperienceDetails, form=WorkExperienceFrom, extra=2)


class LanguagesForm(forms.ModelForm):
    langauges = (
        ("gujarati", "Gujarati"),
        ("hindi", "Hindi"),
        ("english", "English")
    )

    class Meta:
        model = models.LanguagesKnown
        fields = [
            "langauage",
            "isread",
            "isspeak",
            "iswrite",
        ]
        widgets = {
            "lanugage": forms.CharField(max_length=30),
            "isread": forms.CheckboxInput(),
            "isspeak": forms.CheckboxInput(),
            "iswrite": forms.CheckboxInput()
        }


languageFormSet = modelformset_factory(
    models.LanguagesKnown, form=LanguagesForm, extra=3)


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = models.TechnologiesKnown
        fields = [
            "technology",
            "status"
        ]

        widgets = {
            "status": forms.RadioSelect,
        }


technologyFormSet = modelformset_factory(
    models.TechnologiesKnown, form=TechnologyForm, extra=3)


class RefrenceForm(forms.ModelForm):
    class Meta:
        model = models.References
        fields = [
            "rname",
            "rphone_number",
            "relation"
        ]
        widgets = {}
        widget_maker(fields, widgets)

    def clean(self):
        super(RefrenceForm, self).clean()
        rname = self.cleaned_data.get("rname")
        rphone_number = self.cleaned_data.get("rphone_number")
        relation = self.cleaned_data.get("relation")

        fields = (rname, rphone_number, relation)
        empty_check(self, fields)

        # phonere = "^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$"
        # if not re.match(phonere, str(rphone_number)):
        #     self._errors['from_year'] = self.error_class(['Invalid Phone Number'])


referenceformSet = modelformset_factory(models.References, form=RefrenceForm, extra=2)


class PrefrencesForm(forms.ModelForm):
    class Meta:
        model = models.Preferences
        fields = [
            "pref_location",
            "notice_period",
            "department",
            "expected_ctc",
            "actual_ctc"
        ]

        widgets = {}
        widget_maker(fields, widgets)

    def clean(self):
        super(PrefrencesForm, self).clean()
        pref_location = self.cleaned_data.get("pref_location")
        notice_period = self.cleaned_data.get("notice_period")
        department = self.cleaned_data.get("department")
        expected_ctc = self.cleaned_data.get("expected_ctc")
        actual_ctc = self.cleaned_data.get("actual_ctc")

        fields = (pref_location, notice_period,
                  department, expected_ctc, actual_ctc)
        for field in fields:
            empty_check(self, field)
