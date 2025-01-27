from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('facial_recognition_module/model.h5')

@csrf_exempt
def verify_face(request):
    if request.method == 'POST':
        image = request.FILES['image']
        image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
        image = cv2.resize(image, (128, 128))
        image = np.expand_dims(image, axis=0)
        prediction = model.predict(image)
        result = 'Match' if prediction[0] > 0.5 else 'No Match'
        return JsonResponse({'result': result})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
