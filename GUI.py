from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as m
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("ba623367dcfc46f7996d9d29388eec92",
                                                                         "17e48ddd56a74778a057069d587a9ec5"))


def splash(username):
    splash_win = Tk()
    splash_win.title("Music Recommendation App")
    splash_win.geometry("4500x3000")
    splash_win.state('zoomed')
    splash_win.overrideredirect(True)
    Label(splash_win, text="Welcome " + username, fg="green", font=('Times New Roman', 90)).place(x=400, y=350)

    def mainWin():
        splash_win.destroy()
        win = Toplevel()
        win.title("Music Recommendation App")
        win.state('zoomed')
        win.geometry("4500x3000")

        frame1 = Frame(win)
        frame1.pack(anchor=NW, fill=X)
        frame2 = Frame(win, height=600)
        frame2.pack(side=TOP, fill=BOTH)

        def getHappySongs():
            for widgets in frame2.winfo_children():
                widgets.destroy()
            Label(frame2, text='\t').grid(row=0, column=0, padx=20, pady=5, sticky=W)
            Label(frame2, text='Songs\t\t\t\t', font='comics 25 bold underline'). \
                grid(row=0, column=1, pady=5, sticky=W)
            Label(frame2, text='Artist', font='comics 25 bold underline'). \
                grid(row=0, column=2, pady=5, sticky=W)
            genre_list = ['indian']
            s_rec = sp.recommendations(seed_genres=genre_list, limit=70)
            count = 0
            for i in range(70):
                if count < 9:
                    rec = s_rec['tracks'][i]['name']
                    song_id = [s_rec['tracks'][i]['id']]
                    artist = s_rec['tracks'][i]['artists'][0]['name']
                    valence = sp.audio_features(song_id)[0]['valence']
                    if valence >= 0.65:
                        count += 1
                        Label(frame2, text=f'{count} .', font='comics 18 normal'). \
                            grid(row=count, column=0, padx=10, pady=8, sticky=W)
                        Label(frame2, text=rec, font='comics 18 normal').\
                            grid(row=count, column=1, padx=10, pady=8, sticky=W)
                        Label(frame2, text=artist, font='comics 18 normal').\
                            grid(row=count, column=2, padx=10, pady=8, sticky=W)

        def getSadSongs():
            for widgets in frame2.winfo_children():
                widgets.destroy()
            Label(frame2, text='\t').grid(row=0, column=0, padx=20, pady=5, sticky=W)
            Label(frame2, text='Songs\t\t\t\t', font='comics 25 bold underline'). \
                grid(row=0, column=1, pady=5, sticky=W)
            Label(frame2, text='Artist', font='comics 25 bold underline'). \
                grid(row=0, column=2, pady=5, sticky=W)
            genre_list = ['indian']
            s_rec = sp.recommendations(seed_genres=genre_list, limit=70)
            count = 0
            for i in range(70):
                if count < 9:
                    rec = s_rec['tracks'][i]['name']
                    song_id = [s_rec['tracks'][i]['id']]
                    artist = s_rec['tracks'][i]['artists'][0]['name']
                    valence = sp.audio_features(song_id)[0]['valence']
                    if valence <= 0.4:
                        count += 1
                        Label(frame2, text=f'{count} .', font='comics 18 normal'). \
                            grid(row=count, column=0, padx=10, pady=8, sticky=W)
                        Label(frame2, text=rec, font='comics 18 normal').\
                            grid(row=count, column=1, padx=10, pady=8, sticky=W)
                        Label(frame2, text=artist, font='comics 18 normal').\
                            grid(row=count, column=2, padx=10, pady=8, sticky=W)

        def getRelaxedSongs():
            for widgets in frame2.winfo_children():
                widgets.destroy()
            Label(frame2, text='\t').grid(row=0, column=0, padx=20, pady=5, sticky=W)
            Label(frame2, text='Songs\t\t\t\t', font='comics 25 bold underline'). \
                grid(row=0, column=1, pady=5, sticky=W)
            Label(frame2, text='Artist', font='comics 25 bold underline'). \
                grid(row=0, column=2, pady=5, sticky=W)
            genre_list = ['indian']
            s_rec = sp.recommendations(seed_genres=genre_list, limit=70)
            count = 0
            for i in range(70):
                if count < 9:
                    rec = s_rec['tracks'][i]['name']
                    song_id = [s_rec['tracks'][i]['id']]
                    artist = s_rec['tracks'][i]['artists'][0]['name']
                    energy = sp.audio_features(song_id)[0]['energy']
                    if energy <= 0.5:
                        count += 1
                        Label(frame2, text=f'{count} .', font='comics 18 normal'). \
                            grid(row=count, column=0, padx=10, pady=8, sticky=W)
                        Label(frame2, text=rec, font='comics 18 normal').\
                            grid(row=count, column=1, padx=10, pady=8, sticky=W)
                        Label(frame2, text=artist, font='comics 18 normal').\
                            grid(row=count, column=2, padx=10, pady=8, sticky=W)

        def getPartySongs():
            for widgets in frame2.winfo_children():
                widgets.destroy()
            Label(frame2, text='\t').grid(row=0, column=0, padx=20, pady=5, sticky=W)
            Label(frame2, text='Songs\t\t\t\t', font='comics 25 bold underline'). \
                grid(row=0, column=1, pady=5, sticky=W)
            Label(frame2, text='Artist', font='comics 25 bold underline'). \
                grid(row=0, column=2, pady=5, sticky=W)
            genre_list = ['indian']
            s_rec = sp.recommendations(seed_genres=genre_list, limit=70)
            count = 0
            for i in range(70):
                if count < 9:
                    rec = s_rec['tracks'][i]['name']
                    song_id = [s_rec['tracks'][i]['id']]
                    artist = s_rec['tracks'][i]['artists'][0]['name']
                    danceability = sp.audio_features(song_id)[0]['danceability']
                    if danceability >= 0.75:
                        count += 1
                        Label(frame2, text=f'{count} .', font='comics 18 normal'). \
                            grid(row=count, column=0, padx=10, pady=8, sticky=W)
                        Label(frame2, text=rec, font='comics 18 normal').\
                            grid(row=count, column=1, padx=10, pady=8, sticky=W)
                        Label(frame2, text=artist, font='comics 18 normal').\
                            grid(row=count, column=2, padx=10, pady=8, sticky=W)

        def getLoveSongs():
            for widgets in frame2.winfo_children():
                widgets.destroy()

        global pic1
        pic1 = ImageTk.PhotoImage(Image.open('images/happy.png').resize((120, 120)))
        l1 = Label(frame1, text='Happy', fg='dark blue', font='comics 25 bold underline')
        l1.grid(row=0, column=0)
        h = Button(frame1, bd=0, image=pic1, command=lambda: getHappySongs())
        h.grid(row=1, column=0, padx=70, pady=17)

        global pic2
        pic2 = ImageTk.PhotoImage(Image.open("images/sad.png").resize((120, 120)))
        l2 = Label(frame1, text='Sad', fg='dark blue', font='comics 25 bold underline')
        l2.grid(row=0, column=1)
        s = Button(frame1, bd=0, image=pic2, command=lambda: getSadSongs())
        s.grid(row=1, column=1, padx=70, pady=17)

        global pic3
        pic3 = ImageTk.PhotoImage(Image.open("images/love.png").resize((120, 120)))
        l3 = Label(frame1, text='Romantic', fg='dark blue', font='comics 25 bold underline')
        l3.grid(row=0, column=2)
        l = Button(frame1, bd=0, image=pic3, command=lambda: getLoveSongs())
        l.grid(row=1, column=2, padx=70, pady=17)

        global pic4
        pic4 = ImageTk.PhotoImage(Image.open("images/party.png").resize((120, 120)))
        l4 = Label(frame1, text='Party', fg='dark blue', font='comics 25 bold underline')
        l4.grid(row=0, column=3)
        p = Button(frame1, bd=0, image=pic4, command=lambda: getPartySongs())
        p.grid(row=1, column=3, padx=70, pady=17)

        global pic5
        pic5 = ImageTk.PhotoImage(Image.open("images/relaxed.png").resize((120, 120)))
        l5 = Label(frame1, text='Relaxed', fg='dark blue', font='comics 25 bold underline')
        l5.grid(row=0, column=4)
        r = Button(frame1, bd=0, image=pic5, command=lambda: getRelaxedSongs())
        r.grid(row=1, column=4, padx=70, pady=17)

    splash_win.after(500, mainWin)


mainWindow = Tk()
mainWindow.title("Login")
mainWindow.geometry("4500x3000")
mainWindow.state('zoomed')
mainWindow.config()

image1 = Image.open("login.jpg")
image1 = image1.resize((1530, 795), Image.ANTIALIAS)
test1 = ImageTk.PhotoImage(image1)
label1 = Label(image=test1)
label1.image = test1
label1.place(x=0, y=0)


# LOGIN PASSWORD CHECK
def login_check():
    fd = open("login.json")
    dct = json.load(fd)
    username1 = login_username.get().lower()
    password1 = login_password.get()
    for i in dct.keys():
        if dct[i]["username"] == username1 and dct[i]["password"] == password1:
            splash(username1)
            login_username.delete(0, END)
            login_password.delete(0, END)
            break

    else:
        login_username.delete(0, END)
        login_password.delete(0, END)
        m.showerror(title="Error", message="Username and Password don't match")
        login_done = Button(mainWindow, text="Login", bg='#C6E2FF', width=10, font="poppins 12 bold",
                            command=login_check)
        login_done.place(x=450, y=500)


# REGISTRATION INFO SAVING
def get_regIngo():
    username = input_username.get().lower()
    password = input_password.get()
    age = input_age.get()
    gender = input_gender.get()

    if username == '' or password == '':
        m.showinfo(title="Registration Failed", message='Please fill all fields to continue.')
    else:
        try:
            fd = open("login.json")
            dct = json.load(fd)
            dct[len(dct.keys()) + 1] = {"username": username, "password": password, "age": age, "gender": gender}
        except (Exception,):
            dct = {1: {"username": username, "password": password, "age": age, "gender": gender}}
        ls = json.dumps(dct)
        fh = open('login.json', 'w')
        fh.write(ls)
        fh.close()
        m.showinfo(title="Registration Done", message='''Registration successful
            Please Login to continue''')
    input_username.delete(0, END)
    input_password.delete(0, END)
    input_age.delete(0, END)
    input_gender.delete(0, END)


# LOGIN PART
Label(mainWindow, text="LOGIN", fg="red", font="poppins 25 bold").place(x=420, y=170)
Label(mainWindow, text="REGISTER", fg="red", font="poppins 25 bold").place(x=870, y=170)
Label(mainWindow, text="Username:", fg="blue", font="poppins 15 bold").place(x=350, y=270)
login_username = Entry(mainWindow, font="poppins 15 bold")
login_username.place(x=450, y=270)
Label(mainWindow, text="Password ", fg="blue", font="poppins 15 bold").place(x=350, y=370)
login_password = Entry(mainWindow, show="*", font="poppins 15 bold")
login_password.place(x=450, y=370)
Login_done = Button(mainWindow, text="Login", bg='#C6E2FF', width=10, font="poppins 12 bold", command=login_check)
Login_done.place(x=450, y=500)

# REGISTRATION PART
sign_in = Button(mainWindow, text="Register", bg='#C6E2FF', width=10, font="poppins 12 bold", command=get_regIngo)
sign_in.place(x=900, y=500)
Label(mainWindow, text="Username:", fg="red", font="poppins 15 bold").place(x=800, y=270)
input_username = Entry(mainWindow, font="poppins 15 bold")
input_username.place(x=900, y=270)
Label(mainWindow, text="Password ", fg="red", font="poppins 15 bold").place(x=800, y=320)
input_password = Entry(mainWindow, font="poppins 15 bold")
input_password.place(x=900, y=320)
Label(mainWindow, text="Age ", fg="red", font="poppins 15 bold").place(x=800, y=370)
input_age = Entry(mainWindow, font="poppins 15 bold")
input_age.place(x=900, y=370)
Label(mainWindow, text="Gender ", fg="red", font="poppins 15 bold").place(x=800, y=420)
input_gender = Entry(mainWindow, font="poppins 15 bold")
input_gender.place(x=900, y=420)

mainloop()

