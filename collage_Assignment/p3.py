# john and his Series (Arthmetic progression) 

a=int(input("Enter the first term (a) :"))
d=float(input("Enter the common difference (d) :"))
n=int(input("Enter the number of terms (n) :"))

#formula for nth term
nth_term=a+(n-1)*d

#sum of n terms
sum=(n/2)*(2*a+(n-1)*d)

print(f"nth term = {nth_term}")
print(f"Sum of first n terms = {sum}")