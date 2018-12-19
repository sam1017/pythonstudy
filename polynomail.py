class Polynomailitem():
   def __init__(self, coaf, expn):
       self.coaf = coaf
       self.expn = expn

   def get_coaf(self):
       return self.coaf

   def get_expn(self):
       return self.expn

   def show(self):
       print(str(self.coaf) + " " + str(self.expn))
def polynomail_mult(polynomail, polynomail_a):
    polynomail_result= []
    for polynomail_1 in polynomail_a:
        result_coaf = polynomail.get_coaf() * polynomail_1.get_coaf()
        result_expn = polynomail.get_expn() + polynomail_1.get_expn()
        polynomail_result.append(Polynomailitem(result_coaf, result_expn))
    return polynomail_result

def polynomail_add(polynomail_a, polynomail_b):
    polynomail_result= []
    i = 0
    j = 0
    while i<len(polynomail_a) and j< len(polynomail_b):
        if polynomail_a[i].get_expn() < polynomail_b[j].get_expn():
            polynomail_result.append(polynomail_a[i])
            i=i+1
        elif polynomail_a[i].get_expn() > polynomail_b[j].get_expn():
            polynomail_result.append(polynomail_b[j])
            j=j+1
        else:
            result_coaf = polynomail_a[i].get_coaf() + polynomail_b[j].get_coaf();
            if result_coaf != 0 :
                polynomail_result.append(Polynomailitem(result_coaf, polynomail_a[i].get_expn()))
            i = i+1
            j = j+1
    while i<len(polynomail_a):
        polynomail_result.append(polynomail_a[i])
        i=i+1
    while j<len(polynomail_b):
        polynomail_result.append(polynomail_b[j])
        j=j+1
    return polynomail_result

def polynomail_multi(polynomail_a, polynomail_b):
    polynomail_result= []
    for polynomail_1 in polynomail_a:
        polynomail_result = polynomail_add(polynomail_result, polynomail_mult(polynomail_1, polynomail_b))
    return polynomail_result

polynomail_a = [Polynomailitem(7, 0), Polynomailitem(3, 1), Polynomailitem(9,8), Polynomailitem(5,17)]
polynomail_b = [Polynomailitem(8,1), Polynomailitem(22,7), Polynomailitem(-9,8)]
print("polynomail_a")
for polynomal in polynomail_a:
    polynomal.show()
print("polynomail_b")
for polynomal in polynomail_b:
    polynomal.show()

polynomail_c = polynomail_add(polynomail_a, polynomail_b)
print("polynomail_a + polynomail_b = ")
for polynomal in polynomail_c:
    polynomal.show()

polynomail_d = polynomail_multi(polynomail_a, polynomail_b)
print("polynomail_a * polynomail_b = ")
for polynomal in polynomail_d:
    polynomal.show()
