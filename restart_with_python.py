import os       #importing os liabrary 
check = input('Want to shutdown your PC ? (y/n):')      #Display prompt if user want to restart pc or not
if check == 'n':                    #if user presses n it will exit 
	exit()
else:                               #else it will restart pc
	os.system('shutdown /r /t 5')
