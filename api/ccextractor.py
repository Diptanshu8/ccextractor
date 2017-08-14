# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ccextractor')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ccextractor')
    _ccextractor = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ccextractor', [dirname(__file__)])
        except ImportError:
            import _ccextractor
            return _ccextractor
        try:
            _mod = imp.load_module('_ccextractor', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ccextractor = swig_import_helper()
    del swig_import_helper
else:
    import _ccextractor
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def g608_grid_former(line,text,color,font):
    if "text[" in line:
        line = str(line.split(":", 1)[1])
        line = str(line.split("\n")[0])
        text.append(line)
    if "color[" in line:
        line = str(line.split(":", 1)[1])
        line = str(line.split("\n")[0])
        color.append(line)
    if "font[" in line:
        line = str(line.split(":", 1)[1])
        line = str(line.split("\n")[0])
        font.append(line)

def print_g608_grid(case,text,color,font):
    help_string = """
    Case is the value that would give the desired output.
    case = 0 --> print start_time,end_time,text,color,font
    case = 1 --> print start_time,end_time,text
    case = 2 --> print start_time,end_time,color
    case = 3 --> print start_time,end_time,font
    case = 4 --> print start_time,end_time,text,color
    case = 5 --> print start_time,end_time,text,font
    case = 6 --> print start_time,end_time,color,font
    """
    if case==0:
        if text:
            print "\n".join(text)
        if color:
            print "\n".join(color)
        if font:
            print "\n".join(font)

    elif case==1:
        if text:
            print "\n".join(text)
    elif case==2:
        if color:
            print "\n".join(color)
    elif case==3:
        if font:
            print "\n".join(font)
    elif case==4:
        if text:
            print "\n".join(text)
        if color:
            print "\n".join(color)
    elif case==5:
        if text:
            print "\n".join(text)
        if font:
            print "\n".join(font)
    elif case==6:
        if color:
            print "\n".join(color)
        if font:
            print "\n".join(font)
    else:
        print help_string


EXIT_OK = _ccextractor.EXIT_OK
EXIT_NO_INPUT_FILES = _ccextractor.EXIT_NO_INPUT_FILES
EXIT_TOO_MANY_INPUT_FILES = _ccextractor.EXIT_TOO_MANY_INPUT_FILES
EXIT_INCOMPATIBLE_PARAMETERS = _ccextractor.EXIT_INCOMPATIBLE_PARAMETERS
EXIT_UNABLE_TO_DETERMINE_FILE_SIZE = _ccextractor.EXIT_UNABLE_TO_DETERMINE_FILE_SIZE
EXIT_MALFORMED_PARAMETER = _ccextractor.EXIT_MALFORMED_PARAMETER
EXIT_READ_ERROR = _ccextractor.EXIT_READ_ERROR
EXIT_WITH_HELP = _ccextractor.EXIT_WITH_HELP
EXIT_NO_CAPTIONS = _ccextractor.EXIT_NO_CAPTIONS
EXIT_NOT_CLASSIFIED = _ccextractor.EXIT_NOT_CLASSIFIED
EXIT_ERROR_IN_CAPITALIZATION_FILE = _ccextractor.EXIT_ERROR_IN_CAPITALIZATION_FILE
EXIT_BUFFER_FULL = _ccextractor.EXIT_BUFFER_FULL
EXIT_MISSING_ASF_HEADER = _ccextractor.EXIT_MISSING_ASF_HEADER
EXIT_MISSING_RCWT_HEADER = _ccextractor.EXIT_MISSING_RCWT_HEADER
CCX_COMMON_EXIT_FILE_CREATION_FAILED = _ccextractor.CCX_COMMON_EXIT_FILE_CREATION_FAILED
CCX_COMMON_EXIT_UNSUPPORTED = _ccextractor.CCX_COMMON_EXIT_UNSUPPORTED
EXIT_NOT_ENOUGH_MEMORY = _ccextractor.EXIT_NOT_ENOUGH_MEMORY
CCX_COMMON_EXIT_BUG_BUG = _ccextractor.CCX_COMMON_EXIT_BUG_BUG
CCX_OK = _ccextractor.CCX_OK
CCX_FALSE = _ccextractor.CCX_FALSE
CCX_TRUE = _ccextractor.CCX_TRUE
CCX_EAGAIN = _ccextractor.CCX_EAGAIN
CCX_EOF = _ccextractor.CCX_EOF
CCX_EINVAL = _ccextractor.CCX_EINVAL
CCX_ENOSUPP = _ccextractor.CCX_ENOSUPP
CCX_ENOMEM = _ccextractor.CCX_ENOMEM

def fdprintf(fd, fmt):
    return _ccextractor.fdprintf(fd, fmt)
fdprintf = _ccextractor.fdprintf

def millis_to_time(milli, hours, minutes, seconds, ms):
    return _ccextractor.millis_to_time(milli, hours, minutes, seconds, ms)
millis_to_time = _ccextractor.millis_to_time

def freep(arg):
    return _ccextractor.freep(arg)
freep = _ccextractor.freep

def dbg_print(mask, fmt):
    return _ccextractor.dbg_print(mask, fmt)
dbg_print = _ccextractor.dbg_print

def debug_608_to_ASC(ccdata, channel):
    return _ccextractor.debug_608_to_ASC(ccdata, channel)
debug_608_to_ASC = _ccextractor.debug_608_to_ASC

def add_cc_sub_text(sub, str, start_time, end_time, info, mode, arg7):
    return _ccextractor.add_cc_sub_text(sub, str, start_time, end_time, info, mode, arg7)
add_cc_sub_text = _ccextractor.add_cc_sub_text
class python_subs_modified(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, python_subs_modified, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, python_subs_modified, name)
    __repr__ = _swig_repr
    __swig_setmethods__["buffer_count"] = _ccextractor.python_subs_modified_buffer_count_set
    __swig_getmethods__["buffer_count"] = _ccextractor.python_subs_modified_buffer_count_get
    if _newclass:
        buffer_count = _swig_property(_ccextractor.python_subs_modified_buffer_count_get, _ccextractor.python_subs_modified_buffer_count_set)
    __swig_setmethods__["srt_counter"] = _ccextractor.python_subs_modified_srt_counter_set
    __swig_getmethods__["srt_counter"] = _ccextractor.python_subs_modified_srt_counter_get
    if _newclass:
        srt_counter = _swig_property(_ccextractor.python_subs_modified_srt_counter_get, _ccextractor.python_subs_modified_srt_counter_set)
    __swig_setmethods__["start_time"] = _ccextractor.python_subs_modified_start_time_set
    __swig_getmethods__["start_time"] = _ccextractor.python_subs_modified_start_time_get
    if _newclass:
        start_time = _swig_property(_ccextractor.python_subs_modified_start_time_get, _ccextractor.python_subs_modified_start_time_set)
    __swig_setmethods__["end_time"] = _ccextractor.python_subs_modified_end_time_set
    __swig_getmethods__["end_time"] = _ccextractor.python_subs_modified_end_time_get
    if _newclass:
        end_time = _swig_property(_ccextractor.python_subs_modified_end_time_get, _ccextractor.python_subs_modified_end_time_set)
    __swig_setmethods__["buffer"] = _ccextractor.python_subs_modified_buffer_set
    __swig_getmethods__["buffer"] = _ccextractor.python_subs_modified_buffer_get
    if _newclass:
        buffer = _swig_property(_ccextractor.python_subs_modified_buffer_get, _ccextractor.python_subs_modified_buffer_set)
    __swig_setmethods__["g608_grid_color_count"] = _ccextractor.python_subs_modified_g608_grid_color_count_set
    __swig_getmethods__["g608_grid_color_count"] = _ccextractor.python_subs_modified_g608_grid_color_count_get
    if _newclass:
        g608_grid_color_count = _swig_property(_ccextractor.python_subs_modified_g608_grid_color_count_get, _ccextractor.python_subs_modified_g608_grid_color_count_set)
    __swig_setmethods__["g608_grid_color"] = _ccextractor.python_subs_modified_g608_grid_color_set
    __swig_getmethods__["g608_grid_color"] = _ccextractor.python_subs_modified_g608_grid_color_get
    if _newclass:
        g608_grid_color = _swig_property(_ccextractor.python_subs_modified_g608_grid_color_get, _ccextractor.python_subs_modified_g608_grid_color_set)
    __swig_setmethods__["g608_grid_font_count"] = _ccextractor.python_subs_modified_g608_grid_font_count_set
    __swig_getmethods__["g608_grid_font_count"] = _ccextractor.python_subs_modified_g608_grid_font_count_get
    if _newclass:
        g608_grid_font_count = _swig_property(_ccextractor.python_subs_modified_g608_grid_font_count_get, _ccextractor.python_subs_modified_g608_grid_font_count_set)
    __swig_setmethods__["g608_grid_font"] = _ccextractor.python_subs_modified_g608_grid_font_set
    __swig_getmethods__["g608_grid_font"] = _ccextractor.python_subs_modified_g608_grid_font_get
    if _newclass:
        g608_grid_font = _swig_property(_ccextractor.python_subs_modified_g608_grid_font_get, _ccextractor.python_subs_modified_g608_grid_font_set)

    def __init__(self):
        this = _ccextractor.new_python_subs_modified()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ccextractor.delete_python_subs_modified
    __del__ = lambda self: None
python_subs_modified_swigregister = _ccextractor.python_subs_modified_swigregister
python_subs_modified_swigregister(python_subs_modified)
cvar = _ccextractor.cvar

class python_subs_array(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, python_subs_array, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, python_subs_array, name)
    __repr__ = _swig_repr
    __swig_setmethods__["temporary_file"] = _ccextractor.python_subs_array_temporary_file_set
    __swig_getmethods__["temporary_file"] = _ccextractor.python_subs_array_temporary_file_get
    if _newclass:
        temporary_file = _swig_property(_ccextractor.python_subs_array_temporary_file_get, _ccextractor.python_subs_array_temporary_file_set)
    __swig_setmethods__["fp"] = _ccextractor.python_subs_array_fp_set
    __swig_getmethods__["fp"] = _ccextractor.python_subs_array_fp_get
    if _newclass:
        fp = _swig_property(_ccextractor.python_subs_array_fp_get, _ccextractor.python_subs_array_fp_set)
    __swig_setmethods__["output_filename"] = _ccextractor.python_subs_array_output_filename_set
    __swig_getmethods__["output_filename"] = _ccextractor.python_subs_array_output_filename_get
    if _newclass:
        output_filename = _swig_property(_ccextractor.python_subs_array_output_filename_get, _ccextractor.python_subs_array_output_filename_set)
    __swig_setmethods__["has_api_start_exited"] = _ccextractor.python_subs_array_has_api_start_exited_set
    __swig_getmethods__["has_api_start_exited"] = _ccextractor.python_subs_array_has_api_start_exited_get
    if _newclass:
        has_api_start_exited = _swig_property(_ccextractor.python_subs_array_has_api_start_exited_get, _ccextractor.python_subs_array_has_api_start_exited_set)
    __swig_setmethods__["old_sub_count"] = _ccextractor.python_subs_array_old_sub_count_set
    __swig_getmethods__["old_sub_count"] = _ccextractor.python_subs_array_old_sub_count_get
    if _newclass:
        old_sub_count = _swig_property(_ccextractor.python_subs_array_old_sub_count_get, _ccextractor.python_subs_array_old_sub_count_set)
    __swig_setmethods__["sub_count"] = _ccextractor.python_subs_array_sub_count_set
    __swig_getmethods__["sub_count"] = _ccextractor.python_subs_array_sub_count_get
    if _newclass:
        sub_count = _swig_property(_ccextractor.python_subs_array_sub_count_get, _ccextractor.python_subs_array_sub_count_set)
    __swig_setmethods__["subs"] = _ccextractor.python_subs_array_subs_set
    __swig_getmethods__["subs"] = _ccextractor.python_subs_array_subs_get
    if _newclass:
        subs = _swig_property(_ccextractor.python_subs_array_subs_get, _ccextractor.python_subs_array_subs_set)
    __swig_setmethods__["is_transcript"] = _ccextractor.python_subs_array_is_transcript_set
    __swig_getmethods__["is_transcript"] = _ccextractor.python_subs_array_is_transcript_get
    if _newclass:
        is_transcript = _swig_property(_ccextractor.python_subs_array_is_transcript_get, _ccextractor.python_subs_array_is_transcript_set)

    def __init__(self):
        this = _ccextractor.new_python_subs_array()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ccextractor.delete_python_subs_array
    __del__ = lambda self: None
python_subs_array_swigregister = _ccextractor.python_subs_array_swigregister
python_subs_array_swigregister(python_subs_array)


def api_init_options():
    return _ccextractor.api_init_options()
api_init_options = _ccextractor.api_init_options

def check_configuration_file(api_options):
    return _ccextractor.check_configuration_file(api_options)
check_configuration_file = _ccextractor.check_configuration_file

def compile_params(api_options, argc):
    return _ccextractor.compile_params(api_options, argc)
compile_params = _ccextractor.compile_params

def api_add_param(api_options, arg):
    return _ccextractor.api_add_param(api_options, arg)
api_add_param = _ccextractor.api_add_param

def api_start(api_options):
    return _ccextractor.api_start(api_options)
api_start = _ccextractor.api_start

def api_param_count(api_options):
    return _ccextractor.api_param_count(api_options)
api_param_count = _ccextractor.api_param_count

def api_param(api_options, count):
    return _ccextractor.api_param(api_options, count)
api_param = _ccextractor.api_param

def sigterm_handler(sig):
    return _ccextractor.sigterm_handler(sig)
sigterm_handler = _ccextractor.sigterm_handler

def sigint_handler(sig):
    return _ccextractor.sigint_handler(sig)
sigint_handler = _ccextractor.sigint_handler

def print_end_msg():
    return _ccextractor.print_end_msg()
print_end_msg = _ccextractor.print_end_msg

def show_extracted_captions_with_timings():
    return _ccextractor.show_extracted_captions_with_timings()
show_extracted_captions_with_timings = _ccextractor.show_extracted_captions_with_timings

def main(argc, argv):
    return _ccextractor.main(argc, argv)
main = _ccextractor.main

def cc_to_python_get_old_count():
    return _ccextractor.cc_to_python_get_old_count()
cc_to_python_get_old_count = _ccextractor.cc_to_python_get_old_count

def cc_to_python_set_old_count():
    return _ccextractor.cc_to_python_set_old_count()
cc_to_python_set_old_count = _ccextractor.cc_to_python_set_old_count

def cc_to_python_get_number_of_subs():
    return _ccextractor.cc_to_python_get_number_of_subs()
cc_to_python_get_number_of_subs = _ccextractor.cc_to_python_get_number_of_subs

def cc_to_python_get_modified_sub(i):
    return _ccextractor.cc_to_python_get_modified_sub(i)
cc_to_python_get_modified_sub = _ccextractor.cc_to_python_get_modified_sub

def cc_to_python_get_modified_sub_buffer_size(i):
    return _ccextractor.cc_to_python_get_modified_sub_buffer_size(i)
cc_to_python_get_modified_sub_buffer_size = _ccextractor.cc_to_python_get_modified_sub_buffer_size

def cc_to_python_get_modified_sub_buffer(i, j):
    return _ccextractor.cc_to_python_get_modified_sub_buffer(i, j)
cc_to_python_get_modified_sub_buffer = _ccextractor.cc_to_python_get_modified_sub_buffer

def __wrap_write(file_handle, buffer, nbyte):
    return _ccextractor.__wrap_write(file_handle, buffer, nbyte)
__wrap_write = _ccextractor.__wrap_write

def call_from_python_api(api_options):
    return _ccextractor.call_from_python_api(api_options)
call_from_python_api = _ccextractor.call_from_python_api

def set_pythonapi(api_options):
    return _ccextractor.set_pythonapi(api_options)
set_pythonapi = _ccextractor.set_pythonapi

def setautoprogram(api_options):
    return _ccextractor.setautoprogram(api_options)
setautoprogram = _ccextractor.setautoprogram

def setstdout(api_options):
    return _ccextractor.setstdout(api_options)
setstdout = _ccextractor.setstdout

def setpesheader(api_options):
    return _ccextractor.setpesheader(api_options)
setpesheader = _ccextractor.setpesheader

def setdebugdvbsub(api_options):
    return _ccextractor.setdebugdvbsub(api_options)
setdebugdvbsub = _ccextractor.setdebugdvbsub
# This file is compatible with both classic and new-style classes.


