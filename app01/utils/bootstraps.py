from django import forms
class Bootstrap(forms.ModelForm):
    bootstrap_exlude_fields=[]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_exlude_fields:
                continue
            if field.widget.attrs:
                field.widget.attrs = {"class":"form-control","placeholder":field.label}
            field.widget.attrs={"class":"form-control","placeholder":field.label}

