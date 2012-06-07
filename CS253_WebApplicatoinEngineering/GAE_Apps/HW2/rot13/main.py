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

form ="""<form method="post">
<textarea name="text">%(text)s</textarea>
<br>
<input type="submit">
</form>"""

charstr= "abcdefghijklmnopqrstuvwxyz"

# stringCrypto aim to make a simple crypto service for the string 
# passed as a parameter
# The method works adding a fixed number (13) to the value of the character.
# The value of the single character is the position in the character array
# (a = 0, b = 1, ... and so on). If the result of the adding will exceed the max value,
# the count have to restart from 0 (circular queue)


def stringCrypto(s):
  uppChars = charstr.upper()
  ret = []
  for a in s:
    p = charstr.find(a)
    if p > -1:
      ret.append(charstr[(p+13)%26])
    else:
      p = uppChars.find(a)
      if (p > -1):
        ret.append(uppChars[(p+13)%26])
      else:
        ret.append(a)
  return "".join(ret)

class MainPage(webapp2.RequestHandler):
  def write_form(self, rottxt =""):
    self.response.out.write(form % {"text": rottxt})

  def get(self):
      #self.response.headers['Content-Type'] = 'text/plain'
#self.response.out.write('Hello, webapp World!')
    self.write_form()

  def post(self):
    text = self.request.get("text")
    res = stringCrypto(text)
    res = cgi.escape(res, quote = True)
    self.write_form(res)

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
