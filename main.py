



from flask import Flask, request #<!--imports flask class from flask module-->
from caesar import rotate_string

app = Flask(__name__) #<!--app is the object created by the constructor Flask.--> 
#<!--name is the variable tells what module it in-->

app.config['DEBUG'] = True
#<!--this will enable the flask configuration and errors ensure-->
#<!-- file changes are reloaded-->

form = """
#<!--global variable-->

<!doctype html>
<html>
<head>
<style>

form {{
    background-color: #eee;
    padding: 20px;
    margin: 0 auto;
    width: 540px;
    font: 16px sans-serif;
    border-radius: 10px;
}}
textarea {{
    margin: 10px;
    width: 540px;
    height: 120px;
}}
</style>
</head>
<body>

<form action="/" method="post">
#<!--"/",sends the form to the index page of the site.
# (normally index.php, but often index.html, or main.html)-->
<label for="rot">Rotate by:
<input type="text" name="rot" value=0 />
</label>
<textarea type="text" name="text">{0}</textarea> 

<input type="submit" value = "SUBMIT"/>
</form>
</body>
</html>
""" 
#<!--SO it can use multiple lines-->
@app.route("/", methods=['POST'])
def encrypt():
    #get posted form data from request.form [""]
    #and query string data from request.args[""]
    info=str(request.form["text"])
    rotx=int(request.form["rot"])
    secret=str(rotate_string(info,rotx))

    return form.format(secret)

@app.route("/") #<!--creates a mapping between the path root and the function i define-->

def index(): #<!--define index with a function fo zero variables-->
    return form.format('') #<!-- # function returns a string literal-->

app.run() #passes control to Flask object. the run function loops forever and should be last.-->
#<!-- it listens for request and sends responses over the network connection.--> 



