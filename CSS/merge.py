files_names = [
   "colour-theme",
   "grid",
   "custom",
   "menus",
   "chatbox",
   "icomoon",
   "kvikun" ]
data = ""

for file_name in files_names :
   with open(file_name+".css" ,"r") as file_handle :
      temp_data = file_handle.read()
      data = data + temp_data 

with open ('styles.min.css', 'w') as file_handle : 
  file_handle.write(data)