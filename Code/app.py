

from flask import Flask, request, render_template
import caesar_cipher
import vigenere_cipher
from genetic_algorithm import run_genetic_algorithm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/caesar', methods=['GET', 'POST'])
def caesar():
    '''
        render respective templates along with function calls for respective encryption, decryption & cracking for Caesar Cipher.
    '''
    if request.method == 'POST':
        plain_text = request.form['plain_text']
        cipher_text = request.form['cipher_text']
        function = request.form.get('choices')
        key_size = int(request.form.get('key_choices'))
        if str(function) == "Encrypt":
            return render_template('caesar.html', data=[25, plain_text, caesar_cipher.encrypt(plain_text, key_size)])
        if str(function) == "Decrypt":
            return render_template('caesar.html', data=[25, caesar_cipher.decrypt(cipher_text, key_size), cipher_text])
        if str(function) == "Crack":
            return render_template('caesar.html', data=[25, caesar_cipher.crack(cipher_text), cipher_text])
    return render_template("caesar.html", data=[25, "Plain Text", "Cipher Text"])

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    '''
        Approach: same as that of Caesar cipher listed above.
    '''
    if request.method == 'POST':
        plain_text = request.form['plain_text']
        cipher_text = request.form['cipher_text']
        function = str(request.form.get('choices'))
        keyword = str(request.form["keyword"])
        if function == "Encrypt":
            return render_template('vigenere.html', data=[plain_text, vigenere_cipher.encrypt(plain_text, keyword)])
        if function == "Decrypt":
            return render_template('vigenere.html', data=[vigenere_cipher.decrypt(cipher_text, keyword), cipher_text])
        if str(function) == "Crack":
            return render_template('genetic_algo.html', data=[cipher_text])
    return render_template("vigenere.html", data=["Plain Text", "Cipher Text"])

@app.route('/ga', methods=['GET','POST'])
def ga():
    '''
        render template and crack crypto system depending on choice of ciphers such as Caesar Cipher or Vigenere ciphers in our case!
    '''
    if request.method == 'POST':
        cipher_text = request.form['cipher_text']
        key_length = int(request.form['key_length'])
        num_of_generations = int(request.form['generations'])
        data = run_genetic_algorithm(key_length=key_length, cipher_text=cipher_text, number_of_generations=num_of_generations)
        data.append(cipher_text)
        return render_template('genetic_algo.html', data=data)
    return render_template('genetic_algo.html')    

if __name__ == '__main__':
	app.run()  
