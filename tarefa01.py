def autenticacao(email, senha):
    return email == "admin" and senha == "admin"

print(autenticacao("admin", "admin"))
