# axemo-
#Author Olu Michael
transactions logic

##### open "app.py" for the main code of af all the processes working together. the main background codes started from line 700 the other codes above line 700 are just mainly codes for rendering the tkinter GUI. but there are also some useful code between those GUI codes.####

#### also see "BITPAPP.py" you might find something useful there.####

##### I also added luno transfers and adress geneation apps and also transaction list checker app 

I used normal threads for the asynchronous code execution because celery was too complicated to set-up and i discovered that they 
basically do the same thing. but celery just needed extra protocols. celery just takes data from the message queue and processes it with
the functions written under it. it executes codes in a thread different fom the main thread. meaning it executes the programs at the same 
as the main programs. this is what the threads i used for this program does. but the difference is that it doesnt need any message queue 
to take data for processing. and also celery would not have helped with this because we needed a code to run on it own at intervals and
query for the transactions list from the endpoints. so, the threads i used executes the functions without waiting for any data to be fed to
it. i used 'while' loops together with try-except blocks. so that the back ground programs continue to run and i programmed it to restart 
the process incase it encounters any errors. i also timed the funcions with time.sleep() functions. you pass in arguments in the function
as an integer or a floating number as seconds. if u pass in '5', the program waits for 5 seconds before running. 
