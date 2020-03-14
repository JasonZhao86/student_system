from django import forms
from .models import Student


class StudentForm(forms.Form):
    name = forms.CharField(label="姓名", max_length=128)
    sex = forms.ChoiceField(label="性别", choices=Student.SEX_ITEM)
    profession = forms.CharField(label="职业", max_length=128)
    email = forms.EmailField(label="邮箱", max_length=128)
    qq = forms.CharField(label="QQ", max_length=128)
    phone = forms.CharField(label="手机", max_length=128)


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "sex", "profession", "email", "qq", "phone")

    def clean_qq(self):
        qq = self.cleaned_data["qq"]
        if not qq.isdigit():
            raise forms.ValidationError("qq必须为数字")
        return int(qq)


