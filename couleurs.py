#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Changer les couleurs dans un terminal
class Palette:
    def __init__(self):
        # Control Sequence Introducer
        self.CSI = "\x1b["

        self.couleurs = {"noir": "0",
                               "rouge": "1",
                               "vert": "2",
                               "jaune": "3",
                               "bleu": "4",
                               "magenta": "5",
                               "cyan": "6",
                               "blanc": "7"}
        self.prefixe_texte = 30
        self.prefixe_fond = 40
    # codes CSI à l'adresse: https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_codes
    def modifier_texte(self, texte, code):
        return self.CSI + code + "m" + texte + self.CSI + "0m"
    def colorer_chaine(self, texte, couleur):
        return self.modifier_texte(texte, "3" + self.couleurs[couleur])
    def colorer_fond(self, texte, couleur):
        return self.modifier_texte(texte, "4" + self.couleurs[couleur])
    def italique(self, texte):
        return self.modifier_texte(texte, "3")
    def gras(self, texte):
        return self.modifier_texte(texte, "2")
def tester():
    p = Palette()
    print p.colorer_chaine("Bonjour", "rouge") + p.italique(" le ") + p.colorer_fond("monde", "bleu")
    print "Texte normal."
    print p.gras("Texte en gras.")
tester()
