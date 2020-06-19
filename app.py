from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from dbhelper import DBHelper
from tkinter import filedialog
import shutil,os


class Tinder:

    def __init__(self):


        self.db = DBHelper()
        # Load GUI
        self.load_login_window()

    def load_login_window(self):
        self._root = Tk()

        self._root.title("Tinder Login™")
        self._root.minsize(400, 600)
        self._root.maxsize(400, 600)
        self._root.config(background="#FE3C72")

        self._label = Label(self._root, text="♠Tinder", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 30))
        self._label.pack(pady=(20, 0))

        self._label = Label(self._root, text="♥ Onestep Solution for Single-ism ♥", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 10))
        self._label.pack(pady=(1, 20))

        self._email = Label(self._root, text="Email", fg="#fff", bg="#FE3C72")
        self._email.config(font=("Times", 16))
        self._email.pack(pady=(10, 0))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(0, 15), ipady=10, ipadx=30)

        self._password = Label(self._root, text="Password", fg="#fff", bg="#FE3C72")
        self._password.config(font=("Times", 16))
        self._password.pack(pady=(5, 0))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(1, 35), ipady=10, ipadx=30)

        self._login = Button(self._root, text="Login ☼", fg="#fff", bg="#FE3C72", width=25, height=2,
                             command=lambda: self.check_login())
        self._login.config(font=("sans-serif", 10))
        self._login.pack()

        self._label = Label(self._root, text="-" * 10 + "or" + '-' * 10, fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 10))
        self._label.pack(pady=(10, 0))

        self._label = Label(self._root, text="Register today to find your love ☻", fg="#fff", bg="#FE3C72")
        self._label.config(font=("Comic Sans MS", 10))
        self._label.pack(pady=(1, 20))

        self._reg = Button(self._root, text="Sign up ■", fg="#fff", bg="#FE3C72", width=25, height=2,
                           command=lambda: self.regwindow())
        self._reg.config(font=("sans-serif", 10))
        self._reg.pack()

        self._root.mainloop()

    def check_login(self):
        email = self._emailInput.get()
        password = self._passwordInput.get()
        data = self.db.check_login(email, password)
        # print(data)
        if len(data) == 0:
            # print("Invalid Credentials")
            messagebox.showerror("Error", "Invalid Credentials")
        else:
            self.user_id = data[0][0]
            self.is_logged_in = 1
            self.login_handler()

    def regwindow(self):
        self.clear()
        self._name = Label(self._root, text="Name", fg="#fff", bg="#FE3C72")
        self._name.config(font=("Comic Sans MS", 16))
        self._name.pack(pady=(5, 0))

        self._nameInput = Entry(self._root)
        self._nameInput.pack(pady=(0, 5), ipady=5, ipadx=20)

        self._email = Label(self._root, text="Email", fg="#fff", bg="#FE3C72")
        self._email.config(font=("Comic Sans MS", 16))
        self._email.pack(pady=(5, 0))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(0, 5), ipady=4, ipadx=28)

        self._password = Label(self._root, text="Password", fg="#fff", bg="#FE3C72")
        self._password.config(font=("Comic Sans MS", 16))
        self._password.pack(pady=(5, 0))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(0, 5), ipady=4, ipadx=28)

        self._gender = Label(self._root, text="Gender", fg="#fff", bg="#FE3C72")
        self._gender.config(font=("Comic Sans MS", 16))
        self._gender.pack(pady=(5, 0))

        self._genderInput = Entry(self._root)
        self._genderInput.pack(pady=(0, 5), ipady=4, ipadx=28)

        self._age = Label(self._root, text="Age", fg="#fff", bg="#FE3C72")
        self._age.config(font=("Comic Sans MS", 16))
        self._age.pack(pady=(5, 0))

        self._ageInput = Entry(self._root)
        self._ageInput.pack(pady=(0, 5), ipady=5, ipadx=20)

        self._city = Label(self._root, text="City", fg="#fff", bg="#FE3C72")
        self._city.config(font=("Comic Sans MS", 16))
        self._city.pack(pady=(5, 0))

        self._cityInput = Entry(self._root)
        self._cityInput.pack(pady=(0, 5), ipady=4, ipadx=28)

        self.dp = Button(self._root, text="Select a picture", command=lambda: self.select_dp())
        self.dp.pack(pady=(5, 0))

        self.dp_filename = Label(self._root)
        self.dp_filename.pack(pady=(0, 5))

        self._reg = Button(self._root, text="Sign Up ►", fg="#fff", bg="#FE3C72", width=25, height=2,
                           command=lambda: self.reg_handler())
        self._reg.config(font=("Comic Sans MS", 10))
        self._reg.pack(side=LEFT)

        self._reg = Button(self._root, text="←- Back", fg="#fff", bg="#FE3C72", width=25, height=2,
                           command=lambda: self.logout())
        self._reg.config(font=("Comic Sans MS", 10))
        self._reg.pack(side=LEFT)

    def select_dp(self):
        self.filename = filedialog.askopenfilename(initialdir="/images", title="Somrhting")
        self.dp_filename.config(text=self.filename)

    def reg_handler(self):

        actual_filename = self.filename.split("/")[-1]

        flag = self.db.register(self._nameInput.get(), self._emailInput.get(), self._passwordInput.get(),
                                self._ageInput.get(), self._genderInput.get(), self._cityInput.get(),
                                actual_filename)

        if flag == 1:

            # File upload

            destination = "C:\\Users\\jawed\\PycharmProjects\\tinder\\images\\" + actual_filename
            shutil.copyfile(self.filename, destination)
            messagebox.showinfo("Success", "Registered Successfully. Login to proceed")
            self._root.destroy()
            self.load_login_window()
        else:
            messagebox.showerror("Error", "Try again!")

    def mainWindow(self, data, flag=0, index=0):
        # Display remaining info about the user

        name = str(data[index][1]) + "," + str(data[index][4])
        # email = "Email: " + str(data[0][2])
        # age = "Age: " + str(data[0][4])
        gender = str(data[index][5]) + " | " + str(data[index][6])
        # city = "City: " + str(data[0][6])
        dp = data[index][7]

        imageUrl = "images/{}".format(data[index][7])

        load = Image.open(imageUrl)
        load = load.resize((350, 320), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render

        img.pack(pady=(5, 5))

        name_label = Label(self._root, text=name, fg="#472A23", bg="#fff")
        name_label.config(font=("Comic Sans MS", 16))
        name_label.pack(pady=(7, 0), ipady=4, ipadx=150)

        # email_label = Label(self._root, text=email, fg="#fff", bg="#F60A40")
        # email_label.config(font=("Arial", 16))
        # email_label.pack(pady=(5, 10))

        # age_label = Label(self._root, text=age, fg="#fff", bg="#F60A40")
        # age_label.config(font=("Arial", 16))
        # age_label.pack(pady=(5, 10))

        gender_label = Label(self._root, text=gender, fg="#472A23", bg="#fff")
        gender_label.config(font=("Times New Roman", 12))
        gender_label.pack(pady=(0, 10), ipady=4, ipadx=180)

        # city_label = Label(self._root, text=city, fg="#fff", bg="#F60A40")
        # city_label.config(font=("Arial", 16))
        # city_label.pack(pady=(5, 10))

        if flag == 1:
            frame = Frame(self._root)
            frame.pack()

            previous = Button(frame, text="◄- Previous", fg="#fff", bg="#FE3C72", width=15, height=2,
                              command=lambda: self.view_others(index - 1))
            previous.pack(side=LEFT)

            propose = Button(frame, text="propose", fg="#fff", bg="#FE3C72", width=15, height=2,
                             command=lambda: self.propose(self.user_id, data[index][0]))
            propose.pack(side=LEFT)

            next = Button(frame, text="Next -►", fg="#fff", bg="#FE3C72", width=15, height=2,
                          command=lambda: self.view_others(index + 1))
            next.pack(side=LEFT)

        elif flag == 2:
            frame = Frame(self._root)
            frame.pack()

            previous = Button(frame, text="◄- Previous", fg="#fff", bg="#FE3C72", width=15, height=2,
                              command=lambda: self.view_proposals(index - 1))
            previous.pack(side=LEFT)

            propose = Button(frame, text="Propose", fg="#fff", bg="#FE3C72", width=15, height=2,
                             command=lambda: self.propose(self.user_id, data[index][0]))
            propose.pack(side=LEFT)

            next = Button(frame, text="Next -►", fg="#fff", bg="#FE3C72", width=15, height=2,
                          command=lambda: self.view_proposals(index + 1))
            next.pack(side=LEFT)

        elif flag == 3:
            frame = Frame(self._root)
            frame.pack()

            previous = Button(frame, text="◄- Previous", fg="#fff", bg="#FE3C72", width=15, height=2,
                              command=lambda: self.view_requests(index - 1))
            previous.pack(side=LEFT)

            next = Button(frame, text="Next -►", fg="#fff", bg="#FE3C72", width=15, height=2,
                          command=lambda: self.view_requests(index + 1))
            next.pack(side=LEFT)

        elif flag == 4:
            frame = Frame(self._root)
            frame.pack()

            previous = Button(frame, text="◄- Previous", fg="#fff", bg="#FE3C72", width=15, height=2,
                              command=lambda: self.view_matches(index - 1))
            previous.pack(side=LEFT)

            next = Button(frame, text="Next -►", fg="#fff", bg="#FE3C72", width=15, height=2,
                          command=lambda: self.view_matches(index + 1))
            next.pack(side=LEFT)

    def propose(self, romeo, juliet):
        flag = self.db.insert_proposal(romeo, juliet)
        if flag == 1:
            messagebox.showinfo("congrats", "proposal sent.Fingers Crossed!")

        elif flag == 2:
            messagebox.showerror("Error", "kitni baar propose karoge?")
        else:
            messagebox.showerror("Nahi hua ", "Din hi kharab hai")

    def login_handler(self):
        # To load user's profile
        # clear screen
        self.clear()
        self.headerMenu()
        data = self.db.fetch_userdata(self.user_id)
        self.mainWindow(data, flag=0)

    def clear(self):
        for i in self._root.pack_slaves():
            print(i.destroy())

    def view_others(self, index=0):

        # fetch data of all other users from db
        data = self.db.fetch_otheruserdata(self.user_id)

        if index == 0:
            self.clear()
            self.mainWindow(data, flag=1, index=0)
        else:
            if index < 0:
                messagebox.showerror("No user Left", "Click on next")
            elif index == len(data):
                messagebox.showerror("No user Left", "click on previous")
            else:
                self.clear()
                self.mainWindow(data, flag=1, index=index)

    def logout(self):

        self.is_logged_in = 0
        self._root.destroy()
        self.load_login_window()

    def headerMenu(self):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command=lambda: self.login_handler())
        filemenu.add_command(label="Edit Profile", command=lambda: self.edit_user())
        filemenu.add_command(label="view profile", command=lambda: self.view_others())
        filemenu.add_command(label="LogOut ←┘", command=lambda: self.logout())

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals", command=lambda: self.view_proposals())
        helpmenu.add_command(label="My Requests", command=lambda: self.view_requests())
        helpmenu.add_command(label="My Matches", command=lambda: self.view_matches())

    def view_proposals(self, index=0):

        data = self.db.fetch_proposals(self.user_id)
        new_data = []
        if len(data) == 0:
            self.clear()
            result = Label(self._root, text="There is no user Currently...", fg="#fff", bg="#FE3C72")
            result.config(font=("Comic Sans MS", 20))
            result.pack(pady=(280, 40))
        else:
            for i in data:
                new_data.append(i[3:])
            if index == 0:
                self.clear()
                self.mainWindow(new_data, flag=2, index=0)
            else:
                if index < 0:
                    messagebox.showerror("Error", "No user left")
                elif index == len(new_data):
                    messagebox.showerror("Error", "No user left")
                else:
                    self.clear()
                    self.mainWindow(new_data, flag=2, index=index)
        # print(data)
        # print(new_data)

    def view_requests(self, index=0):
        data = self.db.fetch_requests(self.user_id)
        new_data = []
        if len(data) == 0:
            self.clear()
            result = Label(self._root, text="No request Found...", fg="#fff", bg="#FE3C72")
            result.config(font=("Comic Sans MS", 20))
            result.pack(pady=(280, 40))
        else:
            for i in data:
                new_data.append(i[3:])

            if index == 0:
                self.clear()
                self.mainWindow(new_data, flag=3, index=0)
            else:
                if index < 0:
                    messagebox.showerror("Error", "No user left")
                elif index == len(new_data):
                    messagebox.showerror("Error", "No user left")
                else:
                    self.clear()
                    self.mainWindow(new_data, flag=3, index=index)

        # print(data)
        # print(new_data)

    def view_matches(self, index=0):

        data = self.db.fetch_matches(self.user_id)

        new_data = []

        if len(data) == 0:
            self.clear()
            result = Label(self._root, text="No user Found...", fg="#fff", bg="#FE3C72")
            result.config(font=("Comic Sans MS", 20))
            result.pack(pady=(280, 40))
        else:

            for i in data:
                new_data.append(i[3:])

            if index == 0:
                self.clear()
                self.mainWindow(new_data, flag=4, index=0)
            else:
                if index < 0:
                    messagebox.showerror("Error", "No user left")
                elif index == len(new_data):
                    messagebox.showerror("Error", "No user left")
                else:
                    self.clear()
                    self.mainWindow(new_data, flag=4, index=index)

    def edit_user(self):

        data = self.db.fetch_userdata(self.user_id)
        self.clear()

        # self._email1 = Label(self._root, text=" Enter New Email id ", fg="#fff", bg="#FE3C72")
        # self._email1.config(font=("Times", 16))
        # self._email1.pack(pady=(10, 0))

        # self._email1Input = Entry(self._root)
        # self._email1Input.pack(pady=(1, 20), ipady=5, ipadx=30)

        # self._password1 = Label(self._root, text="Enter New Password", fg="#fff", bg="#FE3C72")
        # self._password1.config(font=("Times", 16))
        # self._password1.pack(pady=(10, 0))

        # self._password1Input = Entry(self._root)
        # self._password1Input.pack( #pady =(1, 20), #ipady=5, #ipadx=30)

        # self._name1 = Label(self._root, text="Enter your new Name", fg="#fff", bg="#FE3C72")
        # self._name1.config(font=("Times", 16))
        # self._name1.pack(#pady=(10, 0))

        # self._name1Input = Entry(self._root)
        # self._name1Input.pack(#pady=(1, 20), #ipady=5, #ipadx=30)

        self._age = Label(self._root, text="Age", fg="#fff", bg="#FE3C72")
        self._age.config(font=("Comic Sans MS", 16))
        self._age.pack(pady=(10, 0))

        self._ageInput = Entry(self._root)
        self._ageInput.insert(0, data[0][4])
        self._ageInput.pack(pady=(1, 20), ipady=5, ipadx=30)

        self._gender = Label(self._root, text="Gender", fg="#fff", bg="#FE3C72")
        self._gender.config(font=("Comic Sans MS", 16))
        self._gender.pack(pady=(10, 0))

        self._genderInput = Entry(self._root)
        self._genderInput.insert(0, data[0][5])
        self._genderInput.pack(pady=(1, 20), ipady=5, ipadx=30)

        self._city = Label(self._root, text="City", fg="#fff", bg="#FE3C72")
        self._city.config(font=("Comic Sans MS", 16))
        self._city.pack(pady=(10, 0))

        self._cityInput = Entry(self._root)
        self._cityInput.insert(0, data[0][6])
        self._cityInput.pack(pady=(1, 20), ipady=5, ipadx=30)

        self.dp = Button(self._root, text="Update Info", command=lambda: self.update_info())
        self.dp.pack(pady=(5, 5))

    def update_info(self):

        flag = self.db.update_info(self._genderInput.get(), self._ageInput.get(), self._cityInput.get(), self.user_id)

        if flag == 1:
            messagebox.showinfo("Success", "Profile Updated")
        else:
            messagebox.showerror("Error", "Try Again!")


obj = Tinder()
