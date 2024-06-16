from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['SMTP_SERVER'] = 'smtp.gmail.com'
app.config['PORT'] = 465
app.config['USERNAME'] = 'atillanffa@gmail.com'
app.config['PASSWORD'] = 'eate wrro tbta axnz'
app.config['USE_TLS'] = False
app.config['USE_SSL'] = True

mail = Mail(app)
CORS(app, resources={r"/submit-form": {"origins": "*"}})  # Permitir todas as origens para esta rota
def send_email(message):
    try:
        mail.send(message)
        return True
    except SMTPAuthenticationError:
        return False

@app.route('/submit-form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # Obter os dados do formulário do corpo da solicitação
        email =  request.form["email"]
        name = request.form ["name"]
        idade = request.form ["idade"]
        profession = request.form ["profession"]
        hasPets = request.form ["hasPets"] 
        adoptionType = request.form ["adoptionType"]
        
        
        msg = Message("Message from your website", sender=email, recipients=["atillanffa@gmail.com"])
        msg.body = message
        mail.send(msg)
        return render_template ("index.html", success=1)
    return render_template('index.html')
        
       ## form_data = request.form

        # Obter o e-mail do remetente do formulário
       # sender_email = form_data.get('email')
        
        

       # if not sender_email:
         #   return jsonify({'message': 'E-mail do remetente não fornecido'}), 400
        #if send_email(message):
       #     return jsonify({'message': 'E-mail enviado com sucesso'})
      #  else:
  #          return jsonify({'message': 'Falha ao enviar e-mail. Verifique suas credenciais e configurações.'}), 500

        # Configurar detalhes do e-mail

        # Construir mensagem de e-mail
       # message = Message('Novo formulário de adoção/apadrinhamento',
         #                 sender=sender_email,
          #                recipients=[receiver_email])
        ##message.html = f"""
        #<p><strong>Nome:</strong> {form_data['name']}</p>
       # <p><strong>Idade:</strong> {form_data['idade']}</p>
        #<p><strong>Profissão:</strong> {form_data['profession']}</p>
        #<p><strong>Possui animais de estimação:</strong> {form_data['hasPets']}</p>
        #<p><strong>Pretende adotar ou apadrinhar:</strong> {form_data['adoptionType']}</p>
     #   """

        # Enviar e-mail
      ##  mail.send(message)

    ##    return jsonify({'message': 'E-mail enviado com sucesso'})

  ##  else:
##        return 'This route only accepts POST requests.', 405


if __name__ == '__main__':
    app.run(debug=True)
