// Inheritance
// - Is a concept where a class (a derived or child class) inherits properties and behaviors (attributes and methods) 
//   from another class (called a base or parent class). 
//   This allows the child class to reuse code, extend functionality, and promote organized, hierarchical class structures.
// NB: To inherit from parent class it MUST be open

// Example of a Parent Class
open class Animal{

    // functions
    // animal can walk
    fun walk(){
        println("Animal is walking")
    }

    // animal eat
    fun eat(){
        println("Animal is eating")
    }
}

// new class to inherit Animal class
class Dog : Animal(){
    
    // function sleep
    fun sleep(){
        println("Dog is sleeping")
    }
}

// main entry
fun main() {
    // create an instance of Dog
    val myDogObj = Dog()

    // print output
    // println(myDogObj.sleep())
    myDogObj.sleep()
    myDogObj.walk()

}
