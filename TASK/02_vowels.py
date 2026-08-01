# Using match, Check character is vowel or not 

# CASE 1 :
ch = input("Enter a character:")
match ch:
    case 'A':
        print("Vowel")
    case 'a':
        print("Vowel")
    case 'E':
        print("Vowel")
    case 'e':
        print("Vowel")
    case 'I':
        print("Vowel")
    case 'i':
        print("Vowel")
    case 'O':
        print("Vowel")
    case 'o':
        print("Vowel")
    case 'U':
        print("Vowel")
    case 'u':
        print("Vowel")
    case _ :
        print("Not Vowel")


# CASE 2 :
ch = input("Enter a character:")
match ch:
    case 'A' | 'a' | 'E' | 'e' | 'I' | 'i' | 'O' | 'o' | 'U' | 'u' :
        print("Vowel")
    case _ :
        print("Not Vowel")
