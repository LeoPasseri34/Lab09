from model.model import Model

model = Model()
model.buildGraph()
print("Num vertici:", model.getNumVertici())
print("Num archi:", model.getNumArchi())

