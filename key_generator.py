import hashlib as h
import secrets as s

token = h.new('sha256')
token.update(s.token_urlsafe(16).encode("utf-8"))
print(token.hexdigest())
