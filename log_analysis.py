print('''
  _  _                     _      _   _   
 | || |  __ _   _ _   ___ | |_   (_) | |_ 
 | __ | / _` | | '_| (_-< | ' \  | | |  _|
 |_||_| \__,_| |_|   /__/ |_||_| |_|  \__|
                                          ''')
print("IP \t            Date time \t           Request \t")

with open("website.log","r") as f:
    lines= f.readlines()
with open("output.txt", 'w+') as nf:
    for line in lines:
        line = line.split(" ")
        nf.write("{}\t {}\t  {}\n" .format(line[0],line[3].replace('[',' '),line[5].replace('"',' ')))
            
    

