# Посчитать количество слов в первом абзаце текста: https://ru.lipsum.com/feed/html

paragraph = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas dapibus quam in dignissim blandit. ' \
            'Nulla ut porttitor neque. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam a sapien non ' \
            'magna maximus sagittis a sit amet ante. Pellentesque consectetur vitae diam eget pellentesque. Sed ' \
            'gravida hendrerit lorem, a pellentesque mauris condimentum a. Morbi dictum facilisis dolor, et vehicula ' \
            'ante bibendum a. Ut sed nulla et dui sollicitudin iaculis id eu arcu. Nam at urna nec sapien r' \
            'honcus scelerisque eu sit amet felis.'

paragraph = paragraph.replace('.', ',')
list_paragraph = paragraph.split()

print(len(list_paragraph))