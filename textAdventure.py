import time


# KNOW THE ROOM?
room_door = True
kitchen_door = False
living_door = False

# itens
vault = False
passwrd = False
key = False
crowbar = False


def clear():
	print("\n" * 100)


def room(inside):
	global room_door, kitchen_door, living_door
	
	input("\n[[precione enter para continuar]]")
	clear()
	
	print("--QUARTO ABANDONADO--\n")
	time.sleep(2)
	print("  Voce olha ao redor")
	time.sleep(1)
	print("  Voce esta em um quarto empoeirado e cheio de teias de aranha")
	time.sleep(1)
	print("  sua unica iluminação vem de buracos no teto e na parede")
	time.sleep(2)
	print("  A unica janela esta fechada e trancada")
	time.sleep(1)
	print("  ...")
	time.sleep(1)
	print("  É impossivel ver qualquer coisa por ela")
	if(inside):  # caso esteja dentro da sala
		time.sleep(1)
		print("  Há apenas uma unica porta no quarto")
	else:
		time.sleep(1)
		print("  Há apenas a porta pela qual voce entrou")
	choose = input("--voce vai olhar o quarto ou sair pela porta?  ")
	while ("olhar" not in choose and "sair" not in choose):
		print("  não entendi o que voce quis dizer...")
		choose = input("--voce vai olhar o quarto novamente ou sair pela porta?  ")

	while ("olhar" in choose):
		print("  voce olha o quarto novamente")
		time.sleep(1)
		print("  ...")
		time.sleep(1)
		print("  não encontra nada")
		choose = input("--voce vai olhar o quarto novamente ou sair pela porta?  ")
		while ("olhar" not in choose and "sair" not in choose):
			print("  não entendi o que voce quis dizer...")
			choose = input("--voce vai olhar o quarto novamente ou sair pela porta?  ")
	hall(room_door, kitchen_door, living_door)


def hall(knw_room, knw_kitchen, knw_living):
	global vault, passwrd, key

	input("\n[[precione enter para continuar]]")
	clear()

	print("--CORREDOR--\n")
	time.sleep(2)
	print("  Voce esta agora no corredor da casa")
	time.sleep(1)
	print("  Há alguns quadros na parede")
	if (vault):
		print("  Há um cofre que esta escondido")
	time.sleep(1)
	print("  voce consegue ver 4 portas")
	time.sleep(2)
	choose = input("--voce vai olhar o corredor ou entrar nas portas? ")
	while ("olhar" not in choose and "porta" not in choose and "entrar" not in choose):
		print("  não entendi o que voce quis dizer...")
		choose = input("--voce vai olhar o corredor ou entrar nas portas? ")
	while ("olhar" in choose):
		if (vault):
			time.sleep(1)
			print("  O unico segredo é o cofre")
		else:
			print("  voce começa a olhar os quadros")
			time.sleep(1)
			print("  varias figuras macabras estão pintadas neles")
			time.sleep(3)
			print("  voce sem querer derruba um quadro")
			time.sleep(0.5)
			print("  O quadro cai no chao")
			time.sleep(1)
			print("  onde estava o quadro voce descobre um cofre")
			vault = True 
		choose = input("--voce vai investigar o cofre? ")
		while ("sim" not in choose and "nao" not in choose):
			print("  não entendi o que voce quis dizer...")
			choose = input("--voce vai investigar o cofre? ")
		if ("sim" in choose):
			if (passwrd and not key):
				print("  voce usou a senha no cofre")
				time.sleep(2)
				print("  o cofre foi destrancado")
				time.sleep(1)
				print("  voce conseguiu uma chave")
				key = True
			elif (key):
				print("  não ha mais nada dentro do cofre")
			else:
				print("  O cofre esta trancado")
				time.sleep(1)
				print("  é necessario uma senha para abrir")
		choose = input("--voce vai olhar o corredor ou entrar nas portas? ")
		while ("olhar" not in choose and "porta" not in choose and "entrar" not in choose):
			print("  não entendi o que voce quis dizer...")
			choose = input("--voce vai olhar o corredor novamente ou entrar nas portas? ")

	print("--qual porta voce quer entrar?")
	time.sleep(1)
	print("---porta 1: quarto abandonado")
	if (knw_living):
		print("---porta 2: sala")
	else:
		print("---porta 2: desconhecido")
	if (knw_kitchen):
		print("---porta 3: cozinha")
	else:
		print("---porta 3: desconhecido")
	print("---porta 4: desconhecido")
	choose = input()

	while (choose not in ['porta 1', 'porta 2', 'porta 3', 'porta 4', '1', '2', '3', '4']):
		print("  não entendi o que voce quis dizer...")
		choose = input("--qual porta voce quer entrar? ")
	if ('1' in choose):
		room(False)
	elif ('2' in choose):
		living()
	elif ('3' in choose):
		kitchem()
	else:
		if (key):
			time.sleep(1)
			print("  voce destranca a porta")
			time.sleep(1)
			print("  quando abre a porta vc vê a liberdade")
			time.sleep(1)
			print("  parabens... voce escapou")
			time.sleep(2)
			print("  ...")
			time.sleep(3)
			print("  mas algo o impediu")
			time.sleep(2)
			clear()			
			time.sleep(3)
			print("  fim")
			time.sleep(3)
			clear()
			print("  fim ?")
			time.sleep(3)
			clear()
		else:
			print("  Porta trancada, parece que é a saida")
			time.sleep(1)
			print("  voce volta a olhar o corredor")
			hall(room_door, kitchen_door, living_door)


def kitchem():
	global crowbar, room_door, kitchen_door, living_door

	kitchen_door = True

	input("\n[[precione enter para continuar]]")
	clear()

	print("--Cozinha--\n")
	time.sleep(2)
	print("  Voce esta agora na cozinha da casa")
	time.sleep(1)
	print("  em cima da mesa voce panelas nojentas infestadas de baratas")
	time.sleep(1)
	print("  eu não mecheria ai")
	if (not crowbar):
		print("  preso na porta do armario voce ve um pé de cabra")
		choose = input("--pegar o pé de cabra? ")
		while ("sim" not in choose and "não" not in choose):
			print("  não entendi o que voce quis dizer...")
			choose = input("--pegar o pé de cabra? ")
		if ("sim" in choose):
			print("  voce pegou o pé de cabra")
			time.sleep(2)
			print("  o armario se abre revelando comidas velhas e estragadas")
			time.sleep(2)
			print("  uma barata sai de dentro dele e sobe na sua mão")
			time.sleep(1)
			print("  voce tira ela... que nojo")
			crowbar = True
	choose = input("--sair pela porta que voce entrou ou olhar novamente? ")
	while ("sair" not in choose and "olhar" not in choose):
			print("  não entendi o que voce quis dizer...")
			choose = input("--sair pela porta que voce entrou ou olhar novamente? ")
	while ("olhar" in choose):
		print("  não ha mais nada aqui..")
		choose = input("--sair pela porta que voce entrou ou olhar novamente? ")
		while ("sair" not in choose and "olhar" not in choose):
			print("  não entendi o que voce quis dizer...")
			choose = input("--sair pela porta que voce entrou ou olhar novamente? ")

	print("  voce sai pela porta")
	hall(room_door, kitchen_door, living_door)


def living():
	global crowbar, passwrd, room_door, kitchen_door, living_door
	living_door = True

	input("\n[[precione enter para continuar]]")
	clear()

	print("--Sala--\n")
	time.sleep(2)
	print("  voce entrou na sala")
	time.sleep(1)
	print("  esta tão abandonada como o resto da casa")
	time.sleep(1)
	print("  mas talvez o sofa velho possa ser aconchegante")
	time.sleep(1)
	print("  há um armario trancado com pedaços de madeiras pregadas no canto")
	choose = input("--investigar sala ou voltar pela porta? ")
	while ("investigar" not in choose and "voltar" not in choose):
		print("  não entendi o que voce quis dizer...")
		choose = input("--investigar sala ou voltar pela porta? ")
	while ("investigar" in choose):
		if (not passwrd):
			if(crowbar):
				print("  voce usa o pé de cabra para abrir o armario..")
				time.sleep(1)
				print("  dentro do antigo armario voce encontra uma senha..")
				time.sleep(1)
				print("  pode ser util")
				passwrd = True
			else:
				print("  voce fica intrigado com o armario")
				time.sleep(2)
				print("  mas não consegue arrombar agora")
		else:
			print("  não há mais nada aqui")
		choose = input("--investigar sala ou voltar pela porta? ")
		while ("investigar" not in choose and "voltar" not in choose):
			print("  não entendi o que voce quis dizer...")
			choose = input("--investigar sala ou voltar pela porta? ")
	print("  voce sai de volta pela porta")
	hall(room_door, kitchen_door, living_door)


def game():
	clear()
	print("--Voce acordou dentro de uma casa abandonada--\n")
	time.sleep(2)
	print("  seu objetivo é simplesmente sair daqui")
	time.sleep(2)
	room(True)


def main():
	start = True
	while (start):
		game()	
		x = input("jogar de novo? [s/n] ")
		if (x not in ['y', 'Y', 's', 'S']):
			start = False


main()

