from os import system
from usuarios import usuarios, cadastrar_usuario, encontrar_usuario
from tabela import montar_tabela

while True:
	print('1: Listar usuários')
	print('2: Cadastro de usuário')
	print('3: Atualizar usuário')
	print('4: Excluir usuário')
	print('5: Detalhar usuário')
	print('6: Sair')

	comando = int(input('Digite o comando: '))
	match comando:
		case 1:
			if len(usuarios) == 0:
				system('clear') or None
				print('lista vazia!')
				continue
			system('clear') or None
			print(montar_tabela(usuarios))
		case 2:
			nome = input('Digite o nome: ')
			email = input('Digite o email: ')
			cpf = input('Digite o cpf: ')
			cadastrar_usuario(nome, email, cpf)
			system('clear') or None
			print('Usuário cadastrado com sucesso')
		case 3:
			cpf_usuario = input('Digite o cpf do usuario que deseja atualizar: ')
			usario_encontrado = encontrar_usuario(cpf_usuario)
			if not usario_encontrado:
				system('clear') or None
				print('Usuário não encontrado')
				continue
			nome = input('Digite o nome: ')
			email = input('Digite o email: ')
			cpf = input('Digite o cpf: ')
			usario_encontrado.update({
				'nome': nome,
				'email': email,
				'cpf': cpf
			})
			system('clear') or None
			print('Usuário atualizado com sucesso')
		case 4:
			cpf_usuario = input('Digite o cpf do usuario que deseja excluir: ')
			usario_encontrado = encontrar_usuario(cpf_usuario)
			if not usario_encontrado:
				system('clear') or None
				print('Usuário não encontrado')
				continue
			usuarios.remove(usario_encontrado)
			system('clear') or None
			print('Usuário excluido com sucesso')
		case 5:
			cpf_usuario = input('Digite o cpf do usuario que deseja encontrar: ')
			usario_encontrado = encontrar_usuario(cpf_usuario)
			if not usario_encontrado:
				system('clear') or None
				print('Usuário não encontrado')
				continue
			system('clear') or None
			print(f"""
Nome: {usario_encontrado['nome']}
Email: {usario_encontrado['email']}
CPF: {usario_encontrado['cpf']}
			""")
		case 6:
			system('clear') or None
			break