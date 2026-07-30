WEB_DIRECTORY = "./web"

# Import suite_nodes symbols. Use relative import in normal package contexts,
# but fall back to top-level import so tests running modules directly still work.
try:
    from .suite_nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
except Exception:
    from suite_nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
