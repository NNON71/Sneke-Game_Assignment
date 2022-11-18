st = ['100coolguy' , '50otherguy' , '10coolguy' , '2000coolguy' ,'2otherguy']

def find_int(text):
    return int(''.join(t for t in text if t.isdigit()))


st.sort(key=find_int, reverse=True)
print(st)