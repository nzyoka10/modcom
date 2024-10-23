// program that calculates a persons BMI and classify on condition

fun main() {
    // BMI = weight / height * height
    val weight: Double = 73.4
    val height: Double = 1.75
    val bmi: Double = weight / (height * height)

    // Debug: Print BMI rounded to 2 decimal places
    println(String.format("%.2f", bmi))

    // BMI classification
    if (bmi < 18.5) {
        println(String.format("%.2f: Underweight", bmi))

    } else if (bmi >= 18.5 && bmi <= 24.9) {
        println(String.format("%.2f: Normal weight", bmi))

    } else if (bmi >= 25.0 && bmi < 30.0) {
        println(String.format("%.2f: Overweight", bmi))

    } else if (bmi >= 30) {
        println(String.format("%.2f: Obesity", bmi))

    } else {
        println(String.format("%.2f: Invalid BMI", bmi))
    }
}


