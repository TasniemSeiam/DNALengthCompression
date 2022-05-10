# GUI lib
from tkinter import *
# from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# will make tkinter window

root = Tk()
# for giving width & length for window
# NOTE: we dont  use * but x
root.geometry("380x210")

filepath = ""


def readFastq(filename):
    seqs = ""
    with open(filename) as file_1:
        while True:
            file_1.readline()
            seq = file_1.readline().rstrip()
            file_1.readline()
            base = file_1.readline()
            if len(seq) == 0:
                break
            seqs += seq
    return seqs


# getting the fastq file

def Filepath():
    filepath = filedialog.askopenfilename(initialdir="/", title="select a file", filetypes=[("Fastq files", "*.fastq")])
    # call readfastq func.
    re = readFastq(filepath)
    return re


def compression():
    s = entry.get()
    print("Before Compression : ", len(s))

    res = ""
    cnt = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            cnt += 1
        else:
            res = res + s[i - 1]
            if cnt > 1:
                res += str(cnt)
            cnt = 1
    res = res + s[-1]
    if cnt > 1:
        res += str(cnt)

    print("After Compression : ", len(res))

    # creat file and save compressed in it
    ff = open("compressed.txt", 'w')
    ff.write(res + '\n')
    ff.close()

    return messagebox.showinfo('Thanks', f'Gene has been comperissed successfully!')


def showcompress():
    readcompfile = open("compressed.txt", "r")
    readcomp = readcompfile.read()
    readcompfile.close()
    return messagebox.showinfo('Thanks', f'Comperssed Gene \n\n \t {readcomp}')


root.configure(bg="#ffc1b7")
root.title("Gene Length Compression")
label = Label(root, text=" Gene Length Compression ", font="times 15 bold italic", bg="#ff715b", fg="white")
label.pack(side=TOP, fill=X)
# label = Label(root, text=" ", font="times 12 bold italic", bg="black", fg="white")
# label.pack(side=BOTTOM, fill=X)

gene_2_be_compressed = Label(root, text=" Gene to be Compressed ", font="times 14 italic", bg="#ffc1b7")
gene_2_be_compressed.place(x=0, y=80)

gene_2_be_compressed_value = StringVar

entry = Entry(root, textvariable=gene_2_be_compressed_value)
# entry = Text(root, state="normal",height=5,width=20)
entry.place(x=200, y=85, width=170)
entry.insert(END, Filepath())
# entry.pack()


Button(text="Submit", bg="#ff715b", fg="white", command=compression).place(width=110, height=30, x=85, y=120)
Button(text="showcompress", bg="#ff715b", fg="white", command=showcompress).place(width=110, height=30, x=205, y=120)

# closing my project
root.resizable(False, False)
root.mainloop()