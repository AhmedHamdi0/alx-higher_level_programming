#!/usr/bin/python3
print(', '.join(str(i).zfill(2) if i != 99 else str(i) for i in range(100)))
