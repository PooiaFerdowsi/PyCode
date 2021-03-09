""" Main Code """
import mod
from typing import (
  Any
)
import http.server
""" Create Server """
mod.start().serve_forever() # method caching 

def function(*,func,
             **kwd
            ) -> Any:
   return func
  
function(func=lambda :"HelloWorld!")()
function(func=lambda x,y:x.split("y")(x="Hello , World",y=",")
f = function(func=lambda :"HelloWorld!")
f()
del f

def function(func,
             **kwd
             ,/
            ) -> Any:
   return func()
  
function(lambda :"HelloWorld")
  
def function(*params):
         return type(params) # tuple
         
 def function(**kwd):
         return type(kwd) # dict

 class Handler(http.server.BaseHTTPRequestHandler):
         pass
         
 class UsrErr(BaseException):
         """The UsrErr is normally used in raise"""
         pass
 

         
         
def tuple_args(*args):
         return type(args) # tuple
         
def dict_args(**args):
         return type(args) # dict

#bad comment        
#@Overridde
#bad comment
#good comment
raise UsrErr
# create a new  UsrErr Exception &  The UsrErr Exception is a BaseException child class
#good comment
         
