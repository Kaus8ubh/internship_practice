
ones=["", "one", "two", "three", "four", "five", "six", "seven","eight", "nine"]
teens=["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens=["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty","ninety"]
def no_to_word(no):
  if no==0:
    return "zero"
  word=""
  if no >= 100000:
    word += ones[no//100000] + " lakh "
  no %= 100000
  if (no//1000 >= 10 and no//1000 <= 19):
    word += teens[no//1000] + " thousand "
  if no >= 20000:
    word += tens[no//10000]
  no %= 10000
  if no >= 1000:
    word += ones[no//1000] + " thousand "
  no%=1000
  if no >= 100:
    word += ones[no//100] + " hundred "
  no%=100
  if no >= 10 and no<=19:
    word += teens[no-10]
  if no >= 20:
    word += tens[no//10] 
  no%=10
  if no>=0:
    word += ones[no]

  return word

print(no_to_word(321967))