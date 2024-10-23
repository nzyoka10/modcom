fun main() {
    // This program checks the amount and shows Mpesa charges based on the amount

    val amount: Int = 8000 

    // Check if the amount is negative
    if (amount < 0) {
        println("No Funds in account!")  
    }
    // Check if the amount is between 1 and 200
    else if (amount >= 1 && amount <= 200) {
        println("No Mpesa charges included!") 
    }
    // Check if the amount is between 201 and 2500
    else if (amount >= 201 && amount <= 2500) {
        println("Mpesa charges: Kes. 34") 
    }
    // Check if the amount is between 2501 and 5000
    else if (amount >= 2501 && amount <= 5000) {
        println("Mpesa charges: Kes. 67")  
    }
    // Check if the amount is between 5001 and 10000
    else if (amount >= 5001 && amount <= 10000) {
        println("Mpesa charges: Kes. 112")  
    }
    // Check if the amount is between 10001 and 20000
    else if (amount >= 10001 && amount <= 20000) {
        println("Mpesa charges: Kes. 197")  
    }
    // If the amount is not in any of the above ranges, it's invalid
    else {
        println("Invalid amount") 
    }
}
