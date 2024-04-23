from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

usuarios = {
    "enrico": {
        "senha": b'\xaf\xe0\x84\x02\xb5\xef\xd5y\x02\xe8\xaaU}\x8a\xae',
        "saldo": 1000.00
    }
}

chave = get_random_bytes(16)
iv = get_random_bytes(16)

criptografar_senha = lambda senha: AES.new(chave, AES.MODE_CBC, iv).encrypt(pad(senha.encode(), 16))

descriptografar_senha = lambda senha_criptografada: unpad(AES.new(chave, AES.MODE_CBC, iv).decrypt(senha_criptografada), 16).decode()

verificar_usuario_existe = lambda nome_usuario: nome_usuario in usuarios

verificar_senha_usuario = lambda nome_usuario, senha: criptografar_senha(senha) == usuarios.get(nome_usuario, {}).get("senha")

verificar_saldo_usuario = lambda nome_usuario, valor: usuarios.get(nome_usuario, {}).get("saldo", 0) >= valor


debitar_conta_usuario = lambda nome_usuario, valor: usuarios[nome_usuario].update({"senha": usuarios[nome_usuario]["senha"], "saldo": usuarios[nome_usuario]["saldo"] - valor})


@app.route("/")
def index():
    return redirect(url_for("pagina_cadastro"))


@app.route("/cadastro")
def pagina_cadastro():
    return render_template("cadastro.html")


@app.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
    dados = request.form
    nome_usuario = dados["nome_usuario"]
    senha = dados["senha"]
    saldo = float(dados["saldo"])

    if verificar_usuario_existe(nome_usuario):
        return jsonify({"mensagem": "Usuário já existe"}), 400

    usuarios[nome_usuario] = {
        "senha": criptografar_senha(senha),
        "saldo": saldo
    }

    return redirect(url_for("pagina_login"))


@app.route("/login")
def pagina_login():
    return render_template("login.html")


@app.route("/login_usuario", methods=["POST"])
def login_usuario():
    dados = request.form
    nome_usuario = dados["nome_usuario"]
    senha = dados["senha"]

    if not verificar_usuario_existe(nome_usuario):
        return jsonify({"mensagem": "Usuário não encontrado"}), 404

    if not verificar_senha_usuario(nome_usuario, senha):
        return jsonify({"mensagem": "Senha incorreta"}), 401

    session["nome_usuario"] = nome_usuario

    return redirect(url_for("informacoes_usuario", nome_usuario=nome_usuario))

@app.route("/informacoes_usuario/<nome_usuario>")
def informacoes_usuario(nome_usuario):
    if not verificar_usuario_existe(nome_usuario):
        return jsonify({"mensagem": "Usuário não encontrado"}), 404

    saldo = usuarios.get(nome_usuario, {}).get("saldo", 0)
    senha_criptografada = usuarios.get(nome_usuario, {}).get("senha")
    senha = descriptografar_senha(senha_criptografada)

    return render_template("informacoes_usuario.html", nome_usuario=nome_usuario, saldo=saldo, senha_criptografada=senha_criptografada, senha=senha)

if __name__ == "__main__":
    app.run(debug=True)



