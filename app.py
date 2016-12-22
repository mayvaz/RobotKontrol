
from flask import Flask, render_template, request, redirect, url_for, make_response
import motors
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #GPIO kurulum

app = Flask(__name__) #Flask server kurulum

#Kök(root) IP seçildiğinde, index.html sayfasına dön
@app.route('/')
def index():

	return render_template('index.html')

#Index.html üzerindeki düğmeye basmak için hangi pinin değiştirileceğini öğrenin
#Her buton, bu işleve bir komut tetikleyen bir sayı döndürür
#
#Motorları çalıştırmak için motors.py'den GPIO'ya komut gönderilir.
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) #Changepin'i bir int değerine ata

	if changePin == 1:
		motors.turnLeft()
	elif changePin == 2:
		motors.forward()
	elif changePin == 3:
		motors.turnRight()
	elif changePin == 4:
		motors.backward()
	else:
		motors.stop()


	response = make_response(redirect(url_for('index')))
	return(response)

app.run(debug=True, host='0.0.0.0', port=8000) #Sunucuyu 8000 numaralı bağlantı noktasına hata ayıklama modunda kurma
