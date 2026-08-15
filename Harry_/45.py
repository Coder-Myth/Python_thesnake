# how if __name__ = "__main__" works in python

from sample import rakesh 

print(rakesh())
# rakesh() now if this is not in if __name__ = "__main__"=====> this prints rakesh ed techaer 2 times if inside this file 
# prints it one time only if imported in the other file if in the same file it makes the function run 

print(__name__ )# tells you from where is this file imported or if inside the same file it shows __main__

