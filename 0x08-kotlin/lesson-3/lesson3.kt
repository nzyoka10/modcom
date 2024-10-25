// Loops
fun main(){
    // for loops :- a control flow statement that repeats a set of instructions multiple times
    
    // 1. loop through a range
    for(k in 1..10){
        println(k)
    }

    // loop through 30 to 50
    for(j in 30..50){
        println(j)
    }

    // 2. Loop through a range in steps
    // loop from 1 to 10 in step 2
    for(z in 1..10 step 2){
        println(z)
    }

    // 3. Loop through a range in down steps
    // loop from 100 to 0 in down steps of 5
    for (q in 100 downTo 0 step 5){
        println(q)
    }

    // 4. Loop through a list (collection of items)
    val list = arrayOf("Metro", "Karuri", "Atomic", "Kinatwa", "Cost Air")
    for(j in list){
        println(j)
    }
}