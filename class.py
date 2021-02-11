class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stop")

    def done(self):
        print("done")

    def model1(self):
        print("model:   ",self.model)

    

audi=Car("a7","red","audi",220)

audi.start()
audi.stop()
audi.done()
audi.model1()