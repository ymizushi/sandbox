class Promise
    def __init__(self, f):
        self._f = f

    def then(self, succeed, failed):
        status = self._f()
        if status:
            succeed()
        else:
            failed()

    def catch(self):
        pass


def __name__== '__main__':
    promise = Promise()
    promise.then(
      lambda x: x
    )
    .then(
            lambda x: x)
    .catch(
            )


