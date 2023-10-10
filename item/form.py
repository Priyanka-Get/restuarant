from django import forms
from .models import items


class itemform(forms.ModelForm):


    class Meta:
       model = items
       fields ='__all__'
       labels={
        
        'Item_id':'id',
        'Item_name':'item_name',
        'Quantity':'Quantity',
        'Price':'Price',
        


       }

    def _init_(self,*args,**kwargs):
        super(itemform,self)._init_(*args,**kwargs)
       
        self.fields['Quantity'].required=False