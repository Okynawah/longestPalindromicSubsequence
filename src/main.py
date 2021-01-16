def largestSubseq_n2(word):
    i = 0
    lenght = len(word)
    lenghtCounter = 0
    palindrom = ""

    while i < lenght:
        j = 0
        while j < i:
            print(word[i-j] + " and " + word[i+j])
            if word[i-j] != word[i+j]:
                break
            j += 1
        if j > lenghtCounter:
            lenghtCounter = j
            palindrom = word[i-j:i+j]
        i += 1
    
    return lenghtCounter, palindrom





word = "kayak"


answer, palindrom = largestSubseq_n2(word)

print (str(answer) + " is " + palindrom)