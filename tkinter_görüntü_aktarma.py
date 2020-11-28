import tkinter
import cv2
import PIL.Image,PIL.ImageTk
import time
import urllib
import json
import numpy
import random
import requests

#print(help(requests.status_codes))


class App:
    def __init__(self, window, window_title,geometry =0, video_source=0,video_width=0,video_height=0):
        self.window = window
        self.window.geometry(geometry)
        self.window.state("zoomed")
        self.window.title(window_title)
        self.video_source = video_source
        self.window.resizable(False,False)
        self.first_time = time.time() 
        self.canvas_color = "#ebe426"
        self.constant_height = 20
        self.left_constant = 0
        self.right_constant = 130
        self.center_constant = 0
        self.left_constant_width =int(325 + self.left_constant -self.right_constant/2 -self.center_constant/2)
        self.right_constant_width =int(400 + self.right_constant -self.left_constant/2 -self.center_constant/2)
        self.center_constant_width = int(600 + self.center_constant -self.left_constant/2 -self.right_constant/2)
        self.text_list = ["enlem : ", "boylam : ", "irtifa : ", "dikilme : ","yönelme : ", "yatış : ","zaman farkı :"]
        self.delay = 50

        self.all_objects()
        self.about_data()
        self.comes(self.takım_1_frame2)
        self.comes(self.takım_2_frame2)
        self.comes(self.takım_3_frame2)
        self.comes(self.takım_4_frame2)

        self.frame1_text = self.comes_2(self.takım_1_frame2)
        self.frame2_text = self.comes_2(self.takım_2_frame2)
        self.frame3_text = self.comes_2(self.takım_3_frame2)
        self.frame4_text = self.comes_2(self.takım_4_frame2)

        self.update()
        self.window.mainloop()

    def all_objects(self):  

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
        self.img = PIL.Image.open("C:/PROJELER/iha_GUI/alanya.jpg")
        
        self.cvimg = cv2.cv2.resize(numpy.array(self.img),(int(self.center_constant_width), int(400)), PIL.Image.NEAREST)
        self.img = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cvimg))


        self.video_canvas = tkinter.Canvas(self.window,bg= self.canvas_color, width = int(self.right_constant_width) , height = 700)
        self.map_canvas = tkinter.Canvas(self.window,bg = self.canvas_color,width=int(self.center_constant_width),height=700 )
        self.mostLeft_canvas = tkinter.Canvas(self.window,bg = self.canvas_color, width =int(self.left_constant_width) , height = 700)
        self.map_canvas.create_image(int(self.center_constant_width/2),int(0), image = self.img, anchor = tkinter.N)

        self.video_canvas.place(x = 1360 ,y = 5 ,anchor = tkinter.NE)
        self.map_canvas.place(x = 1350-int(self.right_constant_width) , y = 5 ,anchor = tkinter.NE)
        self.mostLeft_canvas.place(x = 10 , y = 5 , anchor = tkinter.NW)

        self.takım_1_frame = tkinter.Frame(self.mostLeft_canvas ,bg = "blue" , width = int((self.left_constant_width-20)/2) ,height = 220)
        self.takım_2_frame = tkinter.Frame(self.mostLeft_canvas ,bg = "blue" , width = int((self.left_constant_width-20)/2) ,height = 220)
        self.takım_3_frame = tkinter.Frame(self.mostLeft_canvas ,bg = "blue" , width = int((self.left_constant_width-20)/2) ,height = 220)
        self.takım_4_frame = tkinter.Frame(self.mostLeft_canvas ,bg = "blue" , width = int((self.left_constant_width-20)/2) ,height = 220)
        self.sistem_zamanı = tkinter.Frame(self.map_canvas ,bg = "blue" , width = int((self.left_constant_width-15))   ,height = 140)

        self.takım_1_frame2 = tkinter.Frame(self.takım_1_frame ,bg = "green" , width = int((self.left_constant_width-20)/2) ,height = 220)
        self.takım_2_frame2 = tkinter.Frame(self.takım_2_frame ,bg = "green" , width = int((self.left_constant_width-20)/2) ,height = 220)
        self.takım_3_frame2 = tkinter.Frame(self.takım_3_frame ,bg = "green" , width = int((self.left_constant_width-20)/2) ,height = 220)
        self.takım_4_frame2 = tkinter.Frame(self.takım_4_frame ,bg = "green" , width = int((self.left_constant_width-20)/2) ,height = 220)
        
        self.takım_1_labels = tkinter.Label(self.takım_1_frame,text = "TAKIM 1",bg = "red",font=("Times New Roman",15,"bold"))
        self.takım_2_labels = tkinter.Label(self.takım_2_frame,text = "TAKIM 2",bg = "red",font=("Times New Roman",15,"bold"))
        self.takım_3_labels = tkinter.Label(self.takım_3_frame,text = "TAKIM 3",bg = "red",font=("Times New Roman",15,"bold"))
        self.takım_4_labels = tkinter.Label(self.takım_4_frame,text = "TAKIM 4",bg = "red",font=("Times New Roman",15,"bold"))

        self.takım_1_labels.place(x = int((self.left_constant_width-20)/4) ,y = 20,anchor= tkinter.CENTER)
        self.takım_2_labels.place(x = int((self.left_constant_width-20)/4),y = 20,anchor= tkinter.CENTER)
        self.takım_3_labels.place(x = int((self.left_constant_width-20)/4),y = 20,anchor= tkinter.CENTER)
        self.takım_4_labels.place(x = int((self.left_constant_width-20)/4),y = 20,anchor= tkinter.CENTER)

        self.takım_1_frame.place(x = 10,y = 10,anchor = tkinter.NW)
        self.takım_2_frame.place(x = self.left_constant_width - 5,y = 10,anchor = tkinter.NE)
        self.takım_3_frame.place(x = 10 ,y = 20+250,anchor = tkinter.NW)
        self.takım_4_frame.place(x = self.left_constant_width - 5,y = 20 + 250,anchor = tkinter.NE)

        self.takım_1_frame2.place(x = int((self.left_constant_width-20)/4),y = 125,anchor = tkinter.CENTER)
        self.takım_2_frame2.place(x = int((self.left_constant_width-20)/4),y = 125,anchor = tkinter.CENTER)
        self.takım_3_frame2.place(x = int((self.left_constant_width-20)/4),y = 125,anchor = tkinter.CENTER)
        self.takım_4_frame2.place(x = int((self.left_constant_width-20)/4),y = 125,anchor = tkinter.CENTER)

        self.sistem_zamanı.place(x = int((self.left_constant_width)/2)+3,y = 540,anchor = tkinter.N)

        

        self.delay_ = tkinter.Label(self.sistem_zamanı,text = "Delay time :",width = 20,height = 2,bg = "red",font=("Times New Roman",10,"bold"))
        self.delay_.grid(row =0,column =0,sticky = tkinter.W)
        self.delay_text = tkinter.Label(self.sistem_zamanı,text = "",width = 20,height = 2,bg = "red",font=("Times New Roman",10,"bold"))
        self.delay_text.grid(row =0,column =1,sticky = tkinter.W)
  
    def about_data(self):
        self.data_frame = tkinter.Frame(self.video_canvas,bg = "blue" , width = int((self.right_constant_width-15)) ,height = 170)
        self.enter_button = tkinter.Button(self.data_frame, text = "Giriş",width = 19,bg = "red",command= self.giris)
        self.out_button = tkinter.Button(self.data_frame, text = "Çıkış",width = 19,bg = "red")
        self.entry_adress = tkinter.Entry(self.data_frame,width = 30)
        self.user_name = tkinter.Entry(self.data_frame,width = 30)
        self.password = tkinter.Entry(self.data_frame,width = 30)
        self.adress_text = tkinter.Label(self.data_frame,text="Ağ Adresi",width = 20,bg = "green")
        self.user_name_text = tkinter.Label(self.data_frame,text="Kullanıcı adı",width = 20,bg = "green")
        self.password_text = tkinter.Label(self.data_frame,text="Parola",width = 20,bg = "green")
        self.status_code = tkinter.Label(self.data_frame,text = "Status code",fg = "red",font=("Times New Roman",20,"bold"), width = 9,height = 1)
               


        self.data_frame.place(x = 10,y = 690,anchor = tkinter.SW)
        self.enter_button.place(x = 505,y =110,anchor = tkinter.NE)
        self.out_button.place(x = 505,y =140,anchor = tkinter.NE)
        self.entry_adress.place(x=170,y=10)
        self.user_name.place(x=170,y=41)
        self.password.place(x=170,y=72)
        self.adress_text.place(x=10,y = 10)
        self.user_name_text.place(x=10,y = 40)
        self.password_text.place(x=10,y = 70)
        self.status_code.place(x = 509,y = 10,anchor = tkinter.NE)

    def giris(self):
        self.adres,kullanıcı,parola = (self.entry_adress.get(),self.user_name.get(), self.password.get())
        data = {
            "kadi":"{}".format(kullanıcı),
            "sifre":"{}".format(parola)
                }
        #r = requests.post(url = self.adres+"/api/giris",data=data)
        r = requests.post(url = 'http://95.172.70.131:12975',data = data)
        status = r.status_code
        self.status_code["text"] = status
        r = r.text
        print(self.adres,kullanıcı,parola,r,status)
    def cıkıs(self):
        r = requests.get(url= self.adres+"/api/cikis")
        r = r.text
    def telemetri_gonder(self):
        data ={ "takim_numarasi": 1, 
                "IHA_enlem": 433.5, 
                "IHA_boylam": 222.3, 
                "IHA_irtifa": 222.3, 
                "IHA_dikilme": 5, 
                "IHA_yonelme": 256, 
                "IHA_yatis": 0, 
                "IHA_hiz": 223, 
                "IHA_batarya": 20, 
                "IHA_otonom": 0, 
                "IHA_kilitlenme": 1, 
                "Hedef_merkez_X": 315, 
                "Hedef_merkez_Y": 220, 
                "Hedef_genislik": 12, 
                "Hedef_yukseklik": 46, 
                "GPSSaati": {         
                            "saat": 19,         
                            "dakika": 1,         
                            "saniye": 23,        
                            "milisaniye": 507     
                            } 
                } 
        r = requests.post(url = self.adres+" /api/telemetri_gonder",data= data)
        r = r.json()
    def sunucu_saati(self):
        self.server_time = requests.get(url = self.adres+"/api/sunucusaati")
    def kilitlenme_bilgisi(self):
        data = {     
                "kilitlenmeBaslangicZamani": {         
                    "saat": 19,         
                    "dakika": 1,         
                    "saniye": 23,         
                    "milisaniye": 507     
                    },     
                "kilitlenmeBitisZamani": {         
                    "saat": 19,         
                    "dakika": 1,         
                    "saniye": 45,         
                    "milisaniye": 236     
                    },     
                "otonom_kilitlenme": 0 
  
                }
        r = requests.post(url = self.adres+"/api/kilitlenme_bilgisi",data= data)
        r = r.text

    def comes(self,takım_numarası):
        for text in self.text_list:
            takım_text = tkinter.Label(takım_numarası,text = text,width = 10,bg = "orange",font=("Times New Roman",10,"bold"))
            takım_text.grid(row = self.text_list.index(text),column= 0,sticky = tkinter.E)
       
    def comes_1(self,takım_ismi):
        takım_ismi[0]["text"] = "{}".format(random.randint(1,100))
        takım_ismi[1]["text"] = "{}".format(random.randint(1,100))
        takım_ismi[2]["text"] = "{}".format(random.randint(1,100))
        takım_ismi[3]["text"] = "{}".format(random.randint(1,100))
        takım_ismi[4]["text"] = "{}".format(random.randint(1,100))
        takım_ismi[5]["text"] = "{}".format(random.randint(1,100))
        takım_ismi[6]["text"] = "{}".format(random.randint(1,100))

    def comes_2(self,takım_numarası):
        text_list = []
        for i in range(7):
            text = tkinter.Label(takım_numarası,text = "SERDAR",width = 10,bg = "orange",font=("Times New Roman",10,"bold"))
            text.grid(row = i,column= 1,sticky = tkinter.W)
            text_list.append(text)
        return text_list
    def delay_time(self,initial_time,final_time): 
        self.delay_text["text"] = round(final_time - initial_time + self.delay/1000,4)
        self.delay_text["padx"] = 20

    def update(self):
        last_time = time.time()

        self.comes_1(self.frame1_text)
        self.comes_1(self.frame2_text)
        self.comes_1(self.frame3_text)
        self.comes_1(self.frame4_text)
    
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        frame =cv2.cv2.resize(frame,(int(self.right_constant_width) , 400), PIL.Image.NEAREST)
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.video_canvas.create_image(int(self.right_constant_width)/2,0, image = self.photo, anchor = tkinter.N)
        self.delay_time(last_time,time.time())
        self.window.after(self.delay, self.update)

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.cv2.VideoCapture(video_source)

        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)


    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cv2.cvtColor(frame, cv2.cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()




App(tkinter.Tk(), "İHA GUI","1356x700+0+0")