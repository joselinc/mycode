#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
proto1 = ["ssh", "http", "https"]
print(proto)
proto.append("dns")
proto1.append("dns")
proto2 = [20, 80, 443, 53]
proto.extend(proto2)
print(proto)
proto1.append(proto2)
print(proto1)

