import psutil
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")

def utility():
    cpu_using = psutil.cpu_percent()
    mem_using = psutil.virtual_memory().percent
    Report = "Under Utilized"
    if cpu_using > 80 and mem_using > 80:
        Report = "!!! Warning !!! CPU and Memory Utilization is high !!! Warning !!!"
    elif cpu_using > 80 and mem_using < 80:
        Report = "!!! Warning !!! CPU Utilization is high !!! Warning !!!"
    elif mem_using > 80 and cpu_using < 80:
        Report = "!!! Warning !!! Memory Utilization is high !!! Warning !!!"
    return render_template("index.html", cpu_using=cpu_using, mem_using=mem_using, report=Report)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')