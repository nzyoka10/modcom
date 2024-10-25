// Kotlin functions
fun main(){

    // function with parameters
    fun goingToWork(gift: String){
        println("I am going to buy a $gift")
    }

    // calling the function
    goingToWork("Bike")
    goingToWork("Tractor")

    // function to add two numbers
    fun add(num1: Int, num2: Int){
        val sum = num1 + num2
        println("Sum: $sum")
    }

    // call function add
    add(10, 10)
    add(47, 18)

    // multiply
    fun myFunction(x: Int): Int {
        return (x * 5)
    }

    // call function
    var result = myFunction(3)
    var result1 = myFunction(10)
    println("myFuntion: $result")
    println("myFuntion: $result1")
}