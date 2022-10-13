def reverse_string():
    s = input()
    n = len(s) - 1

    if n <= 0:
        return ''

    s_reversed = ''
    i_word_start = n
    i_word_end = n + 1  # i_word_end includes following space
    i = n
    while i > 0: 
        if s[i] != ' ':
           i_word_start -= 1
        else:
            s_reversed += s[i_word_start+1:i_word_end]
            # Need to insert space after the first word
            if i_word_end == n + 1:
                s_reversed += " "

            i_word_end = i_word_start + 1# - 1
            i_word_start = i - 1  # -1 as i_start will be equal to i

        i -= 1


    # Last word without space afterwards
    if len(s_reversed):
        s_reversed += s[i_word_start:i_word_end-1]
    else:
        s_reversed += s[i_word_start:i_word_end]

    return s_reversed


print(reverse_string())
