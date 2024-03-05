from flask import Flask, jsonify, json
from random import choice

app = Flask(__name__)
json.provider.DefaultJSONProvider.ensure_ascii = False

@app.route('/api/8ball')
def iball():
    messages = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
                "Мне кажется — «да»", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят — «да»", "Да",
                "Пока не ясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
                "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ — «нет»", "По моим данным — «нет»",
                "Перспективы не очень хорошие", "Весьма сомнительно"]
    return jsonify({"answer": choice(messages)}), 200

@app.route('/api/is-even/<string:number>')
def is_even(number: str):
    try:
        num = int(number)
        return jsonify({"number": number, "isEven": num % 2 == 0}), 200
    except:
        return jsonify({"error": "Не удалось преобразовать параметр в число"}), 400