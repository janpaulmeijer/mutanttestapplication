from django import forms

from mutant.forms import FieldDefinitionTypeField
from django.contrib.contenttypes.models import ContentType
from mutant.models.field import FieldDefinition


from testapp.utils import FIELD_TYPES, get_mutant_type


class AddFieldForm(forms.Form):
    field_type = forms.ChoiceField(choices=FIELD_TYPES)

    def clean_field_type(self):
        return int(self.cleaned_data['field_type'])


def get_field_def_form(field_type_pk, model_def_queryset):

    class Meta:
        model = get_mutant_type(field_type_pk)

        fields ='__all__'

        queryset = ContentType.objects.filter(
            **FieldDefinition.subclasses_lookup('pk')
            )

    form_attrs = {

        'Meta': Meta,
        'content_type': FieldDefinitionTypeField(ContentType.objects.filter(**FieldDefinition.subclasses_lookup('pk'))),
        'model_def': forms.ModelChoiceField(queryset=model_def_queryset, widget=forms.HiddenInput)
    }

    return type('FieldDefinitionForm', (forms.ModelForm,), form_attrs)
