def getdetails():
    sname=(input("enterservername:"))
    passwd=(input("enterpassword:"))
    uname=(input("enterusername:"))
    dbname=(input("enterdatabasename:"))
    return "servername=%s,password=%s,username=%s,databasename=%s"%(sname,passwd,uname,dbname)
