import cipher_ascii_art as c, word_dict as w
print(c.logo)
ch="yes"
while(ch=="yes"):
    i=1
    while(i==1):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction=="encode" or direction=="decode":
            i=0
        else:
            print("Invalide Choice")

        
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    def caeser(text,shift,direction):
        new=""
        for i in text:
                if i not in w.alphabet:
                    i=str(i)
                    new=new+i
                else:
                    pos=w.alphabet.index(i)
                    if direction=="encode":
                        new=new+w.alphabet[(pos+shift)%26]
                    elif direction=="decode":
                        new=new+w.alphabet[(pos-shift)%26]
        print(f"The {direction}d text is {new}")
    caeser(text,shift,direction)
    ch=input("Do you want to do this again? Yes or No? ").lower()

print("Good Bye")
