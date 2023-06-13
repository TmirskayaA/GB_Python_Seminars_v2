import json 

string_1 = '{"subj1":"Computer Science","subj2":"Physics","subj3":"Chemistry","subj4":"Mathematics"}' 
print("String_1 is ",string_1) 

res_dict=json.loads(string_1) 

print("The resultant dictionary is ",res_dict) 