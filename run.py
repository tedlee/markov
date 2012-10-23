# Run me!

file = open('corpus')
import markovgen
markov = markovgen.Markov(file)
markov.generate_markov_text()
