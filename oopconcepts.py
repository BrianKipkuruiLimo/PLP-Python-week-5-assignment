from abc import ABC, abstractmethod
import random

# ============================================================================
# ASSIGNMENT 1: DESIGN YOUR OWN CLASS - DIGITAL DEVICES
# ============================================================================

class Device:
    """Base class for all digital devices - demonstrates inheritance and encapsulation"""
    
    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self.__battery_life = battery_life  # Private attribute (encapsulation)
        self.is_on = False
        self.apps_installed = []
    
    # Getter and Setter for private attribute (encapsulation)
    def get_battery_life(self):
        return self.__battery_life
    
    def set_battery_life(self, hours):
        if hours >= 0:
            self.__battery_life = hours
        else:
            print("❌ Battery life cannot be negative!")
    
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"🔋 {self.brand} {self.model} is now ON!")
        else:
            print(f"✅ {self.brand} {self.model} is already on.")
    
    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"💤 {self.brand} {self.model} is now OFF!")
        else:
            print(f"😴 {self.brand} {self.model} is already off.")
    
    def install_app(self, app_name):
        if self.is_on:
            self.apps_installed.append(app_name)
            print(f"📱 '{app_name}' installed on {self.model}!")
        else:
            print("❌ Device must be on to install apps!")
    
    def get_info(self):
        status = "ON" if self.is_on else "OFF"
        return f"🔷 {self.brand} {self.model} - ${self.price} - Battery: {self.__battery_life}h - Status: {status}"

class Smartphone(Device):
    """Smartphone class inheriting from Device"""
    
    def __init__(self, brand, model, price, battery_life, screen_size, camera_mp):
        super().__init__(brand, model, price, battery_life)
        self.screen_size = screen_size
        self.camera_mp = camera_mp
        self.contacts = []
    
    def make_call(self, contact):
        if self.is_on:
            print(f"📞 Calling {contact} from {self.model}...")
            if contact not in self.contacts:
                self.contacts.append(contact)
        else:
            print("❌ Phone must be on to make calls!")
    
    def take_photo(self):
        if self.is_on:
            photo_quality = "HD" if self.camera_mp >= 12 else "Standard"
            print(f"📸 Taking {photo_quality} photo with {self.camera_mp}MP camera!")
            return f"{photo_quality}_photo_{random.randint(1000, 9999)}.jpg"
        else:
            print("❌ Phone must be on to take photos!")
            return None
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - Screen: {self.screen_size}\" - Camera: {self.camera_mp}MP"

class Laptop(Device):
    """Laptop class inheriting from Device"""
    
    def __init__(self, brand, model, price, battery_life, ram_gb, storage_gb):
        super().__init__(brand, model, price, battery_life)
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb
        self.files = []
    
    def run_software(self, software_name):
        if self.is_on:
            if self.ram_gb >= 8:
                print(f"💻 Running {software_name} smoothly on {self.model}!")
            else:
                print(f"⚠️  Running {software_name} (may be slow due to low RAM)")
        else:
            print("❌ Laptop must be on to run software!")
    
    def save_file(self, filename):
        if self.is_on:
            if len(self.files) * 100 < self.storage_gb * 1024:  # Rough calculation
                self.files.append(filename)
                print(f"💾 File '{filename}' saved successfully!")
            else:
                print("❌ Not enough storage space!")
        else:
            print("❌ Laptop must be on to save files!")
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - RAM: {self.ram_gb}GB - Storage: {self.storage_gb}GB"

class Tablet(Device):
    """Tablet class inheriting from Device"""
    
    def __init__(self, brand, model, price, battery_life, screen_size, has_stylus):
        super().__init__(brand, model, price, battery_life)
        self.screen_size = screen_size
        self.has_stylus = has_stylus
        self.drawings = []
    
    def draw(self, artwork_name):
        if self.is_on:
            if self.has_stylus:
                self.drawings.append(artwork_name)
                print(f"🎨 Created beautiful artwork '{artwork_name}' with stylus!")
            else:
                print(f"👆 Drew '{artwork_name}' with finger (consider getting a stylus!)")
        else:
            print("❌ Tablet must be on to draw!")
    
    def read_ebook(self, book_title):
        if self.is_on:
            print(f"📚 Reading '{book_title}' on {self.screen_size}\" screen. Perfect for reading!")
        else:
            print("❌ Tablet must be on to read!")
    
    def get_info(self):
        base_info = super().get_info()
        stylus_info = "With Stylus" if self.has_stylus else "No Stylus"
        return f"{base_info} - Screen: {self.screen_size}\" - {stylus_info}"

# ============================================================================
# ASSIGNMENT 2: POLYMORPHISM CHALLENGE - TRANSPORTATION SYSTEM
# ============================================================================

class Vehicle(ABC):
    """Abstract base class for all vehicles - demonstrates polymorphism"""
    
    def __init__(self, name, speed, fuel_type):
        self.name = name
        self.speed = speed
        self.fuel_type = fuel_type
        self.is_moving = False
    
    @abstractmethod
    def move(self):
        """Abstract method that each vehicle must implement differently"""
        pass
    
    @abstractmethod
    def stop(self):
        """Abstract method for stopping the vehicle"""
        pass
    
    def get_info(self):
        return f"{self.name} - Speed: {self.speed} km/h - Fuel: {self.fuel_type}"

class Car(Vehicle):
    """Car class implementing Vehicle - demonstrates polymorphism"""
    
    def __init__(self, name, speed, fuel_type, doors):
        super().__init__(name, speed, fuel_type)
        self.doors = doors
    
    def move(self):
        if not self.is_moving:
            self.is_moving = True
            print(f"🚗 {self.name} is driving on the road at {self.speed} km/h!")
        else:
            print(f"🚗 {self.name} is already driving!")
    
    def stop(self):
        if self.is_moving:
            self.is_moving = False
            print(f"🛑 {self.name} has stopped and parked.")
        else:
            print(f"🅿️ {self.name} is already parked.")
    
    def honk(self):
        print(f"🔊 {self.name}: BEEP BEEP!")

class Plane(Vehicle):
    """Plane class implementing Vehicle - demonstrates polymorphism"""
    
    def __init__(self, name, speed, fuel_type, altitude):
        super().__init__(name, speed, fuel_type)
        self.altitude = altitude
        self.is_flying = False
    
    def move(self):
        if not self.is_moving:
            self.is_moving = True
            self.is_flying = True
            print(f"✈️ {self.name} is flying through the sky at {self.speed} km/h and {self.altitude}m altitude!")
        else:
            print(f"✈️ {self.name} is already flying!")
    
    def stop(self):
        if self.is_moving:
            self.is_moving = False
            self.is_flying = False
            print(f"🛬 {self.name} has landed at the airport.")
        else:
            print(f"🏢 {self.name} is already at the airport.")
    
    def announce(self, message):
        if self.is_flying:
            print(f"📢 Captain announces on {self.name}: '{message}'")

class Boat(Vehicle):
    """Boat class implementing Vehicle - demonstrates polymorphism"""
    
    def __init__(self, name, speed, fuel_type, boat_type):
        super().__init__(name, speed, fuel_type)
        self.boat_type = boat_type
    
    def move(self):
        if not self.is_moving:
            self.is_moving = True
            print(f"⛵ {self.name} ({self.boat_type}) is sailing across the water at {self.speed} km/h!")
        else:
            print(f"⛵ {self.name} is already sailing!")
    
    def stop(self):
        if self.is_moving:
            self.is_moving = False
            print(f"⚓ {self.name} has docked at the harbor.")
        else:
            print(f"🏠 {self.name} is already docked.")
    
    def sound_horn(self):
        print(f"📯 {self.name}: HOOOONK!")

class Bicycle(Vehicle):
    """Bicycle class implementing Vehicle - demonstrates polymorphism"""
    
    def __init__(self, name, speed, gears):
        super().__init__(name, speed, "Human Power")
        self.gears = gears
    
    def move(self):
        if not self.is_moving:
            self.is_moving = True
            print(f"🚴 {self.name} is pedaling along the bike path at {self.speed} km/h!")
        else:
            print(f"🚴 {self.name} is already pedaling!")
    
    def stop(self):
        if self.is_moving:
            self.is_moving = False
            print(f"🚲 {self.name} has stopped and is parked.")
        else:
            print(f"🚲 {self.name} is already parked.")
    
    def ring_bell(self):
        print(f"🔔 {self.name}: RING RING!")

# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demonstrate_devices():
    """Demonstrate the Device class hierarchy with inheritance and encapsulation"""
    print("🏗️  ASSIGNMENT 1: DEVICE CLASS DEMONSTRATION")
    print("=" * 60)
    
    # Create different devices
    phone = Smartphone("Apple", "iPhone 15", 999, 20, 6.1, 48)
    laptop = Laptop("Dell", "XPS 13", 1200, 12, 16, 512)
    tablet = Tablet("Samsung", "Galaxy Tab S9", 600, 15, 11, True)
    
    devices = [phone, laptop, tablet]
    
    # Demonstrate each device
    for device in devices:
        print(f"\n📱 Testing {device.__class__.__name__}:")
        print(device.get_info())
        device.power_on()
        
        # Device-specific methods
        if isinstance(device, Smartphone):
            device.make_call("John")
            device.take_photo()
            device.install_app("Instagram")
        elif isinstance(device, Laptop):
            device.run_software("Visual Studio Code")
            device.save_file("my_project.py")
        elif isinstance(device, Tablet):
            device.draw("Digital Landscape")
            device.read_ebook("Python Programming")
        
        # Demonstrate encapsulation
        print(f"🔋 Current battery: {device.get_battery_life()} hours")
        device.set_battery_life(device.get_battery_life() + 2)
        print(f"🔋 After charging: {device.get_battery_life()} hours")
        
        device.power_off()
        print()

def demonstrate_polymorphism():
    """Demonstrate polymorphism with different vehicle types"""
    print("\n🎭 ASSIGNMENT 2: POLYMORPHISM DEMONSTRATION")
    print("=" * 60)
    
    # Create different vehicles
    vehicles = [
        Car("Tesla Model 3", 200, "Electric", 4),
        Plane("Boeing 747", 900, "Jet Fuel", 10000),
        Boat("Ocean Explorer", 45, "Diesel", "Yacht"),
        Bicycle("Mountain Bike Pro", 25, 21)
    ]
    
    print("🚀 Starting the Great Transportation Demo!")
    print()
    
    # Demonstrate polymorphism - same method name, different behaviors
    for vehicle in vehicles:
        print(f"🔷 {vehicle.get_info()}")
        vehicle.move()  # Each vehicle moves differently!
        
        # Vehicle-specific methods
        if isinstance(vehicle, Car):
            vehicle.honk()
        elif isinstance(vehicle, Plane):
            vehicle.announce("Welcome aboard! Enjoy your flight!")
        elif isinstance(vehicle, Boat):
            vehicle.sound_horn()
        elif isinstance(vehicle, Bicycle):
            vehicle.ring_bell()
        
        vehicle.stop()  # Each vehicle stops differently!
        print()
    
    print("🎯 Notice how each vehicle implements move() and stop() differently!")
    print("This is POLYMORPHISM in action! 🎭")

def interactive_demo():
    """Interactive demonstration allowing user to control devices and vehicles"""
    print("\n🎮 INTERACTIVE DEMO")
    print("=" * 40)
    
    # Create some objects
    my_phone = Smartphone("Google", "Pixel 8", 700, 24, 6.2, 50)
    my_car = Car("Honda Civic", 180, "Gasoline", 4)
    
    while True:
        print("\nChoose an option:")
        print("1. Control your smartphone")
        print("2. Control your car")
        print("3. Exit demo")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            my_phone.power_on()
            my_phone.make_call("Mom")
            photo = my_phone.take_photo()
            if photo:
                print(f"📷 Photo saved as: {photo}")
        
        elif choice == '2':
            print(f"🚗 Your car: {my_car.get_info()}")
            my_car.move()
            my_car.honk()
            my_car.stop()
        
        elif choice == '3':
            print("👋 Thanks for trying the OOP demo!")
            break
        
        else:
            print("❌ Invalid choice!")

# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Main program demonstrating OOP concepts"""
    print("🐍 PYTHON OOP MASTERCLASS 🐍")
    print("Classes, Inheritance, Encapsulation & Polymorphism")
    print("=" * 70)
    
    try:
        # Run demonstrations
        demonstrate_devices()
        demonstrate_polymorphism()
        
        # Interactive demo
        run_interactive = input("\n🎮 Would you like to try the interactive demo? (y/n): ").lower()
        if run_interactive == 'y':
            interactive_demo()
        
        print("\n🎉 CONGRATULATIONS! 🎉")
        print("You've successfully learned:")
        print("✅ Class creation and constructors")
        print("✅ Inheritance and method overriding")
        print("✅ Encapsulation with private attributes")
        print("✅ Polymorphism with abstract methods")
        print("✅ Real-world OOP design patterns")
        
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. See you next time!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()