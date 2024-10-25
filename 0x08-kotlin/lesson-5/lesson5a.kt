// class fish
class Fish(){

    // fish properties
    val name: String = "Tilapia"
    val age: Int = 4
    val weight: Double = 2.5
    val source: String = "L. Victoria"
    val food: String = "Omena"

    // fish functions
    // fish name
    fun getFishName() {
        println("Fish: $name")
    }

    // weight
    fun getWeight(){
        println("Weight: $weight kg")
    }

    // age
    fun getAge(){
        println("Age: $age years")
    }

    // swim
    fun swim(){
        println("The fish happy swimming!")
    }

    // eat
    fun eat(){
        println("The fish is eating $food!")
    }

    // source
    fun fishSource(){
        println("The fish is from $source!")
    }
}

// create an object
fun main(){
    val myFishObj = Fish()

    // access the properties
    println(myFishObj.name)
    println(myFishObj.age)
    println(myFishObj.weight)
    println(myFishObj.source)

    // new line
    print("\n")

    // access the functions
    myFishObj.getFishName()
    myFishObj.getWeight()
    myFishObj.getAge()
    myFishObj.swim()
    myFishObj.eat()
}