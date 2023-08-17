from bs4 import BeautifulSoup

html_code = """
	
"""

soup = BeautifulSoup(html_code, 'html.parser')

questions = soup.find_all('div', class_='panel-heading')
for question in questions:
    question_text = question.get_text(strip=True)
    print(f"Pitanje: {question_text}")

    answers = question.find_next('table').find_all('td', class_='has-radio-button')
    for index, answer in enumerate(answers):
        answer_text = answer.find_next('td').get_text(strip=True)
        print(f"Odgovor {index + 1}: {answer_text}")