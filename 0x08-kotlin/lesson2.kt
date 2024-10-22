// control flows
fun main()
{
    // program to store some amount to withdraw in a variable,
    // using if--else, statements.
    // determine the mpesa charges

    val amount: Int = 6000
    val charges: Int
    printCharges(amount)
}

// charges function
fun printCharges(amount: Int) 
{
    if(amount >= 20000)
    {
        charges = 197
    }
    else if(amount >= 10000)
    {
        charges = 112
    }
    else if(amount >= 5000)
    {
        charges = 67
    }
    else if(amount >= 2500){
        charges = 34
    }
    else{
        charges = 0
    }
}