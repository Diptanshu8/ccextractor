###
#MANDATORY UPDATES IN EVERY PYTHON SCRIPT
###
import ccextractor as cc
import api_support
from multiprocessing import Queue,Process,Event 
import sys
import time

def templer(cb):
    s =  cc.api_init_options()
    cc.check_configuration_file(s)
    for i in sys.argv[1:]:
        cc.api_add_param(s,str(i))
    #very mandatory for keeping a track of pythonapi call. Always must be set.
    c = callback_class()
    cc.my_pythonapi(s,cb )
    #cc.my_pythonapi(s,callback )
    
    compile_ret = cc.compile_params(s,len(sys.argv[1:]));
    
    #very mandatory for keeping a track of pythonapi call. Always must be called so that the program knows that the call is from pythonapi.
    cc.call_from_python_api(s)

    start_ret = cc.api_start(s);

class callback_class(object):
    def callback(self, line, encoding):
        api_support.generate_output_srt(line,str(encoding))
def callback(line, encoding):
    api_support.generate_output_srt(line, str(encoding))
if __name__=="__main__":
    cb = callback_class()
    templer(cb)
