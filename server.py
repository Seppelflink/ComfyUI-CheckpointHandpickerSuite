class _RoutesDef:
    """Minimal routes decorator container: provides get/post/etc that return
    no-op decorators so route-decorated functions remain defined during tests.
    """

    def _decorator(self, *args, **kwargs):
        def deco(func):
            return func

        return deco

    def get(self, *args, **kwargs):
        return self._decorator(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self._decorator(*args, **kwargs)

    def put(self, *args, **kwargs):
        return self._decorator(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._decorator(*args, **kwargs)


class PromptServer:
    """Minimal PromptServer shim for local import/testing."""

    def __init__(self):
        self.routes = _RoutesDef()
        self.client_id = None

    def send_sync(self, name, payload, client_id=None):
        # No-op for testing; real environment provides interactive behavior.
        return None


# Singleton instance used by suite_nodes
instance = PromptServer()
# Backwards-compatible attribute access: PromptServer.instance
PromptServer.instance = instance
