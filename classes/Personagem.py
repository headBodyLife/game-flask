# from jinja2 import Template
# from flask import Flask, render_template
class Personagem():

	def __init__(self,nome='Guerreiro Silencioso',vocacao='Knight',nivel=99):
		self.nome= nome
		self.vocacao= vocacao
		self.nivel= nivel
		# t = self.mensagem("{{ n }}","{{ v }}", "{{ l }}")
		# t = Template("{{ n }} {{ v }} {{ l }} ")
		# msg = (t.render_template(n=nome,v=vocacao,l=nivel))
		# print(msg)
		print(self.mensagem(self.nome,self.vocacao,self.nivel))

	def getNome(self):
		return self.nome

	def setNome(self,nome):
		self.nome = nome

	def getVocacao(self):
		return self.vocacao

	def setVocacao(self,vocacao):
		self.vocacao = vocacao

	def setNivel(self,nivel):
		self.nivel = nivel

	def getNivel(self):
		return self.nivel

	def mensagem(self,nome,vocacao,nivel):
		return f"Olá {nome}\nBem vindo ao Game!\nVocê é um {vocacao} nivel {nivel}"

	def promover(self,nivel,vocacao):
		if nivel < 20:
			print('Não tens nivel suficiente')
		else:
			if self.getVocacao() == 'Knight':
				self.setVocacao("Elite Knight")
			if self.getVocacao() == 'Paladin':
				self.setVocacao("Royal Paladin")
			if self.getVocacao() == 'Druid':
				self.setVocacao("Elder Druid")
			if self.getVocacao() == 'Sorcerer':
				self.setVocacao("Master Sorcerer")

		return (self.mensagem(self.getNome(),self.getVocacao(),self.getNivel()))

