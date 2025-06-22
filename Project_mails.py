import gmail

def send_mail_for_openacn(to_mail,uacno,uname,upass,udate):
        con=gmail.GMail('vishwapriyaranjan8022@gmail.com','xiqm eobj rfgg grcy')
        sub='Account Opened with Dhan Laxmi Cheat Bank'

        body=f"""Dear {uname},
        Your account has been opened successfully with Dhan Laxmi Cheat Bank and details are
    ACN = {uacno}
    Pass = {upass}
    Open date = {udate}

    Kindly change your password when you login first time
    Thanks
    Dhan LaxmiCheat Bank
    Noida
    """
        msg=gmail.Message(to=to_mail,subject=sub,text=body)
        con.send(msg)

def send_otp(to_mail,uname,uotp):
    con=gmail.GMail('vishwapriyaranjan8022@gmail.com','xiqm eobj rfgg grcy')
    sub='OTP for password recovery'
    body=f"""Dear {uname},
        Your OTP to get password = {uotp}
   
    Kindly verify this otp to application 
    Thanks
    Dhan LaxmiCheat Bank
    Noida
    """
    msg=gmail.Message(to=to_mail,subject=sub,text=body)
    con.send(msg)