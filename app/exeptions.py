
class ServiceError(Exception):
    data_fields = ["userMessage", "errorCode", "status"]

    def __init__(self, **kwargs):
        super(ServiceError, self).__init__()
        self.userMessage = kwargs.get("userMessage")
        self.errorCode = kwargs.get("errorCode")
        self.status = kwargs.get("status")

    def info(self):
        return {"userMessage": self.userMessage,
                "errorCode": self.errorCode}
