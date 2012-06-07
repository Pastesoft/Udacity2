import webapp2
import cgi

#form="""<form action="http://www.google.com/search">

# redirecting the output of the main form to testform that is managed by the TestHandler
# form="""<form method="post" action="/testform">
form="""
<form method="post">
What is your birthday?
<br>
<label>
<input type="text" name="month" value="%(month)s"></label>
<label>Day <input type="text" name="day" value="%(day)s"></label>
<label>Year <input type="text" name="year" value="%(year)s"></label>
<div style="color: red">%(errormsg)s</div>
<input type="submit">
<br>
<br>
</form>"""

# function section 
#
def escape_html(s):
  return cgi.escape(s, quote = True)


months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    if month:
        #month = month.capitalize()
        month = month[0].upper() + month[1:]
        #print "month = " + month
        if month in months:
            return month


def valid_year(year):
  if year and year.isdigit():
    ny = int(year)
    if ny >= 1950 and ny <= 2020:
      return ny

def valid_day(day):
  if day and day.isdigit():
    nd = int(day)
    if (nd > 0) and (nd <= 31):
      return nd

  
#
# end function section
#
class MainPage(webapp2.RequestHandler):
# defining a simple method to rewrite the form, managing the error msg (if there is one)
  def write_form(self, err="", month="", day="", year=""):
    self.response.out.write(form % {"errormsg": err,
                                    "month": escape_html(month),
                                    "year": escape_html(year),
                                    "day": escape_html(day)})
#
  def get(self):
#self.response.headers['Content-Type'] = 'text/html'
      #self.response.out.write(form)
    self.write_form()

#class TestHandler(webapp2.RequestHandler):
#  def get(self):
#q = self.request.get("q")
#self.response.out.write(q)
#    self.response.headers['Content-Type'] = 'text/html'
#    self.response.out.write(self.request)

  def post(self):
    # q = self.request.get("q")
    user_month = self.request.get('month')
    user_day = self.request.get('day')
    user_year = self.request.get('year')

    month = valid_month(user_month)
    day = valid_day(user_day)
    year = valid_year(user_year)

    # if there is some error the app return the same page again
    if not (month and day and year):
      self.write_form("That doesn't look valid to me, mate!", user_month, user_day, user_year)
    else:
      self.redirect("/thanks")


class ThanksHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("Thanks! The date is valid")


app = webapp2.WSGIApplication([('/', MainPage),
                      ('/thanks', ThanksHandler)],
                      #('/testform', TestHandler)],
                              debug=True)
