from flask import Flask,request,render_template
from utils import create_random_list,apply_gestform_processing_to_list

app = Flask(
    __name__,
    template_folder="templates")

@app.route('/')                                                         
def in_list():                                              #On affiche ici la page où l'on choisi la longueur de la liste aléatoire à créer
    return render_template("input.html")

@app.route('/',methods=['POST'])    
def in_list_post():                                         #Une fois la longueur choisi on renvoie la liste générée et la liste traitée
    length = int(request.form['length'])
    random_list = create_random_list(length)
    return render_template(
        'result.html',
        random_list=', '.join(str(e) for e in random_list),
        processed_list=apply_gestform_processing_to_list(random_list)
    )
