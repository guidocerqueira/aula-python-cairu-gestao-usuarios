from prettytable import PrettyTable

def montar_tabela(items):
	tabela = PrettyTable()
	for i in items:
		tabela.field_names = [chave for chave in i]
		tabela.add_row([i.get(chave) for chave in i])
	return tabela