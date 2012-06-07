# implement the function escape_html() which replaces:
# > to &gt;
# < to &lt;
# " to &quot;
# & to &amp;
# and returns the escaped string

htmlEscape = [("&", "&amp;"),
                (">", "&gt;"),
                ("<", "&lt;"),
                ('"', "&quote;")]

def escape_html(hstr):
  for(i, o) in htmlEscape:
    print i 
    hstr = hstr.replace(i, o)
  return hstr

print escape_html("test&")
print escape_html("test>>")
print escape_html('test<< another test"')

