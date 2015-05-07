welcome1 = 'Welcome to Space Odyssey!'
welcome2  = 'Make your way through the Asteroid Belt and return to the Earth!'
loose_c = "You've lost the game. Try again!"
length = 0
length1 = 0
length = len(welcome1)
length1 = len(welcome2)
def makebold(fn):
    def wrapped():
        print ('_'*length1,'\n')
        fn()
        print('_'*length1)
    return wrapped

def first_welcome():
    need_l = int((length1-length)/2-1)
    @makebold
    def big ():
        def makecenter(fn):
            def wrapped(welcomef):
                print('_'*need_l, end=" ")
                print(fn(welcomef), end = " ")
                print('_'*need_l)
            return wrapped
        @makecenter
        def first(welcomef):
            return welcomef
        first(welcome1)
        print (welcome2)
    big()


def level_2_welcome():
    @makebold
    def encourage_1():
        print('Good job! Second level is upon us!')

def loose_conf():
    @makebold
    def conf():
        print(loose_c)
    conf()

