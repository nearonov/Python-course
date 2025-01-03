from django import forms
from .models import Course, Product


class CourseForm(forms.ModelForm):
    title = forms.CharField(label="назва курса",
                            max_length=30,
                            initial="Введіть назву курса",
                            )

    # category = forms.ChoiceField(label="категорія курсів",
    #                              choices=((1, 'Programming'),
    #                                       (2, 'Data science'),
    #                                       (3, 'Web designer')))

    class Meta:
        model = Course
        fields = ['title', 'category', 'price', 'foto']


class CourseEdit(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'price']
        labels = {'title': "Змінити назву курса", 'price': 'Ціна'}


class ProductsCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'discount']
        labels = {'name': "Ввести назву подукта",
                  'price': 'Ввести ціну',
                  'discount': 'знижка'
                  }

