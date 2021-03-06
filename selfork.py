
from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import *
import time


class instagramModul:
    def __init__(self, username, password, urlto):
        self.PATH = "C:\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
        self.username = username
        self.password = password
        self.user = urlto
        self.url = "https://www.instagram.com/?hl=tr"
        self.urlto = f"https://www.instagram.com/{urlto}/followers/"
        self.urlToflw = f"https://www.instagram.com/{urlto}/following/"

    def getting(self, url):
        self.drivercontrol = self.driver.get(url)
        time.sleep(1)

    def loginsystem(self, second):
        self.getting(self.url)
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(self.username)
        password.send_keys(self.password)
        button = self.driver.find_elements_by_class_name("sqdOP")
        button[1].click()
        self.driver.implicitly_wait(second)
        time.sleep(4)

    def dataFork(self):
        self.getting(self.urlto)
        time.sleep(3)

        pop_up_window = WebDriverWait(
            self.driver, 2).until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='_aano']")))  # UPDATE CLASS!
        array = [0, 1, 2, 3, 4]
        counter = -1
        followers = self.driver.find_elements_by_class_name("_ac2a")  # UPDATE CLASS!
        followerCount = int(followers[1].text)
        while True:
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
            time.sleep(1)
            users = self.driver.find_elements_by_css_selector(
                "._aacl._aaco._aacw._aacx._aad7._aade")  # UPDATE CLASS!
            usersLength = len(users)
            counter += 1
            # NEW! ??nerilen kullan??c??lar i??in al??nan ??nlem.
            if(usersLength >= followerCount):
                break
            if(counter == 5):
                counter = 0
            array.insert(counter, usersLength)
            if(array[0] == array[1] and array[0] == array[2] and array[0] == array[3] and array[0] == array[4]):
                break

        users = self.driver.find_elements_by_css_selector(
            "._aacl._aaco._aacw._aacx._aad7._aade")  # UPDATE CLASS!

        # Liste tan??mlamas?? ve kullan??c?? adlar??n??n aktar??lmas??.
        flwrs_list = []
        for item in users:
            counter += 1
            flwrs_list.insert(counter, item.text)
        print(
            "===================[Takip??i Listesi ??ekildi]=======================================")
        print("          {user} Kullan??c??s??n??n Takip??iler listesinin uzunlu??u: {len}".format(
            user=self.user, len=len(flwrs_list))),
        print("===================================================================================")

        self.getting(self.urlToflw)
        time.sleep(3)

        pop_up_window = WebDriverWait(
            self.driver, 2).until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='_aano']")))  # UPDATE CLASS!
        array = [0, 1, 2, 3, 4]
        counter = -1
        follow = self.driver.find_elements_by_class_name("_ac2a")  # UPDATE CLASS!
        followCount = int(follow[2].text)

        while True:
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
            time.sleep(1)
            users = self.driver.find_elements_by_css_selector("._aacl._aaco._aacw._aacx._aad7._aade")  # UPDATE CLASS!
            usersLength = len(users)
            counter += 1
            # NEW! ??nerilen kullan??c??lar i??in al??nan ??nlem.
            if(usersLength >= followCount):
                break
            if(counter == 5):
                counter = 0
            array.insert(counter, usersLength)
            if(array[0] == array[1] and array[0] == array[2] and array[0] == array[3] and array[0] == array[4]):
                break

        users = self.driver.find_elements_by_css_selector("._aacl._aaco._aacw._aacx._aad7._aade")  # UPDATE CLASS!

        flw_list = []  # Liste tan??mlamas?? ve kullan??c?? adlar??n??n aktar??lmas??.
        for item in users:
            counter += 1
            flw_list.insert(counter, item.text)
        print(
            "========================[Takip Edilenler Listesi ??ekildi]=======================================")
        print("           {user} Kullan??c??s??n??n Takip listesinin uzunlu??u: {len}".format(
            user=self.user, len=len(flw_list)))
        print("================================================================================================\n\n\n")
        doNotFollow = []
        doNotFollowers = []
        doNotFollow = list(set(flw_list) - set(flwrs_list))
        doNotFollowers = list(set(flwrs_list) - set(flw_list))
        doNotFollowCount=len(doNotFollow)
        doNotFollowerCount=len(doNotFollowers)
        print("{user} kullan??c??s??n?? Takip etmeyenler: {doNotFollow}\n".format(
            user=self.user, doNotFollow=doNotFollow))
        print("{user} kullan??c??s??n??n Takip etmedikleri: {doNotFollowers}\n\n".format(
            user=self.user, doNotFollowers=doNotFollowers))
        lostFollowers = followerCount-len(flwrs_list)
        lostFollow = followCount-len(flw_list)
        print(
            "========================[Analiz Performans??]=======================================")
        print("{user} kullan??c??s??n??n takip??iler listesindeki kay??p say??s??: {lost}".format(
            user=self.user, lost=lostFollowers))
        print("{user} kullan??c??s??n??n takip listesindeki kay??p say??s??: {lost}".format(
            user=self.user, lost=lostFollow))
        print("===================================================================================")
        time.sleep(5)
        self.driver.quit()
        elemanlar = {
                "follow": {
                    "de??er": doNotFollowCount,
                    "renk": "green",
                },
                "followers": {
                    "de??er": lostFollowers,
                    "renk": "red",
                }
            }

        successRate=round(100-(100*lostFollowers/doNotFollowCount),2)
        notSuccessRate=round(100*lostFollowers/doNotFollowCount,2)
        
        degerler = [t["de??er"] for t in elemanlar.values()]
        # kullan??c?? aray??z?? ayarlar??
        arayuz = tk.Tk()
        f = tk.Frame()
        arayuz.title("Instagram Analiz Uygulamas??")
        ekran_gen = int(arayuz.winfo_screenwidth() * 0.45)
        ekran_yuk = int(arayuz.winfo_screenheight() * 0.4)
        ekran_boyutu = str(ekran_gen)+'x'+str(ekran_yuk)
        arayuz.geometry(ekran_boyutu)
        arayuz.title("??nstagram Analiz Uygulamas??")
        arayuz.resizable(False, False)
        canvas = tk.Canvas(arayuz, width=ekran_gen,
                        height=ekran_yuk, background="#252525")
        canvas.pack(expand=0)
        analysis = Label(arayuz, text="Analiz Performans Grafi??i",relief="raised",bg="#252525",fg="white").place(x=85, y=2)
        greenBox = Label(arayuz, text="",bg="green").place(x=80, y=270,width=15,height=15)
        lblSuccessRate=Label(arayuz, text="Ba??ar?? Oran??: % {success}".format(success=successRate),bg="#252525",fg="white",relief="raised",bd=3).place(x=105, y=270)
        redBox = Label(arayuz, text="",bg="red").place(x=80, y=295,width=15,height=15)
        lblNotSuccesRate=Label(arayuz, text="Kay??p Oran??: % {notSuccess}".format(notSuccess=notSuccessRate),bg="#252525",fg="white",relief="raised",bd=3).place(x=105, y=295)
        followerName = Label(arayuz, text="kullan??c?? ad??: {user}".format(user=self.user),relief="raised").place(
            x=447, y=50, width=350, height=30)
        lblDoNotFollowCount = Label(
            arayuz, text="Takip etmeyenlerin say??s?? \n{notFollow}".format(notFollow=doNotFollowCount),relief="raised").place(x=445, y=300, width=155)
        lblDoNotFollowerCount = Label(
            arayuz, text="Takip etmediklerimizin say??s?? \n{notFollowers}".format(notFollowers=doNotFollowerCount),relief="raised").place(x=650, y=300, width=155)
        follower = Label(arayuz, text="Takip??i Say??s??: {follower}".format(follower=followerCount),relief="raised").place(x=445, y=350, width=155)
        follow = Label(arayuz, text="Takip Say??s??: {follow}".format(follow=followCount),relief="raised").place(x=650, y=350, width=155)
        
        if(lostFollowers==0):
            note="Analiz ba??ar??l??! Hi??bir kay??p kullan??c?? verisi bulunmamaktad??r."
        else:
            note="D??KKAT! Analiz performans?? takip??iler listesindeki eksikleri\n g??stermektedir. Bu da {loss} ki??inin asl??nda sizi takip ediyor \nolabilece??ini g??stermektedir. "
        
        note = Label(arayuz, text=note.format(loss=lostFollowers), bg="#252525", fg="red").place(x=20, y=320, width=320)
        lblForkFollow=Label(arayuz, text="??ekilen Takip Say??s??: {forkFollow}".format(forkFollow=len(flw_list)),relief="raised").place(x=650, y=385, width=155)
        lblForkFollowers=Label(arayuz, text="??ekilen Takip??i Say??s??:  {forkFollowers}".format(forkFollowers=len(flwrs_list)),relief="raised").place(x=445, y=385, width=155)

        list1 = tk.Listbox()
        list1.place(x=450, y=100, width=150)
        for i in doNotFollow:
            list1.insert(tk.END, i)
        list2 = tk.Listbox()
        list2.place(x=650, y=100, width=150)
        for i in doNotFollowers:
            list2.insert(tk.END, i)
        bas = 0
        if(lostFollowers==0):
            arc = canvas.create_arc(25, 25, 250, 250, start=bas,extent=359, fill="green",width="0")
        else:
            for i, j in elemanlar.items():
                

                aciklik = (j["de??er"] / sum(degerler)) * 360  # dilimin derecesi

                arc = canvas.create_arc(25, 25, 250, 250, start=bas,extent=aciklik, fill=j["renk"], width=3)

                bas += aciklik

        arayuz.mainloop()
