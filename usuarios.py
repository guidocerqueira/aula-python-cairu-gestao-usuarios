usuarios = []

def cadastrar_usuario(nome, email, cpf):
	novo_usuario = {
		'nome': nome,
		'email': email,
		'cpf': cpf
	}
	usuarios.append(novo_usuario)

def encontrar_usuario(cpf):
	usario_encontrado = None
	for usuario in usuarios:
		if usuario['cpf'] == cpf:
			usario_encontrado = usuario
	return usario_encontrado