import module_1
import module_2
import numpy as np

class Human:
    number_of_humans = 0

    def __init__(self,first_name="Max", last_name="Mustermann", age=100, sex="gay"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        Human.number_of_humans = Human.number_of_humans + 1

    def get_email(self):
        return self.first_name + '.' + self.last_name + '@web.de'


class Deutsch(Human):
    def __init__(self,first_name="Max", last_name="Mustermann", age=100, sex="gay",Kanzler="Merkel"):
        Human.__init__(self,first_name,last_name,age,sex)
        self.Kanzler= Kanzler

if __name__ == "__main__":

    B = [[22,11], [222,5]]

    B = np.array(B)
    print(B.shape[0])

    C = np.array([[78, 7], [45, 10]])

    D = np.ndarray(shape=(2,2))
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            # print(i,j)
                D[i][j] =  B[i][j] + C[i][j]

    print(type(D[0][0]))
    print("thomas_" + "bernhard")
