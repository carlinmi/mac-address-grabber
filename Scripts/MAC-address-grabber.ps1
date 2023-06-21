$thisPath = $MyInvocation.MyCommand.Path
$thisDrive = $thisPath[0]
$destPath = $thisDrive + ":/MacAddressGrabber/MacAddresses.txt"

get-netadapter | select MacAddress | foreach-object MacAddress | add-content $destPath

$message = "Addresses added to " + $destPath + "`nPress Enter to exit"
Read-Host -Prompt $message