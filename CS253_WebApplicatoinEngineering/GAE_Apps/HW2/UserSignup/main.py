#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

form ="""<form method="post">
<h1>HW2</h1>
<table>
<tr>
  <td>Username </td>
  <td><input name ="username" type="text" value="%(username)s"></td>
  <td style="color: red">%(err_name)s</td>
</tr>
<tr>
  <td>Password </td>
  <td><input name="password" type="password" value="%(password)s"></td>
  <td style="color: red">%(err_pwd)s</td>
</tr>
<tr>
  <td>Verify Password </td>
  <td><input name="verify" type="password" value="%(verify)s"></td>
  <td style="color: red">%(err_ver)s</td>
</tr>
<tr>
  <td>Email (optional) </td>
  <!-- <td><input name="email" type="email" value="%(email)s"></td> -->
  <td><input name="email" type="text" value="%(email)s"></td>
  <td style="color: red">%(err_email)s</td>
</tr>
</table>
<br>
<input type="submit">
</form>"""

# regular expression section. Use to verify if 
# username, password, email
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PWD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(user):
  return USER_RE.match(user)
def valid_pwd(pwd):
  return PWD_RE.match(pwd)
def valid_email(email):
  return EMAIL_RE.match(email)

def user_check(user):
  if user:
    if valid_username(user):
      return user

def password_check(pwd):
  if pwd:
    if valid_pwd(pwd):
      return pwd

def pwd_verify(pwd, ver):
  if pwd == ver:
    return ver

def email_check(email):
  if email:
    if not valid_email(email):
      return False, email
  return True, email

class MainPage(webapp2.RequestHandler):
  def write_html(self, username="", pwd="", verify="", email="",
    erru =  "", errp = "", errv = "", erre = ""):
    self.response.out.write(form % {"username" : username, 
        "password" : pwd, 
        "verify" : verify, 
        "email" : email,
        "err_name" : erru,
        "err_pwd" : errp,
        "err_ver": errv,
        "err_email": erre})

  def get(self):
    self.write_html()
#self.response.out.write('Hello, webapp World!')

  def post(self):
    i_user = cgi.escape(self.request.get('username'), quote = True)
    i_pwd = cgi.escape(self.request.get('password'), quote = True)
    i_ver = cgi.escape(self.request.get('verify'), quote = True)
    i_email = cgi.escape(self.request.get('email'), quote = True)

    user = user_check(i_user)
    pwd = password_check(i_pwd)
    verify = pwd_verify(i_pwd, i_ver)
    okemail, email = email_check(i_email)

    erru = errp = errv = erre = ""

    if (not user or not pwd or not verify or not okemail):
      if not user:
        erru = "That's not a valid username."
      if not pwd:
        errp = "That's not a valid password."
      if not verify:
        errv = "Your password didn't match."
      if not okemail:
        if i_email:
          erre = "That's not a valid email."
    else:
      self.redirect("/welcome?username=" + user)
    #self.write_html(i_user, i_pwd, i_ver, i_email, erru, errp, errv, erre)
    self.write_html(i_user, "", "", i_email, erru, errp, errv, erre)



class WelcomeHandler(webapp2.RequestHandler):
  def get(self):
    user = self.request.get("username")
    self.response.out.write("<h2>Welcome, " + user + "!</h2>")

app = webapp2.WSGIApplication([('/', MainPage),("/welcome", WelcomeHandler)],
                              debug=True)
