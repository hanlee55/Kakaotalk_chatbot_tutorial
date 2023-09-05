from flask import Flask, jsonify, request
import sys, json, datetime
application = Flask(__name__)

days_of_the_week_list = ['월', '화', '수', '목', '금', '토', '일']
@application.route("/day", methods=["POST"])
def day_of_the_week():
    request_data = json.loads(request.get_data(), encoding='utf-8')
    print(request_data)
    date_string = request_data['action']['detailParams']['sys_date']['origin']
    print(date_string)

    date_string = date_string.replace(" ", "")
    for i in ["%y년%m월%d일", "%m월%d일", "%Y년%m월%d일"]:
        try:
            date_obj = datetime.datetime.strptime(date_string, i)
            if i == "%m월%d일":
                date_obj = date_obj.replace(year=datetime.datetime.now().year)
            break
        except:
            continue
    print(date_obj)

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": days_of_the_week_list[date_obj.weekday()] + "요일"
                    }
                }
            ]
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
