from datetime import datetime
import datetime as dt



def teste1(palavra, nlinha):
	t = 1
	if len(palavra)>20 or len(palavra)==0:
		print(erro,nlinha, 'pos', t)

def teste2(palavra, nlinha):
	t = 2
	if len(palavra)>20 or len(palavra)==0:
		print(erro, nlinha, 'pos', t)

def teste3(palavra, nlinha):
	t = 3
	if len(palavra) != 13:
		print(erro,nlinha, 'pos', t)
	else:
		try:
			if int(palavra) < 1000000000000:
				print(erro,nlinha, 'pos', t)
		except:
			print(erro,nlinha, 'pos', t)

def teste4(palavra, nlinha):
	t = 4
	if len(palavra) > 30:
		print(erro,nlinha, 'pos', t)

def teste5(palavra, nlinha):
	t = 5
	if len(palavra) > 20:
		print(erro,nlinha, 'pos', t)


def teste6(data, nlinha):
	t = 6
	y2s = 31557600
	if len(data) != 8:
		print(erro, nlinha, 'pos', t)
		return
	try:
		if int(data)<19000000:
			print(erro, nlinha, 'pos', t)
			return
	except:
		print(erro, nlinha, 'pos', t)
		return

	datahoje = dt.date.today()
	try:
		datafile =  datetime.strptime(data, '%Y%m%d').date()
	except:
		print(erro, nlinha, 'pos', t)
		return
	sub = datahoje - datafile

	if sub.total_seconds()/y2s >= 100:	
		print(erro, nlinha, 'pos', t)
		return

def teste7(palavra, nlinha):
	t = 7
	if len(palavra)>13 or len(palavra)==0:
		print(erro,nlinha, 'pos', t)
	try: 
		if int(palavra) < 0:
			print(erro,nlinha, 'pos', t)
	except:
		print(erro,nlinha, 'pos', t)

def teste8(letra, nlinha):
	t = 8
	if len(letra)==1:
		match letra:
			case 'F':
				return
			case 'S':
				return
			case 'V':
				return
			case 'M':
				return
			case _:
				print(erro, nlinha, 'pos', t)
	else:
		print(erro, nlinha, 'pos', t)

def teste9(palavra, nlinha):
	t = 9
	if len(palavra)>20 or len(palavra)==0:
		print(erro,nlinha, 'pos', t)
	try:
		if int(palavra) < 0:
			print(erro,nlinha, 'pos', t)
	except:
		print(erro,nlinha, 'pos', t)

def teste10(palavra, nlinha):
	t = 10
	if len(palavra) > 8:
		print(erro,nlinha, 'pos1', t)
		return
	try:
		if float(palavra) < 0:
			print(erro,nlinha, 'pos1.1', t)
	except:
		print(erro,nlinha, 'pos1.2', t)
	palavra = palavra.split('.')
	if len(palavra) == 2:
		if len(palavra[1])>3:
			print(erro,nlinha, 'pos3', t)
			return
		else:
			return
	elif len(palavra) == 1:
		return
	else:
		print(erro,nlinha, 'pos3.1', t)

#while True:
	#file = input('Enter file name: ')
	#if file == 'qa.txt':
	#	file = open(file, 'r')
	#	break
	#else:
	#	print('Nome de ficheiro inválido')

file = open('qa.txt', 'r')
count = 1
erro = "Erro na linha"

for line in file:
	line = line.split(';')
	line[-1] = line[-1].strip()
	if len(line) != 10:
		print(erro, count)
		count += 1
		continue

	teste1(line[0], count)
	teste2(line[1], count)
	teste3(line[2], count)
	teste4(line[3], count)
	teste5(line[4], count)
	teste6(line[5], count)
	teste7(line[6], count)
	teste8(line[7], count)
	teste9(line[8], count)
	teste10(line[9], count)


	count += 1
	
print('Fim')


