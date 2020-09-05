from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from app2 import models

# Create your views here.
class id():
	light_on = 'a76e264d-edb1-4456-8ba1-88d9011fdb41'
	light_off = '20373e93-4234-413b-abbe-880c5143e203'
	light_up = '9cdb16ae-7fdd-40ff-acca-17fc973d848a'
	light_down = 'd04b4f6c-1d0d-4f4a-ad09-1cbcef818347'
	light_max = '21a80993-5a5f-4fce-bf2f-96fa1fd29440'
	light_night = '0bb6c52b-2dfb-4e8b-8e38-b55f584797fa'
	circulator_on = '3b18e292-326e-4de0-a1ba-51e28eddfb41'
	circulator_off = 'fde4e0b6-25bc-4a7d-97c9-1e572e01fe02'
	circulator_plus = '3b18e292-326e-4de0-a1ba-51e28eddfb41'
	aircon = '7f862f22-ba66-46fa-aa4e-54ba726db942'

def return_json(params):
	return {'il':int((params[0]+1)/256*100), 'te':round(params[1],1), 'hu':params[2], 'mo':params[3]}

def view_test(request):
	return render(request, 'test.html')

def control_light(request):
	if request.method == 'POST':
		if 'on' in request.POST:
			models.signal_send(id.light_on)
		elif 'off' in request.POST:
			models.signal_send(id.light_off)
		elif 'up' in request.POST:
			models.signal_send(id.light_up)
		elif 'down' in request.POST:
			models.signal_send(id.light_down)
		elif 'max' in request.POST:
			models.signal_send(id.light_max)
		elif 'night' in request.POST:
			models.signal_send(id.light_night)
	params = return_json(models.get_state())
	params['name']='light'
	return render(request,'control.html',params)


def control_circulator(request):
	if request.method == 'POST':
		if 'on' in request.POST:
			models.signal_send(id.circulator_on)
		elif 'off' in request.POST:
			models.signal_send(id.circulator_off)
		elif 'plus' in request.POST:
			models.signal_send(id.circulator_plus)
	params = return_json(models.get_state())
	params['name']='circulator 〄'
	return render(request,'control_circulator.html',params)


def control_aircon(request):
	if request.method == 'POST':
		if 'on' in request.POST:
			data = {'button':''}
			models.aircon_settings(id.aircon, data)
		elif 'off' in request.POST:
			data = {'button':'power-off'}
			models.aircon_settings(id.aircon, data)
		elif 'cool' in request.POST:
			data = {'operation_mode':'cool'}
			models.aircon_settings(id.aircon, data)
		elif 'dry' in request.POST:
			data = {'operation_mode':'dry'}
			models.aircon_settings(id.aircon, data)
		elif 'warm' in request.POST:
			data = {'operation_mode':'warm'}
			models.aircon_settings(id.aircon, data)
		elif 'dir_1' in request.POST:
			data = {'air_direction':'1'}
			models.aircon_settings(id.aircon, data)
		elif 'dir_2' in request.POST:
			data = {'air_direction':'2'}
			models.aircon_settings(id.aircon, data)
		elif 'dir_3' in request.POST:
			data = {'air_direction':'3'}
			models.aircon_settings(id.aircon, data)
		elif 'dir_4' in request.POST:
			data = {'air_direction':'4'}
			models.aircon_settings(id.aircon, data)
		elif 'dir_5' in request.POST:
			data = {'air_direction':'5'}
			models.aircon_settings(id.aircon, data)
		elif 'dir_auto' in request.POST:
			data = {'air_direction':'auto'}
			models.aircon_settings(id.aircon, data)
		elif 'dir_swing' in request.POST:
			data = {'air_direction':'swing'}
			models.aircon_settings(id.aircon, data)
		elif 'temp' in request.POST:
			data = {'temperature':int(str(request.POST['temp']).replace('temp \uf2c9 ',''))}
			print(data)
			models.aircon_settings(id.aircon, data)
	params = return_json(models.get_state())
	params['name']='aircon'
	return render(request,'control_aircon.html',params)
