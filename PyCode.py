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
         
         
# walrus from Russian (:) # The Animal
         
try:
         param = "Hello World If I"
         print(f"Hello {x:=len(param)}")
except:
         import http.server
         class Handlerr(http.server.BaseHTTPRequestHandler):
                def do_get(this):
                    this.send_response(200)
                    this.send_header("Content-type: text/html")
                    this.end_headers()
                    this.wfile.write("<h1> You have a Exception You can not use of walrus in f-str ( formatted string ) </h1>")
        http.server.HTTPServer(("localhost",373),Handlerr);
        exit()
        quit()

def HelloWorld(f): # function is not-std ( Pascal-case )
         return "Hello World"
         
@HelloWorld
def printing():
         return """
         if I don any work !!!!
         I only !!!!
         print 
         "Hello World"::::->()(!!!!
         Good{}
         bye[]
         bytes[];
         *ptr;
         **dptr;
         <Generic>
         (param) -> {code} lambda java
         lambda param:code lambda python
         #include "" import C
         String...name == *param:str # True or 1 or true
         """
         
print(printing())
         # Hello World
         
 
