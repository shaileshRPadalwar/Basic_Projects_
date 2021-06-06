from django import forms


class FeedbackForm(forms.Form):
    name=forms.CharField(max_length=40)
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)


    def clean_name(self):
        print("Validating name")
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            print("The minimum number of characters should be 4")
            raise forms.ValidationError("The minimum number of characters of name should be 4")
        return inputname+'SHAILESH'

    #Method1 : clean_fieldname(self)

    def clean_rollno(self):
        #print(self) #self is a object
        inputrollno=self.cleaned_data['rollno']
        if len(str(inputrollno))!=3:
            raise forms.ValidationError("Roll number should be of 3 digits ")
        return inputrollno

    def clean_bot_handler(self):
        inputbot_handler=self.cleaned_data['bot_handler']
        if inputbot_handler!=None:
            raise forms.ValidationError(" Request from BOT cannot be submit ")



class StudentRegistration(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField(label='Roll Number')
    standard=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(label='New Password',widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    def clean(self):
        total_cleaned_data=super().clean()
        print(total_cleaned_data)#dictionary
        inputpassword=total_cleaned_data['password']
        inputrpassword=total_cleaned_data['rpassword']
        inputrollno=total_cleaned_data['rollno']
        inputemail=total_cleaned_data['email']


        l=len(inputemail)
        l1=l-9
        l2=l-4
        gmail=inputemail[l1:l2:]
        print(gmail)
        print(inputemail[l1:l2:])
        if inputpassword!=inputrpassword:
            raise forms.ValidationError("Two passwords are not same")
        if inputrollno<0 or inputrollno>100:
            raise forms.ValidationError('Enter correct roll number')
        if inputemail[l1:l2:]!='gmail':
            raise forms.ValidationError("Enter correct gmail")











