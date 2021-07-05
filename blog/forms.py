from django import forms 

options = [
    ("entertain", "Entertainment"),
    ("edu", "Education"),
    ("political", "political"),
    ("dance", "Dance"),
    ("music", "Music"),
    ("travel", "Travel"),
    ("fitness", "Fitness"),
    ("sport", "Sport"),
    ("environ", "Environment"),
]

class Addblog(forms.Form):
    title = forms.CharField(max_length=200)
    blog = forms.CharField(widget=forms.Textarea)
    category = forms.CharField(widget=forms.Select(choices=options))


# <select>
#   <option>ENTERTAINMENT</option>