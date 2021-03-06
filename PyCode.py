""" Main Code """
import mod
from typing import (
  Any
)
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

 
