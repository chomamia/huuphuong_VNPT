from dataclasses import field
from email.policy import strict
from operator import xor
from timeit import repeat
from .extension import ma
from marshmallow import Schema, fields
import re

class StaffSchema(ma.Schema):
    class Meta:
        fields = ('user_name', 'email', 'password', 'repeat_password')

class StaffSchemaCategory(ma.Schema):
    class Meta:
        fields = ('name_category', 'category_code', 'parent_category', 'status' )

class StaffSchemagetCategory(ma.Schema):
    class Meta:
        fields = ('name_category', 'category_code', 'time' )

def validate_category(x):
    if not re.search("['~','!','@','#','$','%','^','&','*','(',')','+','-','=','<','>','.','?','/','\',')','(','}','{','.']", x):
        return True
    else:
        return False

def validate_user(x):
    if not re.search("\W", x):
        return True
    else:
        return False

def validate_password(x):
    if (re.search("[a-z]", x) and re.search("[A-Z]", x) and re.search("[0-9]", x)
     and re.search("\W",x)):
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

class CustomerCategory(Schema):
    name_category = fields.Str(required=True, validate = lambda x: (len(x) <=100 and validate_category(x)))
    category_code = fields.Str(required=True, validate = lambda x: (len(x) <=100 and validate_user(x)))
    parent_category = fields.Str()
    status = fields.Str()
