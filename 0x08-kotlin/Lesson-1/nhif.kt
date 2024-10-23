// This program checks the amount and shows NHIF deduction charges based on the amount
fun main(){

    // Gross income amount
    val grossIncome: Int = 1165000
    
    // if statement to check amount to be deducated
    if (grossIncome <= 0) {
        println("Invalid amount")

        } else if(grossIncome > 0 && grossIncome <= 5999){
            println("NHIF deduction charges: Kes 150.0")

        } else if (grossIncome >= 6000 && grossIncome <= 7999) {
            println("NHIF deduction charges: Kes 300.0")

        } else if (grossIncome >= 8000 && grossIncome <= 11999) {
            println("NHIF deduction charges: Kes 400.0")

        } else if (grossIncome >= 12000 && grossIncome <= 14999) {
            println("NHIF deduction charges: Kes 500.0")

        } else if (grossIncome >= 15000 && grossIncome <= 19999) {
            println("NHIF deduction charges: Kes 600.0")

        } else if (grossIncome >= 20000 && grossIncome <= 24999) {
            println("NHIF deduction charges: Kes 750.0")

        } else if (grossIncome >= 25000 && grossIncome <= 29999) {
            println("NHIF deduction charges: Kes 850.0")

        } else if (grossIncome >= 30000 && grossIncome <= 34999) {
            println("NHIF deduction charges: Kes 900.0")

        } else if (grossIncome >= 35000 && grossIncome <= 39999) {
            println("NHIF deduction charges: Kes 950.0")

        } else if (grossIncome >= 40000 && grossIncome <= 44999) {
            println("NHIF deduction charges: Kes 1000.0")

        } else if (grossIncome >= 45000 && grossIncome <= 49999) {
            println("NHIF deduction charges: Kes 1100.0")

        } else if (grossIncome >= 50000 && grossIncome <= 59999) {
            println("NHIF deduction charges: Kes 1200.0")

        } else if (grossIncome >= 60000 && grossIncome <= 69999) {
            println("NHIF deduction charges: Kes 1200.0")

        } else if (grossIncome >= 70000 && grossIncome <= 79999) {
            println("NHIF deduction charges: Kes 1400.0")

        } else if (grossIncome >= 80000 && grossIncome <= 89999) {
            println("NHIF deduction charges: Kes 1500.0")

        } else if (grossIncome >= 90000 && grossIncome <= 99999) {
            println("NHIF deduction charges: Kes 1600.0")

        } else if (grossIncome >= 100000) {
            println("NHIF deduction charges: Kes 1700.0")

        } else{
            println("Invalid income")
        }
}