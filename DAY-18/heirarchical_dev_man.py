#h create a class developer and manager which is inheriting the properties from the class employee also create class member and object members for them respectively.

class employee:
    def work(self):
        print('Employee is working')

class developer(employee):
    def code(self):
        print('Developers is coding')

class manager(employee):
    def manage(self):
        print('Manager is Managing')

dev = developer()
dev.code()
dev.work()

man = manager()
man.manage()
man.work()
