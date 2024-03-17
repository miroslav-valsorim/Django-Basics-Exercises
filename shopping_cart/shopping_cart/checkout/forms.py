from django import forms

PAYMENT_CHOICES = (
    ("Stripe", "Stripe"),
    ("PayPal", "PayPal"),
)


class CheckoutForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': "First Name"}
        )
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': "Last Name"}
        )
    )

    street_address = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "Street Address"}
        )
    )
    apartment_address = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': "Apartment"}
        )
    )
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "Country"}
        )
    )
    zip = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "Zip"}
        )
    )

    # payment_option = forms.ChoiceField(
    #     widget=forms.RadioSelect, choices=PAYMENT_CHOICES
    # )

    same_shipping_address = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput
    )
    save_info = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput
    )


# class CheckoutForm(forms.Form):
#     shipping_address = forms.CharField(required=False)
#     shipping_address2 = forms.CharField(required=False)
#     shipping_country = CountryField(blank_label='(select country)').formfield(
#         required=False,
#         widget=CountrySelectWidget(attrs={
#             'class': 'custom-select d-block w-100',
#         }))
#     shipping_zip = forms.CharField(required=False)
#
#     billing_address = forms.CharField(required=False)
#     billing_address2 = forms.CharField(required=False)
#     billing_country = CountryField(blank_label='(select country)').formfield(
#         required=False,
#         widget=CountrySelectWidget(attrs={
#             'class': 'custom-select d-block w-100',
#         }))
#     billing_zip = forms.CharField(required=False)
#
#     same_billing_address = forms.BooleanField(required=False)
#     set_default_shipping = forms.BooleanField(required=False)
#     use_default_shipping = forms.BooleanField(required=False)
#     set_default_billing = forms.BooleanField(required=False)
#     use_default_billing = forms.BooleanField(required=False)
#
#     payment_option = forms.ChoiceField(
#         widget=forms.RadioSelect, choices=PAYMENT_CHOICES)