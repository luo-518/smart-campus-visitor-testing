from flask import Flask, render_template, request, redirect
from datetime import datetime
import uuid
from storage import add_booking, get_all_bookings, find_booking_by_code, blacklist

app = Flask(__name__)

# 首页：预约表单
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        visitor_name = request.form['visitor_name']
        visitor_id = request.form['visitor_id']
        host = request.form['host']
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        visitor_code = uuid.uuid4().hex[:8]  # 简化版访客码

        booking = {
            "visitor_name": visitor_name,
            "visitor_id": visitor_id,
            "host": host,
            "start_time": start_time,
            "end_time": end_time,
            "status": "PENDING",
            "visitor_code": visitor_code
        }

        add_booking(booking)
        return redirect('/admin')

    return render_template('index.html')

# 审批列表页面
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    all_bookings = get_all_bookings()

    if request.method == 'POST':
        code = request.form['code']
        action = request.form['action']

        booking = find_booking_by_code(code)
        if booking:
            if booking["status"] == "PENDING":
                if action == "approve":
                    booking["status"] = "APPROVED"
                elif action == "reject":
                    booking["status"] = "REJECTED"

        return redirect('/admin')

    return render_template('admin.html', bookings=all_bookings)

# 门禁验证
@app.route('/gate', methods=['GET', 'POST'])
def gate():
    result = None

    if request.method == 'POST':
        code = request.form['code']
        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        booking = find_booking_by_code(code)
        if not booking:
            result = "拒绝进入：预约不存在"
        else:
            # 黑名单检查
            if booking["visitor_name"] in blacklist:
                result = "拒绝进入：访客在黑名单中"
            
            # 审批检查
            elif booking["status"] != "APPROVED":
                result = "拒绝进入：预约未通过审批"
            
            # 时间检查
            else:
                now_dt = datetime.now()
                start_dt = datetime.strptime(booking["start_time"], "%Y-%m-%dT%H:%M")
                end_dt = datetime.strptime(booking["end_time"], "%Y-%m-%dT%H:%M")


                if start_dt <= now_dt <= end_dt:
                    result = "允许进入：欢迎访问校园"
                else:
                    result = "拒绝进入：不在预约时间范围内"

    return render_template('gate.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
