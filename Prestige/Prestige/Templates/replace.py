
x = "about.html"
# Read in the file
with open(x, 'r',errors='ignore') as file :
  filedata = file.read()

#.jpg" -> .jpg' %}"
#'.jpg\"' -> '.jpg\' %}\''

# Replace the target string
filedata = filedata.replace('.jpg"','.jpg\' %}"')
filedata = filedata.replace('.jpg)','.jpg\' %})')
filedata = filedata.replace('.png"','.png\' %}"')
filedata = filedata.replace('.css"','.css\' %}"')
filedata = filedata.replace('.js"','.js\' %}"')
filedata = filedata.replace('.svg"','.svg\' %}"')

# "images/  -> "{% static 'images/
filedata = filedata.replace( '"images/' , '"{% static \'images/' )
filedata = filedata.replace( '(images/','({% static \'images/'   )
filedata = filedata.replace( '"vendor/' , '"{% static \'vendor/' )
filedata = filedata.replace( '"vendor1/' , '"{% static \'vendor1/' )
filedata = filedata.replace( '"fonts/' , '"{% static \'fonts/' )
filedata = filedata.replace( '"css/' , '"{% static \'css/' )
filedata = filedata.replace( '"css1/' , '"{% static \'css1/' )
filedata = filedata.replace( '"css2/' , '"{% static \'css2/' )
filedata = filedata.replace( '"screens/' , '"{% static \'screens/' )
filedata = filedata.replace( '"js/' , '"{% static \'js/' )

#images/  "vendor/ "fonts/ "css/ "js/ 
#.png .js .css



# Write the file out again
with open(x, 'w') as file:
  file.write(filedata)
