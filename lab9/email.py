def linear_search(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)

    for i in range(text_length - pattern_length + 1):
        match = True
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i, i + pattern_length

    return -1


fin = open('email.html', encoding='UTF-8')
text = fin.read()

pattern = 'mailto:'
pos = linear_search(text, pattern)
emails = []

while pos != -1:
    email_start = pos[1]
    text = text[email_start:]
    pos = linear_search(text, '"')
    email_end = pos[0]
    emails.append(text[:email_end])
    pos = linear_search(text, pattern)

print('\n'.join(emails))
