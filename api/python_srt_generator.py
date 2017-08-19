import ccextractor as cc
import re

def generate_file_handle(filename, mode):
    fh = open(filename,mode)
#    print "Creating output file: ", fh.name
    return fh

def delete_file_handle(fh):
    fh.close()
##
# data would be a dictionary containg the following keys:
# text, color, font
##
def generate_output_srt_time( fh, data):
    data = data.split("-")
    end_time = str(data[-1].split("\n")[0])
    start_time = str(data[1].split("\t")[0])
    fh.write(start_time)
    fh.write(" --> ")
    fh.write(end_time)
    fh.write("\n")
    fh.flush()

"""
            #Handling underline
            buff = ""
            underline_flag = 0
            for i,font_type in enumerate(font_line): 
                if font_type == 'U' and not underline_flag:
                        buff = buff + '<u> '
                        underline_flag = 1
                        underline=1
                elif font_type =="R" and underline_flag: 
                        buff = buff + '</u>'
                        underline_flag = 0
                        continue;
                buff +=  letter[i]
            #adding a new line after buff has seen underline
            #need to cross check with CCExtractor output as to how they are doing
            if underline:
                buff+= "\n"
            else:
                buff=""
"""
color_text={
        "0":"",
        "1":"<font color=\"#00ff00\">",
        "2":"<font color=\"#0000ff\">",
        "3":"<font color=\"#00ffff\">",
        "4":"<font color=\"#ff0000\">",
        "5":"<font color=\"#ffff00\">",
        "6":"<font color=\"#ff00ff\">",
        "7":"<font color=\"",
        "8":"",
        "9":""
};
def comparing__grids(text, font, color):
    temp = []
    for letter,color_line in zip(text,color):
        if "                                " not in letter:
            buff=""
            color_flag = 0
            for i,font_type in enumerate(color_line): 
                if font_type != '9' and not color_flag:
                        buff = buff + color_text[font_type]
                        color_flag = 1
                elif font_type =="9" and color_flag: 
                        buff = buff + '</font>'
                        color_flag = 0
                buff +=  letter[i]
            print buff
"""
    for letter,font_line in zip(text,font):
        if "                                " not in letter:
            buff=""
            underline,italics = 0,0
            #Handling italics
            italics_flag = 0
            for i,font_type in enumerate(font_line): 
                if font_type == 'I' and not italics_flag:
                        buff = buff + '<i>'
                        italics_flag = 1
                elif font_type =="R" and italics_flag: 
                        buff = buff + '</i>'
                        italics_flag = 0
                buff +=  letter[i]
            temp.append(buff)
    return (temp,font, color)
"""

    
def generate_output_srt( fh, d):
    temp = []
    comparing__grids(d['text'],d['font'],d['color'])
    """
    d['text'],d['font'], d['color']= comparing_text_font_grids(d['text'],d['font'], d['color'])
    for item in d['text']:
        if "                                " not in item:
            o = re.sub(r'[\x00-\x1e]',r'',item)
            o = re.sub(r'\x1f[!@#$%^&*()]*', r'', o)
            temp.append(o)
            fh.write(o)
            fh.write("\n")
            fh.flush()
    fh.write("\n")
    """
