import customtkinter

# class MyCheckboxFrame(customtkinter.CTkFrame):
#     def __init__(self, master, values):
#         super().__init__(master)
#         self.grid_columnconfigure(0)
#         self.values = values
#         self.checkboxes = []
        

#         for i, value in enumerate(self.values):
#             checkbox = customtkinter.CTkCheckBox(self, text=value, font=(property, 20))
#             checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
#             self.checkboxes.append(checkbox)

#     def get(self):
#         checked_checkboxes = []
#         for checkbox in self.checkboxes:
#             if checkbox.get() == 1:
#                 checked_checkboxes.append(checkbox.cget("text"))
#         return checked_checkboxes
    
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        # self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0, font=(property, 220))
        # self.textbox.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
        # self.textbox.insert("0.0", "카메라\n" * 50)
        # self.textbox.configure(fg_color="gray")
        self.textbox = customtkinter.CTkTextbox(master=self, width=650, height=550, corner_radius=10,font=(property, 25))
        self.textbox.grid(padx= 10, pady=10)
        self.textbox.place(x=650,y=0)
        self.textbox.insert("0.0", "                                     옵션" )
        self.textbox.configure(fg_color="light gray")


        self.title("Limo Camera") #팝업창 이름 설정
        self.geometry("1300x550") #크기 설정
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        # self.place(x=500,y=100)
        self.configure(fg_color="white")
    
        # self.checkbox_frame_1 = MyCheckboxFrame(self, values=["얼굴인식"]) #타이틀, 옵션 생성
        # # self.checkbox_frame_1.grid(row=0, column=1, padx=(490, 0), pady=(135, 0), sticky="nsew" ) #좌표 설정
        # self.checkbox_frame_1.place(x=890,y=100)
        # self.checkbox_frame_1.configure(fg_color="white") # 프레임 바탕색 변경

        self.switch_var = customtkinter.StringVar(value="on")
        self.switch = customtkinter.CTkSwitch(self, text="얼굴인식", command=self.switch_event,variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.place(x=975,y=100)
        self.switch.configure(fg_color="white")
       
        
        
        #전진 버튼
        self.button_1 = customtkinter.CTkButton(self, text="전진", command=self.button_callback) #버튼 생성
        self.button_1.place(x=905,y=300)
        self.button_1.configure(fg_color="green")

        #후진 버튼
        self.button_2 = customtkinter.CTkButton(self, text="후진", command=self.button_callback) #버튼 생성
        self.button_2.place(x=905,y=400)
        self.button_2.configure(fg_color="red")
        
        # self.button = customtkinter.CTkButton(self, text="저장", command=self.button_callback, width=650) #버튼 생성
        # self.button.place(x=650,y=500)

    def button_callback(self):
        print(self.button_1.get())
        print(self.button_2.get())

    def switch_event(self):
        print("switch toggled, current value:", self.switch_var.get())

app = App()
app.mainloop()