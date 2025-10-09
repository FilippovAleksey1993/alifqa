import allure
import json

def attach_reqres(response):
    request = response.request


    allure.attach(request.method, name='Метод Запроса',
                  attachment_type=allure.attachment_type.TEXT)

    allure.attach(request.url, name='URL Запроса',
                  attachment_type=allure.attachment_type.TEXT)
    
    if request.body:
        allure.attach(response.request.body, name='Тело Запроса',
                  attachment_type=allure.attachment_type.JSON)

    # allure.attach(request.headers, name='Header Запроса',
    #               attachment_type=allure.attachment_type.JSON)
