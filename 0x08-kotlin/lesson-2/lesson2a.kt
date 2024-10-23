// Day 2 of Kotlin
fun main(){
    
    // student grade
    val studentGrade: Int = 84

    // check grade range
    if(studentGrade < 0){
        println("$studentGrade : Negative value!")

    }else if(studentGrade >= 1 && studentGrade <= 49){
        println("$studentGrade : Fail")

    }else if(studentGrade >= 50 && studentGrade < 60){
        println("$studentGrade : Pass")

    }else if(studentGrade >= 60 && studentGrade < 70){
        println("$studentGrade : Credit")

    }else if(studentGrade >= 70 && studentGrade < 90){
        println("$studentGrade : Distinction")

    }else if(studentGrade >= 90 && studentGrade <= 100){
        println("$studentGrade : High Distinction")

    }else{
        println("$studentGrade : Invalid grade")
    }
}