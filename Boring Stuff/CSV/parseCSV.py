import csv,json



with open('names.csv') as fr:
##    csv_reader=csv.reader(fr)
##
##    #next(csv_reader)
##
##    for line in csv_reader:
##        print(line[2])


    with open('new_names.csv','w') as fw:
        #csv_writer=csv.writer(fw,delimiter='\t')
        fldname=['first_name','last_name']
        csv_writer=csv.DictWriter(fw,fldname,delimiter=',')
        csv_writer.writeheader()
    
        csv_reader=csv.DictReader(fr)
        for line in csv_reader:
            #print(line['email'])
            #print(json.dumps(line,indent=2))

            del line['email']

            csv_writer.writerow(line)
