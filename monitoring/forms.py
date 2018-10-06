from django import forms

class dataForm(forms.Form):

	# username = forms.CharField(
 #        required = True,
 #        label = 'Username',
 #        max_length = 32,
 #        widget = forms.TextInput(
 #            attrs={
 #            "class": "form-control",
 #            }
 #        )
 #    ) 

	temperature = forms.DecimalField(
        required = True,
        label = 'Temperature',
        widget = forms.NumberInput(
            attrs={
            "class": "form-control",
            }
        )
    )

	moisture = forms.DecimalField(
        required = True,
        label = 'Moisture',
        widget = forms.NumberInput(
            attrs={
            "class": "form-control",
            }
        )
    )
    # moisture = forms.DecimalField(
    #     required = True,
    #     label = 'Moisture',
    #     widget = forms.NumberInput(
    #         attrs={
    #         "class": "form-control",
    #         }
    #     )
    # )
    # temperature = forms.DecimalField(
    #     required = True,
    #     label = 'Temperature',
    #     widget = forms.NumberInput(
    #         attrs={
    #         "class": "form-control",
    #         }
    #     )
    # )