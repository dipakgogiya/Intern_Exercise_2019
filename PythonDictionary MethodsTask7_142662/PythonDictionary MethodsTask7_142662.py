import calendar

class PythonDictionaryMethod:
     
    def check_month_sequene(self,month_keys):
        """
        @Func :- It will sort the purchase products month wise
        @Param1 :- month_keys is the key in dictionary AND it's type is string
        @Return :- It will return the key number as per odd even condition 
        """
        if month_keys in ('january' ,'march' ,'may' ,'july' ,'september' ,'november'):
            return 1
        else:
            return 0
    def check_date_of_month(self,day_keys):
        """
        @Func :- It will sort the purchase products month wise
        @Param1 :- month_keys is the key in dictionary AND it's type is string
        @Return :- It will return the key number as per number of date in month
        """
        if day_keys in ('january' ,'march' ,'may' ,'july' ,'august' ,'october' ,'december'):
            return 31
        elif ('april','june','september','november'):
            return 30
        elif 'february':
            return 28
        else:
            print("Invalid input")   
    def repeat_value(self,dictionary_data):
        """
        @Func :- It will sort the purchase products month wise
        @Param1 :- month_keys is the key in dictionary AND it's type is string
        @Return :- It will return the sorted dictionary in most repeates value wise
        """
        #Sort it by most Repeats Value
        desired_values = []
        remain_value = []
        vals = dictionary_data.values()
        for value in dictionary_data.items():
            if vals.count(value) > 1:
                desired_values.append(value)
            else:
                remain_value.append(value)
        result = sorted(desired_values) + sorted(remain_value)
        return result
        
    def Purchase(self):
        """
        @Func :- It will sort the purchase products month wise
        """
        product_dictionary = {"April":200,"may":500,"June":400,"july":600,"August":100,"september":300,"October":150,"november":250,"December":100,"january":800,"February":500,"march":100}
        print(product_dictionary) 
        print(sorted(product_dictionary)) # Sort by Month alphabetically in increasing order
        print(sorted(product_dictionary,reverse = True)) # Sort by Month alphabetically in decreasing order
        print(sorted(product_dictionary.values())) #Sort by it's Value in increasing values 
        print(sorted(product_dictionary.values(),reverse = True)) #Sort by it's Value in decreasing values
        print(sorted(product_dictionary,key = product_dictionary.__getitem__)) #Return Key by sorting Values. 
        print(sorted(product_dictionary.items(),key = lambda x:x[1]))
        print(sorted((key.lower(),value) for key,value in product_dictionary.items())) #Sort by lower key Value
        print(sorted((key.upper(),value) for key,value in product_dictionary.items())) #Sort by upper key value
        
        #Remove Duplicate value
        
        result = {}
        for key,value in product_dictionary.items():
            if value not in result.values():
                result[key] = value

        print(sorted(result.values())) #Remove Duplicate value and sort it in increasing order
        print(sorted(result.values(),reverse=True)) #Remove Duplicate value and sort it in decreasing order
        
        for key in range(0,len(product_dictionary.items()),2):
            print(product_dictionary.keys()[key])
         
        repeat_value_result = self.repeat_value(product_dictionary)
        print(repeat_value_result)
        dictinonary_lower = dict(sorted((key.lower(),value) for key,value in product_dictionary.items()))
        print(sorted(dictinonary_lower.keys(),key = self.check_month_sequene))# sort the dictionary month wise
        
        print(sorted(dictinonary_lower.keys(),key = self.check_date_of_month)) #sort the dictionary date wise in increasing order
        print(sorted(dictinonary_lower.keys(),key = self.check_date_of_month,reverse = True)) #sort the dictionary date wise in decreasing order        
        
    def Sale(self):
        """
        @Func :- It will sort the sale products month wise
        """     
        sale_dict = {"April":100,"may":500,"June":150,"july":450,"August":200,"september":300,"October":300,"november":200,"December":100,"january":600,"February":500,"march":400}
        print(sale_dict)
        print(sorted(sale_dict))# Sort by Month alphabetically in increasing order
        print(sorted(sale_dict,reverse = True))# Sort by Month alphabetically in decreasing order
        print(sorted(sale_dict.values()))#Sort by it's Value in increasing values
        print(sorted(sale_dict.values(),reverse = True))#Sort by it's Value in decreasing values
        print(sorted(sale_dict,key = sale_dict.__getitem__))#Return Key by sorting Values.
        print(sorted(sale_dict.items(),key = lambda x:x[1]))#Return Key,value pair by sorting Values.
        print(sorted((key.lower(),value) for key,value in sale_dict.items()))#Sort by lower key Value
        print(sorted((key.upper(),value) for key,value in sale_dict.items()))#Sort by upper key Value
        
        repeat_value_result = self.repeat_value(sale_dict)
        print(repeat_value_result)
        
        dictinonary_lower = dict(sorted((key.lower(),value) for key,value in sale_dict.items()))
        print(sorted(dictinonary_lower.keys(),key = self.check_month_sequene))# sort the dictionary month wise
        
        print(sorted(dictinonary_lower.keys(),key = self.check_date_of_month)) #sort the dictionary date wise in increasing order
        print(sorted(dictinonary_lower.keys(),key = self.check_date_of_month,reverse = True)) #sort the dictionary date wise in decreasing order        
        
        
        
dictionary_object = PythonDictionaryMethod()
print("1.Purchase Product:")
print("2.Sale Product:")
print("3.Exit")
while(True):
    number = int(input("Enter the number given in the operation:"))
    if number == 1:
        dictionary_object.Purchase()
    if number == 2:
        dictionary_object.Sale()