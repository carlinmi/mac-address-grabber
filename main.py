import subprocess
import re

def get_physical_mac_addresses():
    result = str(subprocess.run('ipconfig /all', capture_output=1))
    expression = re.compile(r'(Physical Address(?:\.\s)+:\s(?:[A-a-z0-9][A-a-z0-9]-?){6})')
    physical_addresses = re.findall(expression, result)
    clean_addresses = [address.split(':')[1].strip() for address in physical_addresses]
    return clean_addresses


def get_removable_disk_drive_leter():
    result = str(subprocess.run('wmic logicaldisk get deviceid, volumename, description', capture_output=1))
    removable_disk_drive_leter_regular_expression = r'(?:Removable Disk\s*)([A-Z])(?::\s*MAC-address)'
    removable_disk_drive_leter = re.search(removable_disk_drive_leter_regular_expression, result).group(1)
    return removable_disk_drive_leter


# print(get_physical_mac_addresses())
print(get_removable_disk_drive_leter())

#add SSH Remote on Mac
#add SSH Remote on PC
#test ssh 2

#Egit clone git@github.com:octocat/Spoon-Knife