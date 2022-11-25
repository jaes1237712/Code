    #include <iostream>
    
namespace wallet {
    int amount(500);
}

/// START YOUR CODE HERE ///
namespace bank {
    int amount(1000);
    void deposit(int cash) {
        bank::amount += cash;
    }
    int draw(int cash) {
        if(cash>bank::amount){
            int tmp{bank::amount};
            bank::amount = 0;
            return tmp;
        }
        bank::amount -= cash;
        return cash;
    }
    int check_balance() {
        return bank::amount;
    }
}
//// END YOUR CODE HERE ////
    
int main()
{
    std::cout << "Cash in your wallet: " << wallet::amount << "\n";
    std::cout << "Try to draw 500 from the bank.\n";
    int cash = bank::draw(500);
    wallet::amount += cash;
    std::cout << "Managed to get " << cash << " from the bank.\n";
    std::cout << "Cash in your wallet: " << wallet::amount << "\n";
    std::cout << "Remaining balance in the bank: " << bank::check_balance() << "\n\n";
    
    std::cout << "Try to draw 2000 from the bank.\n";
    cash = bank::draw(2000);
    wallet::amount += cash;
    std::cout << "Managed to get " << cash << " from the bank.\n";
    std::cout << "Cash in your wallet: " << wallet::amount << "\n";
    std::cout << "Remaining balance in the bank: " << bank::check_balance() << "\n\n";
    
    std::cout << "Save 500 back to the bank.\n";
    wallet::amount -= 500;
    bank::deposit(500);
    std::cout << "Cash in your wallet: " << wallet::amount << "\n";
    std::cout << "Remaining balance in the bank: " << bank::check_balance() << "\n\n";
    
    std::cout << "Received salary 5000.\n";
    wallet::amount += 5000;
    std::cout << "Cash in your wallet: " << wallet::amount << "\n\n";
    std::cout << "Remaining balance in the bank: " << bank::check_balance() << "\n\n";
    
    std::cout << "Save 4500 back to the bank.\n";
    wallet::amount -= 4500;
    bank::deposit(4500);
    std::cout << "Cash in your wallet: " << wallet::amount << "\n";
    std::cout << "Remaining balance in the bank: " << bank::check_balance() << "\n\n";
    
    return 0;
}
