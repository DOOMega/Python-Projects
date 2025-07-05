
class Package:

    def __init__(self, package_id, sender, receiver, status = "Pending"):
        self.p_id = package_id
        self.sender = sender
        self.receiver = receiver
        self.status = status
    
    def update_id(self, new_id):
        self.p_id = new_id

    def display_package(self):
        print(f'Package id: {self.p_id} | sender: {self.sender} | receiver: {self.receiver} | status: {self.status}')

    def update_status(self, new_status):
        self.status = new_status


class Logistic_System():

    def __init__(self):
        self.Packages = []

    def add_package(self):
        new_package_id = input("Enter Package id Name: ")
        new_sender = input("Enter Sender Name: ")
        new_receiver = input("Enter Receiver Name: ")
        new_package = Package(new_package_id, new_sender, new_receiver)

        self.Packages.append(new_package)
        print('New package added.\n')
   
    def view_packages(self):
        if not self.Packages:
            print('No Packages.\n')
            return
        
        for package in self.Packages:
            package.display_package()
        
    def update_package(self):
        pack_id = input("Enter pack id to update: ")
        for pack in self.Packages:
            if pack.p_id == pack_id:
                new_status = input("Enter status to update: ")
                pack.update_status(new_status)
                print("Status updated.\n")
                return
            
            print("package not found.\n")


    def run(self):
        while True:

            print("Logistic App Menu")

            print("1. Add Package")

            print("2. View Package")

            print("3. Update Package Status")

            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_package()
            elif choice == "2":
                self.view_packages()
            elif choice == "3":
                self.update_package()
            elif choice == "4":
                print("Exiting...\n")
                break
            else:
                print("Invalid choice.\n")

if __name__ == "__main__":
    app = Logistic_System()
    app.run()