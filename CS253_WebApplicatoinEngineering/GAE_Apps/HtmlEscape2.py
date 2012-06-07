# implement the function escape_html() which replaces:
# > to &gt;
# < to &lt;
# " to &quot;
# & to &amp;
# and returns the escaped string

# we use the escape method from the cgi library 
import cgi

def escape_Html(hstr):
  return cgi.escape(hstr, quote = True)

print escape_Html('<b>try this string & this one too"cc"')
