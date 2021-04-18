class A:

    def __init__(self):
        self.a = "A's attribute"
        self.b = "A's attribute for collision"
        print('>>> Initializing A')
        super().__init__()

    def method_a(self):
        return 'owned by A'

    def collision(self):
        return 'owned by A'


class B:

    def __init__(self):
        self.b = "B's attribute"
        print('>>> Initializing B')
        super().__init__()

    def method_b(self):
        return 'owned by B'

    def collision(self):
        return 'owned by B'


class C(A, B):
    
    def __init__(self):
        # A.__init__(self)
        # B.__init__(self)

        super().__init__()  # super(C, self).__init__()
        print('>>> Initializing C')


if __name__ == '__main__':
    obj_c = C()

    print(obj_c.a)
    print(obj_c.b)

    print(isinstance(obj_c, B))

    print('method_a for obj_c', obj_c.method_a())
    print('method_b for obj_c', obj_c.method_b())
    print('collision for obj_c', obj_c.collision())
