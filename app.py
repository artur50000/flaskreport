from flask import Flask
from flask import render_template, request
from racing_pkg import report

def get_app():

    app = Flask(__name__)

    whole_list = report.load_data("data")
    whole_list = sorted(whole_list, key=lambda x: x.Abbreviation)

    @app.route('/')
    @app.route('/report')
    def common(whole_list=whole_list):
        order = request.args.get('order')
            
        drivers_list, fail_list = report.build_report(whole_list)

        drivers_list = sorted(drivers_list, key=lambda x: x.result_time)
            
        if order == 'desc':
            drivers_list = reversed(drivers_list)

        return render_template('home.html', drivers_list=drivers_list, fail_list=fail_list)

    @app.route('/report/drivers')
    def drivers(whole_list=whole_list):

        driver_id = request.args.get('driver_id')
        order = request.args.get('order')
        one_list = []
        
        if order == 'desc':
            whole_list = reversed(whole_list)

        if driver_id:
            for item in whole_list:
                if item.Abbreviation == driver_id:
                    one_list.append(item)
            return render_template('detailed.html', one_list=one_list)
        else:
            return render_template('drivers.html', whole_list=whole_list)

    return app


if __name__ == '__main__':
    app = get_app()
    app.run(debug=True)
    