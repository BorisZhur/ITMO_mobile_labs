import csv

number="968247916"
free_inp_mins=5
free_sms=5
sms_price = 1
outp_price = 4
inp_price = 1

with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['msisdn_origin']==number:
            if int(row['sms_number'])<free_sms:
                sms=0
            else:
                sms = int(row['sms_number'])-free_sms
            inp = sms*1 + float(row['call_duration'])*outp_price
        elif row['msisdn_dest']==number:
            if float(row['call_duration'])>float(free_inp_mins):
                outp = (float(row['call_duration'])-float(free_inp_mins))*inp_price
print(inp+outp)