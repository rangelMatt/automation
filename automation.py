import re

with open("./assets/potential-contacts.txt")as f:
  text_from_file = f.read()

def number_slicer(phone_number):
  complete_num = phone_number[:3] + '-' + phone_number[3:6] + "-" + phone_number[6:]
  return complete_num

def find_phone_numbers(txt):
  pattern1 = re.compile(r"\d{3}\D?\d{3}\D?\d{4}")
  
  found_numbers = re.findall(pattern1, text_from_file)

  stripped = []
  for num in found_numbers:
    stripped_numbers = re.sub('[-.)(]', "", num)
    stripped.append(stripped_numbers)
    # print(stripped)
  
  dashed_nums = []
  for phone_num in stripped:
    final_num = number_slicer(phone_num)
    dashed_nums.append(final_num)
    number_set = list(set(dashed_nums))
    # print(number_set)
    
    with open("phone_numbers.txt","w") as f:
      for x in number_set:
        f.write(x)
        f.write('\n')
    
find_phone_numbers(text_from_file)

def find_emails(text):
  pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
  extracted_emails = re.findall(pattern, text_from_file)
  email_set = list(set(extracted_emails))
  
  


  with open("email.txt","w") as efile:
    for x in email_set:
      efile.write(x)
      efile.write('\n')
      
find_emails(text_from_file)