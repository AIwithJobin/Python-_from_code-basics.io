book={}

book["tom"]={
    'name':'tom',
    'address':'1 red street,NY',
    'phone':'9744469742',
}
book["jobin"]={
    'name': 'melani',
    'address': 'kolecnchery house,manickamangalam',
    'phone': '9744469742',

}
import json
s=json.dumps(book)
with open("C://Users//jobin jose//OneDrive//Desktop//book.txt","w")as f:
    f.write(s)

