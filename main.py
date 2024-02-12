from Singleton import Singleton
# To create or get the singleton instance
s = Singleton.getInstance()
print(s)

# Trying to create another instance will raise an exception
try:
    s2 = Singleton()
except Exception as e:
    print(e)

# However, getting the instance again will return the same instance
s3 = Singleton.getInstance()
print(s3)  # This will print the same instance as before