#!/usr/bin/python3
# coding: utf-8
import cgi
import sys, io 

# python -m http.server 8000 --cgi 
# http://localhost:8000/cgi-bin/calc1.py

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form1 = cgi.FieldStorage() 

str01 = form1.getvalue( 'TextBox1', '0' ) 
str02 = form1.getvalue( 'TextBox2', '0' ) 
str03 = str( int( str01 ) + int( str02 ) ) 
# str03 = str( float( str01 ) + float( str02 ) ) 

str0 = '''
<html>
  <body>
    <form name="Form" method="POST" action="/cgi-bin/calc1.py">
      <input type="text" size="10" name="TextBox1" value="{str11}"> + 
      <input type="text" size="10" name="TextBox2" value="{str12}"> = 
      <input type="text" size="10" name="TextBox3" value="{str13}"><br><br>
      <input type="submit" value="calculate" name="button1">
    </form>
  </body>
</html>
'''.format( str11=str01, str12=str02, str13=str03 ) 

print("Content-Type: text/html; charset=UTF-8;\n")
print( str0 ) 
