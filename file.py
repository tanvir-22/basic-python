fp = open('myfile.txt','w')

fp.write("this is a test file")
lines = ['arafi\n','evan\n','munna\n','farabi\n']
fp.writelines(lines)

fp.close()