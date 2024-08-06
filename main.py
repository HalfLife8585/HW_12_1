import re
import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    # Читання вхідного файлу
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Видалення HTML-тегів
    clean_text = re.sub(r'<[^>]+>', '', html)

    # Очищення від порожніх рядків
    clean_text = '\n'.join([line.strip() for line in clean_text.split('\n') if line.strip()])

    # Запис очищеного тексту у вихідний файл
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(clean_text)


# Приклад використання
delete_html_tags('draft.html', 'cleaned.txt')
