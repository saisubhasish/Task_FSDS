# logging module is used to store the activities performed during program execution
import datetime
import logging
import os
import smtplib
import socket
import time
import cv2

class List_class:


    def reverse_without_func(self):
        ''' This is my list reverse method without use of
        in-built function '''
        l=[1,2,3,4,5]
        logging.info(l[::-1])


    def list_Collection(self):
        ''' This is my list method to exctract all the list
        elements '''
        l = [3, 4, 5, 6, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (256, 6657, 6),{'key1': 'sai', 234: [23, 56, 656]}]
        l1=[]
        for i in l:
            if type(i)==list:
                l1.append(i)
        logging.info(l1)


    def extract(self):
        """ This is my list method to extract 'sai' from the
        list """
        m,n=0,0
        s=''
        l = [3, 4, 5, 6, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (256, 6657, 6),{'key1': 'sai', 234: [23, 56, 456]}]
        for i in l:
            if type(i) == dict:
                for j in i.keys():
                    if j == 234:
                        m = j
                for j in i.values():
                    if type(j)==list:
                        for k in j:
                            if k == 456:
                                n=k
                for j in i.values():
                    if j=='sai':
                        s=j
        logging.info(s)


    def keys_in_dict(self):
        ''' This is my list method to extract all the keys in
         list'''
        l = [3, 4, 5, 6, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (256, 6657, 6),{'key1': 'sai', 234: [23, 56, 456]}]
        l1=[]
        for x in l:
            if type(x)==dict:
                for j in x.keys():
                    l1.append(j)
            else:
                for y in l:
                    if type(y)==dict:
                        for i in y.keys():
                            l1.append(i)
        logging.info(l1)


    def values_in_dict(self):
        ''' This is my list method to extract all the values
         in list '''
        l = [3, 4, 5, 6, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (256, 6657, 6), {'key1': 'sai', 234: [23, 56, 456]}]
        l=[]
        for x in l:
            if type(x)==dict:
                for i in x.values():
                    l.append(i)
            else:
                for y in x:
                    if type(y)==dict:
                        for j in y.values():
                            l.append(j)
        logging.info(l)


class Pattern:
    def pattern(self):
        ''' This is py program to print pattern
        ineuron
        ineuron ineuron
        ineuron ineuron ineuron
        ineuron ineuron ineuron ineuron
        ineuron ineuron ineuron ineuron ineuron'''
        for i in range(5):
            logging.info('ineuron  '*(i+1))
        x = 0
        while x < 8:
            content = ""
            y = 0
            while y < x:
                z = 0
                sum = 0
                while z < y:
                    sum += 6 - z
                    z += 1
                if (x + 64 + sum) <= (64 + 26):
                    content += " " + chr(x + 64 + sum)
                y += 1
            logging.info(content)
            x += 1


    def diamond(self):
        """ This is my pattern program to print
                        ineuron
                 ineuron       ineuron
          ineuron                     ineuron
                 ineuron       ineuron
                        ineuron"""
        for i in range(6):
            if i<=3:
                n=i
            else:
                n=6-i
            logging.info(('ineuron '*n).center(50,''))


class Loop:
    def div_by_3(self):
        ''' This is my program to get the numbers
         divisible by 3 in between (40,400) '''
        l=[]
        try:
            for x in range(40,400):
                if x%3==0:
                    l.append(x)
        except Exception as e:
            logging.exception(e)
        logging.info(l)


    def vowels(self):
        ''' This is my function to find vowels in a
          string'''
        s='hdbhdsbjhvbiuanuiavuindsvbefbkjasn'
        vowels=['a','e','i','o','u']
        l=[]
        i=0
        try:
            while i<len(s):
                for x in s:
                    if x in vowels:
                        l.append(x)
                    i+=1
        except Exception as e:
            logging.info(e)
        logging.info(e)


    def even_num(self):
        """ This is my function to print even numbers in
         a range of (1,1000) """
        l=[]
        for i in range(1,1000):
            try:
                if i%2==0:
                    l.append(i)
            except Exception as e:
                logging.info(e)
        logging.info(l)


    def system_date_time(self):
        '''  This is my function to print today's date and
         current time'''
        now = datetime.now()
        try:
            current_time = now.strftime("%H:%M:%S")
            today= datetime.date.today()
            logging.info(current_time, today)
        except Exception as e:
            logging.info(e)


    def mail(self):
        """ This is my function to send auto email """
        try:
            server = smtplib.SMTP('smtp.gmail.com', 25)
            server.starttls()
            server.login('saisubhasishrout777@gmail.com', 'bdasijns2ru8932udnoiefoioewh4864')
            server.sendmail('saisubhasishrout777@gmail.com', 'somyaranjan333@gmail.com', 'Hello, This is Sai here.')
            logging.info('Mail sent')
        except Exception as e:
            logging.info(e)


    def txt_to_voice(str1):
        """ This is my fynction to convert text to voice  """
        try:
            tts = gtts.gTTS(str1)
            tts.save("Hello.mp3")
            playsound("Hello.mp3")
            Text = input("Enter the text to convert to voice: ")
            txt_to_voice(Text)
        except Exception as e:
            logging.info(e)


    def alarm(self):
        """  This is my function to auto play alarm  """
        try:
            alarm_time = '10:22'
            if time.asctime()[11:-8] == alarm_time:
                absolute_path = os.path.abspath("texttovoice.mp3")
                logging.info(absolute_path)
                playsound.playsound(absolute_path)
        except Exception as e:
            logging.info(e)


    def ip_address(self):
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        logging.info("your ip address is ", ip)
        logging.info("your computer name is ", host)
    def installation(self):
        logging.info(list(winapps.list_installed()))
    def length_string(s):
        i=1
        for j in s:
            i+=1
        return i
    def element_index(n):
        for i in range(n):
            j=0
            if i==n:
                k=i
        return j
    def dict_to_list(d):
        l=[]
        for i in d:
            if type(i)!=dict:
                l.append(i)
            if type(i)==dict:
                for k in i:
                    l.append(k)
        return l
    def list_concat(l):
        s=''
        for i in l:
            for j in i:
                s+=j
        return s
    def read_img():
        a = cv2.imread('D:/abc.png')
        cv2.imshow("myimg", a)
        cv2.waitKey(5000)
        cv2.destroyWindow('myimg')
    def prime_in_range(n):
        '''This is my prime number in a range function'''
        prime = []
        for i in range(n):
            if i <= 1:
                continue
            else:
                try :
                    for j in range(2, int(i / 2) + 1):
                        if i % j == 0:
                            break
                    else:
                        prime.append(i)
                except Exception as e:
                    logging.exception(e)
            return prime
    def print_func(n):
        print = lambda *x: x
        print(n)
    def list_append(l):
        append = lambda *x: [i for i in x]
        append(l)
    def extend(*n):
        '''This is my extend function'''
        output = ''
        for x in n:
            if type(x) == list or type(x) == tuple or type(x) == set:
                output += str(x)
        return output
    def pop(l):
        '''This is my pop function'''
        output=''
        if type(l) == list:
            output = l[-1]
            del (l[-1])
        return output
    def str(self):
        list = eval(input('Enter a sequence of string :'))
        ''.join(list)
        reduce = (lambda x, y: x + y, list)
        import functools, operator
        functools.reduce(operator.add, list)
        return list
    def square(x):
        square = lambda x: x * x
        l = []
        a = 0
        for i in range(100):
            a = square(i)
            l.append(a)
        square(x)
        return  l
    def lambda_func(self):
        x = lambda a, b, c: a + b + c
        logging.info(x(10, 20, 30))
        x = lambda x, n: x ** n
        logging.info(x(10, 20))
        x = lambda x: x * 2
        logging.info(x(10))
        x = lambda x: x + x
        logging.info(x(11))
        l = [1, 2, 3, 4, 5, 6, 7]
        output = list(filter(lambda x: x % 2 == 0, l))
        logging.info(output)
        l = [1, 2, 3, 4, 5, 6]
        output = list(map(lambda x: x * x, l))
        logging.info(output)
        s = [5, 6, 7, 8, 9, 4]
        output = set(map(lambda x: x * x * x, s))
        logging.info(output)
        s = list(range(20))
        output = list(filter(lambda x: x % 2 != 0, s))
        logging.info(output)
        maximum = lambda a, b: a if a > b else b
        logging.info(maximum(10, 20))
        citizen = [10, 52, 86, 45, 69, 47, 75, 92]
        old = list(filter(lambda senior: senior > 60, citizen))
        logging.info(old)
    def read(self):
        open('test.txt')



s=String_class()
logging.basicConfig(filename='test.log', level=logging.INFO)
logging.info(s.index())
logging.info(s.reverse())
logging.info(s.split())
logging.info(s.lower())
logging.info(s.capitalize())
logging.info(s.strip())
logging.info(s.replace())
logging.info(s.center())

l=List_class()
logging.info(l.reverse_without_func())
logging.info(l.reverse_with_function())
logging.info(l.list_Collection())
logging.info(l.extract())
logging.info(l.key())

p=Pattern()
p.pattern()
p.diamond()

l=Loop()
logging.info(l.div_by_3())
logging.info(l.vowels())
logging.info(l.even_num())
logging.info(l.system_date_time())
l.mail()
l.txt_to_voice()
l.alarm()
l.ip_address()
l.installation()
logging.info(l.length_string('subhasish'))
logging.info(l.element_index(9))
logging.info(l.dict_to_list({1:2},{4:6},{9:8}))
logging.info(l.list_concat(['sai','subhasish','rout'],['pragati','parida']))
logging.info(l.prime_in_range(1000))
logging.info(l.print_func((1,2,3,4,5)))
logging.info(l.list_append(1, 3, 5, 4, 8, 8656, 6, 6))
logging.info(l.extend([4, 2, 5, 8, 6, 9], {1, 5, 8, 8, 9, 6}))
logging.info(l.pop([1, 2, 5, 4, 8, 6]))
logging.info(l.str())
logging.info(l.square(100))
l.lambda_func()
logging.info(l.read())













