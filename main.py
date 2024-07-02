import csv

def collect_bad_word(word:str,status:str)->None:
    with open('bad-words.csv','w') as db:
        writer = csv.writer(db)
        writer.writerow([word,status])
        print(f"das Word '{word}' wurde gespichern\n",'status: bad\n','tschuss :)')
        exit()

def check_for_word(word:str)->None:
    with open('./badwords.csv','r') as db:
        csv_reader = csv.reader(db)

        for row in csv_reader:
            if word == row[0]:
                print('dieses Wort wurde bereites gesammelt\n', f'status: {row[1]}\n','tschuss :)')
                quit()


word:str = input('Bitte geben Sie dein Wort ein: ')

check_for_word(word)

status:str = input('ist das Wort schlecht (J/N)? ')

if status == 'J' or 'j':
    collect_bad_word(word,'bad')
else:
    print('dein eingeben Wort ist nicht schlecht.\n','tschuss :)')
    exit()