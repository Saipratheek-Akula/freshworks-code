
import time

class Freshworks():

    global d
    d = {"one": ["first",0]}
    @staticmethod
    def create(key,value,timeout=0):

        if key in d.keys():
            print("Error: This type of key already exists")
        else:
            if key.isalpha():
                if len(d)<(1024*1020*1024) and len(value)<=(16*1024*1024):
                    if timeout==0:
                        l=[value,timeout]
                    else:
                        l=[value,time.time()+timeout]
                    if len(key)<=32:
                        d[key]=l
                else:
                    print("Error: memory limit exceeded!!** ")
            else : print("Error: invalid keyname!** keyname should contain only alphabets but not special characters or numbers")
        return d

    @staticmethod
    def read(key):
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key")
        else:
            b=d[key]

            if b[1]!=0:
                if time.time()<int(b[1]):
                    stri=str(key)+":"+str(b[0])
                    print("the value for " + key + " is: " + str(d[key][0]))
                    return stri
                else:
                    print("error: time-to-live of",key,"has expired")
            else:
                stri=str(key)+":"+str(b[0])
                print(stri)
                print("the value for " + key + " is: " + str(d[key][0]))
                return stri

    @staticmethod
    def delete(key):
        if key not in d:
            print("Error: given key does not exist in database. Please enter a valid key")
        else:
            b=d[key]
            if b[1]!=0:
                if time.time()<int(b[1]):
                    del d[key]
                    print("key is successfully deleted")
                    print("dataset after deleting "+key+": "+str(d))
                else:
                    print("Error: time to live offff",key,"has been expired")
            else:
                del d[key]
                print("key had been succesfully deleted")
                print("dataset after deleting " + key + ": " + str(d))
        return d


print("*****************************CREATE TEST RESULTS******************************************************")
dict_afterCreate = Freshworks().create("one","first")
print("data set after adding an existing key: "+str(dict_afterCreate))
print("***********************************************************************************")
dict_afterCreate = Freshworks().create("two","second")
print("data set after adding a new key: "+str(dict_afterCreate))
print("***********************************************************************************")
dict_afterCreate = Freshworks().create("123","second")
print("data set after adding an invalid key: "+str(dict_afterCreate))
print("*****************************READ TEST RESULTS******************************************************")
Freshworks().read("one")
print("***********************************************************************************")
Freshworks().read("ten")
print("*****************************DELETE TEST RESULTS******************************************************")
Freshworks.delete("invalidkeyy")
print("***********************************************************************************")
Freshworks.delete("two")
print("***********************************************************************************")
