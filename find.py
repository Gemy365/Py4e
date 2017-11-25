#Try To Print 0.8475 From text
text = "X-DSPAM-Confidence:    0.8475"

pos = text.find('0')    #Search On [0] & Get The Index Of This Number

floating = float(text[pos : ]) #Get Chunck Of String From Index [pos] To [end]

print(floating)
