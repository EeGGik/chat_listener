from views import HeathCheck, MessageChecker


def add_routes(app):
    app.add_url_rule('/manage/health',
                     view_func=HeathCheck.as_view(name='health_check'),
                     methods=['GET'])

    app.add_url_rule("/check_message",
                     view_func=MessageChecker.as_view(name='message_checker'),
                     methods=['POST'])
    return app
