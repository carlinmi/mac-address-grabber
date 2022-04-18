import subprocess
import re



result = str(subprocess.run('ipconfig /all', capture_output=1))

expression = re.compile(r'(Physical Address(?:\.\s)+:\s(?:[A-a-z0-9][A-a-z0-9]-?){6})')
physical_addresses = re.findall(expression, result)

clean_addresses = [address.split(':')[1].strip() for address in physical_addresses]



print(clean_addresses)

#add SSH Remote on Mac
#add SSH Remote on PC
#test ssh 2

#Egit clone git@github.com:octocat/Spoon-Knife