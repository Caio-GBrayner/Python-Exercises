valueOnWallet = float(input("How much do you have in your wallet: R$"))

dollarExchangeRate= float(5.50)

print(f"With {valueOnWallet:.2f} you can buy US${(valueOnWallet/dollarExchangeRate):.2f}")