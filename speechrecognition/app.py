
from tkinter import *                   #xây dựng giao diện
from tkinter import filedialog          #chọn nơi mở và nơi lưu tệp
from tkinter import messagebox as mb    #hiển thị thông báo 
import speech_recognition as sr         #xây dựng hàm nhận diện giọng nói
from playsound import playsound         #phát trực tiếp tệp âm thanh


def listen_file():
    t1.delete('1.0',END) #xóa nội dung có trong widget Text
    r=sr.Recognizer()   #biến để tương tác với các phương thức nhận dạng giọng nói
    mic=sr.Microphone(sample_rate=48000,chunk_size=1024) #biến microphone
    with mic as source: #trình quản lý ngữ cảnh 
        r.adjust_for_ambient_noise(source)  #điều chỉnh lọc tiếng ồn
        mb.showinfo(title="Listen",message="Xin mời nói")   #thông báo để bắt đầu nhận dạng
        audio=r.listen(source)  #biến lưu dữ liệu âm thanh thu được từ microphone
        try:
            text=r.recognize_google(audio,language="vi-VN") #nhận dạng giọng nói dùng API Google SPeech Recognition
            t1.insert('1.0',text)   #hiện thị văn bản nhận dạng được trên widget Text
        except sr.UnknownValueError:
            mb.showerror(title="Speech Recognition", message="Giọng nói không rõ")
        except sr.WaitTimeoutError:
            mb.showerror(title="Speech Recognition", message="Thời gian chờ quá lâu")   #thông báo các trường hợp bị lỗi                   
        except sr.RequestError:
            mb.showerror(title="Speech Recognition", message="Bị lỗi hoặc không có kết nối Internet")

def open_file():
    t1.delete("1.0",END)
    r=sr.Recognizer()
    filetype=(("wav file","*.wav"),("flac file",".flac"),("aiff file",".aiff")) #thiết lập định dạng của tệp âm thanh cần mở
    filename=filedialog.askopenfilename(title="Open a file",initialdir="/",filetypes=filetype) #mở tệp âm thanh

    with sr.AudioFile(filename) as source:
        r.adjust_for_ambient_noise(source)
        playsound(filename) #phát tệp âm thanh
        audio = r.record(source)  #lưu lại dữ liệu từ tệp âm thanh
    try:
        t1.insert('1.0',r.recognize_google(audio,language="vi-VN")) 
  
    except sr.UnknownValueError:
        mb.showerror(title="Speech Recognition", message="Giọng nói không rõ")
    except sr.WaitTimeoutError:
        mb.showerror(title="Speech Recognition", message="Thời gian chờ quá lâu")
    except sr.RequestError:
        mb.showerror(title="Speech Recognition", message="Không có từ khóa hoặc không có kết nối Internet")

def record_file():
    r = sr.Recognizer()
    mic = sr.Microphone(sample_rate=48000,chunk_size=1024)

    mb.showinfo("Recording",message="Xin mời nói")
    with mic as source:
        audio = r.listen(source)
    file=filedialog.asksaveasfile(mode="wb",defaultextension=".wav") #lấy địa chỉ nơi cần lưu tệp
    file.write(audio.get_wav_data())    #chuyển dữ liệu âm thanh nhận dạng được sang định dạng WAV để lưu
    file.close()

w=Tk()                      
w.geometry("500x400+500+200")
w.title("Speech to text")

t1=Text(w,font=("arial",15))                
t1.place(x=10,y=50,width=300,height=300)

b1=Button(w,text="Listen",font=("arial",15),fg="#123234",bg="#03aaf9",command=listen_file)
b1.place(x=350,y=50,width=75,height=75)

b2=Button(w,text="Open",font=("arial",15),fg="#3e331d",bg="#00cc1a",command=open_file)
b2.place(x=350,y=150,width=75,height=75)

b3=Button(w,text="Record",font=("arial",15),fg="#263d4d",bg="#ff4612",command=record_file)
b3.place(x=350,y=250,width=75,height=75)

w.mainloop()
