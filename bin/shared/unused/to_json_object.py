import json
from json import encoder, JSONEncoder

class SelectiveEncoder(JSONEncoder):

    export_keys = []

    def default(self, o):
        return {k: o.__dict__[k] for k in set(self.export_keys) & set(o.__dict__.keys())}

class ToJsonObject(JSONEncoder):

    def to_JSON(self):
        encoder.FLOAT_REPR = lambda o: format(o, '.3f')
        # return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

    def to_JSON_file(self, filename, mode='w'):
        f = open(filename, mode)
        f.write(self.to_JSON())
        f.close()



if __name__ == '__main__' :
    class ExternalMyData():
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def JSON(self):
            encoder.FLOAT_REPR = lambda o: format(o, '.3f')
            return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)


    class InternalMyData():
        def __init__(self, address):
            self.address = address


    class MyData(ExternalMyData, InternalMyData):
        def __init__(self, name, age , address):
            ExternalMyData.__init__(self, name, age)
            InternalMyData.__init__(self, address)


        def to_JSON(self):
            ExternalMyData.JSON(self)

    me = MyData('Lee', [11.2334, 23.45], 'Seoul, 111')

    print (me.to_JSON())

    #me.to_JSON_file('test.json')
    #t = list(set(['age']) & set(me.__dict__.keys()))

    #print me.__dict__['age']
