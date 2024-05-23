import timeit
import logging

# perf_logger = logging.getLogger()
ON = logging.INFO
OFF = logging.WARNING
formatter = logging.Formatter('%(asctime)s:%(message)s')
perf_logger = logging.getLogger(__name__)
perf_logger.setLevel(ON)
perf_handler = logging.FileHandler('perflogs.log')
perf_handler.setFormatter(formatter)
perf_logger.addHandler(perf_handler)



# logging.basicConfig(filename = 'perflogs.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(module)s:%(message)s')

def perflogs(function):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = function(*args,**kwargs)
        end = timeit.default_timer()
        perf_logger.info(function.__qualname__ + ":"+str(function.__code__)+":" + '{:.4f}'.format((end-start)*1000) + "ms")
        return result
    return wrapper


#calc_square(100000)
#print("hi deba")
if '__name__' == '__main__':
    class blue:
        @perflogs
        def black(self):
            lst=[]
            for x in range(101010):
                lst.append(x)



    @perflogs
    def calc_square(numbers):
        result = []
        for number in range(numbers):
            result.append(number*number)
        return result


    @perflogs
    def calc_cube(numbers):
        result = []
        for number in range(numbers):
            result.append(number*number*number)
        return result

    calc_square(100000)
    calc_cube(100000)
    print("hi")

    # obj = blue()
    # obj.black()
    # calc_cube(10000000)
