import re
mo=re.compile(r'''
\d\d\d        #area code(without parens, with dash)
-             #first dash 
\d\d\d        #first 3 digits
-             #second dash
\d\d\d\d      #last 4 digits
\sx\d{2,4}    #extension,like x1234'''   , re.IGNORECASE |re.DOTALL|re.VERBOSE)
print(mo)
mo=re.compile(r'''
\d\d\d        #area code(without parens, with dash)
-             #first dash 
\d\d\d        #first 3 digits
-             #second dash
\d\d\d\d      #last 4 digits
\sx\d{2,4}    #extension,like x1234'''   , re.VERBOSE)
print(mo)
mo=re.compile(r'''
\d\d\d        #area code(without parens, with dash)
-             #first dash 
\d\d\d        #first 3 digits
-             #second dash
\d\d\d\d      #last 4 digits
\sx\d{2,4}    #extension,like x1234''')
print(mo)
