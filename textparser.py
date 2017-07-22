def Parser(filename):
	lis = []	
	#AFTER TAKING A LOOK AT THE DATA WE SOME CLEANING REQUIRED TO EXTRACT THE NECESSARY FEATURES 
	with open(filename) as fp:

		for line in fp:
			if not line.isspace():
				new = line.partition('\'')[-1].rpartition('\'')[0]
				lis.append(new)
	fp.close()	
	return lis


	#WRITING THE LIST TO A NEW FILE FOR FURTHER USE 
def ParseDataWriter(parse_list):

	with open('ParsedParameters.txt','w') as output:
		for line in parse_list:
			output.write(str(line)+'\n')

	output.close()	

	
if __name__ == "__main__":

	#TEXT DATA OF THE REQUIRED FEATURES GIVEN BY IIA
	filename = 'parameters.txt'
	#PARSING THE TEXT DATA AND REMOVING ONLY A LIST OF THE FEATURES 
	parse_list = Parser(filename)

	#WRITING THE PARSED DATA INTO A NEW FILE FOR FURTHER REFERENCES 
	ParseDataWriter(parse_list)

