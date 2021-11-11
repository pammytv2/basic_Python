# def greetings(lang):
#     if lang =='th':
#         print('สวัสดี')
#     elif lang =='en':
#         print('Hello')
#     elif lang =='jp':
#         print('こんにちは')
#     else:
#         print('Erro')

# greetings("th")
eng = int(input('คะแนนภาษาอังกฤษ: '))
interview = int(input('คะแนนการสอบ: '))
math = int(input('คะแนนความรู้ทางคณิตศาสตร์: '))


def meet(eng, interview,math):
    if eng > 70  and interview > 80 and math > 60 and eng + interview + math > 180:
        print('ผ่าน')
        return True
    else:
        return False
print(meet(eng, interview,math))

