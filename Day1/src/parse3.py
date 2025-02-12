# -*- coding: utf-8 -*-
"""
Created on Wed May 08 16:11:28 2013

@author: kshmirko
"""
import re
from io import StringIO
from ios.readMeteoBlock import readMeteoFile, readMeteoCtx

from datetime import datetime, timedelta

class ParserException(Exception):
    def __init__(self, text):
        super(ParserException, self).__init__(text)

regex = re.compile("(?P<stid>[0-9]+)([a-zA-Z ()]+)(?P<time>[0-9]+\w [0-9]+ \w+ [0-9]+)",re.IGNORECASE|re.UNICODE|re.DOTALL)


def parse_h2(line):
    r = regex.match(line).groupdict()
    
    stid = int(r['stid'])
    date = datetime.strptime(r['time'],'%HZ %d %b %Y')
    return stid, date

def parse_pre1(line):
    sfile = StringIO.StringIO(line)
    meteo = readMeteoFile(sfile)
    return meteo
    
def parse_pre2(line):
    sfile = StringIO.StringIO(line)
    ctx = readMeteoCtx(sfile)    
    return ctx

def parse_h3(line):
    pass
    
def parse_observation(tags):
    tmp = tags.pop()
    if tmp.tag=='h2':
        stid, date = parse_h2(tmp.text)
    else:
        raise ParserException("Can't parse string '%s'\n"%(tmp.text))

    tmp = tags.pop()
    if tmp.tag=='pre':
        meteo = parse_pre1(tmp.text)
    else:
        raise ParserException("Can't parse string '%s'\n"%(tmp.text))
        
    tmp = tags.pop()
    if tmp.tag=='h3':
        parse_h3(tmp.text)
    else:
        raise ParserException("Can't parse string '%s'\n"%(tmp.text))
        
    tmp = tags.pop()
    if tmp.tag=='pre':
        ctx = parse_pre2(tmp.text)
    else:
        raise ParserException("Can't parse string '%s'\n"%(tmp.text))
    
    
    return [stid, date, meteo, ctx]