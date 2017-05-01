import os
import sys
from sklearn.metrics import classification_report as report

directory = "F:\\To_server\\model\\test_results\\"
#filename = "tagging.test.hyp.txt"
#filename = "test.txt"
filename = sys.argv[1]

with open(directory + filename) as f:
	prediction = [];
	label = [];
	unique_label = {}
	label_names = []
	for line in f:
		contentlist = line.split()
		#if (len(contentlist) != 0 and len(contentlist) !=3):
			#print(line)
			#print(len(contentlist))
		
		if (len(contentlist) == 0 or contentlist[0] == "BOS" or contentlist[0] == "EOS"):
			continue
		else:
			label.append(contentlist[1])
			prediction.append(contentlist[2])
			if (contentlist[1] in unique_label):
				unique_label[contentlist[1]] += 1
			else:
				label_names.append(contentlist[1])
				unique_label[contentlist[1]] = 1

print(report(label, prediction, label_names, target_names=label_names))


