import os

def lvm():
	while(True):
		os.system('tput setaf 6')
		print("\t\t\tWelcome to the LVM-Automation")
		os.system('tput setaf 4')
		print("""
		press 1 :  List all the availablle Disk
 		press 2 :  To Create Physical Volume
		Press 3 :  To Describe Physical Volume
		Press 4 :  To Create Volume Group
		Press 5 :  To Describe Volume Group
		Press 6 :  To Create Logical Volume
		Press 7 :  To Describe Logical Volume
		Press 8 :  To Format the partition
		Press 9 :  To Mount Partition to the folder
		Press 10 : Extend the LVM
		Press 11 : Show all the partition
		Press 12 : Exit
		""")
		os.system('tput setaf 7')
		
		ch = int(input("Enter Your Choice :-"))
		print(ch)
		
		if(ch==1):
			os.system("fdisk -l")
		elif(ch==2):
			pvname = input("Enter your Diskname:")
			os.system("pvcreate {}".format(pvname))
		elif(ch==3):
			x = input("Enter your Physical Volume name:")
			os.system("pvdisplay {}".format(x))
		elif(ch==4):
			vgp = input("Enter Volume Group name: ")
			dname = input("Enter your PV name: ")
			os.system("vgcreate {0} {1}".format(vgp,dname))
		elif(ch==5):
			a = input("Enter Volume Group name: ")
			os.system("vgdisplay {}".format(a))
		elif(ch==6):
			lgp = input("Enter Logical volume name: ")
			size = input("Enter size of LV: ")
			vg = input("Enter Volume group name: ")
			os.system("lvcreate --size {0} --name {1} {2}".format(size,lgp,vg))
		elif(ch==7):
			b = input("Enter VG name: ")
			os.system("lvdisplay {}".format(b))
		elif(ch==8):
			c = input("Enter device name to be format :")
			os.system("mkfs.ext4 {}".format(c))
			print("\t\tDevice formatted succesfully")
		elif(ch==9):
			d = input("Create the Directory:")
			os.system("mkdir {}".format(d))
			e = input("Enter the partition name :")
			f = input("Enter the directory to be mount: ")
			os.system("mount {0} {1}".format(e,f))
		elif(ch==10):
			vg = input("Enter VG name :")
			lv = input("Enter LV name :")
			size = input("Enter the size: ")
			os.system("lvextend --size +{0} /dev/{1}/{2}".format(size,vg,lv))
			os.system("resize2fs /dev/{0}/{1}".format(vg,lv))
		elif(ch==11):
			os.system("lsblk")
		elif(ch==12):
			exit()
		else:
			print("Choose valid Option")



lvm()		


