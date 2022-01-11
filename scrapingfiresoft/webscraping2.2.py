import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text
import http.cookiejar

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('https://panel.firesoft.cl/')


# Select the second (index one) form (the first form is a search query box)
br.select_form(nr=1)

# User credentials
br.form['user'] = 'cbpa9'
br.form['clave'] = 'd5g6h1'

# Login
br.submit()

print(br.open('https://panel.firesoft.cl/').read())