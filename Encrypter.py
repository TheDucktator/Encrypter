import tkinter as tk
import base64

def toenc():
    keyname.configure(text="""Enter your secret key below. 
Use this to unlock the encrytion later.""")
    keyget.delete(0, 'end')
    textlbl.configure(text="Enter the message you want encrypted.")
    textget.configure(state='normal')
    encryptB.configure(text = "Encrypt", command=encrypt)
def todec():
    keyname.configure(text="""Enter your secret key below. 
        The key you received will decypt the message.""")
    keyget.delete(0, 'end')
    textlbl.configure(text="The message will be displayed below.")
    textget.delete("1.0", "10000000.0")
    textget.configure(state='disabled')
    encryptB.configure(text = "Decrypt", command = decrypt)
    
def makeSnafucated():
    #Make Snafucated
    x = 1
def encrypt():
    message = textget.get("1.0", "1000000.0")
    thefile = fileget.get()
    key = keyget.get()
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(message[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    thefile = thefile + ".txt"
    f = open(thefile, 'w')
    f.write(base64.urlsafe_b64encode("".join(enc).encode()).decode())
    f.close()
    keyget.delete(0, 'end')
    
    
def decrypt():
    key = keyget.get()
    thefile = fileget.get()
    thefile = thefile + ".txt"
    f = open(thefile, 'r')
    enc = f.read()
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    textget.configure(state='normal')
    textget.insert('1.0', "".join(dec))
    textget.configure(state='disabled')
    keyget.delete(0, 'end')

window = tk.Tk()
window.title("Encrypter")

encrypter = tk.Button(window, text="Encryption",
    command = toenc)
decryption = tk.Button(window, text="Decryption", 
    command = todec)
decryption.grid(row=1, column=5, columnspan=1)
encrypter.grid(row=1, column=3, columnspan=1)

label1 = tk.Label(window, text="     ")
label2 = tk.Label(window, text="     ")
label3 = tk.Label(window, text=" ")
label1.grid(row=1, column=1, columnspan=2)
label2.grid(row=1, column=7, columnspan=2)
label3.grid(row=2, column=4, columnspan=2)


filenames = tk.Label(window, text="Enter your filename below.")
fileget = tk.Entry(window)
filenames.grid(row=3,column=3, columnspan=3)
fileget.grid(row=4, column=3, columnspan=3)

keyname = tk.Label(window, text="""Enter your secret key below. 
Use this to unlock the encrytion later.""")
keyget = tk.Entry(window)
keyname.grid(row=5,column=3, columnspan=3)
keyget.grid(row=6, column=3, columnspan=3)

textlbl = tk.Label(window, text="Enter the message you want encrypted.")
textget = tk.Text(window, height="10", width="30")
textlbl.grid(row=7,column=3, columnspan=3)
textget.grid(row=8, column=3, columnspan=3)

encryptB = tk.Button(window, text = "Encrypt", command=encrypt)
encryptB.grid(row=9, column=4, columnspan=1)

window.mainloop()
