// program that calculates a persons BMI and classify on condition

fun main() {
    // BMI = weight / height * height
    val weight: Double = 70.0
    val height: Double = 1.75
    val bmi: Double = weight / (height * height)

    // Print BMI rounded to 2 decimal places
    println("%.2f".format(bmi))

    // BMI classification
    if (bmi < 18.5) {
        println("%.2f : Underweight".format(bmi))

    } else if (bmi >= 18.5 && bmi <= 24.9) {
        println("%.2f : Normal weight".format(bmi))

    } else if (bmi >= 25.0 && bmi < 30.0) {
        println("%.2f : Overweight".format(bmi))
        
    } else {
        println("%.2f : Obese".format(bmi))
    }
}

