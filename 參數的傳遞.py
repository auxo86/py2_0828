def sample_var_args_call(arg1, arg2, arg3):
    print '---'
    print arg1, arg2, arg3

tupleArguments = ('two', 3)
sample_var_args_call(1, *tupleArguments)
args2 = ['one', 'two', 'three']
sample_var_args_call(*args2)
args3 = {'X': 'X\'s mas', 'Y': 'y-combinator', 'Z': 'Zoo'}
sample_var_args_call(*args3)