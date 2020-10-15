
    import pickle
    import tkinter as tk
    import tkinter.messagebox
    from functools import partial
    from tkinter import filedialog




    try:
        import PIL.Image
        from PIL import ImageTk
    except ModuleNotFoundError:
        import os
        os.system("pip install pillow")
        
        from PIL import ImageTk
        import PIL.Image

    

    fobj=open("logindata.dat",'ab')
    fobj.close()
    fobj=open('products.dat','ab')
    fobj.close()
    fobj=open("userhistory.dat",'ab')
    fobj.close()
    welcome=tk.Tk()
    welcomeimg=ImageTk.PhotoImage(PIL.Image.open("welcome.png")) 
    welcomelab=tk.Label(welcome,image=welcomeimg)
    welcomelab.pack(fill=tk.BOTH,expand=1)
    def weldes():
        welcome.destroy()
            
    weldesbtn=tk.Button(welcome,text="Proceed!",fg="blue",font=("Arial",15,"bold"),command=weldes).pack()
    welcome.mainloop()
    def main():
        
        
        
        
        top = tk.Tk()
        def login(uservar,pasvar):
            
            loginobj=open("logindata.dat",'rb')
            global userid
            userid=uservar.get()
            password=pasvar.get()
            myd={userid:password}
            found=False
            try:
                while True:
                    logindic=pickle.load(loginobj)
                    if logindic==myd:
                        found=True
                        tkinter.messagebox.showinfo("Logged in","You have been logged in!")


                        try:
                            top.destroy()
                        except:
                            pass
                        def afterlogfn():
                            afterlog=tk.Tk()
                            afterlog.minsize(300,280)
                            afterlog.title("Dashboard")
                            def sell(): 
                                def putupforsale(pname,pdesc,ptype,pmfr,pprice,pquantity,pdel):
                                    global imagelocation
                                    with open('products.dat','ab') as productsobj:
                                        pd={}
                                        pd["Product Name:"]=pname.get()
                                        pd["Product Description:"]=pdesc.get()
                                        pd["Product Type:"]=ptype.get()
                                        pd["Product Manufacturers/Company:"]=pmfr.get()
                                        pd["Price:"]=pprice.get()
                                        pd["Quantity left in stock:"]=pquantity.get()
                                        pd["Delivery in:"]=pdel.get()
                                        pd["ImageLoc"]=imagelocation
                                        pickle.dump(pd,productsobj)
                                        tkinter.messagebox.showinfo("Product Up for sale","Your product has been Put up for sale!")
                                        with open("userhistory.dat","rb+") as uhis:
                                            try:
                                                while True:
                                                    pos=uhis.tell()
                                                    bob=pickle.load(uhis)
                                                    
                                                    if userid in bob:
                                                        bob[userid]["sold"].append(pd["Product Name:"])
                                                        uhis.seek(pos)
                                                        pickle.dump(bob,uhis)
                                                        break
                                            except :
                                                pass
                                                
                                        sellwin.destroy()
                                        afterlogfn()     
                            
                                afterlog.destroy()
                                sellwin=tk.Tk()
                                sellwin.title("Enter Product details")
                                sellwin.minsize(500,400)
                                def backtoafterlog():
                                    try:
                                        sellwin.destroy()
                                    except:
                                        pass
                                    afterlogfn()
                                backbtn=tk.Button(sellwin,text="Back<",font=("Arial",8,"bold"),command=backtoafterlog).grid(row=0,column=0) 
                                pnamelab=tk.Label(sellwin,text="Product Name:",font=("times",10,"bold")).grid(row=1,column=1,padx=5,pady=20)
                                pdesclab=tk.Label(sellwin,text="Product Description:",font=("times",10,"bold")).grid(row=2,column=1,padx=5,pady=15)
                                ptypelab=tk.Label(sellwin,text="Product Type:",font=("times",10,"bold")).grid(row=3,column=1,padx=5,pady=15)
                                pmfrlab=tk.Label(sellwin,text="Product Manufacturers/Company:",font=("times",10,"bold")).grid(row=4,column=1,padx=5,pady=15)
                                ppricelab=tk.Label(sellwin,text="Price:",font=("times",10,"bold")).grid(row=5,column=1,padx=5,pady=15)
                                pquantitylab=tk.Label(sellwin,text="Quantity left in stock:",font=("times",10,"bold")).grid(row=6,column=1,padx=5,pady=15)
                                pdellab=tk.Label(sellwin,text="Delivery in:",font=("times",10,"bold")).grid(row=7,column=1,padx=5,pady=15)
                                pimageab=tk.Label(sellwin,text="Upload Picture of your product:",font=("times",10,"bold")).grid(row=8,column=1,padx=5,pady=15)
                                pname=tk.Entry(sellwin,font=("Arial",10))
                                pname.grid(row=1,column=2,padx=5,pady=20,ipadx=30)
                                pdesc=tk.Entry(sellwin,font=("Arial",10))
                                pdesc.grid(row=2,column=2,padx=5,pady=20,ipadx=30,ipady=30)
                                ptype=tk.Entry(sellwin,font=("Arial",10))
                                ptype.grid(row=3,column=2,padx=5,pady=20,ipadx=30)
                                pmfr=tk.Entry(sellwin,font=("Arial",10))
                                pmfr.grid(row=4,column=2,padx=5,pady=20,ipadx=30)
                                pprice=tk.Entry(sellwin,font=("Arial",10))
                                pprice.grid(row=5,column=2,padx=5,pady=20,ipadx=30)
                                pquantity=tk.Entry(sellwin,font=("Arial",10))
                                pquantity.grid(row=6,column=2,padx=5,pady=20,ipadx=30)
                                pdel=tk.Entry(sellwin,font=("Arial",10))
                                pdel.grid(row=7,column=2,padx=5,pady=20,ipadx=30)
                                def browseimage():
                                    tkinter.messagebox.showinfo("Note","Maximum Image dimensions 500 x 500 px")
                                    global myimg
                                    sellwin.filename=filedialog.askopenfilename(title="Upload pictures of your product",filetypes=[("image", ".jpeg"),("image", ".png"),("image", ".jpg")])
                                    global imagelocation                     
                                    imagelocation=sellwin.filename
                                    
                                    print(imagelocation)
                                    
                                    myimg=ImageTk.PhotoImage(PIL.Image.open(sellwin.filename))
                                    blah=tk.Label(sellwin,text=" Uploaded Image:",font=("times",10,"bold")).grid(row=1,column=4)
                                    myimglab=tk.Label(sellwin,image=myimg).grid(row=2,rowspan=5,column=4,padx=5,pady=15)
                                    
                                browseimgbtn=tk.Button(sellwin,text="Browse",fg="red",command=browseimage)
                                browseimgbtn.grid(row=8,column=2,padx=5,pady=20)
                                putupforsale=partial(putupforsale,pname,pdesc,ptype,pmfr,pprice,pquantity,pdel)
                                salebtn=tk.Button(sellwin,text="Put up for sale",fg="blue",font=("Arial",10,"italic"),command=putupforsale).grid(row=0,column=2,padx=10,pady=10,ipadx=10,ipady=10)

                                
                                sellwin.mainloop()
                            def buy():
                                try:                 
                                    afterlog.destroy()
                                except:
                                    pass
                                buywin=tk.Tk()
                                buywin.title("Buy Products")
                                buywin.minsize(500,400)
                                productsobj=open("products.dat",'rb')
                                def backtoafterlog():
                                    buywin.destroy()
                                    afterlogfn()
                                backbtn=tk.Button(buywin,text="Back<",font=("Arial",10,"bold"),command=backtoafterlog).grid(row=0,column=0)
                                try:
                                    slno=1
                                    while True:
                                        def detailed(prod):
                                            try:
                                                buywin.destroy()
                                            except:
                                                pass
                                            buyp=tk.Tk()
                                            buyp.title("Buy {} ".format(prod["Product Name:"]))  
                                            def backtobuywin():
                                                buyp.destroy()   
                                                buy()   
                                            backbtn=tk.Button(buyp,text="Back<",font=("Arial",10,"bold"),command=backtobuywin).grid(row=0,column=0)

                                            
                                            pnamelab=tk.Label(buyp,text="Product Name:",font=("times",10,"bold")).grid(row=1,column=1,padx=5,pady=20)
                                            pdesclab=tk.Label(buyp,text="Product Description:",font=("times",10,"bold")).grid(row=2,column=1,padx=5,pady=15)
                                            ptypelab=tk.Label(buyp,text="Product Type:",font=("times",10,"bold")).grid(row=3,column=1,padx=5,pady=15)
                                            pmfrlab=tk.Label(buyp,text="Product Manufacturers/Company:",font=("times",10,"bold")).grid(row=4,column=1,padx=5,pady=15)
                                            ppricelab=tk.Label(buyp,text="Price:",font=("times",10,"bold")).grid(row=5,column=1,padx=5,pady=15)
                                            pquantitylab=tk.Label(buyp,text="Quantity left in stock:",font=("times",10,"bold")).grid(row=6,column=1,padx=5,pady=15)
                                            pdellab=tk.Label(buyp,text="Delivery in:",font=("times",10,"bold")).grid(row=7,column=1,padx=5,pady=15)
                                            pnamelabs=tk.Label(buyp,text=prod["Product Name:"],font=("times",10,"italic")).grid(row=1,column=2,padx=5,pady=20)
                                            pdesclabs=tk.Label(buyp,text=prod["Product Description:"],font=("times",10,"italic")).grid(row=2,column=2,padx=5,pady=15)
                                            ptypelabs=tk.Label(buyp,text=prod["Product Type:"],font=("times",10,"italic")).grid(row=3,column=2,padx=5,pady=15)
                                            pmfrlabs=tk.Label(buyp,text=prod["Product Manufacturers/Company:"],font=("times",10,"italic")).grid(row=4,column=2,padx=5,pady=15)
                                            ppricelabs=tk.Label(buyp,text=prod["Price:"],font=("times",10,"italic")).grid(row=5,column=2,padx=5,pady=15)
                                            pquantitylabs=tk.Label(buyp,text=prod["Quantity left in stock:"],font=("times",10,"italic")).grid(row=6,column=2,padx=5,pady=15)
                                            pdellabs=tk.Label(buyp,text=prod["Delivery in:"],font=("times",10,"italic")).grid(row=7,column=2,padx=5,pady=15)
                                            imlc=prod["ImageLoc"]
                                            print(imlc) 
                                            
                                            global notmyimg
                                            notmyimg=ImageTk.PhotoImage(PIL.Image.open(imlc))   
                                            myimglab=tk.Label(image=notmyimg).grid(row=2,rowspan=5,column=3,padx=5,pady=15)
                                            def ordered():                                                                                               
                                                def placed():
                                                    tkinter.messagebox.showinfo("Ordered","Your Order has been placed!")
                                                    with open("userhistory.dat","rb+") as uhis1:
                                                        try:
                                                            while True:
                                                                pos=uhis1.tell()
                                                                bob=pickle.load(uhis1)
                                                                
                                                                if userid in bob:
                                                                    bob[userid]["bought"].append(prod["Product Name:"])
                                                                    uhis1.seek(pos)
                                                                    pickle.dump(bob,uhis1)
                                                                    break
                                                        except :
                                                            pass
                                                    orderedwin.destroy()
                                                    try:
                                                        buyp.destroy()
                                                    except:
                                                        pass
                                                    afterlogfn()
                                                orderedwin=tk.Tk()
                                                orderedwin.title("Proceed with Order")
                                              
                                                adresslab=tk.Label(orderedwin,text="Deliver to Address:",font=("times",10,"bold")).pack(pady=5)
                                                address=tk.Entry(orderedwin).pack(ipadx=20,ipady=20,pady=5)
                                                deliverytime=tk.Label(orderedwin,text="Delivery Time:",font=("times",10,"bold")).pack(pady=5)
                                                def sel():
                                                    pass
                                                var=0   
                                                office=tk.Radiobutton(orderedwin,text="Office delivery: 9 AM - 5 PM",variable=var,value=1,command=sel)
                                                office.pack(pady=5)
                                                home=tk.Radiobutton(orderedwin,text="Home delivery: 7 AM - 9 PM",variable=var,value=2,command=sel)
                                                home.pack(pady=5)
                                                deliver=tk.Label(orderedwin,text=f'Your Product {prod["Product Name:"]} will arrive in {prod["Delivery in:"]}',font=("times",10,"bold")).pack(pady=5)
                                                cash=tk.Label(orderedwin,text="Payement Mode - Cash on Delivery only.",font=("times",10,"bold")).pack(pady=5)    
                                                finalizebtn=tk.Button(orderedwin,text="Order",font=("MS Serif",15,"bold"),fg="blue",command=placed).pack(pady=5)                             
                                                

                                                


                                            buypbtn=tk.Button(buyp,text="Buy Now",font=("MS Serif",15,"bold"),fg="red",command=ordered)
                                            buypbtn.grid(row=1,column=3,padx=5,pady=15)
                                        

                                            




                                        prod=pickle.load(productsobj)
                                        slnolab=tk.Label(buywin,text=f'{slno}.',font=("Arial",13,"bold")).grid(row=slno,column=0)
                                        pnamelab=tk.Label(buywin,text=prod["Product Name:"],font=("Arial",13,"italic")).grid(row=slno,column=1)
                                        
                                        viewpbtn=tk.Button(buywin,text="View Product",fg="red",command=lambda prod=prod:detailed(prod))
                                        viewpbtn.grid(row=slno,column=2,padx=5,pady=5,ipadx=5,ipady=5)
                                        slno+=1
                                    
                                except EOFError:
                                    pass
                                finally:
                                    productsobj.close()


                                


                            sellbtn=tk.Button(afterlog,text="SELL",fg="green",width=10,height=5,command=sell).pack(side='right',pady=30,padx=30)
                            buybtn=tk.Button(afterlog,text="BUY",fg="red",width=10,height=5,command=buy).pack(side='left',pady=30,padx=30)
                            def history():
                                hiswin=tk.Tk()
                                hiswin.title("User History")
                                hiswin.minsize(400,400)
                                pboughtlab=tk.Label(hiswin,text="Products Bought",font=("MS Serif",15,"underline")).grid(row=0,column=0,padx=10,pady=5,ipadx=10,ipady=5)
                                psoldlab=tk.Label(hiswin,text="Products Sold",font=("MS Serif",15,"underline")).grid(row=0,column=1,padx=5,pady=5,ipadx=5,ipady=5)
                                with open('userhistory.dat','rb') as uhis3:
                                    
                                    try:
                                        
                                        while True:
                                            
                                            bob=pickle.load(uhis3)
                                            if userid in bob:
                                                soldlist=bob[userid]["sold"]
                                                boughtlist=bob[userid]["bought"]
                                                
                                                for i in boughtlist:
                                                    j=boughtlist.index(i)+1
                                                    _k=tk.Label(hiswin,text=f'{j}.{i}',font=("times",10,"italic")).grid(row=j,column=0,padx=5,pady=5,ipadx=5,ipady=5)
                                                for i in soldlist:
                                                    j=soldlist.index(i)+1
                                                    _k=tk.Label(hiswin,text=f'{j}.{i}',font=("times",10,"italic")).grid(row=j,column=1,padx=5,pady=5,ipadx=5,ipady=5)
                                                break




                                    except :
                                        pass
                            def backtotop():
                                try:
                                    afterlog.destroy()
                                except:
                                    pass
                                main()
                            backbtn=tk.Button(afterlog,text="Back<",fg="black",command=backtotop).place(anchor=tk.NW)
                            userhistorybtn=tk.Button(afterlog,text="History",fg="blue",font=("MS Serif",10,"bold"),command=history).pack(ipadx=2,ipady=2,pady=5)
                        
                            
                        afterlogfn()
                        break
                        
            except EOFError:
                if found==False:
                        tkinter.messagebox.showerror("Invalid","Invalid Username/Password")
            finally:
                loginobj.close()
                        

            
        def signup():
        
            def createacc(nuv,npv):
                nuserid=nuv.get()
                npassword=npv.get()
                newacc={nuserid:npassword}
                with open('logindata.dat','ab') as signupobj:
                    pickle.dump(newacc,signupobj)
                    tkinter.messagebox.showinfo("Account Created","Your Account has been created! Login with this Username and Password")
                    with open('userhistory.dat','ab') as uhis:
                        _c=[]
                        _d=[]
                        _b={}
                        _b["sold"]=_c
                        _b["bought"]=_d
                        _a={}
                        _a[nuserid]=_b
                        pickle.dump(_a,uhis)
                        main.destroy()

            main=tk.Tk()
            
            newuserlab=tk.Label(main,text="Create Username:",font=("times",10,"bold")).grid(row=1,column=1,padx=5,pady=10,ipadx=10,ipady=10)
            nuserin=tk.Entry(main)
            nuserin.grid(row=1,column=2,padx=5,pady=10,ipadx=10,ipady=5)
            newpasslab= tk.Label(main,text="Create Password:",font=("times",10,"bold")).grid(row=2,column=1,padx=5,pady=10,ipadx=10,ipady=10)
            npassin=tk.Entry(main)
            npassin.grid(row=2,column=2,padx=5,pady=10,ipadx=10,ipady=5)
            createacc=partial(createacc,nuserin,npassin)
            btn=tk.Button(main,text="Submit",fg="blue",font=("times",10,"bold"),command=createacc).grid(row=4,column=2,padx=5,pady=10,ipadx=10,ipady=10)  
        
        signupbtn=tk.Button(top,text="Not a member yet?, Sign Up now!",fg='red',command=signup)
        signupbtn.grid(row=4,column=2,padx=5,pady=10,ipadx=10,ipady=10)

        userlab=tk.Label(top,text="Enter Username:",font=("MS Serif",10,"bold")).grid(row=1,column=1,padx=5,pady=10,ipadx=10,ipady=10)
        useridvar=tk.StringVar()
        userin= tk.Entry(top,textvariable=useridvar).grid(row=1,column=2,padx=5,pady=10,ipadx=10,ipady=10)

        passlab= tk.Label(top,text="Enter Password:",font=("MS Serif",10,"bold")).grid(row=2,column=1,padx=5,pady=10,ipadx=10,ipady=10)
        passwordvar=tk.StringVar()
        passin=tk.Entry(top,textvariable=passwordvar,show='*').grid(row=2,column=2,padx=5,pady=10,ipadx=10,ipady=10)
        login=partial(login,useridvar,passwordvar)

        loginbtn = tk.Button(top, text = "Log in", fg = "green",command=login)  
        loginbtn.grid(row=4,column=1,padx=5,pady=10,ipadx=10,ipady=10)
        top.mainloop()


    main()

