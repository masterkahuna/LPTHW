the_sentence_1 = "Here is a sentence"
print the_sentence_1

the_sentence_2 = "Like all sentences, it has a %s, a %s and a %s"  % ("subject", "verb", "object")

print the_sentence_2

home = "ile"
the_sentence_3 = "We are all going", home
print the_sentence_3
# The above is very interesting. Study it more closely 

print "We are all going", home



print "Tell me your name:",
name = raw_input()

print "Tell me your age:",
age = raw_input()

print "Tell me your weight:",
weight = raw_input()

print "So %r, you are %r years old and weigh %r pounds" % (name, age, weight)

print "Version 2: "

print "So %s, you are %s years old and weigh %s pounds" % (name, age, weight)