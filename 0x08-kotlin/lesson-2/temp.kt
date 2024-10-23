// program that accepts a temp value in degree 
// celsius and classifies it based on:-
fun main(){
    val temp: Double = 25.3

    // Debug: line
    println("Temperature: $temp")

    // classify
    if(temp < 0){
        println("$temp : Freezing!")

    }else if(temp >= 0 && temp < 16){
        println("$temp : Cold!")

    }else if(temp >= 16 && temp < 26){
        println("$temp : Moderate!")

    }else if(temp >= 26 && temp < 35){
        println("$temp : Warm!")

    }else if(temp >= 35){
        println("$temp : Hot!")

    }else{
        println("Invalid temperature!")
    }
}