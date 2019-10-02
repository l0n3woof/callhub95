import pickle
fib_dict = {}
with open('fib_dict.pickle', 'rb') as handle:
    fib_dict = pickle.load(handle)
