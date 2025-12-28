from django.shortcuts import render, get_object_or_404

developers_list = [
    {"first_name": "Ichigo", "last_name": "kurosaki", "username": "Tensa Zangetsu", "skills": ["Bankai", "hollow"]},
    {"first_name": "Ichimaru", "last_name": "Gin", "username": "Kamishini No Yari", "skills": ["Bankai", "kido"]},
]

def developers_list_view(request):
    return render(request, 'developers_list.html', {'developers': developers_list})

def developer_cv_view(request, username):
    dev = next((d for d in developers_list if d['username'] == username), None)
    if not dev:
        return render(request, '404.html')  
    return render(request, 'developer_cv.html', {'developer': dev})