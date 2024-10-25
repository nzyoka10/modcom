// OOP - Object Oriented Programming
// Objects and Classes are essential building blocks for OOP

// A class is a blueprint for creating objects
// - class defines the properties and functions(behaviors) that the object will have

// A Object is an instance of a class meaning an object is a specific object create with class blueprint

// class person
class Person {

    // properties
    val fname: String = "Super"
    val lname: String = "Metro"
    val age: Int = 20
    val gender: String = "Male"
    val favouriteFood: String = "Pilau"
    val isEmployed: Boolean = true
    val weight: Int = 500
    val eyeColor: String = "Black"
    val height: Int = 156
    val county: String = "Kenya"
    val favCar: String = "Mercedez Benz E-200"

    // functions / behaviours of a person
    fun speak(){
        println("Hello, my name is $fname $lname and I am $age years old!")
    }

    // eat - function
    fun eat(){
        println("I am eating $favouriteFood today!")
    }

    // learn
    fun learn(){
        println("I am learning new things every day!")
    }

    // sing
    fun sing(){
        println("I love singing!")
    }

    // drink
    fun drink(){
        println("I am drinking water!")
    }

    // drive
    fun drive(){
        println("I am driving a my new car, $favCar!")
    }
}

// create an object
fun main(){
    val myObj = Person()

    // access the properties
    println(myObj.fname)
    println(myObj.age)
    println(myObj.favCar)
    println(myObj.county)

    // new line
    print("\n")

    // access the functions
    myObj.speak()
    myObj.drive()
}
