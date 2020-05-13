from django import forms
from .models import LeaveDate

class LeaveForm(forms.ModelForm):
    
    class Meta:
        model = LeaveDate        
        fields = '__all__'
        labels = {
            'type': 'Leave type',
            'leaveDate': 'Date of leave',
            'leaveEndDate': 'Till date',
            'createTime': 'Create leave date'
        }

    def __init__(self, *args, **kwargs):
        super(LeaveForm, self).__init__(*args, **kwargs)
        self.fields['fullName'].empty_label = "Select"
        self.fields['position'].empty_label = "Select"
        self.fields['description'].empty_label = "Select"
        self.fields['type'].empty_label = "Select"
        
        




    # fullName    
    # position
    # description 
    # type 
    # leaveDate
    # leaveEndDate    
    # createTime