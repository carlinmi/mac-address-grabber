import subprocess
import re

def get_physical_mac_addresses():
    # run the ipconfig /all command and capture the output
    result = str(subprocess.run('ipconfig /all', capture_output=1)) 

    # create regular expression to roughly parse out the physical mac addresses
    expression = r'(Physical Address(?:\.\s)+:\s(?:[A-a-z0-9][A-a-z0-9]-?){6})'
   
    # find all phbysical adresses bases on the above expression
    physical_addresses = re.findall(expression, result) 
    
    # extract the mac adresses from the parsed info and add them to a list
    clean_addresses = [address.split(':')[1].strip() for address in physical_addresses] 
    
    # return the list of clean mac addresses
    return clean_addresses 


def get_removable_disk_drive_leter():
    # get a list of all drives on the computer
    result = str(subprocess.run('wmic logicaldisk get deviceid, volumename, description', capture_output=1)) 

    # create a regular expression to find the correct drive letter fot the removable drive
    removable_disk_drive_leter_regular_expression = r'(?:Removable Disk\s*)([A-Z])(?::\s*OIT-CONFIG)'

    # find the drive letter
    removable_disk_drive_leter = re.search(removable_disk_drive_leter_regular_expression, result).group(1) 
    
    return removable_disk_drive_leter 

# open mac-adresses.txt, append the addresses to it and save/close the file
with open(f'{get_removable_disk_drive_leter()}:\\mac-addresses.txt', 'a') as file:
    mac_addresses = get_physical_mac_addresses()
    for address in mac_addresses:
        file.write(address + '\n')


