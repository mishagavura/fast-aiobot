from commands import *

print("----Hello, this lib was created by mgvr ( evdev )")
print("----https://instagram.com/everything_development\n")
print('----happy telewriting\n')

def main():
	file = open('text_to_bot.txt', 'r', encoding='utf-8')
	file = file.read().split('\n')
	k = 0
	for item in file:
		func_name = item.split(' | ')[0]
		# specialChars = "" 
		func_type = item.split(' | ')[1]
		# print(func_name)
		# print(func_type)
		if func_type == 'options':
			if not check_installed(item.split(' | ')[0]):
				func_options_list = item.split(' | ')[2].split(', ')
				try:
					new_state = file[k+1].split(' | ')[0]
				except Exception:
					new_state = 'free'
				set_text = 'Оберіть потрібну вам категорію'
				prev_state = item.split(' | ')[0]
				write_to_bot_options(prev_state, new_state, 'options', set_text, func_options_list, item.split(' | ')[3])
				find_callback_func = find_callback()
				print('--find callback_func => ', find_callback_func)
				if find_callback_func == -1:
					create_callback()
					installed_to_bot('callback_func')
				else:
					pass
				try:
					text = file[k+1].split(' | ')[2]
				except Exception:
					text = 'Thanks! Everything was saved!'
				add_to_callback(callback_command(func_options_list, text, new_state, item.split(' | ')[3]))
			else:
				prev_state = item.split(' | ')[0]
				print(f'--already installed => {prev_state}')
		elif func_name == 'start':
			if not check_installed(item.split(' | ')[0]):

				new_state = file[k+1].split(' | ')[0]
				# print('new_state ', new_state)
				set_text = item.split(' | ')[2]
				write_to_bot('', f'{new_state}', 'start', f'{set_text}')
			else:
				prev_state = item.split(' | ')[0]
				print(f'--already installed => {prev_state}')
		elif func_type == 'text':
			if not check_installed(item.split(' | ')[0]):
				try:
					new_state = file[k+1].split(' | ')[0]
				except Exception:
					new_state = 'free'

				set_text = item.split(' | ')[2]
				prev_state = item.split(' | ')[0]
				write_to_bot(prev_state, f'{new_state}', 'text', f'{set_text}')
			else:
				prev_state = item.split(' | ')[0]
				print(f'--already installed => {prev_state}')
		elif func_type == 'run_bot':
			if not check_installed(item.split(' | ')[1]):
				install_to_bot(run_bot)
				installed_to_bot('run_bot')
				print('\n--installed => run_bot')
			else:
				print('--already installed => run_bot')
		k+=1
def initialize():
	file = open('new_bot_config.txt', 'r', encoding='utf-8')
	for item in file.read().split('\n'):
		if item.split(' ')[0] == '--initialize':
			# write_to_bot('')
			if item.split(' ')[1] == 'aiogram':
				if not check_installed('aiogram'):
					install_to_bot(aiogram_init_cmd)
					print('--initializing aiogram')
					installed_to_bot('aiogram')
				else:
					print('--already initialized => aiogram')
					
		elif item.split(' ')[0] == '--install':
			if item.split(' ')[1] == 'logs':
				if not check_installed('logs'):
					install_to_bot(logs_cmd)
					print('--installing logs')
					installed_to_bot('logs')
					f = open("logs.txt","w+")
					print('--created file => logs.txt')
				else:
					print('--already installed => logs')

			elif item.split(' ')[1] == 'send_logs':
				if not check_installed('send_logs'):
					install_to_bot(send_logs_cmd)
					print('--installing send_logs def')
					installed_to_bot('send_logs')
				else:
					print('--already installed => send_logs def')


def write_to_bot_options(prev_state_name, new_state_name, type_func, text, options_arr, t_sel):
	installed_to_bot(prev_state_name)
	file = open('ready_bot.txt', 'a', encoding='utf-8')
	command = f"""
@dp.message_handler(content_types=['text'], state='{prev_state_name}')""" \
"""
async def save_name(message, state: FSMContext):
	markup = types.InlineKeyboardMarkup(row_width=1)"""
	k = 0
	str_btns = []
	for item in options_arr:
		command += f"""
	btn{k} = types.InlineKeyboardButton(text='{item}', callback_data=json.dumps(""" + """{'t': """ + f"""'{t_sel}',""" + """ 'v':""" + f"""'{item}'""" + """}))"""
		str_btns.append(f'btn{k}')
		k+=1
	# btn1 = types.InlineKeyboardButton(text='Housing / Житлом', callback_data=json.dumps({'t': 'help_provide', 'v':'housing'}))
	# btn2 = types.InlineKeyboardButton(text='Transportation / Транспортом', callback_data=json.dumps({'t': 'help_provide', 'v':'transport'}))
	# btn3 = types.InlineKeyboardButton(text='Baby sitting / Доглядом за дітьми', callback_data=json.dumps({'t': 'help_provide', 'v': 'baby_sitting'}))
	str_btns_str = ', '.join(str_btns)
	command += f"""
	markup.add({str_btns_str})
	await bot.send_message(message.from_user.id, '{text}', reply_markup=markup)

	"""
	print(f'--enabled {type_func} => "{text}"')
	print(f'--changed state => "{new_state_name}"\n')
	file.write(f'{command}')
	file.close()


def write_to_bot(prev_state_name, new_state_name, type_func, text):
	file = open('ready_bot.txt', 'a', encoding='utf-8')
	if type_func == 'start':
		installed_to_bot('start')

		command = """
		
@dp.message_handler(commands=['start'], state='*')
async def start_def(message, state: FSMContext):""" \
f"""
	await bot.send_message(message.from_user.id, '{text}')
	await state.set_state('{new_state_name}')
"""
		print(f'--enabled start => "{text}"')
		print(f'--changed state => "{new_state_name}"\n')


	elif type_func == 'text':
		installed_to_bot(prev_state_name)

		command = f"""
@dp.message_handler(content_types=['text'], state='{prev_state_name}')""" \
f"""
async def save_name(message, state: FSMContext):
	await bot.send_message(message.from_user.id, '{text}')
	await state.set_state('{new_state_name}')
	"""
	print(f'--enabled {type_func} => "{text}"')
	print(f'--changed state => "{new_state_name}"\n')
	file.write(f'{command}')
	file.close()


def install_to_bot(command):
	file = open('ready_bot.txt', 'a', encoding='utf-8')
	file.write(f'{command}')
	file.close()


def installed_to_bot(title):
	file = open('installed_to_bot.txt', 'a', encoding='utf-8')
	file.write(f'{title}\n')
	file.close()

def check_installed(title):
	file = open('installed_to_bot.txt', 'r', encoding='utf-8')
	# file.write(f'{title}\n')
	installed = False
	for item in file.read().split('\n'):
		if item == title:
			installed = True
	return (installed)
	file.close()     

def find_callback():
	file = open('ready_bot.txt', 'r', encoding='utf-8').read()
	return (file.find(search_text))



def create_callback():
	file = open('ready_bot.txt', 'a', encoding='utf-8')
	command = """
	
@dp.callback_query_handler(lambda c: c.data, state='*')
async def inline_echo(callback_query: types.CallbackQuery, state: FSMContext):
	json_callback = json.loads(callback_query.data)	
	"""
	file.write(command)
	file.close()

def write_after_symbol(length, symbol, text):
	file = open('ready_bot.txt', 'r', encoding='utf-8').read()
	file_before = file[:symbol]
	file_after = file[length + symbol:]
	new_file = file_before + search_text + text + file_after
	file_write = open('ready_bot.txt', 'w', encoding='utf-8')
	file_write.write(new_file)
	file_write.close()


def add_to_callback(command):
	call_back_place = find_callback()
	if call_back_place != -1:
		write_after_symbol(len(search_text), call_back_place, command)
		print(f'\n--added      => new command')

	else:
		print('--error there is no callback function')

# add_to_callback()
initialize()
main() 



