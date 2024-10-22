// control flows
fun main()
{
    // program to store some amount to withdraw in a variable,
    // using if--else, statements.
    // determine the mpesa charges

    val amount: Int = 10

    if(amount < 0){
        // negative 
        println("No Funds in account!")
    }
    else if(amount > 0 && amount <= 200){
        // Amount: Kes. 1 - 199 
        println("No Mpesa charges include!")
    }
    else if(amount < 200 && amount <= 2500){
        // Amount: Kes. 200 - 2,500
        println("Mpesa charges: Kes. 34")
    }
    else if(amount > 2500 && amount <= 5000){
        // Amount: Kes. 2,501 - 5,000
        println("Mpesa charges: Kes. 67")
    }
    else if(amount > 5000 && amount <= 10000){
        // Amount: Kes. 5,001 - 10,000
        println("Mpesa charges: Kes. 112")
    }
    else if(amount > 10000 && amount <= 20000){
        // Amount: Kes. 10,001 - 20,000
        println("Mpesa charges: Kes. 197")
    }
    else{
        println("Invalid amount")
    }

}