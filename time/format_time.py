#method
#strformat
import time
t=time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t))
print(time.strptime('2020-01-28 08:16:44',"%Y-%m-%d %H:%M:%S"))
'''
%Y-->year's number
%m-->month's number
%B-->month's name
%b-->month's abbreviation
%d-->day's number
%A-->week's name
%a-->week's abbreviation
%H-->24h
%h-->12h
%p-->PM or AM
%M-->min
%S-->second
'''
