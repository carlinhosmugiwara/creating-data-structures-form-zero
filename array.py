# coding an array from the ground up
def array(size, data_type):
	array_ = []
	if(data_type == "string"):
		for i in range(0, size):
			if(i<size):
				array_.append(input("Enter the strings: "))
	
	elif(data_type == "float"):
		for i in range(0, size):
			if(i<size):
				array_.append(float(input("Enter the floats: ")))
	elif(data_type == "integer" or data_type == "int"):
		for i in range(0, size):
			if(i<size):
				array_.append(int(input("Enter the integers")))
	
	return array_


x = array(int(input("Enter the size: ")), input("Enter the data type in lower case: "))
print()
print()
print(x)
