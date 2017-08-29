from flask import Flask, abort
from flask import render_template
import requests
#utf8

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/1")
def index1():
    lista= ["joao", "ana", "bruno"]
    return render_template("index1.html", nomes=lista)

@app.route("/sobre")
def sobre():
    return "Sobre"

@app.route("/perfil/<string:username>")
def perfil(username):
    token= "?access_token=3653d9cd7a9a21d167470b0668dc2f2ef28cd816"
    url= "https://api.github.com/users/"+username+token
    r= requests.get(url)
    if r.status_code==200:
        url_repos= r.json()['repos_url']+token
        repos= requests.get(url_repos).json()
        return render_template("perfil.html", usuario=r.json(), repos=repos)
        #return str(r.json()['public_repos'])
    else:
        return abort(404)

if __name__=="__main__":
    app.run(debug=True)
