from docxtpl import DocxTemplate
import csv
from datetime import datetime
def lab1():
    number = "968247916"
    free_inp_mins = 5
    free_sms = 5
    sms_price = 1
    outp_price = 4
    inp_price = 1

    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['msisdn_origin'] == number:
                if int(row['sms_number']) < free_sms:
                    sms = 0
                else:
                    sms = (int(row['sms_number']) - free_sms) * sms_price
                inp = sms * 1 + float(row['call_duration']) * outp_price
            elif row['msisdn_dest'] == number:
                if float(row['call_duration']) > float(free_inp_mins):
                    outp = (float(row['call_duration']) - float(free_inp_mins)) * inp_price
    return (inp + outp)

def lab2():
    addr = "192.168.250.1"
    kb = 0
    x = []
    y = []
    with open('data3.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['sa'] == addr) | (row['da'] == addr):
                kb = kb + int(row['ibyt'])
                x.append(datetime.strptime(row['ts'], "%Y-%m-%d %H:%M:%S"))
                y.append(kb / 1048576)
    # print(x)
    # print(y)
    k = 0.5
    sum = 0.5
    sum = sum - 0.5
    mb = kb / 1048576
    # print(mb)
    while mb >= 500:
        sum = sum + (500 * k)
        k = k + 0.5
        mb = mb - 500

    sum = sum + (mb * k)
    return (sum)

doc = DocxTemplate("lab3_tmpl.docx")
context = { 'bank' : 'ПАО Известный Банк',
            'bik' : '547454',
            'kpp':'665464',
            'reciever':'ЗАО Планета',
            'first': '21456454564',
            'second': '8765465465',
            'inn': '213546574',
            'address1' : 'г. Москва, ул. Пушкина, д. 11',
            'index' : '987654',
            'address2' : 'г. Москва, ул.Красного Текситльщика, д.145 ',
            'osnovanie':'Договор №6 от 19.05.2020',
            'name1':'Телефония',
            'name2':'Интернет',
            'sum1': lab1(),'sum2': lab2(),
            'overall': lab1()+lab2(),
            'director':'Петров.П.П.',
            'accountant':'Петрова.П.П.',
            'n':'2','d':'1 июня','y':'20', 'buy':'ООО Зеленоглазое такси', 'rus': 'rub'}
doc.render(context)
doc.save("lab3.docx")