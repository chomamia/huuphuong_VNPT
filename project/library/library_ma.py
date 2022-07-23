from dataclasses import field
from email.policy import strict
from timeit import repeat
from .extension import ma
from marshmallow import Schema, fields
import re

class StaffSchema(ma.Schema):
    class Meta:
        fields = ('user_name', 'email', 'password', 'repeat_password')

def validate_user(x):
    if not re.search("['~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=','<','>','.','?','/','\',')','(','}','{','.']", x):
        return True
    else:
        return False

def validate_password(x):
    if (re.search("[a-z]", x) and re.search("[A-Z]", x) and re.search("[0-9]", x)
     and re.search("['~','!','@','#','$','%','^','&','*','(',')','_','+','-','=','<','>','.','?','/','\',')','(','}','{']", x)):
        return True
    else:
        return False

class CustomerSchema(Schema):
    user_name = fields.Str(required=True, validate = lambda x: (6<= len(x) <=30 and validate_user(x)))
    password = fields.Str(required=True, validate = lambda x: (8<= len(x) and validate_password(x)))
    repeat_password = fields.Str()
    email = fields.Email()

    class Meta:
        strict = True