# Stub ipywidgets for headless/CI execution.
# Replaces blocking widget calls with no-ops so notebooks execute without hanging.
# In Colab/Jupyter with a real frontend, the real ipywidgets is used instead.
#
# Installed into ~/.ipython/profile_default/startup/ by the setup-ci-tools action
# so it runs automatically before any notebook cell when nbconvert spawns a kernel.
import sys
import types
import inspect


class _NoOpWidget:
    """A no-op stand-in for any ipywidgets widget class."""

    children = []

    def __init__(self, *args, **kwargs):
        # Preserve value/options so _Interact can extract call defaults
        object.__setattr__(self, "value", kwargs.get("value", None))
        object.__setattr__(self, "options", kwargs.get("options", []))

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    def __getattr__(self, name):
        # Return a no-op callable for any unknown method/attribute
        return lambda *args, **kwargs: None


class _Interact:
    """Stub for widgets.interact / widgets.interactive.

    Calls the wrapped function once with default values extracted from
    widget stubs so that matplotlib outputs are captured by nbconvert.
    """

    def __call__(self, *args, **kwargs):
        if len(args) == 1 and callable(args[0]) and not kwargs:
            # Bare @widgets.interact — extract defaults from widget params
            return self._call_with_defaults(args[0])
        # @widgets.interact(param=slider) — return decorator
        widget_kwargs = kwargs

        def decorator(f):
            return self._call_with_defaults(f, widget_kwargs)

        return decorator

    def _call_with_defaults(self, f, widget_kwargs=None):
        sig = inspect.signature(f)
        call_kwargs = {}
        for name, param in sig.parameters.items():
            widget = (widget_kwargs or {}).get(name)
            if widget is None and param.default is not inspect.Parameter.empty:
                widget = param.default
            if isinstance(widget, _NoOpWidget) and widget.value is not None:
                call_kwargs[name] = widget.value
            elif widget is not None and not isinstance(widget, _NoOpWidget):
                call_kwargs[name] = widget
        try:
            f(**call_kwargs)
        except Exception as e:
            print(f"[stub] interact call skipped: {e}")
        return f


class _StubModule(types.ModuleType):
    """ipywidgets stub module.

    Any attribute access returns _NoOpWidget so that
    'from ipywidgets import AnythingAtAll' always succeeds.
    """

    interact = _Interact()
    interactive = _Interact()

    def __getattr__(self, name):
        if name.startswith("__"):
            raise AttributeError(name)
        return _NoOpWidget


stub = _StubModule("ipywidgets")
stub.widgets = stub  # support: from ipywidgets import widgets
sys.modules["ipywidgets"] = stub
sys.modules["ipywidgets.widgets"] = stub

print("ipywidgets stubbed for headless CI execution")
