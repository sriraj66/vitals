passwd = ["q81vzG", "94xP3m", "H1lS2T", "4pOM7v", "6W9Fwo",
          "yKn2Qd", "sN4jaE", "e5pDJh", "vzB8nR", "p9SxYu"]
username = ["arjun", "divya", "gowtham", "kavitha",
            "manoj", "nithya", "prakash", "rani", "suresh", "vani"]
name = ["Arjun", "Divya", "Gowtham", "Kavitha", "Manoj",
        "Nithya", "Prakash", "Rani", "Suresh", "Vani"]
numbers = ["9678564321", "9123456789", "9567890123", "9009876543", "9112233445",
           "9900012345", "9555500001", "9444433332", "9888899997", "9777755556"]
email = [
    "arjun@gmail.com",
    "divya@yahoo.com",
    "gowtham@outlook.com",
    "kavitha@hotmail.com",
    "manoj@example.com",
    "nithya@gmail.com",
    "prakash@yahoo.com",
    "rani@outlook.com",
    "suresh@hotmail.com",
    "vani@example.com"
]

name[i],username[i],passwd[i],numbers[i],email[i]

def create_user(name, u, p, n,e):
    user = User(username=u, password=p, first_name=name,email=e)
    user.set_password(p)
    user.save()
    pro = Profile(user=user,desg='DOCTOR',number=n)
    pro.save()

    print(user.id,pro.id)

