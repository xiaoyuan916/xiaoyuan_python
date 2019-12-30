import langid
text1 = "I am a coder and love data mining"
text2 = "请注明作者和出处并保留声明和联系方式"

print langid.classify(text1)
print langid.classify(text2)