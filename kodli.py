import tkinter as cl
from tkinter import messagebox
import math
import time
from datetime import datetime as dt
import pytz as tzz
from tkinter import scrolledtext as scrl

w=cl.Tk();w.title("ANALOG CLOCK");w.geometry("1400x750");w.config(bg="ghostwhite")
k,ubg,ufg=0,'ghostwhite','midnightblue'
mbg,mfg='ghostwhite','black'
sfg='#007fff'
tc,tct,ctb='black','Dark Theme','ghostwhite'
ebg,efg='#eeeeff','black'
on,off,spl='#007fff','#aaaaaa','#87abff'
can=cl.Canvas(width=400,height=400,bg='ghostwhite',highlightbackground='ghostwhite');can.place(x=300,y=0)
bgl=cl.PhotoImage(file="D:\\pythen\\pyclk.png.png")
#o = Label(image = bgl);o.pack()
bgd=cl.PhotoImage(file="D:\\pythen\\pyclk.png.png")
#k = Label(image=bgd);k.pack()
dc_lbl=cl.Label(w,text="",font="Helvetica 20 bold",bg='ghostwhite');dc_lbl.place(x=500,y=422,anchor='center',bordermode='outside')
dt_lbl=cl.Label(w,text="dd-mm-yyyy",font="Helvetica 15 bold",bg="ghostwhite");dt_lbl.place(x=500,y=455,anchor='center')
tzlbl=cl.Label(w,text="CUSTOM TIME ZONES",font="Helvetica 10 bold",fg='navy',bg='ghostwhite');tzlbl.place(x=865,y=20,anchor='center')
oclklbl=cl.Label(w,text="OTHER FEATURES",font="Helvetica 10 bold",fg='navy',bg='ghostwhite');oclklbl.place(x=65,y=10)
k,t,p,tzn=1,1,0,''

def clkhndmove(sec,mint,hour):
    sec_x=160*math.sin(math.radians(sec*6))+200
    sec_y=-1*160*math.cos(math.radians(sec*6))+200
    can.coords(sec_hand,200,200,sec_x,sec_y)

    ashx=16*math.sin(math.radians((sec+30)*6))+200
    ashy=-1*16*math.cos(math.radians((sec+30)*6))+200
    can.coords(ash,200,200,ashx,ashy)

    min_x=140*math.sin(math.radians((mint*6)+(0.08*sec)))+200
    min_y=-1*140*math.cos(math.radians((mint*6)+(0.08*sec)))+200
    can.coords(min_hand,200,200,min_x,min_y)

    amx=14*math.sin(math.radians(((mint+30)*6)+(0.08*sec)))+200
    amy=-1*14*math.cos(math.radians(((mint+30)*6)+(0.08*sec)))+200
    can.coords(amh,200,200,amx,amy)

    hour_x=100*math.sin(math.radians((hour*30)+(mint/2)))+200
    hour_y=-1*100*math.cos(math.radians((hour*30)+(mint/2)))+200
    can.coords(hour_hand,200,200,hour_x,hour_y)

    ahx=95*math.sin(math.radians((hour*30)+(mint/2)))+200
    ahy=-1*95*math.cos(math.radians((hour*30)+(mint/2)))+200
    can.coords(ahh,200,200,ahx,ahy)

def defclk():
    if tzn!='' or p==1:
        return defa_btn.config(bg=off)
    defa_btn.config(bg=on,fg='black')
    hour=int(time.strftime("%I"))
    mint=int(time.strftime("%M"))
    sec=int(time.strftime("%S"))
    a_or_p=time.strftime("%p")
    dd=int(time.strftime("%d"))
    mm=time.strftime("%B")
    yy=time.strftime("%Y")
    dy=time.strftime("%A")
    clkhndmove(sec,mint,hour)
    dc_lbl.config(text="{:02d} : {:02d} : {:02d} - {}".format(hour,mint,sec,a_or_p))
    dt_lbl.config(text="{} - {:02d} - {} - {}".format(dy,dd,mm,yy))
    w.after(100,defclk)
def deft():
    global p,tzn
    p,tzn=0,''
    defclk()
defa_btn=cl.Button(w,text="Device Time",command=deft,bg=off,fg='ghostwhite',border=3,font='calibre 10 bold');defa_btn.place(x=340,y=645)

def p0(date,month,year,h,m,s,a,wd):
    global p
    p=0
    seted_time(date,month,year,h,m,s,a,wd)

def rfs():
    erlbl.config(text="",font='calibre 10 bold')

def sclk():
    ent=e1.get()
    ent2=e2.get()
    ent3=e3.get()
    try:
        h, m, s = map(int, ent.split(":"))
    except ValueError:
        erlbl.config(text="Enter format HH:MM:SS and AM or PM")
        return erlbl.after(4000,rfs)
    try:
        b = str(ent2)
    except ValueError:
        erlbl.config(text="Enter AM or PM")
        return erlbl.after(4000,rfs)
    if not(b.lower()=='am' or b.lower()=='pm'):
        erlbl.config(text="Enter 'AM' or 'PM'")
        return erlbl.after(4000,rfs)
    if b.lower()=='am' or b.lower()=='pm':
        a=b.upper()
    try:
        date,month,year,wd=map(int,ent3.split("-"))
    except ValueError:
        erlbl.config(text="Enter date in format 'dd-mm-yyyy-[(1-7)for(sun-sat)]'")
        return erlbl.after(4000,rfs)
    if month==1 or month== 3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if date>=32:
            erlbl.config(text="Enter valid Date:dd")
            return erlbl.after(4000,rfs)
    if month==4 or month==6 or month==9 or month==11:
        if date>=31:
            erlbl.config(text="Enter valid Date:dd")
            return erlbl.after(4000,rfs)
    if month==2 and year%4==0:
        if date>=30:
            erlbl.config(text="Enter valid Date:dd")
            return erlbl.after(4000,rfs)
    if month==2 and year%4!=0:
        if date>=29:
            erlbl.config(text="Enter valid Date:dd")
            return erlbl.after(4000,rfs)
    if month>=13:
        erlbl.config(text="Enter valid month")
        return erlbl.after(4000,rfs)
    if wd>=8:
        erlbl.config(text="Enter week day number i.e:(1-7)for(sun-sat)")
        return erlbl.after(4000,rfs)
    global p,tzn
    p,tzn=1,'set'
    w.after(1000,p0,date,month,year,h,m,s,a,wd)
el2=cl.Label(w,text="'AM'or'PM'",fg=sfg,bg=mbg,border=3,font='calibre 9 bold') ; el2.place(x=507,y=495,anchor='w')
e2=cl.Entry(w,width=8,border=3,bg=ebg,fg=efg) ; e2.place(x=514,y=522,anchor='w')
el3=cl.Label(w,text="dd-mm-yyyy-week day no/.(1-7)",fg=sfg,bg=mbg,border=3,font='calibre 10 bold') ; el3.place(x=500,y=555,anchor='center')
e3=cl.Entry(w,width=15,border=3,bg=ebg,fg=efg) ; e3.place(x=500,y=582,anchor='center')

def seted_time(d,mo,y,h,m,s,a,wd):
    if tzn!='set' or p==1:
        return set_btn.config(bg=off)
    set_btn.config(bg=on)
    s+=1
    if s==60:
       s=0
       m+=1
    if m==60:
       m=0
       h+=1
    if h==12 and m==0 and s==0:
        if a=='AM':
           a='PM'
        else:
           a='AM'
    if h >= 13:
       h -= 12
    if h==12 and a=='AM' and m==0 and s==0:
        d+=1
        wd+=1
        if wd==8:
            wd=1
    if mo==1 or mo==3 or mo==5 or mo==7 or mo==8 or mo==10 or mo==12:
        if d==32:
            d=1
            mo+=1
    elif mo==4 or mo==6 or mo==9 or mo==11:
        if d==31:
            d=1
            mo+=1
    elif mo==2 and y%4==0:
        if d==30:
            d=1
            mo+=1
    elif mo==2 and y%4!=0:
        if d==29:
            d=1
            mo+=1
    if mo>=13:
        mo=1
        y+=1
    wtl=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    mtl=['January','February','March','April','May','June','July','August','September','October','November','December']
    wt=wtl[wd-1]
    mnt=mtl[mo-1]
    clkhndmove(s,m,h)
    dc_lbl.config(text="{:02d} : {:02d} : {:02d} - {}".format(h,m,s,a))
    dt_lbl.config(text="{} - {:02d} - {} - {}".format(wt,d,mnt,y))
    w.after(1000,seted_time,d,mo,y,h,m,s,a,wd)
set_btn=cl.Button(w,text="Set Clock",command=sclk,bg=off,fg='black',border=3,font='calibre 10 bold') ; set_btn.place(x=462,y=625)
erlbl=cl.Label(w,text="",fg='red',bg='ghostwhite',border=3,font='calibre 10 bold') ; erlbl.place(x=500,y=609,anchor='center')
e1l=cl.Label(w,text='HH:MM:SS',fg=sfg,bg='lightskyblue1',border=3,font='calibre 10 bold') ; e1l.place(x=505,y=495,anchor='e')
e1=cl.Entry(w,width=13,border=3,bg=ebg,fg=efg) ; e1.place(x=513,y=522,anchor='e')

def tzclk(TZ):
    nt=dt.now(TZ)
    nh=int(nt.strftime('%I'))
    nm=int(nt.strftime('%M'))
    ns=int(nt.strftime('%S'))
    na=nt.strftime('%p')
    nmt=nt.strftime('%B')
    nwd=nt.strftime('%A')
    ndd=int(nt.strftime('%d'))
    ny=int(nt.strftime('%Y'))
    clkhndmove(ns,nm,nh)
    dc_lbl.config(text="{:02d} : {:02d} : {:02d} - {}".format(nh,nm,ns,na))
    dt_lbl.config(text="{} - {:02d} - {} - {}".format(nwd,ndd,nmt,ny))

def UTc():
    global tzn,p
    tzn,p='utc',0
    UTC()
def UTC():
    if p==1 or tzn!='utc':
        return utcbtn.config(bg=off,fg='black')
    UTCTZ=tzz.timezone('UTC')
    tzclk(UTCTZ)
    utcbtn.config(bg=on,fg='black')
    w.after(100,UTC)
utcbtn=cl.Button(w,text="UTC",command=UTc,bg=off,fg='black',border=3,font='Helvetica 10 bold') ; utcbtn.place(x=865,y=57,anchor='center',height=27,width=80)

def INd():
    global tzn,p
    tzn,p='ind',0
    IND()
def IND():
    if tzn!='ind' or p==1:
        return inbtn.config(bg=off,fg='black')
    INTZ=tzz.timezone('Asia/Kolkata')
    tzclk(INTZ)
    inbtn.config(bg=on,fg='black')
    w.after(100,IND)
inbtn=cl.Button(w,text="India",command=INd,bg=off,fg='black',border=3,font='Helvetica 10 bold') ; inbtn.place(x=865,y=104,anchor='center',height=27,width=80)

def NYt():
    global tzn,p
    tzn,p='ny',0
    NYT()
def NYT():
    if tzn!='ny' or p==1:
        return nybtn.config(bg=off,fg='black')
    NYTZ=tzz.timezone('America/New_York')
    tzclk(NYTZ)
    nybtn.config(bg=on,fg='black')
    w.after(100,NYT)
nybtn=cl.Button(w,text="New York",command=NYt,bg=off,fg='black',border=3,font='Helvetica 10 bold') ; nybtn.place(x=865,y=151,anchor='center',height=27,width=80)

def ENl():
    global tzn,p
    tzn,p='enl',0
    ENL()
def ENL():
    if tzn!='enl' or p==1:
        return engbtn.config(bg=off,fg='black')
    ENTZ=tzz.timezone('Europe/London')
    tzclk(ENTZ)
    engbtn.config(bg=on,fg='black')
    w.after(100,ENL)
engbtn=cl.Button(w,text="England",command=ENl,bg=off,fg='black',border=3,font='Helvetica 10 bold') ; engbtn.place(x=865,y=198,anchor='center',height=27,width=80)

def JPn():
    global tzn,p
    tzn,p='jpn',0
    JPN()
def JPN():
    if tzn!='jpn' or p==1:
        return jpnbtn.config(bg=off,fg='black')
    ENTZ=tzz.timezone('Asia/Tokyo')
    tzclk(ENTZ)
    jpnbtn.config(bg=on,fg='black')
    w.after(100,JPN)
jpnbtn=cl.Button(w,text="Japan",command=JPn,bg=off,fg='black',border=3,font='Helvetica 10 bold') ; jpnbtn.place(x=865,y=245,anchor='center',height=27,width=80)

def SPr():
    global tzn,p
    tzn,p='spr',0
    SPR()
def SPR():
    if tzn!='spr' or p==1:
        return sprbtn.config(bg=off,fg='black')
    SRTZ=tzz.timezone('Asia/Singapore')
    tzclk(SRTZ)
    sprbtn.config(bg=on,fg='black')
    w.after(100,SPR)
sprbtn=cl.Button(w,text="Singapore",command=SPr,bg=off,fg='black',border=3,font='Helvetica 10 bold') ; sprbtn.place(x=865,y=292,anchor='center',height=27,width=80)

def rfs2():
    ctzlbl.config(text="OR Enter timezone from pytz timezones",fg=sfg)
def CSTm():
    ent4=e4.get()
    tzns=str(ent4)
    if tzns not in tzz.all_timezones:
        ctzlbl.config(text='Invalid Time Zone',fg='red')
        return ctzlbl.after(4000,rfs2)
    global tzn,p,z,j
    tzn,p,z,j=tzns,0,0,0
    CUSTOM(tzns)
e4=cl.Entry(w,width=20,border=3,bg=ebg,fg=efg)
e4.place(x=865,y=360,anchor='center')
def CUSTOM(tzns):
    if tzn!=tzns or p==1:
        return cstmbtn.config(bg=off,fg='black')
    CSTZ=tzz.timezone(tzns)
    tzclk(CSTZ)
    cstmbtn.config(bg=on,fg='black')
    w.after(200,CUSTOM,tzns)
cstmbtn=cl.Button(w,text="set timezone",command=CSTm,bg=off,fg='black',border=3,font='calibre 10 bold') ; cstmbtn.place(x=865,y=390,anchor='center')
ctzlbl=cl.Label(w,text='OR Enter Timezone from pytz timezones',bg=mbg,fg=sfg,font='calibre 10 bold') ; ctzlbl.place(x=865,y=330,anchor='center')

def hands(x):
    global sec_hand,min_hand,hour_hand,d,ash,ahh,amh
    hcl=[['red','black','#0000bb','white'],['red','white','#7777ff','black']]
    shc=hcl[x][0]
    mhc=hcl[x][2]
    hhc=hcl[x][1]
    ahc=hcl[x][3]
    min_hand=can.create_line(200,200,300,300,width=3,fill=mhc)
    hour_hand=can.create_line(200,200,300,300,width=6,fill=hhc)
    ahh=can.create_line(200,200,295,295,width=2,fill=ahc)
    amh=can.create_line(200,200,210,210,width=4,fill=hcl[x][2])
    sec_hand=can.create_line(200,200,300,300,width=2,fill=shc)
    ash=can.create_line(200,200,210,210,width=4,fill='red')
    d=can.create_oval(195,195,205,205,fill='red')

def theme():
    global k
    td={0:[bgl,0],1:[bgd,1]}
    can.delete('all')
    can.create_image(200,200,image=td[k][0])
    hands(td[k][1])

def cteme():
    global k,mbg,mfg,sfg,ebg,efg,tc,tct,ctb
    elbl=[e1l,el2,el3,ctzlbl,srchlbl,el6]
    mlbl=[tzlbl,oclklbl,tzlistlbl]
    slbl=[dc_lbl,dt_lbl,hintlbl]
    e=[e1,e2,e3,e4,e5,e6,res]
    sfg='#007fff'
    if k==0:
        mbg,mfg='#181818','#ddddff'
        efg,ebg='ghostwhite','#444455'
        tc,tct,ctb='#ddddff','Light Theme','black'
        k=1
    elif k==1:
        mbg,mfg='ghostwhite','midnightblue'
        efg,ebg='black','#eeeeff'
        tc,tct,ctb='black','Dark Theme','ghostwhite'
        k=0
    for lbl in elbl:
        lbl.config(bg=mbg,fg=sfg)
    for lbl in mlbl:
        lbl.config(bg=mbg,fg=mfg)
    for lbl in slbl:
        lbl.config(bg=mbg,fg=efg)
    for entry in e:
        entry.config(bg=ebg,fg=efg)
    ctbtn.config(text=tct,bg=tc,fg=ctb)
    erlbl.config(bg=mbg)
    can.config(bg=mbg,highlightbackground=mbg)
    w.config(bg=mbg)
    theme()

ctbtn=cl.Button(w,text='Dark Theme',command=cteme,fg='ghostwhite',bg='black',border=3,font='calibre 10 bold') ; ctbtn.place(x=65,y=50)
hintlbl=cl.Label(w,bg='ghostwhite',text=': Hint :\n * This search is case insensitive                                                  \n* if you dont remember name properly then enter only the\n    perfectly known sequence of letters in that word\n* use "_" in case of spaces                                                         ')
hintlbl.place(x=1028,y=120)

def listz():
    kw=(str(e5.get())).lower()
    l=[tz for tz in tzz.all_timezones if kw in tz.lower()]
    if not l:
        res.delete(1.0,cl.END)
        res.insert(cl.END,f'No Time Zone Found\nfor {kw}')
    else:
        res.delete(1.0,cl.END)
        for tz in l:
            res.insert(cl.END,tz+'\n')
tzlbtn=cl.Button(w,text="list of TZ's",command=listz,bg=spl,fg='black',border=3,font='Helvetica 10 bold',padx=0,pady=0) ; tzlbtn.place(x=1120,y=90)
srchlbl=cl.Label(w,text='search for Time Zone by continent or famous city',bg=mbg,fg=sfg,font='calibre 10 bold') ; srchlbl.place(x=1160,y=50,anchor='center')
e5=cl.Entry(w,width=20,border=3,bg=ebg,fg=efg) ; e5.place(x=1093,y=65)
res=scrl.ScrolledText(w,wrap=cl.WORD,width=35,height=30,bg='#ddddff',border=5,highlightbackground='blue') ; res.place(x=1030,y=210)

hr,mr,sr=0,0,0
def tmrpzpl():
    if tzn!='tmr':
        return
    global p,ppbtn,hr,mr,sr
    if p==0:
        p=1
        ppbtn.config(text='▶')
    elif p==1:
        p=0
        tmr4(hr,mr,sr)
        ppbtn.config(text='| |')

def tmr4(hn,mn,sn):
    global hr,mr,sr
    hr,mr,sr=hn,mn,sn
    if sr==0 and (mr!=0 or hr!=0):
        if mr!=0:
            sr=60;mr-=1
        if mr==0 and hr!=0:
            sr=60;mr=59;hr-=1
    sr-=1
    if sr==0 and (mr!=0 or hr!=0):
        if sr==0 and mr!=0:
            sr=60;mr-=1
        elif sr==0 and mr==0 and hr!=0:
            sr=60;mr=59;hr-=1
    if sr<0 or tzn!='tmr' or p==1:
        return
    clkhndmove(sr,mr,hr)
    dc_lbl.config(text='{:02d} : {:02d} : {:02d}'.format(hr,mr,sr))
    if sr<=0 and mr<=0 and hr<=0:
        #playsound('alarm.mp3')
        return messagebox.showinfo('Timer Notification','   TIME OVER   ')
    dt_lbl.config(text='In Timer Mode')
    w.after(1000,tmr4,hr,mr,sr)

def tmr4_1(hr,mn,sc):
    global p
    p=0
    tmr4(hr,mn,sc)

def tmr3(hr,mn,sc):
    while sc>=60:
        sc-=60
        mn+=1
    while mn>=60:
        mn-=60
        hr+=1
    global tzn,p
    tzn,p='tmr',1
    w.after(1000,tmr4_1,hr,mn,sc)
tn=0
e6=cl.Entry(w,width=15,border=3) ; e6.place(x=0,y=0,anchor='se')
el6=cl.Label(w,text='Enter time in format HH:MM:SS\nEnter 0:0:SS if want timer only in Sec)',bg=mbg,fg=sfg) ; el6.place(x=0,y=0,anchor='se')
ppbtn=cl.Button(w,text='| |',font='Helvetica 10 bold',command=tmrpzpl,bg='skyblue3',fg='white',bd=0, relief="ridge", padx=10, pady=5, borderwidth=2, highlightthickness=0, overrelief="ridge") ; ppbtn.place(x=0,y=0,anchor='se')

def freeze():
    global p
    p=1
frzbtn=cl.Button(w,text='Freeze Clock',command=freeze,bg=spl,fg='black',font='Helvetica 10 bold',padx=0,pady=0,border=3)
frzbtn.place(x=570,y=645)
def ex():
    ans=messagebox.askquestion('Exit confirmation','Do You want to exit analog clock?')
    if ans=='yes':
        exit()
extbtn=cl.Button(w,text='Exit',command=ex,bg='orangered2',fg='ghostwhite',padx=10,pady=8,border=3,font='helvetica 10 bold') ; extbtn.place(x=50,y=600)
tzlistlbl=cl.Label(w,text='LIST OF PYTZ TIME ZONES',fg='NAVY',bg='ghostwhite',font='Helvetica 10 bold') ; tzlistlbl.place(x=1060,y=10)
cteme() ; deft() ; w.mainloop()