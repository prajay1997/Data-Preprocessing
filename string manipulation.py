# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 15:14:01 2021

@author: praja
"""
# Q1) 	Create a string “Grow Gratitude”
# a)	How do you access the letter “G” of “Growth”?
str1 = "GROW GRATITUDE"
print(str1)

 # a)	How do you access the letter “G” of “Growth”?
letter = str1[0] 
print(letter)

# b)	How do you find the length of the string?
 len(str1)
 
 

# c) Count how many times “G” is in the string.

print(str1.count('G'))

#Q2) Number of chars in the string
 string ="Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else."
 len(string)

# Q3) 
word = "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"

# a)	get one char of the word
print(word[0])

# b)	get the first three char
print(word[0:3])

# c)	get the last three char
print(word[-3:])

# Q4)
 word1 = "stay positive and optimistic"
# Write a code to find if:
#     a)The string starts with “H”
 word1.startswith("H")
 
 # b)	The string ends with “d”
  word1.startswith("d")

#c)	The string ends with “c”
word1.endswith("c")


# Q)5	Write a code to print " 🪐 " one hundred and eight times. (only in python)

print("\U0001FA90" *108)  # \U0001FA90 =code for the emoji "🪐" 

# Q)7	Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of”

string1 = "Grow Gratitude"

string1.replace("Grow","Growth of")

#Q8) You have noticed that the story is printed in a reversed order. Rectify the same and write a code to print the same story in a correct order.

sentence =".elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A”"

print(''.join(reversed(sentence)))
