
logs_cmd = """

def save_logs(text):
	file = open('logs.txt', 'a', encoding='utf-8')
	file.write(f'\\n{text}')
	file.close()
"""

send_logs_cmd = """
@dp.message_handler(commands=['logs'], state='*')
async def send_logs(message, state: FSMContext):
	file = open('logs.txt', 'r', encoding='utf-8')
	await bot.send_document(message.from_user.id, file)
"""

aiogram_init_cmd = """

loop = asyncio.get_event_loop()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage) 

"""


search_text = """
@dp.callback_query_handler(lambda c: c.data, state='*')
async def inline_echo(callback_query: types.CallbackQuery, state: FSMContext):
	json_callback = json.loads(callback_query.data)"""


def callback_command(options_arr, text, new_state, t_sel):
	print(f'--generated command => {t_sel}')
	command = f"""
	if json_callback['t'] == '{t_sel}':"""
	for item in options_arr:
		print(f'--generated callback if => {item}')
		command += f"""
		if json_callback['v'] == '{item}':
			await bot.send_message(callback_query.message.chat.id, '{text}')"""
	command += f"""
		await state.set_state('{new_state}')
	"""
	return command



run_bot = """
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
"""
