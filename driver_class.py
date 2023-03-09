import torch

def driver_detection(img):
    # Model
    model_common = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True)
    model_common.eval()


    # Inference
    results_common = model_common(img)

    list_with_classes = []
    b = 0
    d = 0
    for i in results_common.crop():
        list_with_classes.append(i['label'].split())
        
        # print(class_and_prob[0])

        print(list_with_classes)
    
    for class_and_prob in list_with_classes:
        
        if 'person' in class_and_prob[:][0]:
            
            
    #         print('Человек обнаружен')
    #         b = 1
    #     else:
    #         if d == 0:
    #             print('Человек не обнаружен')
    #             d = 1
            
    
    # if b == 1:
            try:
                model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/best.pt') #force_reload=True
                model.eval()

                drivers_dict = {
                        1:'Водитель бодрствует👍',
                        2: 'Водитель бодрствует👍',
                        3: '❗️Водитель зевает❗️', 
                        4: '❗️Водитель зевает❗️', 
                        5: '❗️Водитель спит❗️', 
                        6: '❗️Водитель зевает❗️', 
                        7: '❗️Водитель зевает❗️', 
                        8: 'Водитель в солнцезащитных очках, для корректной работы программы их необходимо снять', 
                    }

                # Inference
                results = model(img)
                results.save()

                # Results
                # results.show()
                # получаем лист из 2 значений: на первом месте - класс, на втором - вероятность принадлежности.
                list_with_class_and_prob = results.crop()[0]['label'].split()

                #обращаемся к словарю по классу, который задетектила модель
                get_class = drivers_dict.get(int(list_with_class_and_prob[0]))

                #записываем ответ с вероятностью принадлежности к классу
                reply_msg = f'{get_class}'
                print(reply_msg)
                return reply_msg

            except Exception:
                no_detection = 'Не удалось обнаружить лицо.'
                return no_detection
    else:
        reply_msg='Прекратите издеваться над животными - пустите человека за руль'
        return reply_msg

# driver_detection('test.jpg')