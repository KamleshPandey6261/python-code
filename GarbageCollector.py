import gc
print(gc.isenabled())
print(gc.disable())
print(gc.isenabled())
gc.enable()
print(gc.isenabled())