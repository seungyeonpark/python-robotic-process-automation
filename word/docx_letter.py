import docx
import datetime

template_file = './input/template/letter-template.docx'
save_file = './output/letter-kim.docx'
now = datetime.datetime.now()

new_data = {
    '★★★ 요청문': '송금 확인 요청문',
    '[[회사명]]': 'JY전자정밀',
    '[[수신인]]': '김진우',
    '[[제품명]]': 'M-123',
    '[[발행일]]': now.strftime('%Y년%m월%d일')
}

cstyle = {
    '★★★ 요청문': True
}

doc = docx.Document(template_file)

for p in doc.paragraphs:
    for k, v in new_data.items():
        if p.text.find(k) >= 0:
            p.text = p.text.replace(k, v)

            if k in cstyle:
                font = p.runs[0].font
                font.bold = True
                font.underline = True
                font.size = docx.shared.Pt(20)

doc.save(save_file)
