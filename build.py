import json

with open('signout.html') as s:
    with open('login.html') as f:
        with open('index.js', 'w') as d:
            d.write("document.body.style.background = \"hsl(206, 12%, 95%)\";\nif (document.getElementById(\"DivSigningOut\") === null) document.querySelector(\".mainDiv\").innerHTML = " + json.dumps(f.read()) + "\nelse document.querySelector(\".mainDiv\").innerHTML = " + json.dumps(s.read()))
