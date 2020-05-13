import math
import hashlib
import functools

lruCache = []


def lru_cache(max_size):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            i = 0
            while i < len(lruCache):
                obj = lruCache[i]
                if obj["params"] == args:
                    print("[cache-hit]")
                    del lruCache[i]
                    lruCache.append(obj)
                    return obj["return"]
                i = i + 1

            res = func(*args)
            obj = {
                "params": args,
                "return": res,
            }
            if len(lruCache) < max_size:
                lruCache.append(obj)
                return res
            else:
                del lruCache[0]
                lruCache.append(obj)
            return res

        return wrapper

    return decorator
