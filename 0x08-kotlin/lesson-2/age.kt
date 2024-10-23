// program that accepts a temp value in degree 
// celsius and classifies it based on:-
fun main(){
    val age: Int = 30

    // Debug: line
    println("Your age: $age")

    // classify
    if(age > 0 && age < 13){
        println("$age : Child!")

    }else if(age >= 13 && age < 20){
        println("$age : Teenager!")

    }else if(age >= 20 && age < 36){
        println("$age : Young Adult!")

    }else if(age >= 36 && age < 55){
        println("$age : Adult!")

    }else if(age >= 55){
        println("$age : Senior Citizen!")

    }else{
        println("Invalid Age!")
    }
}